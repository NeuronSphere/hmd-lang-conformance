"""Checks on the hmd-lang-conformance vocabulary and its generated package."""

import importlib
import json
import pathlib
from importlib.metadata import version

from robot.api.deco import keyword, library

REPO = pathlib.Path(__file__).resolve().parent.parent
SCHEMAS = REPO / "src" / "schemas" / "hmd_lang_conformance"
PACKAGED = REPO / "src" / "python" / "hmd_lang_conformance" / "schemas" / "hmd_lang_conformance"


def _camel(name):
    return "".join(part.capitalize() for part in name.split("_"))


@library
class VocabularyLib:
    @keyword
    def meta_types_type_names(self):
        """Every attribute type hmd-meta-types knows."""
        from hmd_meta_types.entity import type_mapping

        return sorted(type_mapping)

    @keyword
    def schema(self, name):
        return json.loads((SCHEMAS / f"{name}.hms").read_text())

    @keyword
    def nouns(self):
        return [s["name"] for s in map(self.schema, self.schema_names()) if s["metatype"] == "noun"]

    @keyword
    def schema_names(self):
        return sorted(p.stem for p in SCHEMAS.glob("*.hms"))

    @keyword
    def attribute_types(self, name, required=None):
        """The types of a schema's attributes, optionally only required or only optional ones."""
        attrs = self.schema(name)["attributes"]
        return sorted(
            {
                a["type"]
                for a in attrs.values()
                if required is None or bool(a.get("required", False)) == required
            }
        )

    @keyword
    def optional_attributes_except_label_are_optional(self, name):
        attrs = self.schema(name)["attributes"]
        wrong = [k for k, a in attrs.items() if k != "label" and a.get("required", False)]
        if wrong:
            raise AssertionError(f"{name}: required attributes {wrong}")

    @keyword
    def enum_value_counts(self):
        counts = {}
        for name in self.schema_names():
            for attr, a in self.schema(name).get("attributes", {}).items():
                if a["type"] == "enum":
                    counts[f"{name}.{attr}"] = len(a.get("enum_def", []))
        return counts

    @keyword
    def packaged_schema_differences(self):
        """File names whose packaged copy is missing, extra, or differs from src/schemas."""
        src = {p.name: p.read_bytes() for p in SCHEMAS.glob("*.hms")}
        pkg = {p.name: p.read_bytes() for p in PACKAGED.iterdir() if p.is_file()}
        return sorted(n for n in set(src) | set(pkg) if src.get(n) != pkg.get(n))

    @keyword
    def generated_definition(self, name):
        module = importlib.import_module(f"hmd_lang_conformance.{name}")
        return getattr(module, _camel(name)).entity_definition()

    @keyword
    def client_module_exports(self):
        module = importlib.import_module("hmd_lang_conformance.hmd_lang_conformance_client")
        return [n for n in ("HmdLangConformanceClient", "get_client_loader") if hasattr(module, n)]

    @keyword
    def installed_version(self):
        return version("hmd-lang-conformance")

    @keyword
    def repo_version(self):
        return (REPO / "meta-data" / "VERSION").read_text().strip()
