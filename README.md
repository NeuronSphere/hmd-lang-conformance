# hmd-lang-conformance

The shared conformance vocabulary for NeuronSphere's persistence stack.

[NERD005](https://github.com/HMDLabs/hmd-entity-storage/blob/main/docs/proposals/NERD005_Go_Persistence_Stack.rst)
in `hmd-entity-storage` ports the stack (meta-types, the entity-storage engines,
`hmd-ms-base`) to Go and holds the Python and Go implementations to the same
behavior. Both are run against the nouns here: `typed_required` and
`typed_optional` carry one attribute of every `hmd-meta-types` type (string,
integer, float, bool, enum, timestamp, epoch, collection, mapping, blob),
required and optional, plus a relationship between them.

## Layout
- `src/schemas/hmd_lang_conformance/`: the `.hms` schemas, the source of truth.
- `src/python/hmd_lang_conformance/`: the Python package, generated from the schemas and committed.
- `docker/Dockerfile.ms-base-test`: `hmd-ms-base-test` with this package installed.
- `docs/requirements/`: what the vocabulary must cover (sphinx-needs), traced to `test/*.robot`.
- `docs/known_issues.rst`: concerns found in the Python toolchain.

## Use
Everything runs in containers; the private index credential comes from the
keychain (`uv:hmdlabs.jfrog.io`).

```sh
make docker-test         # Robot checks on the vocabulary and the generated package
make docker-reqs-check   # reqtrace: every requirement tested, matrix current
make docker-render       # regenerate src/python from src/schemas (hmd-img-projectbuilder)
make conformance-image   # hmd-ms-base-test + this vocabulary, for a local nsctl deploy
```

`hmd-entity-storage`'s conformance suites install this package in the Bender
container from `test/test_requirements.txt`.
