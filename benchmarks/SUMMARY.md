# benchmark summary — v1.10.10

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_38 benchmark(s)._

| benchmark | real_time | bytes_per_second | numa_blocks | items_per_second | s_per_line |
| --- | --- | --- | --- | --- | --- |
| `bm_arena_block_lifecycle/auto:0/block:4096` | 76.038 ns | 5.387e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:65536` | 475.721 ns | 1.378e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:1048576` | 8503.909 ns | 1.233e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:4194304` | 134090.427 ns | 3.128e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:16777216` | 532539.584 ns | 3.150e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:25165824` | 807792.093 ns | 3.115e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:33554432` | 1.998e+07 ns | 1.679e+09 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:0/block:67108864` | 4.194e+07 ns | 1.600e+09 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:4096` | 80.414 ns | 5.094e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:65536` | 471.959 ns | 1.389e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:1048576` | 8371.505 ns | 1.253e+11 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:4194304` | 132624.161 ns | 3.163e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:16777216` | 533567.589 ns | 3.144e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:25165824` | 800263.508 ns | 3.145e+10 | 0 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:33554432` | 1.996e+07 ns | 1.681e+09 | 1 |  |  |
| `bm_arena_block_lifecycle/auto:1/block:67108864` | 4.110e+07 ns | 1.633e+09 | 1 |  |  |
| `bm_arena_alloc_reset/auto:0/block:4096` | 151.059 ns | 2.712e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:65536` | 2391.074 ns | 2.741e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:1048576` | 38551.953 ns | 2.720e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:4194304` | 155380.894 ns | 2.699e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:16777216` | 619252.804 ns | 2.709e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:25165824` | 927352.552 ns | 2.714e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:33554432` | 1.290e+06 ns | 2.603e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:0/block:67108864` | 2.590e+06 ns | 2.591e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:4096` | 147.302 ns | 2.781e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:65536` | 2377.348 ns | 2.757e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:1048576` | 38613.748 ns | 2.716e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:4194304` | 158727.202 ns | 2.642e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:16777216` | 622175.16 ns | 2.697e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:25165824` | 927256.546 ns | 2.714e+10 | 0 |  |  |
| `bm_arena_alloc_reset/auto:1/block:33554432` | 1.260e+06 ns | 2.663e+10 | 1 |  |  |
| `bm_arena_alloc_reset/auto:1/block:67108864` | 2.594e+06 ns | 2.587e+10 | 1 |  |  |
| `BM_TokenizationThroughput/4` | 1187.156 us |  |  | 842049.599 | 1.188e-06 |
| `BM_TokenizationThroughput/8` | 1131.487 us |  |  | 883466.126 | 1.132e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1141.185 us |  |  | 875940.726 | 1.142e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1078.02 us |  |  | 927227.234 | 1.078e-06 |
| `BM_TokenizationThroughputNestedJson` | 1092.574 us |  |  | 914809.128 | 1.093e-06 |
| `BM_TokenizationThroughputFlatJson` | 453.297 us |  |  | 2.205e+06 | 4.536e-07 |

### `insight-metalog` — compression / MetaLog-document build

_40 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 187.025 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 246.877 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 45.023 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 70.496 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 76.012 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 4.858 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 4.402 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 5565.848 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 11042.983 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 15543.85 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 30568.707 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 63759.549 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 21597.451 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 50.675 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 28.09 us |  |  |  |  |  | 0 | 3.569e+07 | 2.802e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 36.443 us |  |  |  |  |  | 0 | 2.750e+07 | 3.636e-08 |
| `BM_CubeKeyAlloc_MidBand` | 46.511 us |  |  |  |  |  | 0 | 2.156e+07 | 4.639e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 69.117 us |  |  |  |  |  | 0 | 1.448e+07 | 6.904e-08 |
| `BM_MetaLogCompress/1000/16` | 0.789 ms |  |  |  |  |  |  | 1.267e+06 |  |
| `BM_MetaLogCompress/10000/16` | 2.528 ms |  |  |  |  |  |  | 3.956e+06 |  |
| `BM_MetaLogCompress/100000/16` | 11.752 ms |  |  |  |  |  |  | 8.509e+06 |  |
| `BM_MetaLogCompress/1000/32` | 0.757 ms |  |  |  |  |  |  | 1.321e+06 |  |
| `BM_MetaLogCompress/10000/32` | 2.528 ms |  |  |  |  |  |  | 3.956e+06 |  |
| `BM_MetaLogCompress/100000/32` | 11.773 ms |  |  |  |  |  |  | 8.494e+06 |  |
| `BM_MetaLogCompress/1000/64` | 0.742 ms |  |  |  |  |  |  | 1.348e+06 |  |
| `BM_MetaLogCompress/10000/64` | 2.544 ms |  |  |  |  |  |  | 3.930e+06 |  |
| `BM_MetaLogCompress/100000/64` | 11.795 ms |  |  |  |  |  |  | 8.478e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 25.639 us |  |  |  |  |  |  | 3.900e+07 | 2.564e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 52.419 us |  |  |  |  |  |  | 1.908e+07 | 5.242e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 97.149 us |  |  |  |  |  |  | 1.029e+07 | 9.715e-08 |
| `BM_MetaLogIngest_ParamSketch/0` | 33.49 ms |  |  |  |  |  |  | 2.986e+06 | 3.349e-07 |
| `BM_MetaLogIngest_ParamSketch/1` | 421.514 ms |  |  |  |  |  |  | 237239.626 | 4.215e-06 |
| `BM_MetaLogIngest_Where` | 70.551 us |  |  |  |  |  |  | 1.417e+07 | 7.055e-08 |
| `BM_MetaLogIngest_LongText/64` | 1261.641 us |  |  |  |  |  |  | 792617.368 | 1.262e-06 |
| `BM_MetaLogIngest_LongText/4096` | 961.602 us |  |  |  |  |  |  | 1.040e+06 | 9.616e-07 |
| `BM_OrdinalKeyAlloc_None` | 27.071 us |  |  |  |  |  | 0 | 3.704e+07 | 2.700e-08 |
| `BM_OrdinalKeyAlloc_Key15Sso` | 39.556 us |  |  |  |  |  | 0 | 2.534e+07 | 3.947e-08 |
| `BM_OrdinalKeyAlloc_Key16ShipLegOnly` | 37.77 us |  |  |  |  |  | 0 | 2.653e+07 | 3.769e-08 |
| `BM_OrdinalKeyAlloc_Key16TraceMix` | 40.6 us |  |  |  |  |  | 0 | 2.468e+07 | 4.052e-08 |
| `BM_OrdinalKeyAlloc_Key23OverBothSso` | 39.385 us |  |  |  |  |  | 0 | 2.545e+07 | 3.929e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 1793.788 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2178.573 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 5607.213 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 14262.355 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 227.108 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 281.723 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1559.254 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 1940.73 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 5295.681 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 797.708 us |  |  |  |  |  | 0.609 | 0 | 28832.814 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1527.531 us |  |  |  |  |  | 0.857 | 0 | 18330.507 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 5952.175 us |  |  |  |  |  | 0.857 | 0 | 4704.236 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 5944.559 us |  |  |  |  |  | 0.857 | 0 | 4710.225 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 71022.279 us |  |  |  |  |  | 0.98 | 0 | 2759.723 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 71809.859 us |  |  |  |  |  | 0.98 | 0 | 2729.453 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 154881.284 us |  |  |  |  |  | 0.971 | 6 | 1349.433 | 6 | 7 | 193 | 20 | 209 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 307580.446 us |  |  |  |  |  | 0.98 | 0 | 637.231 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 424.687 ns | 2.354e+06 |
| `BM_Pipeline_IngestBatch/64` | 33201.321 ns | 1.927e+06 |
| `BM_Pipeline_IngestBatch/1024` | 446442.05 ns | 2.293e+06 |
| `BM_Pipeline_CloseWindow/1000` | 16516.007 ns | 61300.546 |
| `BM_Pipeline_CloseWindow/10000` | 24028.372 ns | 42989.909 |
| `BM_Pipeline_FullWindow/1000` | 456798.444 ns | 2.189e+06 |
| `BM_Pipeline_FullWindow/10000` | 4.311e+06 ns | 2.319e+06 |

### `logcraft-core` — the deterministic log simulator core

_73 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | peak_frontier_window_frames | peak_window_frames | records | emit_ms | materialize_ms | capacity | ns_per_record | coordinates | ns_per_coordinate | discovered_knob_cap | build_coordinates | discovered_tower_cap | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 10.658 ms | 1 | 562949.611 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 61.401 ms | 4 | 390870.891 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 104.008 ms | 16 | 923002.817 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 53.758 ms | 4 | 446446.274 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 101.803 ms | 16 | 942996.062 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 1.351 ms | 1 | 370015.832 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 1.823 ms | 4 | 1.097e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 3.768 ms | 16 | 2.123e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 12.061 ms | 64 | 2.653e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 39.688 ms | 256 | 3.225e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 11.468 ms | 32 | 1.395e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 7.396 ms | 32 | 2.163e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 6.252 ms | 32 | 2.559e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 6.865 ms | 32 | 2.331e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 2.841 ms | 16 | 2.816e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 3.714 ms | 16 | 2.154e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 3.918 ms | 16 | 2.042e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 4.225 ms | 16 | 1.894e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 4.902 ms | 16 | 1.632e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 6.765 ms | 16 | 1.183e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 9.23 ns |  | 1.083e+08 |  |  | 3.129e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 7.221 ns |  | 1.385e+08 |  |  | 7.201e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 7.537 ns |  | 1.327e+08 |  |  | 1.327e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 13.829 ns |  | 7.231e+07 |  |  | 8.522e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.78 ns |  | 2.092e+08 |  |  | 1.674e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 76.393 ns |  | 1.309e+07 |  |  | 2.487e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 60.652 ns |  | 1.649e+07 |  |  | 9.070e+07 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_IndexPass_Unmetered/iterations:1/real_time` | 420.917 ms |  |  |  |  |  | 25001 | 25000 | 1.800e+06 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_IndexPass_Metered/iterations:1/real_time` | 388.023 ms |  |  |  |  |  | 25001 | 25000 | 1.800e+06 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 361.222 ns |  | 2.768e+06 |  |  | 7.281e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 165.357 ns |  | 6.048e+06 |  |  | 1.101e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 241.806 ns |  | 4.136e+06 |  |  | 3.060e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 85.47 ns |  | 1.170e+07 |  |  | 6.318e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 113.354 ns |  | 8.822e+06 |  |  | 6.264e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 287.752 ns |  | 3.475e+06 |  |  | 6.951e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 398.14 ns |  | 2.512e+06 |  |  | 8.088e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 393.435 ns |  | 2.542e+06 |  |  | 1.769e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 322.956 ns |  | 3.096e+06 |  |  | 8.144e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 117.306 ns |  | 8.525e+06 |  |  | 1.552e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 225.166 ns |  | 4.441e+06 |  |  | 3.287e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 59.902 ns |  | 1.669e+07 |  |  | 9.015e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 84.632 ns |  | 1.182e+07 |  |  | 8.389e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 245.483 ns |  | 4.074e+06 |  |  | 8.147e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 359.187 ns |  | 2.784e+06 |  |  | 8.965e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 341.744 ns |  | 2.926e+06 |  |  | 2.037e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 10.612 ms | 1 |  | 6000 |  |  |  |  |  | 2.212 | 2.814 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 54.174 ms | 4 |  | 24000 |  |  |  |  |  | 39.508 | 8.303 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 105.889 ms | 16 |  | 96000 |  |  |  |  |  | 61.745 | 30.811 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 8343.185 us |  | 1.199e+06 |  |  |  |  |  |  |  |  | 8192 | 8.341e-07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 5687.053 us |  | 1.759e+06 |  |  |  |  |  |  |  |  | 32768 | 5.685e-07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 204.371 us |  | 4.011e+07 |  |  |  |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 793.039 us |  | 4.133e+07 |  |  |  |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate/real_time` | 326.976 us |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 3.270e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate_CiWorld/real_time` | 488.421 us |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 4.884e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisAtCap/real_time` | 28.851 ms |  |  |  |  |  |  |  |  |  |  |  |  | 64 | 4.508e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_TowerAtProductCap/real_time` | 164.277 ms |  |  |  |  |  |  |  |  |  |  |  |  | 256 | 6.417e-04 | 64 | 4 | 256 |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/2/real_time` | 588.009 us |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 2.940e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/4/real_time` | 1017.876 us |  |  |  |  |  |  |  |  |  |  |  |  | 4 | 2.545e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/8/real_time` | 2001.366 us |  |  |  |  |  |  |  |  |  |  |  |  | 8 | 2.502e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/16/real_time` | 4359.528 us |  |  |  |  |  |  |  |  |  |  |  |  | 16 | 2.725e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/32/real_time` | 10571.771 us |  |  |  |  |  |  |  |  |  |  |  |  | 32 | 3.304e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/64/real_time` | 28742.496 us |  |  |  |  |  |  |  |  |  |  |  |  | 64 | 4.491e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 6.659 ms |  | 3.003e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 1.118e+06 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 17.213 ms |  | 4.648e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 1.808e+06 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 182.936 ms |  | 437311.757 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 76899 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 278.064 ms |  | 1.151e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 580949 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 17.143 ms |  | 1.167e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 475 | 0 | 1 | 9.932e+07 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 36.85 ms |  | 2.171e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 4100 | 0 | 4 | 1.370e+09 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 158.857 ms |  | 503599.096 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 85 | 0 | 4 | 3.885e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 295.334 ms |  | 1.084e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 3059 | 0 | 16 | 2.874e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 6.43 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 6.584 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.005 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 29.831 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 30.367 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 30.454 ns | 65536 |
