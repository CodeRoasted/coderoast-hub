# benchmark summary — v1.8.2

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1625.681 us | 615246.451 | 1.625e-06 |
| `BM_TokenizationThroughput/8` | 1535.138 us | 651371.008 | 1.535e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1582.711 us | 631839.207 | 1.583e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1467.439 us | 681434.68 | 1.467e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 252.812 us |  |  |  |  |  |  |  |
| `BM_Diff` | 419.244 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 82.67 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 127.707 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 147.684 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 9.027 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 8.674 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 8134.647 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 16172.672 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 24291.03 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 48988.626 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 99567.796 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 31052.596 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 93.547 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.252 ms |  |  |  |  |  | 798488.088 |  |
| `BM_MetaLogCompress/10000/16` | 4.56 ms |  |  |  |  |  | 2.193e+06 |  |
| `BM_MetaLogCompress/100000/16` | 22.621 ms |  |  |  |  |  | 4.421e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.261 ms |  |  |  |  |  | 793207.929 |  |
| `BM_MetaLogCompress/10000/32` | 4.563 ms |  |  |  |  |  | 2.192e+06 |  |
| `BM_MetaLogCompress/100000/32` | 22.674 ms |  |  |  |  |  | 4.411e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.267 ms |  |  |  |  |  | 789035.183 |  |
| `BM_MetaLogCompress/10000/64` | 4.568 ms |  |  |  |  |  | 2.189e+06 |  |
| `BM_MetaLogCompress/100000/64` | 22.712 ms |  |  |  |  |  | 4.403e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 54.384 us |  |  |  |  |  | 1.839e+07 | 5.438e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 119.586 us |  |  |  |  |  | 8.363e+06 | 1.196e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 250.501 us |  |  |  |  |  | 3.992e+06 | 2.505e-07 |
| `BM_MetaLogIngest_Where` | 125.048 us |  |  |  |  |  | 7.998e+06 | 1.250e-07 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 4412.576 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 5494.676 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 14040.454 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 34509.812 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 268.845 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 344.729 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 4067.471 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4835.049 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 8402.033 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 600.967 us |  |  |  |  |  | 0.6 | 0 | 34897.052 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1504.025 us |  |  |  |  |  | 0.857 | 0 | 19571.344 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 6009.565 us |  |  |  |  |  | 0.857 | 0 | 4903.721 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 9047.314 us |  |  |  |  |  | 0.857 | 0 | 3256.977 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 98817.13 us |  |  |  |  |  | 0.98 | 0 | 2078.862 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 110621.621 us |  |  |  |  |  | 0.98 | 0 | 1856.871 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 157730.202 us |  |  |  |  |  | 0.98 | 6 | 1301.892 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 477474.231 us |  |  |  |  |  | 0.98 | 0 | 430.066 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 383.488 ns | 2.733e+06 |
| `BM_Pipeline_IngestBatch/64` | 32912.229 ns | 2.037e+06 |
| `BM_Pipeline_IngestBatch/1024` | 419863.342 ns | 2.556e+06 |
| `BM_Pipeline_CloseWindow/1000` | 25211.752 ns | 42044.493 |
| `BM_Pipeline_CloseWindow/10000` | 37991.104 ns | 28326.07 |
| `BM_Pipeline_FullWindow/1000` | 571290.696 ns | 1.836e+06 |
| `BM_Pipeline_FullWindow/10000` | 4.227e+06 ns | 2.481e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 10.5 ms | 1 | 571452.616 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 20.286 ms | 4 | 1.183e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 69.165 ms | 16 | 1.388e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 20.951 ms | 4 | 1.146e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 64.575 ms | 16 | 1.487e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.62 ms | 1 | 806794.288 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.819 ms | 4 | 2.441e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.876 ms | 16 | 4.264e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 6.662 ms | 64 | 4.804e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 25.475 ms | 256 | 5.024e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.924 ms | 32 | 3.249e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 3.484 ms | 32 | 4.592e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 3.314 ms | 32 | 4.828e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 4.582 ms | 32 | 3.492e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 5.825 ms | 32 | 2.747e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 2.197 ms | 16 | 3.642e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 2.288 ms | 16 | 3.497e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 2.322 ms | 16 | 3.446e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.605 ms | 16 | 3.071e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 3.485 ms | 16 | 2.296e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 5.094 ms | 16 | 1.570e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 12.132 ns |  | 8.598e+07 |  |  | 2.485e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.761 ns |  | 1.029e+08 |  |  | 5.349e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 19.658 ns |  | 5.369e+07 |  |  | 5.369e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 15.537 ns |  | 6.503e+07 |  |  | 7.645e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 5.316 ns |  | 1.993e+08 |  |  | 1.595e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 102.834 ns |  | 9.856e+06 |  |  | 1.873e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 93.51 ns |  | 1.128e+07 |  |  | 6.205e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 393.362 ns |  | 2.542e+06 |  |  | 6.686e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 197.779 ns |  | 5.288e+06 |  |  | 9.624e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 278.066 ns |  | 3.755e+06 |  |  | 2.779e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 103.369 ns |  | 1.035e+07 |  |  | 5.588e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 143.884 ns |  | 7.389e+06 |  |  | 5.246e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 340.092 ns |  | 3.141e+06 |  |  | 6.282e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 451.752 ns |  | 2.362e+06 |  |  | 7.607e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 436.691 ns |  | 2.437e+06 |  |  | 1.696e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 361.358 ns |  | 2.826e+06 |  |  | 7.432e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 136.826 ns |  | 7.726e+06 |  |  | 1.406e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 253.12 ns |  | 4.235e+06 |  |  | 3.134e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 76.948 ns |  | 1.343e+07 |  |  | 7.252e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 101.82 ns |  | 1.020e+07 |  |  | 7.242e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 279.119 ns |  | 3.721e+06 |  |  | 7.442e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 365.085 ns |  | 2.913e+06 |  |  | 9.380e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 356.13 ns |  | 2.908e+06 |  |  | 2.024e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 9.203 ms | 1 |  | 6000 |  |  | 5.592 | 1.976 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 19.634 ms | 4 |  | 24000 |  |  | 4.59 | 8.877 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 58.088 ms | 16 |  | 96000 |  |  | 13.01 | 18.403 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2907.06 us |  | 3.564e+06 |  |  |  |  |  | 8192 | 2.806e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2729.61 us |  | 3.883e+06 |  |  |  |  |  | 32768 | 2.575e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 232.726 us |  | 3.644e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 941.334 us |  | 3.611e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.91 ms |  | 3.384e+06 |  | 1 |  |  |  |  |  | 0 | 164247 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 17.492 ms |  | 4.574e+06 |  | 1 |  |  |  |  |  | 0 | 298388 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 33.06 ms |  | 2.420e+06 |  | 4 |  |  |  |  |  | 0 | 92425 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 65.317 ms |  | 4.899e+06 |  | 4 |  |  |  |  |  | 0 | 896059 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 86.755 ms |  | 3.689e+06 |  | 16 |  |  |  |  |  | 0 | 713187 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 7.993 ms |  | 2.502e+06 |  | 1 |  |  |  |  |  | 465 | 0 | 1 | 1.829e+07 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 23.895 ms |  | 3.348e+06 |  | 1 |  |  |  |  |  | 961 | 0 | 4 | 2.948e+08 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 55.459 ms |  | 1.443e+06 |  | 4 |  |  |  |  |  | 624 | 0 | 4 | 9.933e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 107.155 ms |  | 2.986e+06 |  | 4 |  |  |  |  |  | 5719 | 0 | 16 | 4.748e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 92.197 ms |  | 3.471e+06 |  | 16 |  |  |  |  |  | 1463 | 0 | 16 | 2.062e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 6.325 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 5.174 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 82.35 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 81.557 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 81.727 ns | 65536 |
