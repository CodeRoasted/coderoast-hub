# benchmark summary — v1.9.1

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1718.084 us | 582021.522 | 1.718e-06 |
| `BM_TokenizationThroughput/8` | 1610.814 us | 620858.656 | 1.611e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1667.154 us | 599844.415 | 1.667e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1552.376 us | 644238.219 | 1.552e-06 |

### `insight-metalog` — compression / MetaLog-document build

_31 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 271.084 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 449.138 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 82.903 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 127.427 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 143.901 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 9.581 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 10.578 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 9084.898 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 18039.506 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 27000.488 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 54405.665 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 110180.062 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 35026.507 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 95.011 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 44.182 us |  |  |  |  |  | 0 | 2.267e+07 | 4.411e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 60.782 us |  |  |  |  |  | 0 | 1.648e+07 | 6.068e-08 |
| `BM_CubeKeyAlloc_MidBand` | 61.781 us |  |  |  |  |  | 0 | 1.621e+07 | 6.169e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 63.954 us |  |  |  |  |  | 0 | 1.566e+07 | 6.386e-08 |
| `BM_MetaLogCompress/1000/16` | 1.291 ms |  |  |  |  |  |  | 774472.841 |  |
| `BM_MetaLogCompress/10000/16` | 4.658 ms |  |  |  |  |  |  | 2.147e+06 |  |
| `BM_MetaLogCompress/100000/16` | 22.558 ms |  |  |  |  |  |  | 4.433e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.3 ms |  |  |  |  |  |  | 769288.943 |  |
| `BM_MetaLogCompress/10000/32` | 4.669 ms |  |  |  |  |  |  | 2.142e+06 |  |
| `BM_MetaLogCompress/100000/32` | 22.515 ms |  |  |  |  |  |  | 4.443e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.306 ms |  |  |  |  |  |  | 765729.002 |  |
| `BM_MetaLogCompress/10000/64` | 4.672 ms |  |  |  |  |  |  | 2.141e+06 |  |
| `BM_MetaLogCompress/100000/64` | 22.542 ms |  |  |  |  |  |  | 4.437e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 40.725 us |  |  |  |  |  |  | 2.456e+07 | 4.072e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 102.219 us |  |  |  |  |  |  | 9.784e+06 | 1.022e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 236.599 us |  |  |  |  |  |  | 4.227e+06 | 2.366e-07 |
| `BM_MetaLogIngest_Where` | 86.04 us |  |  |  |  |  |  | 1.162e+07 | 8.603e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3475.026 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4288.247 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 11000.017 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 27265.154 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 214.039 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 272.842 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3224.06 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 3942.356 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7570 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 477.359 us |  |  |  |  |  | 0.6 | 0 | 41904.387 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1184.891 us |  |  |  |  |  | 0.857 | 0 | 23631.407 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 4804.661 us |  |  |  |  |  | 0.857 | 0 | 5828.447 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 6901.504 us |  |  |  |  |  | 0.857 | 0 | 4057.205 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 77938.511 us |  |  |  |  |  | 0.98 | 0 | 2514.8 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 86320.212 us |  |  |  |  |  | 0.98 | 0 | 2270.953 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 127361.649 us |  |  |  |  |  | 0.98 | 6 | 1539.079 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 388616.599 us |  |  |  |  |  | 0.98 | 0 | 504.431 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 289.967 ns | 3.456e+06 |
| `BM_Pipeline_IngestBatch/64` | 24183.093 ns | 2.646e+06 |
| `BM_Pipeline_IngestBatch/1024` | 308067.118 ns | 3.323e+06 |
| `BM_Pipeline_CloseWindow/1000` | 15374.598 ns | 65503.787 |
| `BM_Pipeline_CloseWindow/10000` | 28682.492 ns | 35197.334 |
| `BM_Pipeline_FullWindow/1000` | 358305.002 ns | 2.791e+06 |
| `BM_Pipeline_FullWindow/10000` | 2.953e+06 ns | 3.386e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.047 ms | 1 | 745591.587 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 15.598 ms | 4 | 1.539e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 42.764 ms | 16 | 2.245e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 15.628 ms | 4 | 1.536e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 42.931 ms | 16 | 2.236e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.516 ms | 1 | 968072.83 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.676 ms | 4 | 2.959e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.51 ms | 16 | 5.297e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.037 ms | 64 | 6.353e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 16.554 ms | 256 | 7.732e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.501 ms | 32 | 3.555e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.8 ms | 32 | 5.715e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.766 ms | 32 | 5.785e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 2.757 ms | 32 | 5.803e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.097 ms | 32 | 5.166e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.444 ms | 16 | 5.539e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.615 ms | 16 | 4.954e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.578 ms | 16 | 5.070e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.144 ms | 16 | 3.731e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.847 ms | 16 | 2.810e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 3.905 ms | 16 | 2.049e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 10.924 ns |  | 9.154e+07 |  |  | 2.646e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 8.919 ns |  | 1.121e+08 |  |  | 5.830e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 16.852 ns |  | 5.934e+07 |  |  | 5.934e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.294 ns |  | 6.996e+07 |  |  | 8.242e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.467 ns |  | 2.239e+08 |  |  | 1.791e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 94.383 ns |  | 1.060e+07 |  |  | 2.013e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 80.91 ns |  | 1.236e+07 |  |  | 6.797e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 369.842 ns |  | 2.704e+06 |  |  | 7.111e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 170.806 ns |  | 5.855e+06 |  |  | 1.066e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 277.974 ns |  | 3.598e+06 |  |  | 2.662e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 88.766 ns |  | 1.127e+07 |  |  | 6.083e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 125.91 ns |  | 7.942e+06 |  |  | 5.639e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 284.805 ns |  | 3.511e+06 |  |  | 7.023e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 396.957 ns |  | 2.519e+06 |  |  | 8.112e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 383.076 ns |  | 2.610e+06 |  |  | 1.817e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 320.952 ns |  | 3.116e+06 |  |  | 8.194e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 122.471 ns |  | 8.165e+06 |  |  | 1.486e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 246.024 ns |  | 4.065e+06 |  |  | 3.008e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 66.191 ns |  | 1.511e+07 |  |  | 8.158e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 92.081 ns |  | 1.086e+07 |  |  | 7.711e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 234.198 ns |  | 4.270e+06 |  |  | 8.540e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 323.015 ns |  | 3.096e+06 |  |  | 9.969e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 315.455 ns |  | 3.170e+06 |  |  | 2.206e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 7.738 ms | 1 |  | 6000 |  |  | 4.876 | 1.665 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 15.448 ms | 4 |  | 24000 |  |  | 3.653 | 7.667 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 42.268 ms | 16 |  | 96000 |  |  | 8.984 | 14.047 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2794.979 us |  | 3.598e+06 |  |  |  |  |  | 8192 | 2.779e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2755.073 us |  | 3.650e+06 |  |  |  |  |  | 32768 | 2.739e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 206.014 us |  | 3.978e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 830.052 us |  | 3.948e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 6.056 ms |  | 3.303e+06 |  | 1 |  |  |  |  |  | 0 | 17079 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.543 ms |  | 4.836e+06 |  | 1 |  |  |  |  |  | 0 | 2719 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 18.966 ms |  | 4.218e+06 |  | 4 |  |  |  |  |  | 0 | 7824 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 39.426 ms |  | 8.117e+06 |  | 4 |  |  |  |  |  | 0 | 108101 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 55.144 ms |  | 5.803e+06 |  | 16 |  |  |  |  |  | 0 | 221159 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.689 ms |  | 2.990e+06 |  | 1 |  |  |  |  |  | 23 | 0 | 1 | 916400 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 18.233 ms |  | 4.388e+06 |  | 1 |  |  |  |  |  | 22 | 0 | 4 | 1.320e+06 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 40.184 ms |  | 1.991e+06 |  | 4 |  |  |  |  |  | 42 | 0 | 4 | 4.858e+06 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 43.835 ms |  | 7.300e+06 |  | 4 |  |  |  |  |  | 1163 | 0 | 16 | 1.446e+08 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 59.049 ms |  | 5.419e+06 |  | 16 |  |  |  |  |  | 1117 | 0 | 16 | 4.908e+08 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 4.664 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 4.632 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 82.105 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 82.18 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 82.111 ns | 65536 |
