# Sift — ci / build (last green) → ci / build (failing)

**Verdict: SUCCESS → FAILURE** — hard regression

**13 changes, 13 structurally significant.**

- ci / build (last green): 3609 lines
- ci / build (failing): 2964 lines

## Significant changes

1. **[CRITICAL · regression]** New error pattern: "##[error]Process completed with exit code <*>" (confidence 0.90)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - retained in the salience reservoir (salience 9000, rare-but-severe, 1x)
2. **[HIGH · regression]** New error pattern: "Package 'a4b45bd0705f7cc1c7858655551872848edb786a' build failed" (confidence 0.85)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - new_error_pattern[level=error]
   - polarity:onset_candidate[new_error]
3. **[HIGH · regression]** New error pattern: "logcraft_core/<*>: ERROR:" (confidence 0.85)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - new_error_pattern[level=error]
   - polarity:onset_candidate[new_error]
4. **[HIGH · regression]** New error pattern: "CMake Generate step failed. Build files cannot be regenerated correctly." (confidence 0.80)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - retained in the salience reservoir (salience 8000, rare-but-severe, 1x)
5. **[HIGH · regression]** New error pattern: "ERROR: logcraft_core/<*>: Error in build() method, line <*>" (confidence 0.80)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - retained in the salience reservoir (salience 8000, rare-but-severe, 1x)
6. **[HIGH · regression]** New error pattern: "ConanException: Error <*> while executing" (confidence 0.80)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - retained in the salience reservoir (salience 8000, rare-but-severe, 1x)
7. **[HIGH · regression]** New error pattern: "<*> tests passed, <*> tests failed out of <*>" (confidence 0.80)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - retained in the salience reservoir (salience 8000, rare-but-severe, 1x)
8. **[HIGH]** Vanished salient line: "logcraft_core/<*> (test package): WARN: On the fly replacement of CMakeDeps by CMakeConfigDeps generator, because 'tools.cmake.cmakedeps:new' incubating conf activated. This conf is incubating and will break in next releases. CMakeConfigDeps is now experimental and can be used as such in recipes."  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - was retained in the salience reservoir on baseline, absent on changed
9. **[HIGH]** New salient line: "conanfile.py (logcraft_core/<*>): WARN: experimental: CMakeConfigDeps is experimental, and might get breaking changes in future releases" — retained by salience  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - retained in the salience reservoir on changed, absent on baseline
10. **[HIGH]** New salient line: "logcraft_core/<*>: WARN: experimental: CMakeConfigDeps is experimental, and might get breaking changes in future releases" — retained by salience  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - retained in the salience reservoir on changed, absent on baseline
11. **[HIGH]** New salient line: "logcraft_core/<*>: WARN: Build folder /home/runner/work/logcraft/logcraft/.conan2/p/b/<*>/b" — retained by salience  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - retained in the salience reservoir on changed, absent on baseline
12. **[HIGH]** Vanished salient line: "logcraft_core/<*> (test package): WARN: experimental: CMakeConfigDeps is experimental, and might get breaking changes in future releases"  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - was retained in the salience reservoir on baseline, absent on changed
13. **[HIGH]** Vanished salient line: ": WARN: deprecated: CMakeConfigDeps does not support module find mode in gtest/<*>"  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - was retained in the salience reservoir on baseline, absent on changed
