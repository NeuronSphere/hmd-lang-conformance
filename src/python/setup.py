from setuptools import setup, find_packages
import pathlib

repo_dir = pathlib.Path(__file__).absolute().parent.parent.parent
version_file = repo_dir / "meta-data" / "VERSION"

with open(version_file, "r") as vfl:
    version = vfl.read().strip()

setup(
    name="hmd-lang-conformance",
    version=version,
    description="Shared conformance vocabulary for the Python and Go persistence implementations (NERD005)",
    author="Brian Greene",
    author_email="brian.greene@hmdlabs.io",
    license="unlicensed",
    package_data={"hmd_lang_conformance": ["schemas/**/*.hms"]},
    packages=find_packages(),
    include_package_data=True,
    install_requires=["hmd-meta-types", "hmd-schema-loader", "hmd-graphql-client"],
)
