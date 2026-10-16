# benchmark summary — v1.10.7

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_37 benchmark(s)._

| benchmark | real_time | bytes_per_second | numa_blocks | items_per_second | s_per_line |
| --- | --- | --- | --- | --- | --- |
| `bm_arena_block_lifecycle/auto:0/block:4096` | 82.835 ns | 4.945e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:65536` | 511.159 ns | 1.282e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:1048576` | 9052.175 ns | 1.158e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:4194304` | 125450.987 ns | 3.343e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:16777216` | 532603.151 ns | 3.150e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:25165824` | 814881.687 ns | 3.088e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:33554432` | 2.188e+07 ns | 1.534e+09 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:67108864` | 4.384e+07 ns | 1.531e+09 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:4096` | 107.743 ns | 3.802e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:65536` | 509.743 ns | 1.286e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:1048576` | 9038.24 ns | 1.160e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:4194304` | 125019.159 ns | 3.355e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:16777216` | 548305.427 ns | 3.060e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:25165824` | 819630.142 ns | 3.070e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:33554432` | 2.129e+07 ns | 1.576e+09 | 1 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:67108864` | 4.433e+07 ns | 1.514e+09 | 1 |  |  |
| `bm_arena_alloc_reset/auto:0/block:4096` | 166.257 ns | 2.464e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:65536` | 2602.479 ns | 2.518e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:1048576` | 41929.188 ns | 2.501e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:4194304` | 166307.834 ns | 2.522e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:16777216` | 662008.288 ns | 2.534e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:25165824` | 1.007e+06 ns | 2.500e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:33554432` | 1.374e+06 ns | 2.441e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:67108864` | 2.835e+06 ns | 2.368e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:4096` | 167.155 ns | 2.450e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:65536` | 2551.933 ns | 2.568e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:1048576` | 41931.798 ns | 2.501e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:4194304` | 165853.946 ns | 2.529e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:16777216` | 668955.575 ns | 2.508e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:25165824` | 994282.194 ns | 2.531e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:33554432` | 1.372e+06 ns | 2.446e+10 | 1 |  |  |
| `bm_arena_alloc_reset/auto:1/block:67108864` | 2.826e+06 ns | 2.375e+10 | 1 |  |  |
| `BM_TokenizationThroughput/4` | 1222.887 us |  |  | 817378.991 | 1.223e-06 |
| `BM_TokenizationThroughput/8` | 1176.485 us |  |  | 849631.312 | 1.177e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1165.629 us |  |  | 857538.843 | 1.166e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1139.205 us |  |  | 877520.925 | 1.140e-06 |
| `BM_TokenizationThroughputNestedJson` | 1672.083 us |  |  | 597812.875 | 1.673e-06 |

### `insight-metalog` — compression / MetaLog-document build

_38 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 183.836 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 257.295 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 53.661 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 84.013 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 96.346 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 4.779 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 4.872 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 5422.498 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 10560.565 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 16042.18 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 32004.86 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 67428.304 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 22603.794 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 55.205 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 29.734 us |  |  |  |  |  | 0 | 3.374e+07 | 2.964e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 39.353 us |  |  |  |  |  | 0 | 2.546e+07 | 3.928e-08 |
| `BM_CubeKeyAlloc_MidBand` | 40.066 us |  |  |  |  |  | 0 | 2.501e+07 | 3.998e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 41.034 us |  |  |  |  |  | 0 | 2.443e+07 | 4.093e-08 |
| `BM_MetaLogCompress/1000/16` | 0.862 ms |  |  |  |  |  |  | 1.160e+06 |  |
| `BM_MetaLogCompress/10000/16` | 2.772 ms |  |  |  |  |  |  | 3.607e+06 |  |
| `BM_MetaLogCompress/100000/16` | 12.349 ms |  |  |  |  |  |  | 8.098e+06 |  |
| `BM_MetaLogCompress/1000/32` | 0.886 ms |  |  |  |  |  |  | 1.129e+06 |  |
| `BM_MetaLogCompress/10000/32` | 2.758 ms |  |  |  |  |  |  | 3.626e+06 |  |
| `BM_MetaLogCompress/100000/32` | 12.558 ms |  |  |  |  |  |  | 7.963e+06 |  |
| `BM_MetaLogCompress/1000/64` | 0.915 ms |  |  |  |  |  |  | 1.093e+06 |  |
| `BM_MetaLogCompress/10000/64` | 2.841 ms |  |  |  |  |  |  | 3.520e+06 |  |
| `BM_MetaLogCompress/100000/64` | 12.59 ms |  |  |  |  |  |  | 7.943e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 26.965 us |  |  |  |  |  |  | 3.709e+07 | 2.696e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 43.938 us |  |  |  |  |  |  | 2.276e+07 | 4.394e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 75.095 us |  |  |  |  |  |  | 1.332e+07 | 7.509e-08 |
| `BM_MetaLogIngest_ParamSketch/0` | 29.52 ms |  |  |  |  |  |  | 3.388e+06 | 2.952e-07 |
| `BM_MetaLogIngest_ParamSketch/1` | 444.236 ms |  |  |  |  |  |  | 225105.201 | 4.442e-06 |
| `BM_MetaLogIngest_Where` | 57.439 us |  |  |  |  |  |  | 1.741e+07 | 5.744e-08 |
| `BM_OrdinalKeyAlloc_None` | 28.199 us |  |  |  |  |  | 0 | 3.558e+07 | 2.811e-08 |
| `BM_OrdinalKeyAlloc_Key15Sso` | 40.825 us |  |  |  |  |  | 0 | 2.455e+07 | 4.074e-08 |
| `BM_OrdinalKeyAlloc_Key16ShipLegOnly` | 39.888 us |  |  |  |  |  | 0 | 2.513e+07 | 3.979e-08 |
| `BM_OrdinalKeyAlloc_Key16TraceMix` | 43.97 us |  |  |  |  |  | 0 | 2.279e+07 | 4.388e-08 |
| `BM_OrdinalKeyAlloc_Key23OverBothSso` | 42.232 us |  |  |  |  |  | 0 | 2.374e+07 | 4.213e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 1971.161 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2344.793 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 6063.693 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 15151.876 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 232.608 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 288.116 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1719.1 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 2089.216 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 5610.092 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 767.422 us |  |  |  |  |  | 0.609 | 0 | 29971.068 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1460.971 us |  |  |  |  |  | 0.857 | 0 | 19165.44 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 5966.22 us |  |  |  |  |  | 0.857 | 0 | 4693.254 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 5864.09 us |  |  |  |  |  | 0.857 | 0 | 4774.819 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 70128.318 us |  |  |  |  |  | 0.98 | 0 | 2794.904 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 70523.825 us |  |  |  |  |  | 0.98 | 0 | 2779.373 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 161703.502 us |  |  |  |  |  | 0.971 | 6 | 1292.539 | 6 | 7 | 193 | 20 | 209 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 309751.989 us |  |  |  |  |  | 0.98 | 0 | 632.797 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 424.885 ns | 2.353e+06 |
| `BM_Pipeline_IngestBatch/64` | 34327.052 ns | 1.864e+06 |
| `BM_Pipeline_IngestBatch/1024` | 445847.106 ns | 2.295e+06 |
| `BM_Pipeline_CloseWindow/1000` | 19027.668 ns | 53226.937 |
| `BM_Pipeline_CloseWindow/10000` | 27806.833 ns | 36887.496 |
| `BM_Pipeline_FullWindow/1000` | 456773.912 ns | 2.189e+06 |
| `BM_Pipeline_FullWindow/10000` | 4.284e+06 ns | 2.334e+06 |

### `logcraft-core` — the deterministic log simulator core

_73 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | peak_frontier_window_frames | peak_window_frames | records | emit_ms | materialize_ms | capacity | ns_per_record | coordinates | ns_per_coordinate | discovered_knob_cap | build_coordinates | discovered_tower_cap | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 9.531 ms | 1 | 629501.302 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 17.517 ms | 4 | 1.370e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 42.393 ms | 16 | 2.265e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 17.101 ms | 4 | 1.403e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 41.987 ms | 16 | 2.286e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.53 ms | 1 | 942876.482 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.701 ms | 4 | 2.854e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.814 ms | 16 | 4.410e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.908 ms | 64 | 5.416e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 21.219 ms | 256 | 6.032e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.6 ms | 32 | 3.478e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.895 ms | 32 | 5.526e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.839 ms | 32 | 5.635e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 3.088 ms | 32 | 5.182e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 0.941 ms | 16 | 8.499e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.532 ms | 16 | 5.220e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.704 ms | 16 | 4.695e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.412 ms | 16 | 3.317e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 3.541 ms | 16 | 2.259e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 5.214 ms | 16 | 1.534e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 9.302 ns |  | 1.075e+08 |  |  | 3.104e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 10.172 ns |  | 9.831e+07 |  |  | 5.112e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 7.774 ns |  | 1.286e+08 |  |  | 1.286e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.116 ns |  | 7.084e+07 |  |  | 8.347e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.732 ns |  | 2.113e+08 |  |  | 1.691e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 83.479 ns |  | 1.198e+07 |  |  | 2.276e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 66.353 ns |  | 1.507e+07 |  |  | 8.291e+07 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_IndexPass_Unmetered/iterations:1/real_time` | 399.928 ms |  |  |  |  |  | 25001 | 25000 | 1.800e+06 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_IndexPass_Metered/iterations:1/real_time` | 411.026 ms |  |  |  |  |  | 25001 | 25000 | 1.800e+06 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 378.765 ns |  | 2.640e+06 |  |  | 6.944e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 171.18 ns |  | 5.842e+06 |  |  | 1.063e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 254.534 ns |  | 3.929e+06 |  |  | 2.907e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 83.429 ns |  | 1.199e+07 |  |  | 6.473e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 120.524 ns |  | 8.297e+06 |  |  | 5.891e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 283.284 ns |  | 3.530e+06 |  |  | 7.060e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 425.101 ns |  | 2.352e+06 |  |  | 7.575e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 418.78 ns |  | 2.388e+06 |  |  | 1.662e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 331.02 ns |  | 3.021e+06 |  |  | 7.945e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 122.535 ns |  | 8.161e+06 |  |  | 1.485e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 226.421 ns |  | 4.417e+06 |  |  | 3.268e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 62.642 ns |  | 1.596e+07 |  |  | 8.621e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 88.504 ns |  | 1.130e+07 |  |  | 8.022e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 250.577 ns |  | 3.991e+06 |  |  | 7.982e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 363.248 ns |  | 2.753e+06 |  |  | 8.864e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 348.536 ns |  | 2.869e+06 |  |  | 1.997e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 9.278 ms | 1 |  | 6000 |  |  |  |  |  | 6.15 | 1.78 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 17.56 ms | 4 |  | 24000 |  |  |  |  |  | 9.376 | 5.396 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 40.542 ms | 16 |  | 96000 |  |  |  |  |  | 19.432 | 13.074 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2718.497 us |  | 3.697e+06 |  |  |  |  |  |  |  |  | 8192 | 2.705e-07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2641.744 us |  | 3.814e+06 |  |  |  |  |  |  |  |  | 32768 | 2.622e-07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 232.551 us |  | 3.524e+07 |  |  |  |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 839.8 us |  | 3.903e+07 |  |  |  |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate/real_time` | 155.95 us |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 1.560e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate_CiWorld/real_time` | 305.903 us |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 3.059e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisAtCap/real_time` | 28.629 ms |  |  |  |  |  |  |  |  |  |  |  |  | 64 | 4.473e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_TowerAtProductCap/real_time` | 162.892 ms |  |  |  |  |  |  |  |  |  |  |  |  | 256 | 6.363e-04 | 64 | 4 | 256 |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/2/real_time` | 398.191 us |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 1.991e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/4/real_time` | 810.107 us |  |  |  |  |  |  |  |  |  |  |  |  | 4 | 2.025e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/8/real_time` | 1757.661 us |  |  |  |  |  |  |  |  |  |  |  |  | 8 | 2.197e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/16/real_time` | 4142.323 us |  |  |  |  |  |  |  |  |  |  |  |  | 16 | 2.589e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/32/real_time` | 10391.134 us |  |  |  |  |  |  |  |  |  |  |  |  | 32 | 3.247e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/64/real_time` | 29395.126 us |  |  |  |  |  |  |  |  |  |  |  |  | 64 | 4.593e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.696 ms |  | 3.511e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 53659 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.438 ms |  | 4.867e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 8531 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 19.665 ms |  | 4.068e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 711 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 40.126 ms |  | 7.975e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 42383 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.304 ms |  | 3.173e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 52 | 0 | 1 | 3.778e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 17.591 ms |  | 4.548e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 126 | 0 | 4 | 1.351e+07 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 20.558 ms |  | 3.891e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 8 | 0 | 4 | 894230 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 42.136 ms |  | 7.594e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 1419 | 0 | 16 | 3.904e+08 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 5.023 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 5.049 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.005 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 29.985 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 30.702 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 31.49 ns | 65536 |
