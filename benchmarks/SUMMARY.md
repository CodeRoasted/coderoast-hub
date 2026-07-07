# benchmark summary — v1.7.3

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_2 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1555.478 us | 642989.338 | 1.555e-06 |
| `BM_TokenizationThroughput/8` | 1447.171 us | 691001.379 | 1.447e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 253.948 us |  |  |  |  |  |  |  |
| `BM_Diff` | 420.229 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 81.247 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 126.828 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 144.675 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 9.456 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 8.658 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 8139.123 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 16171.532 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 24188.486 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 48949.81 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 100668.851 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 30864.825 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 88.426 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.276 ms |  |  |  |  |  | 783727.114 |  |
| `BM_MetaLogCompress/10000/16` | 4.736 ms |  |  |  |  |  | 2.112e+06 |  |
| `BM_MetaLogCompress/100000/16` | 24.362 ms |  |  |  |  |  | 4.105e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.281 ms |  |  |  |  |  | 780422.62 |  |
| `BM_MetaLogCompress/10000/32` | 4.743 ms |  |  |  |  |  | 2.108e+06 |  |
| `BM_MetaLogCompress/100000/32` | 24.3 ms |  |  |  |  |  | 4.116e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.286 ms |  |  |  |  |  | 777825.299 |  |
| `BM_MetaLogCompress/10000/64` | 4.744 ms |  |  |  |  |  | 2.108e+06 |  |
| `BM_MetaLogCompress/100000/64` | 24.364 ms |  |  |  |  |  | 4.105e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 56.27 us |  |  |  |  |  | 1.777e+07 | 5.626e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 119.184 us |  |  |  |  |  | 8.391e+06 | 1.192e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 247.48 us |  |  |  |  |  | 4.041e+06 | 2.474e-07 |
| `BM_MetaLogIngest_Where` | 122.526 us |  |  |  |  |  | 8.162e+06 | 1.225e-07 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3883.278 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 5047.115 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 12102.015 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 31521.49 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 249.43 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 293.29 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3733.843 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4244.966 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 8433.606 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 548.732 us |  |  |  |  |  | 0.6 | 0 | 38873.699 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1379.647 us |  |  |  |  |  | 0.857 | 0 | 21920.405 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 5515.522 us |  |  |  |  |  | 0.857 | 0 | 5472.216 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 8062.095 us |  |  |  |  |  | 0.857 | 0 | 3726.499 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 93262.213 us |  |  |  |  |  | 0.98 | 0 | 2274.822 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 97298.604 us |  |  |  |  |  | 0.98 | 0 | 2071.92 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 149837.397 us |  |  |  |  |  | 0.98 | 6 | 1417.106 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 423359.469 us |  |  |  |  |  | 0.98 | 0 | 465.507 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 343.661 ns | 3.151e+06 |
| `BM_Pipeline_IngestBatch/64` | 27272.23 ns | 2.440e+06 |
| `BM_Pipeline_IngestBatch/1024` | 330749.307 ns | 3.113e+06 |
| `BM_Pipeline_CloseWindow/1000` | 20536.946 ns | 51478.429 |
| `BM_Pipeline_CloseWindow/10000` | 32528.652 ns | 33077.421 |
| `BM_Pipeline_FullWindow/1000` | 390147.119 ns | 2.563e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.500e+06 ns | 3.052e+06 |

### `logcraft-core` — the deterministic log simulator core

_61 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | asio_ns_per_event | events_per_iter | interval_us | scheduler_ns_per_event | scheduler_overhead_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 6.707 ms | 1 | 894575.525 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 30.03 ms | 4 | 799189 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 164.422 ms | 16 | 583863.464 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 30.245 ms | 4 | 793519.994 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 178.236 ms | 16 | 538610.759 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.861 ms | 1 | 581004.975 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 3.103 ms | 4 | 644534.052 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 14.258 ms | 16 | 561100.539 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 87.934 ms | 64 | 363910.476 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 760.455 ms | 256 | 168320.291 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 7.578 ms | 32 | 2.111e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 13.543 ms | 32 | 1.181e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 23.071 ms | 32 | 693520.616 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 34.002 ms | 32 | 470553.857 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 35.367 ms | 32 | 452394.876 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 13.361 ms | 16 | 598764.037 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 14.1 ms | 16 | 567387.14 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 14.309 ms | 16 | 559103.893 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 14.605 ms | 16 | 547768.497 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 14.656 ms | 16 | 545851.43 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 14.869 ms | 16 | 538033.077 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.526 ns |  | 9.146e+07 |  |  | 2.643e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.605 ns |  | 1.099e+08 |  |  | 5.714e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 18.396 ns |  | 5.741e+07 |  |  | 5.741e+07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 16.024 ns |  | 6.590e+07 |  |  | 7.752e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.761 ns |  | 2.217e+08 |  |  | 1.774e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 103.244 ns |  | 1.021e+07 |  |  | 1.941e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 235.063 ns |  | 4.484e+06 |  |  | 2.466e+07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 412.835 ns |  | 2.553e+06 |  |  | 6.995e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 192.515 ns |  | 5.505e+06 |  |  | 1.002e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 283.803 ns |  | 3.734e+06 |  |  | 2.763e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 109.159 ns |  | 9.757e+06 |  |  | 5.269e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 141.239 ns |  | 7.541e+06 |  |  | 5.354e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 327.068 ns |  | 3.254e+06 |  |  | 6.508e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 403.024 ns |  | 2.615e+06 |  |  | 8.421e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 406.991 ns |  | 2.560e+06 |  |  | 1.782e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 332.925 ns |  | 3.128e+06 |  |  | 8.570e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 133.257 ns |  | 7.829e+06 |  |  | 1.425e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 248.419 ns |  | 4.331e+06 |  |  | 3.205e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 75.889 ns |  | 1.417e+07 |  |  | 7.650e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 102.941 ns |  | 1.033e+07 |  |  | 7.337e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 265.705 ns |  | 4.004e+06 |  |  | 8.007e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 335.601 ns |  | 3.137e+06 |  |  | 1.010e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 324.06 ns |  | 3.248e+06 |  |  | 2.261e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2604.1 us |  | 4.097e+06 |  |  |  | 8192 | 2.441e-07 |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2497.149 us |  | 4.278e+06 |  |  |  | 32768 | 2.338e-07 |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 207.087 us |  | 4.173e+07 |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 818.415 us |  | 4.224e+07 |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 6.038 ms |  | 3.312e+06 |  | 1 |  |  |  | 0 | 132818 | 1 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 17.339 ms |  | 4.614e+06 |  | 1 |  |  |  | 0 | 114007 | 4 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 22.586 ms |  | 3.542e+06 |  | 4 |  |  |  | 0 | 103471 | 4 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 47.427 ms |  | 6.747e+06 |  | 4 |  |  |  | 0 | 407647 | 16 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 57.427 ms |  | 5.572e+06 |  | 16 |  |  |  | 0 | 354531 | 16 | 0 |  |  |  |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.892 ms |  | 2.902e+06 |  | 1 |  |  |  | 117 | 0 | 1 | 5.111e+06 |  |  |  |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 18.864 ms |  | 4.241e+06 |  | 1 |  |  |  | 464 | 0 | 4 | 4.652e+07 |  |  |  |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 29.797 ms |  | 2.685e+06 |  | 4 |  |  |  | 306 | 0 | 4 | 2.681e+07 |  |  |  |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 55.62 ms |  | 5.753e+06 |  | 4 |  |  |  | 2777 | 0 | 16 | 1.267e+09 |  |  |  |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 70.418 ms |  | 4.544e+06 |  | 16 |  |  |  | 1391 | 0 | 16 | 9.341e+08 |  |  |  |  |  |
| `BM_SimulationScheduler_TimerDrivenOverhead/250/real_time` | 35.297 ms |  | 1813.191 |  |  |  |  |  |  |  |  |  | 296018.667 | 64 | 250 | 251073.159 | -15.181 |
| `BM_SimulationScheduler_TimerDrivenOverhead/1000/real_time` | 133.962 ms |  | 477.747 |  |  |  |  |  |  |  |  |  | 1.087e+06 | 64 | 1000 | 1.002e+06 | -7.831 |
| `BM_SimulationScheduler_TimerDrivenOverhead/5000/real_time` | 657.687 ms |  | 97.311 |  |  |  |  |  |  |  |  |  | 5.265e+06 | 64 | 5000 | 5.005e+06 | -4.93 |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 80.783 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 80.633 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 80.436 ns | 65536 |
