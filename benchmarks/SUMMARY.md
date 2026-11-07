# benchmark summary — v1.10.11

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_38 benchmark(s)._

| benchmark | real_time | bytes_per_second | numa_blocks | items_per_second | s_per_line |
| --- | --- | --- | --- | --- | --- |
| `bm_arena_block_lifecycle/auto:0/block:4096` | 76.909 ns | 5.326e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:65536` | 473.15 ns | 1.385e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:1048576` | 8447.336 ns | 1.241e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:4194304` | 133080.748 ns | 3.152e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:16777216` | 546710.148 ns | 3.069e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:25165824` | 822997.067 ns | 3.058e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:33554432` | 2.089e+07 ns | 1.606e+09 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:67108864` | 4.273e+07 ns | 1.571e+09 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:4096` | 82.85 ns | 4.944e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:65536` | 489.86 ns | 1.338e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:1048576` | 8563.043 ns | 1.225e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:4194304` | 133288.537 ns | 3.147e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:16777216` | 537630.288 ns | 3.121e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:25165824` | 801015.567 ns | 3.142e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:33554432` | 2.028e+07 ns | 1.655e+09 | 1 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:67108864` | 4.246e+07 ns | 1.580e+09 | 1 |  |  |
| `bm_arena_alloc_reset/auto:0/block:4096` | 155.279 ns | 2.638e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:65536` | 2451.752 ns | 2.673e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:1048576` | 38716.123 ns | 2.708e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:4194304` | 154089.045 ns | 2.722e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:16777216` | 619569.41 ns | 2.708e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:25165824` | 930032.859 ns | 2.706e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:33554432` | 1.269e+06 ns | 2.643e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:67108864` | 2.611e+06 ns | 2.570e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:4096` | 156.49 ns | 2.617e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:65536` | 2465.562 ns | 2.658e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:1048576` | 39208.713 ns | 2.674e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:4194304` | 159200.442 ns | 2.635e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:16777216` | 639912.551 ns | 2.622e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:25165824` | 946897.381 ns | 2.658e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:33554432` | 1.272e+06 ns | 2.638e+10 | 1 |  |  |
| `bm_arena_alloc_reset/auto:1/block:67108864` | 2.683e+06 ns | 2.501e+10 | 1 |  |  |
| `BM_TokenizationThroughput/4` | 1194.879 us |  |  | 836558.832 | 1.195e-06 |
| `BM_TokenizationThroughput/8` | 1146.12 us |  |  | 872139.749 | 1.147e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1143.16 us |  |  | 874408.08 | 1.144e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1081.175 us |  |  | 924508.445 | 1.082e-06 |
| `BM_TokenizationThroughputNestedJson` | 1101.809 us |  |  | 907073.259 | 1.102e-06 |
| `BM_TokenizationThroughputFlatJson` | 468.08 us |  |  | 2.135e+06 | 4.684e-07 |

### `insight-metalog` — compression / MetaLog-document build

_40 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 195.962 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 239.103 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 45.464 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 71.165 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 76.212 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 4.537 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 4.432 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 5180.517 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 10291.933 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 16481.523 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 30573.118 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 61976.547 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 21349.891 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 51.267 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 27.367 us |  |  |  |  |  | 0 | 3.664e+07 | 2.729e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 38.147 us |  |  |  |  |  | 0 | 2.628e+07 | 3.806e-08 |
| `BM_CubeKeyAlloc_MidBand` | 46.389 us |  |  |  |  |  | 0 | 2.160e+07 | 4.630e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 69.028 us |  |  |  |  |  | 0 | 1.451e+07 | 6.894e-08 |
| `BM_MetaLogCompress/1000/16` | 0.793 ms |  |  |  |  |  |  | 1.262e+06 |  |
| `BM_MetaLogCompress/10000/16` | 2.64 ms |  |  |  |  |  |  | 3.788e+06 |  |
| `BM_MetaLogCompress/100000/16` | 11.84 ms |  |  |  |  |  |  | 8.446e+06 |  |
| `BM_MetaLogCompress/1000/32` | 0.74 ms |  |  |  |  |  |  | 1.351e+06 |  |
| `BM_MetaLogCompress/10000/32` | 2.559 ms |  |  |  |  |  |  | 3.908e+06 |  |
| `BM_MetaLogCompress/100000/32` | 11.86 ms |  |  |  |  |  |  | 8.431e+06 |  |
| `BM_MetaLogCompress/1000/64` | 0.753 ms |  |  |  |  |  |  | 1.328e+06 |  |
| `BM_MetaLogCompress/10000/64` | 2.605 ms |  |  |  |  |  |  | 3.839e+06 |  |
| `BM_MetaLogCompress/100000/64` | 12.084 ms |  |  |  |  |  |  | 8.275e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 27.098 us |  |  |  |  |  |  | 3.690e+07 | 2.710e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 52.956 us |  |  |  |  |  |  | 1.888e+07 | 5.296e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 105.823 us |  |  |  |  |  |  | 9.450e+06 | 1.058e-07 |
| `BM_MetaLogIngest_ParamSketch/0` | 31.358 ms |  |  |  |  |  |  | 3.189e+06 | 3.136e-07 |
| `BM_MetaLogIngest_ParamSketch/1` | 459.231 ms |  |  |  |  |  |  | 217754.847 | 4.592e-06 |
| `BM_MetaLogIngest_Where` | 73.705 us |  |  |  |  |  |  | 1.357e+07 | 7.371e-08 |
| `BM_MetaLogIngest_LongText/64` | 1253.557 us |  |  |  |  |  |  | 797736.948 | 1.254e-06 |
| `BM_MetaLogIngest_LongText/4096` | 1022.521 us |  |  |  |  |  |  | 977973.934 | 1.023e-06 |
| `BM_OrdinalKeyAlloc_None` | 27.553 us |  |  |  |  |  | 0 | 3.639e+07 | 2.748e-08 |
| `BM_OrdinalKeyAlloc_Key15Sso` | 41.714 us |  |  |  |  |  | 0 | 2.403e+07 | 4.161e-08 |
| `BM_OrdinalKeyAlloc_Key16ShipLegOnly` | 39.332 us |  |  |  |  |  | 0 | 2.548e+07 | 3.925e-08 |
| `BM_OrdinalKeyAlloc_Key16TraceMix` | 42.751 us |  |  |  |  |  | 0 | 2.345e+07 | 4.264e-08 |
| `BM_OrdinalKeyAlloc_Key23OverBothSso` | 39.921 us |  |  |  |  |  | 0 | 2.510e+07 | 3.984e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 1799.149 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2168.806 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 5640.321 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 14220.313 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 228.618 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 281.189 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1560.353 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 1912.739 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 5326.819 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 777.998 us |  |  |  |  |  | 0.609 | 0 | 29563.564 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1533.055 us |  |  |  |  |  | 0.857 | 0 | 18264.305 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 5942.246 us |  |  |  |  |  | 0.857 | 0 | 4712.023 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 6065.352 us |  |  |  |  |  | 0.857 | 0 | 4616.376 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 69981.227 us |  |  |  |  |  | 0.98 | 0 | 2800.772 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 70172.575 us |  |  |  |  |  | 0.98 | 0 | 2793.134 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 156068.813 us |  |  |  |  |  | 0.971 | 6 | 1339.152 | 6 | 7 | 193 | 20 | 209 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 308768.345 us |  |  |  |  |  | 0.98 | 0 | 634.786 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 431.232 ns | 2.318e+06 |
| `BM_Pipeline_IngestBatch/64` | 33327.59 ns | 1.919e+06 |
| `BM_Pipeline_IngestBatch/1024` | 458142.163 ns | 2.234e+06 |
| `BM_Pipeline_CloseWindow/1000` | 16693.672 ns | 60680.445 |
| `BM_Pipeline_CloseWindow/10000` | 24282.183 ns | 42603.537 |
| `BM_Pipeline_FullWindow/1000` | 461896.291 ns | 2.165e+06 |
| `BM_Pipeline_FullWindow/10000` | 4.473e+06 ns | 2.236e+06 |

### `logcraft-core` — the deterministic log simulator core

_73 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | peak_frontier_window_frames | peak_window_frames | records | emit_ms | materialize_ms | capacity | ns_per_record | coordinates | ns_per_coordinate | discovered_knob_cap | build_coordinates | discovered_tower_cap | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 10.742 ms | 1 | 558565.373 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 60.775 ms | 4 | 394899.829 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 108.139 ms | 16 | 887743.928 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 54.112 ms | 4 | 443525.894 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 111.102 ms | 16 | 864074.339 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 1.367 ms | 1 | 365830.295 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 1.819 ms | 4 | 1.100e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 3.794 ms | 16 | 2.108e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 12.186 ms | 64 | 2.626e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 41.385 ms | 256 | 3.093e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 11.713 ms | 32 | 1.366e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 7.67 ms | 32 | 2.086e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 6.236 ms | 32 | 2.566e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 6.553 ms | 32 | 2.441e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 2.76 ms | 16 | 2.899e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 3.836 ms | 16 | 2.086e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 3.75 ms | 16 | 2.134e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 4.223 ms | 16 | 1.894e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 5.021 ms | 16 | 1.593e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 6.735 ms | 16 | 1.188e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 8.578 ns |  | 1.166e+08 |  |  | 3.366e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 6.445 ns |  | 1.552e+08 |  |  | 8.068e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 7.015 ns |  | 1.425e+08 |  |  | 1.425e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 13.312 ns |  | 7.512e+07 |  |  | 8.849e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.677 ns |  | 2.138e+08 |  |  | 1.710e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 77.852 ns |  | 1.284e+07 |  |  | 2.441e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 67.143 ns |  | 1.489e+07 |  |  | 8.193e+07 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_IndexPass_Unmetered/iterations:1/real_time` | 390.27 ms |  |  |  |  |  | 25001 | 25000 | 1.800e+06 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_IndexPass_Metered/iterations:1/real_time` | 386.261 ms |  |  |  |  |  | 25001 | 25000 | 1.800e+06 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 360.765 ns |  | 2.772e+06 |  |  | 7.290e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 163.884 ns |  | 6.102e+06 |  |  | 1.111e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 247.639 ns |  | 4.038e+06 |  |  | 2.988e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 77.372 ns |  | 1.292e+07 |  |  | 6.979e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 112.661 ns |  | 8.876e+06 |  |  | 6.302e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 268.338 ns |  | 3.727e+06 |  |  | 7.453e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 403.519 ns |  | 2.478e+06 |  |  | 7.980e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 393.724 ns |  | 2.540e+06 |  |  | 1.768e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 322.494 ns |  | 3.101e+06 |  |  | 8.155e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 119.566 ns |  | 8.364e+06 |  |  | 1.522e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 210.811 ns |  | 4.744e+06 |  |  | 3.510e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 60.658 ns |  | 1.649e+07 |  |  | 8.902e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 81.619 ns |  | 1.225e+07 |  |  | 8.699e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 254.114 ns |  | 3.935e+06 |  |  | 7.870e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 336.68 ns |  | 2.970e+06 |  |  | 9.564e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 333.926 ns |  | 2.995e+06 |  |  | 2.084e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 10.46 ms | 1 |  | 6000 |  |  |  |  |  | 2.198 | 2.79 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 54.264 ms | 4 |  | 24000 |  |  |  |  |  | 39.205 | 8.313 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 103.568 ms | 16 |  | 96000 |  |  |  |  |  | 59.162 | 31.044 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 108283.467 us |  | 92366.435 |  |  |  |  |  |  |  |  | 8192 | 1.083e-05 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 67258.839 us |  | 148729.019 |  |  |  |  |  |  |  |  | 32768 | 6.724e-06 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 192.173 us |  | 4.265e+07 |  |  |  |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 779.047 us |  | 4.207e+07 |  |  |  |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate/real_time` | 324.675 us |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 3.247e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate_CiWorld/real_time` | 493.363 us |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 4.934e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisAtCap/real_time` | 28.327 ms |  |  |  |  |  |  |  |  |  |  |  |  | 64 | 4.426e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_TowerAtProductCap/real_time` | 167.384 ms |  |  |  |  |  |  |  |  |  |  |  |  | 256 | 6.538e-04 | 64 | 4 | 256 |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/2/real_time` | 583.178 us |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 2.916e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/4/real_time` | 1024.446 us |  |  |  |  |  |  |  |  |  |  |  |  | 4 | 2.561e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/8/real_time` | 1994.349 us |  |  |  |  |  |  |  |  |  |  |  |  | 8 | 2.493e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/16/real_time` | 4338.936 us |  |  |  |  |  |  |  |  |  |  |  |  | 16 | 2.712e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/32/real_time` | 10694.077 us |  |  |  |  |  |  |  |  |  |  |  |  | 32 | 3.342e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/64/real_time` | 28517.656 us |  |  |  |  |  |  |  |  |  |  |  |  | 64 | 4.456e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 6.726 ms |  | 2.973e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 1.420e+06 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 17.536 ms |  | 4.562e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 1.728e+06 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 282.96 ms |  | 282725.885 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 56459 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 217.573 ms |  | 1.471e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 438106 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 14.582 ms |  | 1.372e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 504 | 0 | 1 | 9.886e+07 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 36.982 ms |  | 2.163e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 4039 | 0 | 4 | 1.334e+09 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 221.399 ms |  | 361339.219 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 145 | 0 | 4 | 5.885e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 293.733 ms |  | 1.089e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 1633 | 0 | 16 | 1.502e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 6.455 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 6.634 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.004 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 29.391 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 29.708 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 30.204 ns | 65536 |
