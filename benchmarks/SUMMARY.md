# benchmark summary — v1.10.12

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_38 benchmark(s)._

| benchmark | real_time | bytes_per_second | numa_blocks | items_per_second | s_per_line |
| --- | --- | --- | --- | --- | --- |
| `bm_arena_block_lifecycle/auto:0/block:4096` | 74.729 ns | 5.483e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:65536` | 469.602 ns | 1.396e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:1048576` | 8619.627 ns | 1.217e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:4194304` | 132936.587 ns | 3.156e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:16777216` | 540443.86 ns | 3.104e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:25165824` | 813360.954 ns | 3.094e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:33554432` | 1.368e+07 ns | 2.453e+09 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:67108864` | 2.773e+07 ns | 2.421e+09 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:4096` | 79.485 ns | 5.155e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:65536` | 474.31 ns | 1.382e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:1048576` | 8637.952 ns | 1.214e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:4194304` | 134793.535 ns | 3.112e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:16777216` | 534894.826 ns | 3.137e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:25165824` | 801050.462 ns | 3.148e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:33554432` | 1.358e+07 ns | 2.470e+09 | 1 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:67108864` | 2.761e+07 ns | 2.431e+09 | 1 |  |  |
| `bm_arena_alloc_reset/auto:0/block:4096` | 149.014 ns | 2.749e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:65536` | 2401.721 ns | 2.729e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:1048576` | 38827.335 ns | 2.701e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:4194304` | 154274.756 ns | 2.727e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:16777216` | 629274.732 ns | 2.666e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:25165824` | 924136.516 ns | 2.727e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:33554432` | 1.246e+06 ns | 2.692e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:67108864` | 2.530e+06 ns | 2.652e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:4096` | 147.459 ns | 2.778e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:65536` | 2394.459 ns | 2.738e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:1048576` | 38554.384 ns | 2.720e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:4194304` | 153346.411 ns | 2.738e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:16777216` | 615938.352 ns | 2.724e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:25165824` | 923414.225 ns | 2.728e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:33554432` | 1.254e+06 ns | 2.677e+10 | 1 |  |  |
| `bm_arena_alloc_reset/auto:1/block:67108864` | 2.625e+06 ns | 2.557e+10 | 1 |  |  |
| `BM_TokenizationThroughput/4` | 1393.538 us |  |  | 717459.954 | 1.394e-06 |
| `BM_TokenizationThroughput/8` | 1302.384 us |  |  | 767663.183 | 1.303e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1330.647 us |  |  | 751361.442 | 1.331e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1218.075 us |  |  | 820793.026 | 1.218e-06 |
| `BM_TokenizationThroughputNestedJson` | 1105.592 us |  |  | 904183.882 | 1.106e-06 |
| `BM_TokenizationThroughputFlatJson` | 453.156 us |  |  | 2.206e+06 | 4.533e-07 |

### `insight-metalog` — compression / MetaLog-document build

_40 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 178.096 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 239.882 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 46.442 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 70.025 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 74.889 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 4.541 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 4.289 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 5195.679 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 10313.66 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 15459.75 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 30763.066 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 63294.705 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 21452.587 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 48.823 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 27.215 us |  |  |  |  |  | 0 | 3.680e+07 | 2.717e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 36.693 us |  |  |  |  |  | 0 | 2.729e+07 | 3.665e-08 |
| `BM_CubeKeyAlloc_MidBand` | 46.454 us |  |  |  |  |  | 0 | 2.155e+07 | 4.641e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 68.822 us |  |  |  |  |  | 0 | 1.454e+07 | 6.878e-08 |
| `BM_MetaLogCompress/1000/16` | 0.742 ms |  |  |  |  |  |  | 1.348e+06 |  |
| `BM_MetaLogCompress/10000/16` | 2.564 ms |  |  |  |  |  |  | 3.900e+06 |  |
| `BM_MetaLogCompress/100000/16` | 11.786 ms |  |  |  |  |  |  | 8.485e+06 |  |
| `BM_MetaLogCompress/1000/32` | 0.748 ms |  |  |  |  |  |  | 1.338e+06 |  |
| `BM_MetaLogCompress/10000/32` | 2.546 ms |  |  |  |  |  |  | 3.927e+06 |  |
| `BM_MetaLogCompress/100000/32` | 12.032 ms |  |  |  |  |  |  | 8.311e+06 |  |
| `BM_MetaLogCompress/1000/64` | 0.753 ms |  |  |  |  |  |  | 1.328e+06 |  |
| `BM_MetaLogCompress/10000/64` | 2.547 ms |  |  |  |  |  |  | 3.930e+06 |  |
| `BM_MetaLogCompress/100000/64` | 11.827 ms |  |  |  |  |  |  | 8.471e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 25.726 us |  |  |  |  |  |  | 3.887e+07 | 2.573e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 53.247 us |  |  |  |  |  |  | 1.878e+07 | 5.324e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 99.366 us |  |  |  |  |  |  | 1.006e+07 | 9.936e-08 |
| `BM_MetaLogIngest_ParamSketch/0` | 31.582 ms |  |  |  |  |  |  | 3.167e+06 | 3.158e-07 |
| `BM_MetaLogIngest_ParamSketch/1` | 410.343 ms |  |  |  |  |  |  | 243712.665 | 4.103e-06 |
| `BM_MetaLogIngest_Where` | 65.162 us |  |  |  |  |  |  | 1.536e+07 | 6.509e-08 |
| `BM_MetaLogIngest_LongText/64` | 1250.277 us |  |  |  |  |  |  | 799859.563 | 1.250e-06 |
| `BM_MetaLogIngest_LongText/4096` | 966.283 us |  |  |  |  |  |  | 1.035e+06 | 9.663e-07 |
| `BM_OrdinalKeyAlloc_None` | 27.099 us |  |  |  |  |  | 0 | 3.696e+07 | 2.706e-08 |
| `BM_OrdinalKeyAlloc_Key15Sso` | 39.477 us |  |  |  |  |  | 0 | 2.538e+07 | 3.939e-08 |
| `BM_OrdinalKeyAlloc_Key16ShipLegOnly` | 37.287 us |  |  |  |  |  | 0 | 2.684e+07 | 3.726e-08 |
| `BM_OrdinalKeyAlloc_Key16TraceMix` | 40.443 us |  |  |  |  |  | 0 | 2.476e+07 | 4.039e-08 |
| `BM_OrdinalKeyAlloc_Key23OverBothSso` | 39.471 us |  |  |  |  |  | 0 | 2.537e+07 | 3.942e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 1833.352 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2215.362 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 5728.192 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 14198.451 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 233.671 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 284.128 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1576.144 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 1941.461 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 5283.402 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 781.207 us |  |  |  |  |  | 0.609 | 0 | 29443.122 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1558.244 us |  |  |  |  |  | 0.857 | 0 | 17969.437 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 6057.098 us |  |  |  |  |  | 0.857 | 0 | 4622.76 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 6059.694 us |  |  |  |  |  | 0.857 | 0 | 4621.106 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 71702.931 us |  |  |  |  |  | 0.98 | 0 | 2733.657 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 70990.961 us |  |  |  |  |  | 0.98 | 0 | 2761.057 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 156420.542 us |  |  |  |  |  | 0.971 | 6 | 1336.15 | 6 | 7 | 193 | 20 | 209 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 311637.739 us |  |  |  |  |  | 0.98 | 0 | 633.201 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 441.808 ns | 2.263e+06 |
| `BM_Pipeline_IngestBatch/64` | 33472.097 ns | 1.913e+06 |
| `BM_Pipeline_IngestBatch/1024` | 450671.933 ns | 2.283e+06 |
| `BM_Pipeline_CloseWindow/1000` | 15146.429 ns | 66521.481 |
| `BM_Pipeline_CloseWindow/10000` | 23149.802 ns | 44313.175 |
| `BM_Pipeline_FullWindow/1000` | 447464.552 ns | 2.235e+06 |
| `BM_Pipeline_FullWindow/10000` | 4.204e+06 ns | 2.379e+06 |

### `logcraft-core` — the deterministic log simulator core

_73 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | peak_frontier_window_frames | peak_window_frames | records | emit_ms | materialize_ms | capacity | ns_per_record | coordinates | ns_per_coordinate | discovered_knob_cap | build_coordinates | discovered_tower_cap | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 10.116 ms | 1 | 593118.803 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 61.881 ms | 4 | 387841.267 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 177.74 ms | 16 | 540115.871 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 53.688 ms | 4 | 447023.298 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 108.357 ms | 16 | 885957.4 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 1.29 ms | 1 | 387706.47 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 1.789 ms | 4 | 1.118e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 3.852 ms | 16 | 2.077e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 12.001 ms | 64 | 2.666e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 41.427 ms | 256 | 3.090e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 11.125 ms | 32 | 1.438e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 7.397 ms | 32 | 2.163e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 6.136 ms | 32 | 2.607e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 6.856 ms | 32 | 2.334e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 2.768 ms | 16 | 2.890e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 3.727 ms | 16 | 2.147e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 3.835 ms | 16 | 2.086e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 4.179 ms | 16 | 1.914e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 4.842 ms | 16 | 1.652e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 6.907 ms | 16 | 1.158e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 8.635 ns |  | 1.158e+08 |  |  | 3.344e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 6.396 ns |  | 1.564e+08 |  |  | 8.131e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 7.224 ns |  | 1.384e+08 |  |  | 1.384e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 13.23 ns |  | 7.559e+07 |  |  | 8.913e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.478 ns |  | 2.233e+08 |  |  | 1.787e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 75.738 ns |  | 1.320e+07 |  |  | 2.509e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 56.76 ns |  | 1.762e+07 |  |  | 9.692e+07 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_IndexPass_Unmetered/iterations:1/real_time` | 372.053 ms |  |  |  |  |  | 25001 | 25000 | 1.800e+06 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_IndexPass_Metered/iterations:1/real_time` | 419.811 ms |  |  |  |  |  | 25001 | 25000 | 1.800e+06 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 364.962 ns |  | 2.740e+06 |  |  | 7.206e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 160.824 ns |  | 6.219e+06 |  |  | 1.132e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 243.71 ns |  | 4.104e+06 |  |  | 3.037e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 78.438 ns |  | 1.275e+07 |  |  | 6.885e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 113.456 ns |  | 8.831e+06 |  |  | 6.270e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 268.578 ns |  | 3.731e+06 |  |  | 7.461e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 401.957 ns |  | 2.488e+06 |  |  | 8.011e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 385.622 ns |  | 2.593e+06 |  |  | 1.805e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 314.182 ns |  | 3.183e+06 |  |  | 8.371e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 112.065 ns |  | 8.924e+06 |  |  | 1.624e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 210.031 ns |  | 4.761e+06 |  |  | 3.523e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 56.331 ns |  | 1.775e+07 |  |  | 9.586e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 80.077 ns |  | 1.249e+07 |  |  | 8.867e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 244.926 ns |  | 4.083e+06 |  |  | 8.167e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 337.063 ns |  | 2.967e+06 |  |  | 9.553e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 315.303 ns |  | 3.172e+06 |  |  | 2.207e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 9.873 ms | 1 |  | 6000 |  |  |  |  |  | 2.055 | 2.691 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 54.07 ms | 4 |  | 24000 |  |  |  |  |  | 40.242 | 8.068 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 105.634 ms | 16 |  | 96000 |  |  |  |  |  | 61.19 | 32.342 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 68421.394 us |  | 146158.165 |  |  |  |  |  |  |  |  | 8192 | 6.842e-06 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 67719.292 us |  | 147699.625 |  |  |  |  |  |  |  |  | 32768 | 6.770e-06 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 189.108 us |  | 4.333e+07 |  |  |  |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 753.679 us |  | 4.349e+07 |  |  |  |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate/real_time` | 302.924 us |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 3.029e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate_CiWorld/real_time` | 447.21 us |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 4.472e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisAtCap/real_time` | 27.811 ms |  |  |  |  |  |  |  |  |  |  |  |  | 64 | 4.345e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_TowerAtProductCap/real_time` | 158.038 ms |  |  |  |  |  |  |  |  |  |  |  |  | 256 | 6.173e-04 | 64 | 4 | 256 |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/2/real_time` | 554.244 us |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 2.771e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/4/real_time` | 975.26 us |  |  |  |  |  |  |  |  |  |  |  |  | 4 | 2.438e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/8/real_time` | 1931.781 us |  |  |  |  |  |  |  |  |  |  |  |  | 8 | 2.415e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/16/real_time` | 4251.533 us |  |  |  |  |  |  |  |  |  |  |  |  | 16 | 2.657e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/32/real_time` | 10274.28 us |  |  |  |  |  |  |  |  |  |  |  |  | 32 | 3.211e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/64/real_time` | 28022.832 us |  |  |  |  |  |  |  |  |  |  |  |  | 64 | 4.379e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 6.806 ms |  | 2.939e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 1.020e+06 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 18.028 ms |  | 4.438e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 1.667e+06 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 704.601 ms |  | 113539.511 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 9392 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 382.044 ms |  | 837600.779 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 469622 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 14.733 ms |  | 1.357e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 345 | 0 | 1 | 6.253e+07 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 35.787 ms |  | 2.235e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 4358 | 0 | 4 | 1.408e+09 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 263.003 ms |  | 304179.093 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 49 | 0 | 4 | 1.823e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 314.57 ms |  | 1.017e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 3061 | 0 | 16 | 2.886e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 5.929 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 5.925 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.004 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 29.295 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 29.967 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 30.652 ns | 65536 |
