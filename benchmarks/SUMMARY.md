# benchmark summary — v1.7.5

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1627.563 us | 614523.221 | 1.627e-06 |
| `BM_TokenizationThroughput/8` | 1520.42 us | 657728.685 | 1.520e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1586.686 us | 630194.804 | 1.587e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1485.358 us | 673272.604 | 1.485e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 255.234 us |  |  |  |  |  |  |  |
| `BM_Diff` | 419.656 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 82.91 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 127.82 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 145.321 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 8.97 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 8.682 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 8131.642 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 16159.478 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 24176.207 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 48960.403 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 99721.786 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 31036.621 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 95.978 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.26 ms |  |  |  |  |  | 793948.44 |  |
| `BM_MetaLogCompress/10000/16` | 4.562 ms |  |  |  |  |  | 2.192e+06 |  |
| `BM_MetaLogCompress/100000/16` | 22.73 ms |  |  |  |  |  | 4.400e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.26 ms |  |  |  |  |  | 793661.59 |  |
| `BM_MetaLogCompress/10000/32` | 4.564 ms |  |  |  |  |  | 2.191e+06 |  |
| `BM_MetaLogCompress/100000/32` | 22.658 ms |  |  |  |  |  | 4.414e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.271 ms |  |  |  |  |  | 786560.254 |  |
| `BM_MetaLogCompress/10000/64` | 4.565 ms |  |  |  |  |  | 2.191e+06 |  |
| `BM_MetaLogCompress/100000/64` | 22.752 ms |  |  |  |  |  | 4.396e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 51.89 us |  |  |  |  |  | 1.927e+07 | 5.189e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 115.741 us |  |  |  |  |  | 8.641e+06 | 1.157e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 243.993 us |  |  |  |  |  | 4.099e+06 | 2.440e-07 |
| `BM_MetaLogIngest_Where` | 117.911 us |  |  |  |  |  | 8.482e+06 | 1.179e-07 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3906.048 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4738.778 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 11918.13 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 29726.425 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 232.399 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 298.292 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3599.749 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4281.73 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7975.817 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 535.187 us |  |  |  |  |  | 0.6 | 0 | 37332.161 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1380.127 us |  |  |  |  |  | 0.857 | 0 | 20267.903 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 5455.353 us |  |  |  |  |  | 0.857 | 0 | 5129.055 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7889.834 us |  |  |  |  |  | 0.857 | 0 | 3546.453 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 89520.559 us |  |  |  |  |  | 0.98 | 0 | 2188.027 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 100866.41 us |  |  |  |  |  | 0.98 | 0 | 1946.878 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 145346.469 us |  |  |  |  |  | 0.98 | 6 | 1350.223 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 435926.537 us |  |  |  |  |  | 0.98 | 0 | 449.237 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 344.321 ns | 2.901e+06 |
| `BM_Pipeline_IngestBatch/64` | 28812.076 ns | 2.218e+06 |
| `BM_Pipeline_IngestBatch/1024` | 361752.719 ns | 2.826e+06 |
| `BM_Pipeline_CloseWindow/1000` | 20830.552 ns | 48608.147 |
| `BM_Pipeline_CloseWindow/10000` | 31695.018 ns | 32354.012 |
| `BM_Pipeline_FullWindow/1000` | 444823.855 ns | 2.249e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.599e+06 ns | 2.779e+06 |

### `logcraft-core` — the deterministic log simulator core

_61 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | asio_ns_per_event | events_per_iter | interval_us | scheduler_ns_per_event | scheduler_overhead_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 6.705 ms | 1 | 894858.467 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 29.249 ms | 4 | 820537.9 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 161.464 ms | 16 | 594560.584 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 28.43 ms | 4 | 844172.275 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 165.787 ms | 16 | 579055.395 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.942 ms | 1 | 530552.48 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 3.156 ms | 4 | 633644.161 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 14.444 ms | 16 | 553862.047 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 84.2 ms | 64 | 380049.744 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 797.761 ms | 256 | 160449.095 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 7.228 ms | 32 | 2.214e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 13.277 ms | 32 | 1.205e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 22.364 ms | 32 | 715420.551 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 32.426 ms | 32 | 493432.733 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 35.011 ms | 32 | 456993.301 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 13.239 ms | 16 | 604255.01 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 14.039 ms | 16 | 569820.926 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 14.262 ms | 16 | 560918.225 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 14.542 ms | 16 | 550129.182 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 14.191 ms | 16 | 563751.44 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 14.509 ms | 16 | 551386.99 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.031 ns |  | 9.066e+07 |  |  | 2.620e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.125 ns |  | 1.096e+08 |  |  | 5.698e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 17.438 ns |  | 5.735e+07 |  |  | 5.735e+07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 15.204 ns |  | 6.577e+07 |  |  | 7.738e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.562 ns |  | 2.192e+08 |  |  | 1.753e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 100.213 ns |  | 9.979e+06 |  |  | 1.896e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 224.289 ns |  | 4.459e+06 |  |  | 2.452e+07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 393.405 ns |  | 2.542e+06 |  |  | 6.965e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 184.909 ns |  | 5.408e+06 |  |  | 9.843e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 275.807 ns |  | 3.626e+06 |  |  | 2.683e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 105.729 ns |  | 9.458e+06 |  |  | 5.107e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 134.319 ns |  | 7.445e+06 |  |  | 5.286e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 314.696 ns |  | 3.178e+06 |  |  | 6.355e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 400.4 ns |  | 2.498e+06 |  |  | 8.043e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 392.125 ns |  | 2.550e+06 |  |  | 1.775e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 327.642 ns |  | 3.052e+06 |  |  | 8.363e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 130.447 ns |  | 7.666e+06 |  |  | 1.395e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 244.234 ns |  | 4.095e+06 |  |  | 3.030e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 71.976 ns |  | 1.389e+07 |  |  | 7.503e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 112.314 ns |  | 8.904e+06 |  |  | 6.322e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 257.247 ns |  | 3.887e+06 |  |  | 7.775e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 338.758 ns |  | 2.952e+06 |  |  | 9.505e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 312.609 ns |  | 3.199e+06 |  |  | 2.226e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2514.373 us |  | 4.041e+06 |  |  |  | 8192 | 2.474e-07 |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2389.825 us |  | 4.250e+06 |  |  |  | 32768 | 2.353e-07 |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 198.623 us |  | 4.126e+07 |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 794.619 us |  | 4.124e+07 |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.599 ms |  | 3.572e+06 |  | 1 |  |  |  | 0 | 165996 | 1 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.323 ms |  | 4.901e+06 |  | 1 |  |  |  | 0 | 105190 | 4 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 22.673 ms |  | 3.528e+06 |  | 4 |  |  |  | 0 | 109542 | 4 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 41.582 ms |  | 7.696e+06 |  | 4 |  |  |  | 0 | 486564 | 16 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 51.44 ms |  | 6.221e+06 |  | 16 |  |  |  | 0 | 389039 | 16 | 0 |  |  |  |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.786 ms |  | 2.947e+06 |  | 1 |  |  |  | 185 | 0 | 1 | 8.742e+06 |  |  |  |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 17.813 ms |  | 4.491e+06 |  | 1 |  |  |  | 529 | 0 | 4 | 6.470e+07 |  |  |  |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 29.607 ms |  | 2.702e+06 |  | 4 |  |  |  | 316 | 0 | 4 | 3.365e+07 |  |  |  |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 51.897 ms |  | 6.166e+06 |  | 4 |  |  |  | 2794 | 0 | 16 | 1.215e+09 |  |  |  |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 69.859 ms |  | 4.581e+06 |  | 16 |  |  |  | 1613 | 0 | 16 | 1.160e+09 |  |  |  |  |  |
| `BM_SimulationScheduler_TimerDrivenOverhead/250/real_time` | 34.28 ms |  | 1866.963 |  |  |  |  |  |  |  |  |  | 280539.187 | 64 | 250 | 250787.689 | -10.545 |
| `BM_SimulationScheduler_TimerDrivenOverhead/1000/real_time` | 130.501 ms |  | 490.416 |  |  |  |  |  |  |  |  |  | 1.033e+06 | 64 | 1000 | 1.001e+06 | -3.089 |
| `BM_SimulationScheduler_TimerDrivenOverhead/5000/real_time` | 642.577 ms |  | 99.599 |  |  |  |  |  |  |  |  |  | 5.034e+06 | 64 | 5000 | 5.001e+06 | -0.667 |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 80.578 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 80.48 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 80.505 ns | 65536 |
