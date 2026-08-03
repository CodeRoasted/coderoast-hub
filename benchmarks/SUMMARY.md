# benchmark summary — v1.9.0

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1672.97 us | 597754.34 | 1.673e-06 |
| `BM_TokenizationThroughput/8` | 1537.154 us | 650442.533 | 1.537e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1616.346 us | 618689.048 | 1.616e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1501.888 us | 665762.65 | 1.502e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 253.538 us |  |  |  |  |  |  |  |
| `BM_Diff` | 421 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 82.527 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 129.624 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 145.935 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 8.938 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 8.651 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 8134.828 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 16165.484 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 24186.194 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 48918.481 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 99265.214 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 31002.073 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 84.117 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.26 ms |  |  |  |  |  | 793511.512 |  |
| `BM_MetaLogCompress/10000/16` | 4.504 ms |  |  |  |  |  | 2.220e+06 |  |
| `BM_MetaLogCompress/100000/16` | 22.006 ms |  |  |  |  |  | 4.545e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.264 ms |  |  |  |  |  | 791322.837 |  |
| `BM_MetaLogCompress/10000/32` | 4.492 ms |  |  |  |  |  | 2.227e+06 |  |
| `BM_MetaLogCompress/100000/32` | 22.004 ms |  |  |  |  |  | 4.545e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.269 ms |  |  |  |  |  | 787889.773 |  |
| `BM_MetaLogCompress/10000/64` | 4.508 ms |  |  |  |  |  | 2.218e+06 |  |
| `BM_MetaLogCompress/100000/64` | 22.099 ms |  |  |  |  |  | 4.526e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 53.727 us |  |  |  |  |  | 1.861e+07 | 5.372e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 118.941 us |  |  |  |  |  | 8.408e+06 | 1.189e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 250.678 us |  |  |  |  |  | 3.989e+06 | 2.507e-07 |
| `BM_MetaLogIngest_Where` | 125.018 us |  |  |  |  |  | 7.999e+06 | 1.250e-07 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3524.027 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4268.533 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 10940.976 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 27443.838 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 214.934 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 273.721 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3206.314 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 3939.372 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7408.1 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 471.99 us |  |  |  |  |  | 0.6 | 0 | 42374.121 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1165.84 us |  |  |  |  |  | 0.857 | 0 | 24017.164 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 4755.903 us |  |  |  |  |  | 0.857 | 0 | 5887.408 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 6898.12 us |  |  |  |  |  | 0.857 | 0 | 4059.069 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 77602.61 us |  |  |  |  |  | 0.98 | 0 | 2525.683 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 86323.474 us |  |  |  |  |  | 0.98 | 0 | 2270.572 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 126994.459 us |  |  |  |  |  | 0.98 | 6 | 1543.406 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 386999.147 us |  |  |  |  |  | 0.98 | 0 | 506.461 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 314.179 ns | 3.182e+06 |
| `BM_Pipeline_IngestBatch/64` | 25588.045 ns | 2.501e+06 |
| `BM_Pipeline_IngestBatch/1024` | 331528.497 ns | 3.088e+06 |
| `BM_Pipeline_CloseWindow/1000` | 16000.805 ns | 62956.234 |
| `BM_Pipeline_CloseWindow/10000` | 31180.099 ns | 33189.424 |
| `BM_Pipeline_FullWindow/1000` | 377705.082 ns | 2.648e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.201e+06 ns | 3.124e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 7.814 ms | 1 | 767864.119 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 15.566 ms | 4 | 1.542e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 42.428 ms | 16 | 2.263e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 15.544 ms | 4 | 1.544e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 43.129 ms | 16 | 2.226e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.505 ms | 1 | 990994.485 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.662 ms | 4 | 3.019e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.527 ms | 16 | 5.238e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.078 ms | 64 | 6.302e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 16.916 ms | 256 | 7.567e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.439 ms | 32 | 3.604e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.804 ms | 32 | 5.706e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.771 ms | 32 | 5.774e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 2.728 ms | 32 | 5.865e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.057 ms | 32 | 5.233e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.44 ms | 16 | 5.557e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.621 ms | 16 | 4.934e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.529 ms | 16 | 5.232e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.147 ms | 16 | 3.725e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.807 ms | 16 | 2.850e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 3.895 ms | 16 | 2.054e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 10.927 ns |  | 9.153e+07 |  |  | 2.645e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 8.931 ns |  | 1.120e+08 |  |  | 5.823e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 16.934 ns |  | 5.906e+07 |  |  | 5.906e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.324 ns |  | 6.981e+07 |  |  | 8.223e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.347 ns |  | 2.300e+08 |  |  | 1.840e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 93.069 ns |  | 1.074e+07 |  |  | 2.042e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 80.027 ns |  | 1.250e+07 |  |  | 6.873e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 366.711 ns |  | 2.727e+06 |  |  | 7.173e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 170.562 ns |  | 5.863e+06 |  |  | 1.067e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 276.121 ns |  | 3.622e+06 |  |  | 2.680e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 88.711 ns |  | 1.128e+07 |  |  | 6.089e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 125.004 ns |  | 8.001e+06 |  |  | 5.681e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 284.776 ns |  | 3.512e+06 |  |  | 7.024e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 401.117 ns |  | 2.493e+06 |  |  | 8.028e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 381.629 ns |  | 2.620e+06 |  |  | 1.824e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 323.235 ns |  | 3.094e+06 |  |  | 8.136e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 123.948 ns |  | 8.069e+06 |  |  | 1.469e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 247.731 ns |  | 4.038e+06 |  |  | 2.988e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 66.617 ns |  | 1.501e+07 |  |  | 8.106e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 92.872 ns |  | 1.077e+07 |  |  | 7.646e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 235.297 ns |  | 4.251e+06 |  |  | 8.501e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 326.152 ns |  | 3.066e+06 |  |  | 9.873e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 312.217 ns |  | 3.203e+06 |  |  | 2.230e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 7.717 ms | 1 |  | 6000 |  |  | 4.859 | 1.663 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 15.319 ms | 4 |  | 24000 |  |  | 3.643 | 7.612 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 41.365 ms | 16 |  | 96000 |  |  | 8.65 | 13.818 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2749.249 us |  | 3.658e+06 |  |  |  |  |  | 8192 | 2.734e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2732.718 us |  | 3.682e+06 |  |  |  |  |  | 32768 | 2.716e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 206.395 us |  | 3.970e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 835.452 us |  | 3.923e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 6.018 ms |  | 3.323e+06 |  | 1 |  |  |  |  |  | 0 | 18982 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.672 ms |  | 4.799e+06 |  | 1 |  |  |  |  |  | 0 | 4393 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 17.714 ms |  | 4.516e+06 |  | 4 |  |  |  |  |  | 0 | 25713 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 39.65 ms |  | 8.071e+06 |  | 4 |  |  |  |  |  | 0 | 129038 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 48.935 ms |  | 6.539e+06 |  | 16 |  |  |  |  |  | 0 | 266974 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.59 ms |  | 3.035e+06 |  | 1 |  |  |  |  |  | 15 | 0 | 1 | 993900 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 16.44 ms |  | 4.866e+06 |  | 1 |  |  |  |  |  | 47 | 0 | 4 | 3.673e+06 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 16.798 ms |  | 4.762e+06 |  | 4 |  |  |  |  |  | 63 | 0 | 4 | 5.739e+06 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 40.824 ms |  | 7.838e+06 |  | 4 |  |  |  |  |  | 4300 | 0 | 16 | 3.726e+08 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 54.211 ms |  | 5.903e+06 |  | 16 |  |  |  |  |  | 1726 | 0 | 16 | 7.076e+08 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 4.646 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 4.551 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 82.032 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 82.174 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 82.041 ns | 65536 |
