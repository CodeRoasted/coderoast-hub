# benchmark summary — v1.8.0

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1553.893 us | 643480.155 | 1.554e-06 |
| `BM_TokenizationThroughput/8` | 1436.171 us | 696245.955 | 1.436e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1492.132 us | 670054.201 | 1.492e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1377.411 us | 725884.555 | 1.378e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 253.358 us |  |  |  |  |  |  |  |
| `BM_Diff` | 420.284 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 82.854 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 127.834 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 149.144 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 9.149 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 8.648 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 8134.244 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 16163.877 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 24194.726 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 48776.522 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 99447.519 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 30801.416 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 92.513 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.263 ms |  |  |  |  |  | 792031.327 |  |
| `BM_MetaLogCompress/10000/16` | 4.539 ms |  |  |  |  |  | 2.203e+06 |  |
| `BM_MetaLogCompress/100000/16` | 22.581 ms |  |  |  |  |  | 4.429e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.266 ms |  |  |  |  |  | 789889.109 |  |
| `BM_MetaLogCompress/10000/32` | 4.553 ms |  |  |  |  |  | 2.196e+06 |  |
| `BM_MetaLogCompress/100000/32` | 22.581 ms |  |  |  |  |  | 4.429e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.276 ms |  |  |  |  |  | 783502.442 |  |
| `BM_MetaLogCompress/10000/64` | 4.565 ms |  |  |  |  |  | 2.191e+06 |  |
| `BM_MetaLogCompress/100000/64` | 22.63 ms |  |  |  |  |  | 4.419e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 54.159 us |  |  |  |  |  | 1.847e+07 | 5.415e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 118.673 us |  |  |  |  |  | 8.427e+06 | 1.187e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 248.887 us |  |  |  |  |  | 4.018e+06 | 2.489e-07 |
| `BM_MetaLogIngest_Where` | 122.642 us |  |  |  |  |  | 8.155e+06 | 1.226e-07 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3625.878 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4342.876 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 11341.954 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 28250.725 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 219.491 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 283.651 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3260.938 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4057.091 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7488.828 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 496.225 us |  |  |  |  |  | 0.6 | 0 | 40305.152 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1204.031 us |  |  |  |  |  | 0.857 | 0 | 23255.655 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 4959.326 us |  |  |  |  |  | 0.857 | 0 | 5646.017 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7357.285 us |  |  |  |  |  | 0.857 | 0 | 3805.818 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 81783.853 us |  |  |  |  |  | 0.98 | 0 | 2396.558 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 90682.871 us |  |  |  |  |  | 0.98 | 0 | 2161.394 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 132092.145 us |  |  |  |  |  | 0.98 | 6 | 1483.808 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 403718.223 us |  |  |  |  |  | 0.98 | 0 | 485.493 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 321.772 ns | 3.107e+06 |
| `BM_Pipeline_IngestBatch/64` | 26865.516 ns | 2.384e+06 |
| `BM_Pipeline_IngestBatch/1024` | 346727.574 ns | 2.952e+06 |
| `BM_Pipeline_CloseWindow/1000` | 16646.191 ns | 60562.881 |
| `BM_Pipeline_CloseWindow/10000` | 27943.193 ns | 36692.404 |
| `BM_Pipeline_FullWindow/1000` | 408572.437 ns | 2.448e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.346e+06 ns | 2.988e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 9.029 ms | 1 | 664540.78 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 17.04 ms | 4 | 1.408e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 46.534 ms | 16 | 2.063e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 17.772 ms | 4 | 1.350e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 44.482 ms | 16 | 2.158e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.59 ms | 1 | 847904.68 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.727 ms | 4 | 2.751e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.622 ms | 16 | 4.933e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.26 ms | 64 | 6.084e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 17.046 ms | 256 | 7.509e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.641 ms | 32 | 3.448e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.868 ms | 32 | 5.579e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.763 ms | 32 | 5.791e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 2.813 ms | 32 | 5.687e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.453 ms | 32 | 4.634e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.515 ms | 16 | 5.280e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.683 ms | 16 | 4.755e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.65 ms | 16 | 4.847e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.069 ms | 16 | 3.867e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.871 ms | 16 | 2.787e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.021 ms | 16 | 1.990e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.544 ns |  | 9.083e+07 |  |  | 2.625e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.371 ns |  | 1.105e+08 |  |  | 5.745e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 17.684 ns |  | 5.842e+07 |  |  | 5.842e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.616 ns |  | 7.069e+07 |  |  | 8.318e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.705 ns |  | 2.196e+08 |  |  | 1.757e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 99.876 ns |  | 1.035e+07 |  |  | 1.966e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 220.21 ns |  | 4.692e+06 |  |  | 2.581e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 394.697 ns |  | 2.618e+06 |  |  | 7.173e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 181.027 ns |  | 5.708e+06 |  |  | 1.039e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 269.025 ns |  | 3.841e+06 |  |  | 2.842e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 93.765 ns |  | 1.102e+07 |  |  | 5.951e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 131.39 ns |  | 7.865e+06 |  |  | 5.584e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 304.576 ns |  | 3.393e+06 |  |  | 6.786e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 406.083 ns |  | 2.545e+06 |  |  | 8.194e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 397.376 ns |  | 2.601e+06 |  |  | 1.810e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 333.112 ns |  | 3.102e+06 |  |  | 8.500e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 127.731 ns |  | 8.090e+06 |  |  | 1.472e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 231.026 ns |  | 4.473e+06 |  |  | 3.310e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 70.36 ns |  | 1.469e+07 |  |  | 7.931e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 96.276 ns |  | 1.073e+07 |  |  | 7.621e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 246.113 ns |  | 4.199e+06 |  |  | 8.398e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 340.809 ns |  | 3.032e+06 |  |  | 9.764e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 333.783 ns |  | 3.096e+06 |  |  | 2.155e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.408 ms | 1 |  | 6000 |  |  | 5.176 | 1.913 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 15.578 ms | 4 |  | 24000 |  |  | 3.659 | 7.973 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 42.577 ms | 16 |  | 96000 |  |  | 9.008 | 14.616 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2869.877 us |  | 3.651e+06 |  |  |  |  |  | 8192 | 2.739e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2699.352 us |  | 3.866e+06 |  |  |  |  |  | 32768 | 2.587e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 212.661 us |  | 3.982e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 848.191 us |  | 3.993e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.917 ms |  | 3.380e+06 |  | 1 |  |  |  |  |  | 0 | 129165 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.24 ms |  | 4.926e+06 |  | 1 |  |  |  |  |  | 0 | 57532 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 24.576 ms |  | 3.255e+06 |  | 4 |  |  |  |  |  | 0 | 43411 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 43.808 ms |  | 7.305e+06 |  | 4 |  |  |  |  |  | 0 | 102528 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 56.923 ms |  | 5.622e+06 |  | 16 |  |  |  |  |  | 0 | 258068 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.576 ms |  | 3.041e+06 |  | 1 |  |  |  |  |  | 29 | 0 | 1 | 1.462e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 16.82 ms |  | 4.756e+06 |  | 1 |  |  |  |  |  | 36 | 0 | 4 | 2.390e+06 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 41.943 ms |  | 1.907e+06 |  | 4 |  |  |  |  |  | 64 | 0 | 4 | 1.480e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 45.57 ms |  | 7.022e+06 |  | 4 |  |  |  |  |  | 3773 | 0 | 16 | 5.648e+08 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 61.928 ms |  | 5.167e+06 |  | 16 |  |  |  |  |  | 1180 | 0 | 16 | 4.648e+08 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 4.839 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 9.65 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 80.843 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 80.712 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 80.626 ns | 65536 |
