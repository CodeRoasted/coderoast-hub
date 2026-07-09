from conan import ConanFile
from conan.tools.files import copy
import os


required_conan_version = ">=2.28"


class InsightScenariosConan(ConanFile):
    """ Public InSight scenario + contract corpus — content only (CC-BY-4.0).

    The single source of truth for the InSight detection scenarios: LogCraft
    scenario YAML, the declarative `*.contract.yaml` expectations, and the input
    fixtures. It ships NO code. The private detection-e2e harness
    (`insight_playground`, in insight-eidos) `test_requires` this package and
    runs the contracts against the engine; coderoast-server also serves the same
    scenario tree read-only at runtime (from a coderoast-hub checkout). One
    corpus, two consumers — no duplication, no drift.
    """

    name = "insight_scenarios"
    version = "1.7.6"
    package_type = "build-scripts"          # pure data: no libs, no headers, no binary
    description = "Public InSight scenario + contract corpus (LogCraft scenarios, declarative contracts, fixtures)."
    license = "CC-BY-4.0"
    no_copy_source = True

    def export_sources(self):
        copy(self, "scenario/*", self.recipe_folder, self.export_sources_folder)

    def layout(self):
        # The corpus lives under `scenario/` in both source (editable) and package
        # (cache) trees; consumers resolve it through `cpp_info.resdirs`, so the same
        # recipe works in editable mode and after `conan create`.
        self.cpp.source.resdirs = ["scenario"]
        self.cpp.package.resdirs = ["scenario"]

    def package(self):
        copy(self, "*", src=os.path.join(self.source_folder, "scenario"),
             dst=os.path.join(self.package_folder, "scenario"))

    def package_info(self):
        self.cpp_info.includedirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.bindirs = []
        self.cpp_info.resdirs = ["scenario"]
