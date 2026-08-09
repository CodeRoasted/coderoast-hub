# benchmark summary — v1.9.2

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_5 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1716.149 us | 582741.658 | 1.716e-06 |
| `BM_TokenizationThroughput/8` | 1591.979 us | 628169.084 | 1.592e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1667.645 us | 599694.676 | 1.668e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1546.574 us | 646595.011 | 1.547e-06 |
| `BM_TokenizationThroughputNestedJson` | 2634.311 us | 379605.321 | 2.634e-06 |

### `insight-metalog` — compression / MetaLog-document build

_31 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 251.224 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 418.686 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 81.89 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 128.237 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 147.213 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 9.064 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 8.421 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 8135.09 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 16170.981 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 24178.675 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 48755.644 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 99926.46 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 31004.636 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 92.444 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 45.176 us |  |  |  |  |  | 0 | 2.220e+07 | 4.505e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 60.05 us |  |  |  |  |  | 0 | 1.669e+07 | 5.991e-08 |
| `BM_CubeKeyAlloc_MidBand` | 62.729 us |  |  |  |  |  | 0 | 1.598e+07 | 6.260e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 66.155 us |  |  |  |  |  | 0 | 1.515e+07 | 6.602e-08 |
| `BM_MetaLogCompress/1000/16` | 1.28 ms |  |  |  |  |  |  | 781487.188 |  |
| `BM_MetaLogCompress/10000/16` | 4.695 ms |  |  |  |  |  |  | 2.130e+06 |  |
| `BM_MetaLogCompress/100000/16` | 23.854 ms |  |  |  |  |  |  | 4.193e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.285 ms |  |  |  |  |  |  | 778249.874 |  |
| `BM_MetaLogCompress/10000/32` | 4.708 ms |  |  |  |  |  |  | 2.124e+06 |  |
| `BM_MetaLogCompress/100000/32` | 23.878 ms |  |  |  |  |  |  | 4.188e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.293 ms |  |  |  |  |  |  | 773236.702 |  |
| `BM_MetaLogCompress/10000/64` | 4.716 ms |  |  |  |  |  |  | 2.121e+06 |  |
| `BM_MetaLogCompress/100000/64` | 23.846 ms |  |  |  |  |  |  | 4.194e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 43.236 us |  |  |  |  |  |  | 2.313e+07 | 4.323e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 103.59 us |  |  |  |  |  |  | 9.654e+06 | 1.036e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 232.773 us |  |  |  |  |  |  | 4.296e+06 | 2.328e-07 |
| `BM_MetaLogIngest_Where` | 93.397 us |  |  |  |  |  |  | 1.071e+07 | 9.339e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3553.945 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4265.034 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 10948.914 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 27355.742 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 215.83 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 273.889 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3237.107 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 3977.273 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7894.3 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 472.057 us |  |  |  |  |  | 0.6 | 0 | 42368.182 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1156.459 us |  |  |  |  |  | 0.857 | 0 | 24212.235 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 4794.054 us |  |  |  |  |  | 0.857 | 0 | 5840.661 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 6916.009 us |  |  |  |  |  | 0.857 | 0 | 4048.662 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 77909.577 us |  |  |  |  |  | 0.98 | 0 | 2515.781 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 86252.624 us |  |  |  |  |  | 0.98 | 0 | 2272.44 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 127205.579 us |  |  |  |  |  | 0.98 | 6 | 1540.827 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 388825.75 us |  |  |  |  |  | 0.98 | 0 | 504.091 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 354.631 ns | 2.819e+06 |
| `BM_Pipeline_IngestBatch/64` | 28473.206 ns | 2.248e+06 |
| `BM_Pipeline_IngestBatch/1024` | 371415.43 ns | 2.756e+06 |
| `BM_Pipeline_CloseWindow/1000` | 16289.539 ns | 61885.914 |
| `BM_Pipeline_CloseWindow/10000` | 30592.089 ns | 34106.122 |
| `BM_Pipeline_FullWindow/1000` | 421005.933 ns | 2.375e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.589e+06 ns | 2.786e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 7.975 ms | 1 | 752391.332 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 15.533 ms | 4 | 1.545e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 43.077 ms | 16 | 2.229e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 15.573 ms | 4 | 1.541e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 42.589 ms | 16 | 2.254e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.51 ms | 1 | 980777.185 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.667 ms | 4 | 3.000e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.524 ms | 16 | 5.249e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.069 ms | 64 | 6.313e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 16.991 ms | 256 | 7.534e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.503 ms | 32 | 3.553e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.773 ms | 32 | 5.770e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.752 ms | 32 | 5.814e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 2.733 ms | 32 | 5.854e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.051 ms | 32 | 5.243e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.446 ms | 16 | 5.532e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.609 ms | 16 | 4.971e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.532 ms | 16 | 5.221e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.14 ms | 16 | 3.738e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.777 ms | 16 | 2.881e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 3.863 ms | 16 | 2.071e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 10.922 ns |  | 9.156e+07 |  |  | 2.646e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 8.821 ns |  | 1.134e+08 |  |  | 5.895e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 17.105 ns |  | 5.846e+07 |  |  | 5.846e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.212 ns |  | 7.036e+07 |  |  | 8.285e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.444 ns |  | 2.250e+08 |  |  | 1.800e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 94.525 ns |  | 1.058e+07 |  |  | 2.010e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 79.726 ns |  | 1.254e+07 |  |  | 6.898e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 367.421 ns |  | 2.722e+06 |  |  | 7.158e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 169.736 ns |  | 5.892e+06 |  |  | 1.072e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 278.763 ns |  | 3.587e+06 |  |  | 2.655e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 88.552 ns |  | 1.129e+07 |  |  | 6.098e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 141.495 ns |  | 7.067e+06 |  |  | 5.018e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 283.95 ns |  | 3.522e+06 |  |  | 7.043e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 397.364 ns |  | 2.517e+06 |  |  | 8.103e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 385.955 ns |  | 2.591e+06 |  |  | 1.803e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 324.332 ns |  | 3.083e+06 |  |  | 8.109e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 122.283 ns |  | 8.178e+06 |  |  | 1.488e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 245.579 ns |  | 4.072e+06 |  |  | 3.013e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 66.326 ns |  | 1.508e+07 |  |  | 8.142e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 106.419 ns |  | 9.397e+06 |  |  | 6.672e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 235.56 ns |  | 4.245e+06 |  |  | 8.491e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 323.038 ns |  | 3.096e+06 |  |  | 9.968e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 314.457 ns |  | 3.180e+06 |  |  | 2.213e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 7.742 ms | 1 |  | 6000 |  |  | 4.882 | 1.663 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 15.497 ms | 4 |  | 24000 |  |  | 3.713 | 7.565 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 41.901 ms | 16 |  | 96000 |  |  | 8.683 | 14.166 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2769.033 us |  | 3.631e+06 |  |  |  |  |  | 8192 | 2.754e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2784.953 us |  | 3.611e+06 |  |  |  |  |  | 32768 | 2.770e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 208.685 us |  | 3.927e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 829.731 us |  | 3.950e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 6.093 ms |  | 3.282e+06 |  | 1 |  |  |  |  |  | 0 | 10510 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 17.109 ms |  | 4.676e+06 |  | 1 |  |  |  |  |  | 0 | 1872 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 20.221 ms |  | 3.956e+06 |  | 4 |  |  |  |  |  | 0 | 16880 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 41.721 ms |  | 7.670e+06 |  | 4 |  |  |  |  |  | 0 | 62590 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 50.144 ms |  | 6.382e+06 |  | 16 |  |  |  |  |  | 0 | 167771 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 7.683 ms |  | 2.603e+06 |  | 1 |  |  |  |  |  | 209 | 0 | 1 | 3.147e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 18.642 ms |  | 4.291e+06 |  | 1 |  |  |  |  |  | 14 | 0 | 4 | 1.289e+06 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 42.545 ms |  | 1.880e+06 |  | 4 |  |  |  |  |  | 19 | 0 | 4 | 795600 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 43.804 ms |  | 7.305e+06 |  | 4 |  |  |  |  |  | 2024 | 0 | 16 | 1.990e+08 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 61.61 ms |  | 5.194e+06 |  | 16 |  |  |  |  |  | 1615 | 0 | 16 | 6.118e+08 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 4.732 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 9.763 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 52.472 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 52.494 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 53.047 ns | 65536 |
