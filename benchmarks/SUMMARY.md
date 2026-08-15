# benchmark summary — v1.9.3

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_5 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1627.903 us | 614434.728 | 1.628e-06 |
| `BM_TokenizationThroughput/8` | 1500.734 us | 666431.344 | 1.501e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1564.475 us | 639115.738 | 1.565e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1442.298 us | 693206.612 | 1.443e-06 |
| `BM_TokenizationThroughputNestedJson` | 2471.682 us | 404559.41 | 2.472e-06 |

### `insight-metalog` — compression / MetaLog-document build

_31 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 252.555 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 419.226 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 82.543 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 128.962 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 147.659 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 8.993 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 8.418 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 8136.45 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 16171.451 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 24196.309 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 48966.065 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 99448.315 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 30980.093 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 86.101 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 45.116 us |  |  |  |  |  | 0 | 2.222e+07 | 4.501e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 59.763 us |  |  |  |  |  | 0 | 1.677e+07 | 5.965e-08 |
| `BM_CubeKeyAlloc_MidBand` | 62.395 us |  |  |  |  |  | 0 | 1.606e+07 | 6.228e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 65.766 us |  |  |  |  |  | 0 | 1.523e+07 | 6.565e-08 |
| `BM_MetaLogCompress/1000/16` | 1.246 ms |  |  |  |  |  |  | 802557.659 |  |
| `BM_MetaLogCompress/10000/16` | 4.52 ms |  |  |  |  |  |  | 2.213e+06 |  |
| `BM_MetaLogCompress/100000/16` | 22.186 ms |  |  |  |  |  |  | 4.508e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.253 ms |  |  |  |  |  |  | 798533.844 |  |
| `BM_MetaLogCompress/10000/32` | 4.509 ms |  |  |  |  |  |  | 2.218e+06 |  |
| `BM_MetaLogCompress/100000/32` | 22.149 ms |  |  |  |  |  |  | 4.515e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.258 ms |  |  |  |  |  |  | 795042.942 |  |
| `BM_MetaLogCompress/10000/64` | 4.518 ms |  |  |  |  |  |  | 2.214e+06 |  |
| `BM_MetaLogCompress/100000/64` | 22.16 ms |  |  |  |  |  |  | 4.513e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 43.369 us |  |  |  |  |  |  | 2.306e+07 | 4.336e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 105.051 us |  |  |  |  |  |  | 9.520e+06 | 1.050e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 234.982 us |  |  |  |  |  |  | 4.256e+06 | 2.349e-07 |
| `BM_MetaLogIngest_Where` | 92.902 us |  |  |  |  |  |  | 1.077e+07 | 9.288e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3928.5 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4844.701 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 12143.216 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 29779.449 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 235.849 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 295.948 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3610.519 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4290.349 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7671.935 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 515.963 us |  |  |  |  |  | 0.6 | 0 | 38763.997 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1318.376 us |  |  |  |  |  | 0.857 | 0 | 21238.419 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 5285.37 us |  |  |  |  |  | 0.857 | 0 | 5297.634 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7664.644 us |  |  |  |  |  | 0.857 | 0 | 3653.181 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 86014.18 us |  |  |  |  |  | 0.98 | 0 | 2278.745 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 95761.719 us |  |  |  |  |  | 0.98 | 0 | 2046.768 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 158057.892 us |  |  |  |  |  | 0.98 | 6 | 1240.132 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 461745.88 us |  |  |  |  |  | 0.98 | 0 | 424.494 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 406.771 ns | 2.458e+06 |
| `BM_Pipeline_IngestBatch/64` | 32959.925 ns | 1.943e+06 |
| `BM_Pipeline_IngestBatch/1024` | 419431.293 ns | 2.440e+06 |
| `BM_Pipeline_CloseWindow/1000` | 22380.876 ns | 45330.245 |
| `BM_Pipeline_CloseWindow/10000` | 37728.887 ns | 26739.161 |
| `BM_Pipeline_FullWindow/1000` | 441494.124 ns | 2.265e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.756e+06 ns | 2.662e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.361 ms | 1 | 717633.273 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 16.55 ms | 4 | 1.450e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 48.119 ms | 16 | 1.995e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 16.242 ms | 4 | 1.478e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 46.695 ms | 16 | 2.056e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.548 ms | 1 | 912471.335 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.658 ms | 4 | 3.040e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.549 ms | 16 | 5.163e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.349 ms | 64 | 5.982e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 18.291 ms | 256 | 6.998e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.556 ms | 32 | 3.512e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.865 ms | 32 | 5.585e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.717 ms | 32 | 5.890e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 2.809 ms | 32 | 5.696e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.48 ms | 32 | 4.597e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.499 ms | 16 | 5.335e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.629 ms | 16 | 4.912e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.563 ms | 16 | 5.119e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.039 ms | 16 | 3.923e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.803 ms | 16 | 2.854e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.079 ms | 16 | 1.961e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.036 ns |  | 9.061e+07 |  |  | 2.619e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.193 ns |  | 1.088e+08 |  |  | 5.656e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 17.276 ns |  | 5.788e+07 |  |  | 5.788e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.804 ns |  | 6.755e+07 |  |  | 7.953e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.62 ns |  | 2.164e+08 |  |  | 1.731e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 95.874 ns |  | 1.043e+07 |  |  | 1.982e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 83.084 ns |  | 1.204e+07 |  |  | 6.620e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 377.052 ns |  | 2.652e+06 |  |  | 6.975e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 177.474 ns |  | 5.635e+06 |  |  | 1.025e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 291.627 ns |  | 3.429e+06 |  |  | 2.538e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 94.814 ns |  | 1.055e+07 |  |  | 5.695e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 129.452 ns |  | 7.725e+06 |  |  | 5.485e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 296.538 ns |  | 3.372e+06 |  |  | 6.744e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 406.733 ns |  | 2.459e+06 |  |  | 7.917e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 395.503 ns |  | 2.528e+06 |  |  | 1.760e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 338.736 ns |  | 2.952e+06 |  |  | 7.764e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 124.507 ns |  | 8.032e+06 |  |  | 1.462e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 261.78 ns |  | 3.820e+06 |  |  | 2.827e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 69.68 ns |  | 1.435e+07 |  |  | 7.750e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 96.639 ns |  | 1.035e+07 |  |  | 7.347e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 250.725 ns |  | 3.988e+06 |  |  | 7.977e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 335.758 ns |  | 2.978e+06 |  |  | 9.590e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 325.349 ns |  | 3.074e+06 |  |  | 2.139e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.269 ms | 1 |  | 6000 |  |  | 5.147 | 1.82 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 16.198 ms | 4 |  | 24000 |  |  | 3.348 | 8.14 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 45.811 ms | 16 |  | 96000 |  |  | 10.168 | 14.818 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2822.579 us |  | 3.572e+06 |  |  |  |  |  | 8192 | 2.799e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2570.183 us |  | 3.938e+06 |  |  |  |  |  | 32768 | 2.539e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 211.88 us |  | 3.868e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 844.987 us |  | 3.879e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.772 ms |  | 3.465e+06 |  | 1 |  |  |  |  |  | 0 | 107350 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.488 ms |  | 4.852e+06 |  | 1 |  |  |  |  |  | 0 | 37066 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 22.22 ms |  | 3.600e+06 |  | 4 |  |  |  |  |  | 0 | 40835 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 45.115 ms |  | 7.093e+06 |  | 4 |  |  |  |  |  | 0 | 318215 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 60.278 ms |  | 5.309e+06 |  | 16 |  |  |  |  |  | 0 | 381212 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 7.299 ms |  | 2.740e+06 |  | 1 |  |  |  |  |  | 328 | 0 | 1 | 7.829e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 17.841 ms |  | 4.484e+06 |  | 1 |  |  |  |  |  | 436 | 0 | 4 | 2.658e+07 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 54.515 ms |  | 1.467e+06 |  | 4 |  |  |  |  |  | 197 | 0 | 4 | 1.110e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 51.737 ms |  | 6.185e+06 |  | 4 |  |  |  |  |  | 3279 | 0 | 16 | 9.087e+08 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 69.392 ms |  | 4.612e+06 |  | 16 |  |  |  |  |  | 1351 | 0 | 16 | 7.916e+08 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 5.231 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 10.265 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 81.705 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 82.076 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 82.004 ns | 65536 |
