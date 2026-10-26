# benchmark summary — v1.10.8

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_38 benchmark(s)._

| benchmark | real_time | bytes_per_second | numa_blocks | items_per_second | s_per_line |
| --- | --- | --- | --- | --- | --- |
| `bm_arena_block_lifecycle/auto:0/block:4096` | 86.628 ns | 4.728e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:65536` | 529.039 ns | 1.239e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:1048576` | 9504.733 ns | 1.103e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:4194304` | 121192.748 ns | 3.461e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:16777216` | 557273.033 ns | 3.013e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:25165824` | 833382.351 ns | 3.020e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:33554432` | 2.350e+07 ns | 1.428e+09 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:67108864` | 4.845e+07 ns | 1.385e+09 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:4096` | 91.4 ns | 4.481e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:65536` | 534.783 ns | 1.225e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:1048576` | 9302.582 ns | 1.127e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:4194304` | 121396.821 ns | 3.455e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:16777216` | 540093.537 ns | 3.106e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:25165824` | 824331.548 ns | 3.053e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:33554432` | 2.330e+07 ns | 1.440e+09 | 1 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:67108864` | 4.752e+07 ns | 1.412e+09 | 1 |  |  |
| `bm_arena_alloc_reset/auto:0/block:4096` | 175.803 ns | 2.330e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:65536` | 2717.014 ns | 2.412e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:1048576` | 43521.453 ns | 2.409e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:4194304` | 179071.928 ns | 2.342e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:16777216` | 720489.574 ns | 2.329e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:25165824` | 1.071e+06 ns | 2.349e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:33554432` | 1.465e+06 ns | 2.292e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:67108864` | 3.039e+06 ns | 2.209e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:4096` | 173.564 ns | 2.361e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:65536` | 2742.209 ns | 2.390e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:1048576` | 44105.657 ns | 2.378e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:4194304` | 177183.814 ns | 2.368e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:16777216` | 708010.794 ns | 2.371e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:25165824` | 1.067e+06 ns | 2.362e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:33554432` | 1.459e+06 ns | 2.300e+10 | 1 |  |  |
| `bm_arena_alloc_reset/auto:1/block:67108864` | 3.038e+06 ns | 2.210e+10 | 1 |  |  |
| `BM_TokenizationThroughput/4` | 1343.685 us |  |  | 743817.006 | 1.344e-06 |
| `BM_TokenizationThroughput/8` | 1248.921 us |  |  | 800265.356 | 1.250e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1266.26 us |  |  | 789429.524 | 1.267e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1236.122 us |  |  | 808547.398 | 1.237e-06 |
| `BM_TokenizationThroughputNestedJson` | 1251.593 us |  |  | 798396.479 | 1.253e-06 |
| `BM_TokenizationThroughputFlatJson` | 554.013 us |  |  | 1.803e+06 | 5.547e-07 |

### `insight-metalog` — compression / MetaLog-document build

_38 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 198.801 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 257.442 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 51.59 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 82.417 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 92.069 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 4.922 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 4.722 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 5301.161 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 10455.086 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 15730.817 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 32190.198 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 65547.004 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 22120.377 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 55.065 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 29.067 us |  |  |  |  |  | 0 | 3.457e+07 | 2.892e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 39.599 us |  |  |  |  |  | 0 | 2.539e+07 | 3.939e-08 |
| `BM_CubeKeyAlloc_MidBand` | 40.297 us |  |  |  |  |  | 0 | 2.490e+07 | 4.016e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 41.099 us |  |  |  |  |  | 0 | 2.441e+07 | 4.097e-08 |
| `BM_MetaLogCompress/1000/16` | 0.888 ms |  |  |  |  |  |  | 1.126e+06 |  |
| `BM_MetaLogCompress/10000/16` | 2.897 ms |  |  |  |  |  |  | 3.452e+06 |  |
| `BM_MetaLogCompress/100000/16` | 12.901 ms |  |  |  |  |  |  | 7.751e+06 |  |
| `BM_MetaLogCompress/1000/32` | 0.953 ms |  |  |  |  |  |  | 1.050e+06 |  |
| `BM_MetaLogCompress/10000/32` | 2.868 ms |  |  |  |  |  |  | 3.487e+06 |  |
| `BM_MetaLogCompress/100000/32` | 12.583 ms |  |  |  |  |  |  | 7.947e+06 |  |
| `BM_MetaLogCompress/1000/64` | 0.952 ms |  |  |  |  |  |  | 1.051e+06 |  |
| `BM_MetaLogCompress/10000/64` | 2.865 ms |  |  |  |  |  |  | 3.491e+06 |  |
| `BM_MetaLogCompress/100000/64` | 12.628 ms |  |  |  |  |  |  | 7.919e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 27.144 us |  |  |  |  |  |  | 3.685e+07 | 2.714e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 42.873 us |  |  |  |  |  |  | 2.332e+07 | 4.287e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 74.899 us |  |  |  |  |  |  | 1.335e+07 | 7.490e-08 |
| `BM_MetaLogIngest_ParamSketch/0` | 30.118 ms |  |  |  |  |  |  | 3.320e+06 | 3.012e-07 |
| `BM_MetaLogIngest_ParamSketch/1` | 456.876 ms |  |  |  |  |  |  | 218877.446 | 4.569e-06 |
| `BM_MetaLogIngest_Where` | 58.11 us |  |  |  |  |  |  | 1.721e+07 | 5.811e-08 |
| `BM_OrdinalKeyAlloc_None` | 28.201 us |  |  |  |  |  | 0 | 3.563e+07 | 2.807e-08 |
| `BM_OrdinalKeyAlloc_Key15Sso` | 41.311 us |  |  |  |  |  | 0 | 2.428e+07 | 4.118e-08 |
| `BM_OrdinalKeyAlloc_Key16ShipLegOnly` | 39.851 us |  |  |  |  |  | 0 | 2.517e+07 | 3.973e-08 |
| `BM_OrdinalKeyAlloc_Key16TraceMix` | 43.814 us |  |  |  |  |  | 0 | 2.291e+07 | 4.364e-08 |
| `BM_OrdinalKeyAlloc_Key23OverBothSso` | 41.959 us |  |  |  |  |  | 0 | 2.390e+07 | 4.184e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 1978.533 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2393.562 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 6195.879 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 15699.493 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 247.827 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 314.165 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1716.02 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 2098.84 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 5745.251 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 868.328 us |  |  |  |  |  | 0.609 | 0 | 26508.657 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1717.874 us |  |  |  |  |  | 0.857 | 0 | 16299.4 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 6592.378 us |  |  |  |  |  | 0.857 | 0 | 4247.415 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 6529.133 us |  |  |  |  |  | 0.857 | 0 | 4288.501 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 79348.777 us |  |  |  |  |  | 0.98 | 0 | 2470.306 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 79311.181 us |  |  |  |  |  | 0.98 | 0 | 2471.273 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 171914.479 us |  |  |  |  |  | 0.971 | 6 | 1215.771 | 6 | 7 | 193 | 20 | 209 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 347674.936 us |  |  |  |  |  | 0.98 | 0 | 563.795 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 456.081 ns | 2.192e+06 |
| `BM_Pipeline_IngestBatch/64` | 34774.043 ns | 1.840e+06 |
| `BM_Pipeline_IngestBatch/1024` | 457494.003 ns | 2.236e+06 |
| `BM_Pipeline_CloseWindow/1000` | 20007.74 ns | 51045.99 |
| `BM_Pipeline_CloseWindow/10000` | 29328.164 ns | 35616.973 |
| `BM_Pipeline_FullWindow/1000` | 484253.871 ns | 2.065e+06 |
| `BM_Pipeline_FullWindow/10000` | 4.506e+06 ns | 2.220e+06 |

### `logcraft-core` — the deterministic log simulator core

_73 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | peak_frontier_window_frames | peak_window_frames | records | emit_ms | materialize_ms | capacity | ns_per_record | coordinates | ns_per_coordinate | discovered_knob_cap | build_coordinates | discovered_tower_cap | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 12.136 ms | 1 | 494412.94 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 67.679 ms | 4 | 354617.046 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 141.875 ms | 16 | 676650.755 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 65.937 ms | 4 | 363983.818 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 128.623 ms | 16 | 746367.966 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 1.565 ms | 1 | 319569.49 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 2.021 ms | 4 | 989693.247 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 4.367 ms | 16 | 1.832e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 13.502 ms | 64 | 2.370e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 47.725 ms | 256 | 2.682e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 12.508 ms | 32 | 1.279e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 8.512 ms | 32 | 1.880e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 6.789 ms | 32 | 2.357e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 7.534 ms | 32 | 2.124e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 3.053 ms | 16 | 2.621e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 4.346 ms | 16 | 1.841e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 4.917 ms | 16 | 1.627e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 4.838 ms | 16 | 1.654e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 5.779 ms | 16 | 1.384e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 7.672 ms | 16 | 1.043e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 10.266 ns |  | 9.741e+07 |  |  | 2.813e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 7.791 ns |  | 1.284e+08 |  |  | 6.675e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 8.033 ns |  | 1.246e+08 |  |  | 1.246e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.707 ns |  | 6.800e+07 |  |  | 8.007e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 5.074 ns |  | 1.974e+08 |  |  | 1.579e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 88.289 ns |  | 1.133e+07 |  |  | 2.152e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 70.593 ns |  | 1.417e+07 |  |  | 7.793e+07 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_IndexPass_Unmetered/iterations:1/real_time` | 445.952 ms |  |  |  |  |  | 25001 | 25000 | 1.800e+06 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_IndexPass_Metered/iterations:1/real_time` | 454.004 ms |  |  |  |  |  | 25001 | 25000 | 1.800e+06 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 404.635 ns |  | 2.471e+06 |  |  | 6.500e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 179.099 ns |  | 5.584e+06 |  |  | 1.016e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 276.226 ns |  | 3.623e+06 |  |  | 2.681e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 85.622 ns |  | 1.168e+07 |  |  | 6.307e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 124.714 ns |  | 8.021e+06 |  |  | 5.695e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 292.472 ns |  | 3.419e+06 |  |  | 6.838e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 444.637 ns |  | 2.249e+06 |  |  | 7.242e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 429.061 ns |  | 2.331e+06 |  |  | 1.622e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 341.703 ns |  | 2.929e+06 |  |  | 7.702e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 125.008 ns |  | 8.000e+06 |  |  | 1.456e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 247.389 ns |  | 4.042e+06 |  |  | 2.991e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 64.146 ns |  | 1.559e+07 |  |  | 8.418e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 101.078 ns |  | 9.894e+06 |  |  | 7.024e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 255.611 ns |  | 3.912e+06 |  |  | 7.824e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 380.969 ns |  | 2.625e+06 |  |  | 8.452e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 349.907 ns |  | 2.861e+06 |  |  | 1.991e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 10.89 ms | 1 |  | 6000 |  |  |  |  |  | 2.255 | 2.825 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 57.233 ms | 4 |  | 24000 |  |  |  |  |  | 41.349 | 8.681 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 106.164 ms | 16 |  | 96000 |  |  |  |  |  | 59.563 | 32.646 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 35660.348 us |  | 280719.216 |  |  |  |  |  |  |  |  | 8192 | 3.562e-06 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 33157.448 us |  | 303473.735 |  |  |  |  |  |  |  |  | 32768 | 3.295e-06 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 217.361 us |  | 3.777e+07 |  |  |  |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 862.49 us |  | 3.804e+07 |  |  |  |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate/real_time` | 321.81 us |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 3.218e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate_CiWorld/real_time` | 486.535 us |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 4.865e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisAtCap/real_time` | 30.829 ms |  |  |  |  |  |  |  |  |  |  |  |  | 64 | 4.817e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_TowerAtProductCap/real_time` | 175.997 ms |  |  |  |  |  |  |  |  |  |  |  |  | 256 | 6.875e-04 | 64 | 4 | 256 |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/2/real_time` | 594.022 us |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 2.970e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/4/real_time` | 1053.257 us |  |  |  |  |  |  |  |  |  |  |  |  | 4 | 2.633e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/8/real_time` | 2079.629 us |  |  |  |  |  |  |  |  |  |  |  |  | 8 | 2.600e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/16/real_time` | 4588.238 us |  |  |  |  |  |  |  |  |  |  |  |  | 16 | 2.868e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/32/real_time` | 11455.405 us |  |  |  |  |  |  |  |  |  |  |  |  | 32 | 3.580e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/64/real_time` | 31092.932 us |  |  |  |  |  |  |  |  |  |  |  |  | 64 | 4.858e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 6.686 ms |  | 2.991e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 1.113e+06 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 15.995 ms |  | 5.001e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 1.934e+06 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 123.323 ms |  | 648702.399 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 55499 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 152.214 ms |  | 2.102e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 497160 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 15.621 ms |  | 1.280e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 475 | 0 | 1 | 1.094e+08 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 38.338 ms |  | 2.087e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 3839 | 0 | 4 | 1.284e+09 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 166.819 ms |  | 479560.464 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 66 | 0 | 4 | 3.259e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 238.468 ms |  | 1.342e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 2739 | 0 | 16 | 2.629e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 7.109 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 7.199 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.005 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 32.314 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 31.796 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 32.468 ns | 65536 |
