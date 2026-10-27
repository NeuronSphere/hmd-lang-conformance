# hmd-lang-conformance: the shared conformance vocabulary (hmd-entity-storage NERD005).
#
# Everything runs in containers, so the host needs no Go or Python toolchain.

GO_IMAGE     ?= golang:1.25
PY_IMAGE     ?= python:3.11-slim
ROBOT_VERSION ?= 7.3.2
REQTRACE := github.com/neuronsphere/hmd-cli-bartleby/src/go/reqtrace/cmd/reqtrace@v0.3.1
DOCKER_GO = docker run --rm -v $(CURDIR):/src -w /src \
              -v hmd-gomod:/go/pkg/mod -v hmd-gocache:/root/.cache/go-build $(GO_IMAGE)

# The private index URL is built from the keychain at run time and passed to
# containers in their environment, never on a command line.
PRIVATE_INDEX = $${PIP_EXTRA_INDEX_URL:-https://hmd_ro:$$(security find-generic-password -s uv:hmdlabs.jfrog.io -a hmd_ro -w | python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.stdin.read().strip(),safe=""))')@hmdlabs.jfrog.io/artifactory/api/pypi/hmd_pypi/simple}

MS_BASE_TEST_IMAGE ?= ghcr.io/hmdlabs/hmd-ms-base-test:0.1.163
CONFORMANCE_TAG    ?= hmd-ms-base-test:0.1
# nsctl's image staging also looks for the registry-qualified name.
CONFORMANCE_GHCR_TAG ?= ghcr.io/hmdlabs/hmd-ms-base-test:0.1
PROJECTBUILDER     ?= ghcr.io/hmdlabs/hmd-img-projectbuilder:0.5.395
HMD_TMPL_VOCABGEN  ?= $(abspath $(CURDIR)/../hmd-tmpl-vocabgen)

.PHONY: reqs reqs-check docker-reqs docker-reqs-check docker-test docker-render conformance-image check help

## reqs: regenerate docs/requirements/traceability.rst (needs Go; see docker-reqs)
reqs:
	go run $(REQTRACE) -repo $(CURDIR)

## reqs-check: fail if a requirement is untested, a test is untagged, or the matrix is stale
reqs-check:
	go run $(REQTRACE) -repo $(CURDIR) -check

## docker-reqs: reqs, in a Go container
docker-reqs:
	$(DOCKER_GO) go run $(REQTRACE) -repo /src

## docker-reqs-check: reqs-check, in a Go container
docker-reqs-check:
	$(DOCKER_GO) go run $(REQTRACE) -repo /src -check

## docker-test: install the package and run test/*.robot in a Python container
docker-test:
	PIP_EXTRA_INDEX_URL="$(PRIVATE_INDEX)" docker run --rm -e PIP_EXTRA_INDEX_URL \
	  -v $(CURDIR):/repo -w /repo -v hmd-pipcache:/root/.cache/pip $(PY_IMAGE) sh -c '\
	    cp -R /repo /tmp/build && \
	    pip install -q --root-user-action=ignore robotframework==$(ROBOT_VERSION) /tmp/build/src/python >/tmp/pip.log 2>&1 || { tail -5 /tmp/pip.log; exit 1; }; \
	    robot --outputdir /tmp/robot test/'

## check: docker-test + docker-reqs-check
check: docker-test docker-reqs-check

## docker-render: regenerate src/python/hmd_lang_conformance from src/schemas (projectbuilder)
docker-render:
	PIP_EXTRA_INDEX_URL="$(PRIVATE_INDEX)" docker run --rm --entrypoint sh -e PIP_EXTRA_INDEX_URL \
	  -v $(CURDIR):/repo -v $(HMD_TMPL_VOCABGEN):/vocabgen:ro $(PROJECTBUILDER) /repo/tools/render.sh

## conformance-image: hmd-ms-base-test + this vocabulary, tagged for a local nsctl deploy
conformance-image:
	docker build -f docker/Dockerfile.ms-base-test \
	  --build-arg BASE_IMAGE=$(MS_BASE_TEST_IMAGE) -t $(CONFORMANCE_TAG) -t $(CONFORMANCE_GHCR_TAG) .

## help: show this help
help:
	@grep -E '^## ' $(MAKEFILE_LIST) | sed 's/^## /  /'
