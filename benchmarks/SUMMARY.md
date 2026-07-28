# benchmark summary — v1.8.5

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1697.285 us | 589185.977 | 1.697e-06 |
| `BM_TokenizationThroughput/8` | 1576.429 us | 634399.041 | 1.576e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1644.749 us | 607956.552 | 1.645e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1523.557 us | 656468.658 | 1.523e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 196.142 us |  |  |  |  |  |  |  |
| `BM_Diff` | 381.091 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 56.69 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 118.83 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 202.311 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 5.129 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 5.563 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 6920.556 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 13489.246 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 29236.494 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 62942.624 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 159572.943 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 25274.089 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 79.987 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 0.916 ms |  |  |  |  |  | 1.092e+06 |  |
| `BM_MetaLogCompress/10000/16` | 3.193 ms |  |  |  |  |  | 3.132e+06 |  |
| `BM_MetaLogCompress/100000/16` | 15.34 ms |  |  |  |  |  | 6.519e+06 |  |
| `BM_MetaLogCompress/1000/32` | 0.911 ms |  |  |  |  |  | 1.098e+06 |  |
| `BM_MetaLogCompress/10000/32` | 3.15 ms |  |  |  |  |  | 3.174e+06 |  |
| `BM_MetaLogCompress/100000/32` | 15.489 ms |  |  |  |  |  | 6.457e+06 |  |
| `BM_MetaLogCompress/1000/64` | 0.906 ms |  |  |  |  |  | 1.103e+06 |  |
| `BM_MetaLogCompress/10000/64` | 3.137 ms |  |  |  |  |  | 3.189e+06 |  |
| `BM_MetaLogCompress/100000/64` | 15.245 ms |  |  |  |  |  | 6.560e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 31.31 us |  |  |  |  |  | 3.194e+07 | 3.131e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 73.547 us |  |  |  |  |  | 1.360e+07 | 7.354e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 169.337 us |  |  |  |  |  | 5.906e+06 | 1.693e-07 |
| `BM_MetaLogIngest_Where` | 76.285 us |  |  |  |  |  | 1.311e+07 | 7.628e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3610.9 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4450.201 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 11280.413 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 28626.985 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 230.156 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 285.801 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3346.621 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4110.181 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7538.7 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 480.225 us |  |  |  |  |  | 0.6 | 0 | 41647.504 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1247.043 us |  |  |  |  |  | 0.857 | 0 | 22453.397 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 5010.944 us |  |  |  |  |  | 0.857 | 0 | 5587.867 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7353.672 us |  |  |  |  |  | 0.857 | 0 | 3807.702 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 81548.255 us |  |  |  |  |  | 0.98 | 0 | 2403.528 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 90635.525 us |  |  |  |  |  | 0.98 | 0 | 2162.503 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 134512.56 us |  |  |  |  |  | 0.98 | 6 | 1457.133 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 392001.35 us |  |  |  |  |  | 0.98 | 0 | 500.002 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 329.801 ns | 3.038e+06 |
| `BM_Pipeline_IngestBatch/64` | 28835.273 ns | 2.219e+06 |
| `BM_Pipeline_IngestBatch/1024` | 384369.151 ns | 2.663e+06 |
| `BM_Pipeline_CloseWindow/1000` | 17783.726 ns | 56744.825 |
| `BM_Pipeline_CloseWindow/10000` | 30139.227 ns | 33957.375 |
| `BM_Pipeline_FullWindow/1000` | 467143.685 ns | 2.141e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.946e+06 ns | 2.534e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.089 ms | 1 | 741719.563 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 15.829 ms | 4 | 1.516e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 42.662 ms | 16 | 2.250e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 15.683 ms | 4 | 1.530e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 43.429 ms | 16 | 2.210e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.538 ms | 1 | 930211.481 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.878 ms | 4 | 2.277e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 2.011 ms | 16 | 3.978e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.453 ms | 64 | 5.868e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 17.087 ms | 256 | 7.491e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.41 ms | 32 | 3.628e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.811 ms | 32 | 5.693e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.722 ms | 32 | 5.878e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 3.178 ms | 32 | 5.035e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.414 ms | 32 | 4.687e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.905 ms | 16 | 4.198e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 2.048 ms | 16 | 3.907e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 2.001 ms | 16 | 3.999e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.574 ms | 16 | 3.108e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 3.238 ms | 16 | 2.471e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.335 ms | 16 | 1.845e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 10.86 ns |  | 9.208e+07 |  |  | 2.661e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 8.845 ns |  | 1.131e+08 |  |  | 5.879e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 16.737 ns |  | 5.975e+07 |  |  | 5.975e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.092 ns |  | 7.096e+07 |  |  | 8.360e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.306 ns |  | 2.322e+08 |  |  | 1.858e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 93.231 ns |  | 1.073e+07 |  |  | 2.038e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 78.772 ns |  | 1.270e+07 |  |  | 6.982e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 360.79 ns |  | 2.772e+06 |  |  | 7.290e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 174.174 ns |  | 5.741e+06 |  |  | 1.045e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 243.336 ns |  | 4.110e+06 |  |  | 3.041e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 89.24 ns |  | 1.121e+07 |  |  | 6.051e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 124.119 ns |  | 8.057e+06 |  |  | 5.720e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 286.707 ns |  | 3.488e+06 |  |  | 6.976e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 380.414 ns |  | 2.629e+06 |  |  | 8.465e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 376.236 ns |  | 2.658e+06 |  |  | 1.850e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 312.029 ns |  | 3.205e+06 |  |  | 8.429e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 121.717 ns |  | 8.216e+06 |  |  | 1.495e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 211.737 ns |  | 4.723e+06 |  |  | 3.495e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 68.079 ns |  | 1.469e+07 |  |  | 7.932e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 91.396 ns |  | 1.094e+07 |  |  | 7.768e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 233.857 ns |  | 4.276e+06 |  |  | 8.552e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 311.625 ns |  | 3.209e+06 |  |  | 1.033e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 300.919 ns |  | 3.323e+06 |  |  | 2.313e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.106 ms | 1 |  | 6000 |  |  | 4.817 | 1.714 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 16.159 ms | 4 |  | 24000 |  |  | 3.545 | 7.759 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 42.434 ms | 16 |  | 96000 |  |  | 8.961 | 14.253 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2727.193 us |  | 3.687e+06 |  |  |  |  |  | 8192 | 2.713e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2667.51 us |  | 3.771e+06 |  |  |  |  |  | 32768 | 2.652e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 204.605 us |  | 4.007e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 817.736 us |  | 4.009e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 6.023 ms |  | 3.321e+06 |  | 1 |  |  |  |  |  | 0 | 13341 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.643 ms |  | 4.807e+06 |  | 1 |  |  |  |  |  | 0 | 1004 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 37.517 ms |  | 2.132e+06 |  | 4 |  |  |  |  |  | 0 | 4199 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 38.99 ms |  | 8.207e+06 |  | 4 |  |  |  |  |  | 0 | 156722 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 49.6 ms |  | 6.452e+06 |  | 16 |  |  |  |  |  | 0 | 179242 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.614 ms |  | 3.024e+06 |  | 1 |  |  |  |  |  | 14 | 0 | 1 | 444900 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 17.574 ms |  | 4.552e+06 |  | 1 |  |  |  |  |  | 16 | 0 | 4 | 238200 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 43.516 ms |  | 1.838e+06 |  | 4 |  |  |  |  |  | 11 | 0 | 4 | 1.434e+06 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 43.95 ms |  | 7.281e+06 |  | 4 |  |  |  |  |  | 3543 | 0 | 16 | 4.876e+08 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 56.189 ms |  | 5.695e+06 |  | 16 |  |  |  |  |  | 1181 | 0 | 16 | 4.237e+08 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 4.624 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 9.736 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 81.83 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 81.976 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 81.808 ns | 65536 |
