import os
import runpy

from conan import ConanFile
from conan.tools.files import copy


required_conan_version = ">=2.28"


class LogcraftDslConan(ConanFile):
    """ The LogCraft DSL contract — content only (CC-BY-4.0).

    The single source of truth for the LogCraft scenario language: the JSON Schema
    (`scenario.schema.json`), the reference it formalizes (`scenario_reference.md`, whose
    § Semantic rules states what a schema cannot), the conformance set (`conformance/`: every case
    an implementation must judge as stated) and the starter scenarios (`scenario/`). It ships NO
    code. The engine (`logcraft_core`) `test_requires` this package and proves in its own build
    that it judges every case as the contract does; the superproject's `dsl` check holds every
    tracked scenario to the schema. The contract leads, the engine complies.
    """

    name = "logcraft_dsl"
    version = "1.10.9"
    package_type = "build-scripts"          # pure data: no libs, no headers, no binary
    description = "The LogCraft DSL contract: JSON Schema, reference, conformance set and starter scenarios."
    license = "CC-BY-4.0"
    no_copy_source = True

    CONTENT_FILES = ("scenario.schema.json", "scenario_reference.md")
    CONTENT_DIRS = ("conformance", "scenario")

    def export_sources(self):
        # The contract is exported through malf's tracked-files helper (DN-142.D4 (b)): a file git
        # does not track is never exported, so the recipe revision is a function of the commit.
        export_tracked = runpy.run_path(self.conf.get("user.malf:recipe_exports"))["export_tracked"]
        for name in (*self.CONTENT_FILES, *self.CONTENT_DIRS):
            export_tracked(self, name, name)

    def layout(self):
        # The contract sits at the package root in both source (editable) and package (cache)
        # trees; consumers resolve it through `cpp_info.resdirs`, so the same recipe works in
        # editable mode and after `conan create`.
        self.cpp.source.resdirs = ["."]
        self.cpp.package.resdirs = ["."]

    def package(self):
        for name in self.CONTENT_FILES:
            copy(self, name, src=self.source_folder, dst=self.package_folder)
        for name in self.CONTENT_DIRS:
            copy(self, "*", src=os.path.join(self.source_folder, name),
                 dst=os.path.join(self.package_folder, name))

    def package_info(self):
        self.cpp_info.includedirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.bindirs = []
        self.cpp_info.resdirs = ["."]
