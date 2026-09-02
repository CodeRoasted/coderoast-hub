# Sift — ci / build (last green) → ci / build (failing)

**Verdict: SUCCESS → FAILURE** — hard regression

**1066 changes, 11 structurally significant.**

- ci / build (last green): 3609 lines
- ci / build (failing): 2964 lines

## Significant changes

1. **[CRITICAL · regression]** New error pattern: "##[error]Process completed with exit code <*>" (confidence 0.90)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - retained in the salience reservoir (salience 9000, rare-but-severe, 1x)
2. **[HIGH · regression]** New error pattern: "logcraft_core/<*>: ERROR:" (confidence 0.85)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - new_error_pattern[level=error]
   - polarity:onset_candidate[new_error]
3. **[HIGH · regression]** New error pattern: "CMake Generate step failed. Build files cannot be regenerated correctly." (confidence 0.80)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - retained in the salience reservoir (salience 8000, rare-but-severe, 1x)
4. **[HIGH · regression]** New error pattern: "ERROR: logcraft_core/<*>: Error in build() method, line <*>" (confidence 0.80)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - retained in the salience reservoir (salience 8000, rare-but-severe, 1x)
5. **[HIGH · regression]** New error pattern: "ConanException: Error <*> while executing" (confidence 0.80)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - retained in the salience reservoir (salience 8000, rare-but-severe, 1x)
6. **[HIGH · regression]** New error pattern: "Package '<*>' build failed" (confidence 0.80)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - retained in the salience reservoir (salience 8000, rare-but-severe, 1x)
7. **[HIGH · regression]** New error pattern: "<*> tests passed, <*> tests failed out of <*>" (confidence 0.80)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - observed 1x on changed
   - retained in the salience reservoir (salience 8000, rare-but-severe, 1x)
8. **[MEDIUM]** New salient line: "logcraft_core/<*>: WARN: Build folder /home/runner/work/logcraft/logcraft/.conan2/p/b/<*>/b" — retained by its level (1x)  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - was retained by its log level on changed; not in the baseline's salience memory
9. **[MEDIUM]** Vanished salient line: "logcraft_core/<*> (test package): WARN: On the fly replacement of CMakeDeps by CMakeConfigDeps generator, because 'tools.cmake.cmakedeps:new' incubating conf activated. This conf is incubating and will break in next releases. CMakeConfigDeps is now experimental and can be used as such in recipes." — retained by its level  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - was retained by its log level on baseline; not in the changed side's salience memory
10. **[MEDIUM]** Vanished salient line: "logcraft_core/<*> (test package): WARN: experimental: CMakeConfigDeps is experimental, and might get breaking changes in future releases" — retained by its level  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - was retained by its log level on baseline; not in the changed side's salience memory
11. **[MEDIUM]** Vanished salient line: ": WARN: deprecated: CMakeConfigDeps does not support module find mode in gtest/<*>" — retained by its level  _(in phase "ci / ci / build ▸ set -euo pipefail")_
   - was retained by its log level on baseline; not in the changed side's salience memory

_1055 changes suppressed as noise (proportional / low-frequency). Per-unit structural deltas in JSON `raw`._
