# benchmark summary — v1.9.5

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_5 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 898.61 us | 1.113e+06 | 8.983e-07 |
| `BM_TokenizationThroughput/8` | 808.919 us | 1.236e+06 | 8.089e-07 |
| `BM_TokenizationThroughputDegenerate/4` | 826.773 us | 1.210e+06 | 8.268e-07 |
| `BM_TokenizationThroughputDegenerate/8` | 769.522 us | 1.300e+06 | 7.695e-07 |
| `BM_TokenizationThroughputNestedJson` | 1313.668 us | 761219.728 | 1.314e-06 |

### `insight-metalog` — compression / MetaLog-document build

_31 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 260.795 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 432.096 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 77.931 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 120.981 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 128.59 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 9.902 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 7.571 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 8881.603 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 17645.304 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 26376.179 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 53571.767 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 108638.552 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 37437.435 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 90.076 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 47.002 us |  |  |  |  |  | 0 | 2.132e+07 | 4.691e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 63.296 us |  |  |  |  |  | 0 | 1.582e+07 | 6.320e-08 |
| `BM_CubeKeyAlloc_MidBand` | 64.075 us |  |  |  |  |  | 0 | 1.563e+07 | 6.397e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 66.282 us |  |  |  |  |  | 0 | 1.511e+07 | 6.619e-08 |
| `BM_MetaLogCompress/1000/16` | 1.258 ms |  |  |  |  |  |  | 795024.536 |  |
| `BM_MetaLogCompress/10000/16` | 4.345 ms |  |  |  |  |  |  | 2.302e+06 |  |
| `BM_MetaLogCompress/100000/16` | 19.971 ms |  |  |  |  |  |  | 5.008e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.262 ms |  |  |  |  |  |  | 792711.77 |  |
| `BM_MetaLogCompress/10000/32` | 4.347 ms |  |  |  |  |  |  | 2.301e+06 |  |
| `BM_MetaLogCompress/100000/32` | 19.971 ms |  |  |  |  |  |  | 5.008e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.271 ms |  |  |  |  |  |  | 787088.452 |  |
| `BM_MetaLogCompress/10000/64` | 4.35 ms |  |  |  |  |  |  | 2.299e+06 |  |
| `BM_MetaLogCompress/100000/64` | 19.949 ms |  |  |  |  |  |  | 5.014e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 43.44 us |  |  |  |  |  |  | 2.302e+07 | 4.344e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 103.472 us |  |  |  |  |  |  | 9.666e+06 | 1.035e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 236.712 us |  |  |  |  |  |  | 4.225e+06 | 2.367e-07 |
| `BM_MetaLogIngest_Where` | 89.049 us |  |  |  |  |  |  | 1.123e+07 | 8.903e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3550.207 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4447.51 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 10956.549 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 26969.715 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 218.936 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 278.669 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3256.333 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 3958.019 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7602.202 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 483.429 us |  |  |  |  |  | 0.6 | 0 | 41371.376 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1208.292 us |  |  |  |  |  | 0.857 | 0 | 23173.159 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 4891.544 us |  |  |  |  |  | 0.857 | 0 | 5724.322 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7177.484 us |  |  |  |  |  | 0.857 | 0 | 3901.121 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 80851.807 us |  |  |  |  |  | 0.98 | 0 | 2424.222 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 89037.407 us |  |  |  |  |  | 0.98 | 0 | 2201.368 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 131448.496 us |  |  |  |  |  | 0.98 | 6 | 1491.075 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 401209.569 us |  |  |  |  |  | 0.98 | 0 | 488.522 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 339.828 ns | 2.941e+06 |
| `BM_Pipeline_IngestBatch/64` | 28095.337 ns | 2.277e+06 |
| `BM_Pipeline_IngestBatch/1024` | 356383.494 ns | 2.871e+06 |
| `BM_Pipeline_CloseWindow/1000` | 20391.982 ns | 49608.062 |
| `BM_Pipeline_CloseWindow/10000` | 33766.775 ns | 30372.005 |
| `BM_Pipeline_FullWindow/1000` | 443110.146 ns | 2.257e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.628e+06 ns | 2.756e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.599 ms | 1 | 697763.119 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 17.938 ms | 4 | 1.338e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 52.241 ms | 16 | 1.838e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 18.229 ms | 4 | 1.317e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 53.257 ms | 16 | 1.803e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.598 ms | 1 | 835719.85 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.74 ms | 4 | 2.704e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.672 ms | 16 | 4.785e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.85 ms | 64 | 5.470e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 20.412 ms | 256 | 6.271e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.622 ms | 32 | 3.461e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.998 ms | 32 | 5.338e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.89 ms | 32 | 5.537e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 3.199 ms | 32 | 5.001e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 4.803 ms | 32 | 3.331e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.791 ms | 16 | 4.468e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.876 ms | 16 | 4.265e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.812 ms | 16 | 4.416e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.228 ms | 16 | 3.590e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.99 ms | 16 | 2.675e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.314 ms | 16 | 1.854e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.047 ns |  | 9.052e+07 |  |  | 2.616e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.601 ns |  | 1.042e+08 |  |  | 5.416e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 18.067 ns |  | 5.535e+07 |  |  | 5.535e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 15.167 ns |  | 6.593e+07 |  |  | 7.756e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 5.095 ns |  | 1.963e+08 |  |  | 1.570e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 87.838 ns |  | 1.138e+07 |  |  | 2.163e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 83.938 ns |  | 1.191e+07 |  |  | 6.552e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 401.052 ns |  | 2.493e+06 |  |  | 6.558e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 181.936 ns |  | 5.496e+06 |  |  | 1.000e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 267.379 ns |  | 3.740e+06 |  |  | 2.768e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 91.624 ns |  | 1.091e+07 |  |  | 5.894e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 132.042 ns |  | 7.573e+06 |  |  | 5.377e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 300.762 ns |  | 3.325e+06 |  |  | 6.650e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 443.001 ns |  | 2.257e+06 |  |  | 7.269e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 432.663 ns |  | 2.311e+06 |  |  | 1.609e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 361.109 ns |  | 2.769e+06 |  |  | 7.283e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 127.244 ns |  | 7.859e+06 |  |  | 1.430e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 238.299 ns |  | 4.196e+06 |  |  | 3.105e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 68.191 ns |  | 1.466e+07 |  |  | 7.919e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 94.97 ns |  | 1.053e+07 |  |  | 7.476e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 266.526 ns |  | 3.752e+06 |  |  | 7.504e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 389.754 ns |  | 2.566e+06 |  |  | 8.261e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 357.711 ns |  | 2.796e+06 |  |  | 1.946e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.474 ms | 1 |  | 6000 |  |  | 5.235 | 1.81 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 16.624 ms | 4 |  | 24000 |  |  | 3.589 | 8.11 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 50.599 ms | 16 |  | 96000 |  |  | 11.162 | 16.392 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2555.618 us |  | 3.965e+06 |  |  |  |  |  | 8192 | 2.522e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2290.839 us |  | 4.425e+06 |  |  |  |  |  | 32768 | 2.260e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 217.367 us |  | 3.769e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 862.396 us |  | 3.799e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.765 ms |  | 3.469e+06 |  | 1 |  |  |  |  |  | 0 | 145737 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.107 ms |  | 4.967e+06 |  | 1 |  |  |  |  |  | 0 | 382422 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 39.147 ms |  | 2.044e+06 |  | 4 |  |  |  |  |  | 0 | 136840 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 54.252 ms |  | 5.898e+06 |  | 4 |  |  |  |  |  | 0 | 924690 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 80.389 ms |  | 3.981e+06 |  | 16 |  |  |  |  |  | 0 | 796363 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.394 ms |  | 3.128e+06 |  | 1 |  |  |  |  |  | 132 | 0 | 1 | 7.404e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 18.503 ms |  | 4.324e+06 |  | 1 |  |  |  |  |  | 955 | 0 | 4 | 1.954e+08 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 66.676 ms |  | 1.200e+06 |  | 4 |  |  |  |  |  | 546 | 0 | 4 | 7.005e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 102.451 ms |  | 3.123e+06 |  | 4 |  |  |  |  |  | 5743 | 0 | 16 | 4.726e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 102.994 ms |  | 3.107e+06 |  | 16 |  |  |  |  |  | 1644 | 0 | 16 | 2.267e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 6.318 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 11.309 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 35.974 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 36.641 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 37.115 ns | 65536 |
