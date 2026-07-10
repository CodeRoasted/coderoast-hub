# benchmark summary — v1.7.7

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1548.918 us | 645602.829 | 1.549e-06 |
| `BM_TokenizationThroughput/8` | 1431.821 us | 698383.825 | 1.432e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1488.503 us | 671756.014 | 1.489e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1377.297 us | 725906.307 | 1.378e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 252.69 us |  |  |  |  |  |  |  |
| `BM_Diff` | 419.907 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 82.381 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 127.867 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 153.115 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 8.968 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 8.672 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 8141.521 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 16159.924 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 24171.593 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 48956.574 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 100340.893 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 31411.264 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 91.022 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.247 ms |  |  |  |  |  | 801806.915 |  |
| `BM_MetaLogCompress/10000/16` | 4.445 ms |  |  |  |  |  | 2.250e+06 |  |
| `BM_MetaLogCompress/100000/16` | 21.689 ms |  |  |  |  |  | 4.611e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.254 ms |  |  |  |  |  | 797594.21 |  |
| `BM_MetaLogCompress/10000/32` | 4.46 ms |  |  |  |  |  | 2.242e+06 |  |
| `BM_MetaLogCompress/100000/32` | 21.726 ms |  |  |  |  |  | 4.604e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.263 ms |  |  |  |  |  | 791993.816 |  |
| `BM_MetaLogCompress/10000/64` | 4.466 ms |  |  |  |  |  | 2.239e+06 |  |
| `BM_MetaLogCompress/100000/64` | 21.718 ms |  |  |  |  |  | 4.605e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 53.691 us |  |  |  |  |  | 1.863e+07 | 5.369e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 118.609 us |  |  |  |  |  | 8.432e+06 | 1.186e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 246.39 us |  |  |  |  |  | 4.059e+06 | 2.464e-07 |
| `BM_MetaLogIngest_Where` | 122.714 us |  |  |  |  |  | 8.150e+06 | 1.227e-07 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3901.893 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4756.929 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 12174.031 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 30951.202 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 241.062 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 308.071 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3565.848 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4336.943 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 8063.552 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 535.692 us |  |  |  |  |  | 0.6 | 0 | 37335.468 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1336.108 us |  |  |  |  |  | 0.857 | 0 | 20957.027 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 5357.432 us |  |  |  |  |  | 0.857 | 0 | 5226.878 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7816.077 us |  |  |  |  |  | 0.857 | 0 | 3582.413 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 88082.857 us |  |  |  |  |  | 0.98 | 0 | 2225.253 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 97017.879 us |  |  |  |  |  | 0.98 | 0 | 2020.313 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 142899.739 us |  |  |  |  |  | 0.98 | 6 | 1371.545 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 430188.716 us |  |  |  |  |  | 0.98 | 0 | 455.618 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 350.181 ns | 2.856e+06 |
| `BM_Pipeline_IngestBatch/64` | 28641.908 ns | 2.234e+06 |
| `BM_Pipeline_IngestBatch/1024` | 373271.341 ns | 2.742e+06 |
| `BM_Pipeline_CloseWindow/1000` | 20684.93 ns | 48927.313 |
| `BM_Pipeline_CloseWindow/10000` | 32483.28 ns | 31568.945 |
| `BM_Pipeline_FullWindow/1000` | 477161.929 ns | 2.096e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.562e+06 ns | 2.808e+06 |

### `logcraft-core` — the deterministic log simulator core

_61 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | asio_ns_per_event | events_per_iter | interval_us | scheduler_ns_per_event | scheduler_overhead_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 6.828 ms | 1 | 878712.523 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 29.886 ms | 4 | 803040.992 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 156.816 ms | 16 | 612183.817 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 28.953 ms | 4 | 828931.965 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 162.299 ms | 16 | 591500.059 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 1.155 ms | 1 | 432934.107 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 3.258 ms | 4 | 613924.285 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 13.982 ms | 16 | 572153.691 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 83.481 ms | 64 | 383319.052 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 715.328 ms | 256 | 178938.965 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 7.388 ms | 32 | 2.166e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 13.25 ms | 32 | 1.208e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 21.917 ms | 32 | 730043.25 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 32.158 ms | 32 | 497546.771 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 31.623 ms | 32 | 505961.178 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 13.177 ms | 16 | 607124.345 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 13.476 ms | 16 | 593646.148 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 14.041 ms | 16 | 569757.984 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 13.999 ms | 16 | 571457.197 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 14.032 ms | 16 | 570132.771 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 14.595 ms | 16 | 548128.27 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 10.907 ns |  | 9.168e+07 |  |  | 2.650e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.044 ns |  | 1.106e+08 |  |  | 5.750e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 17.396 ns |  | 5.749e+07 |  |  | 5.749e+07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 15.169 ns |  | 6.593e+07 |  |  | 7.757e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.251 ns |  | 2.352e+08 |  |  | 1.882e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 99.13 ns |  | 1.009e+07 |  |  | 1.917e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 224.5 ns |  | 4.454e+06 |  |  | 2.450e+07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 401.602 ns |  | 2.490e+06 |  |  | 6.823e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 180.591 ns |  | 5.537e+06 |  |  | 1.008e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 267.621 ns |  | 3.737e+06 |  |  | 2.765e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 96.856 ns |  | 1.032e+07 |  |  | 5.575e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 133.099 ns |  | 7.513e+06 |  |  | 5.334e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 301.105 ns |  | 3.321e+06 |  |  | 6.642e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 413.729 ns |  | 2.417e+06 |  |  | 7.783e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 404.468 ns |  | 2.472e+06 |  |  | 1.721e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 326.226 ns |  | 3.065e+06 |  |  | 8.399e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 127.256 ns |  | 7.859e+06 |  |  | 1.430e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 229.658 ns |  | 4.354e+06 |  |  | 3.222e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 70.866 ns |  | 1.411e+07 |  |  | 7.620e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 96.438 ns |  | 1.037e+07 |  |  | 7.362e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 255.521 ns |  | 3.914e+06 |  |  | 7.827e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 337.256 ns |  | 2.965e+06 |  |  | 9.547e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 330.452 ns |  | 3.026e+06 |  |  | 2.106e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2704.682 us |  | 3.741e+06 |  |  |  | 8192 | 2.673e-07 |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2608.386 us |  | 3.875e+06 |  |  |  | 32768 | 2.580e-07 |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 215.618 us |  | 3.801e+07 |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 866.471 us |  | 3.783e+07 |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.561 ms |  | 3.597e+06 |  | 1 |  |  |  | 0 | 171620 | 1 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 15.503 ms |  | 5.160e+06 |  | 1 |  |  |  | 0 | 167180 | 4 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 24.619 ms |  | 3.250e+06 |  | 4 |  |  |  | 0 | 151767 | 4 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 41.467 ms |  | 7.717e+06 |  | 4 |  |  |  | 0 | 676395 | 16 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 53.973 ms |  | 5.929e+06 |  | 16 |  |  |  | 0 | 394367 | 16 | 0 |  |  |  |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.119 ms |  | 3.269e+06 |  | 1 |  |  |  | 158 | 0 | 1 | 6.790e+06 |  |  |  |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 18.837 ms |  | 4.247e+06 |  | 1 |  |  |  | 443 | 0 | 4 | 4.982e+07 |  |  |  |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 20.914 ms |  | 3.825e+06 |  | 4 |  |  |  | 269 | 0 | 4 | 2.436e+07 |  |  |  |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 52.145 ms |  | 6.137e+06 |  | 4 |  |  |  | 3326 | 0 | 16 | 1.353e+09 |  |  |  |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 62.41 ms |  | 5.127e+06 |  | 16 |  |  |  | 1284 | 0 | 16 | 8.710e+08 |  |  |  |  |  |
| `BM_SimulationScheduler_TimerDrivenOverhead/250/real_time` | 34.269 ms |  | 1867.598 |  |  |  |  |  |  |  |  |  | 280652.414 | 64 | 250 | 251069.586 | -10.559 |
| `BM_SimulationScheduler_TimerDrivenOverhead/1000/real_time` | 130.538 ms |  | 490.28 |  |  |  |  |  |  |  |  |  | 1.034e+06 | 64 | 1000 | 1.001e+06 | -3.159 |
| `BM_SimulationScheduler_TimerDrivenOverhead/5000/real_time` | 642.699 ms |  | 99.58 |  |  |  |  |  |  |  |  |  | 5.036e+06 | 64 | 5000 | 5.001e+06 | -0.701 |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 80.423 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 80.447 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 80.33 ns | 65536 |
