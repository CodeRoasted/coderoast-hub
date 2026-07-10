# benchmark summary — v1.7.6

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1638.224 us | 610419.638 | 1.638e-06 |
| `BM_TokenizationThroughput/8` | 1523.616 us | 656353.434 | 1.524e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1586.212 us | 630406.081 | 1.586e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1488.554 us | 671784.035 | 1.489e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 253.525 us |  |  |  |  |  |  |  |
| `BM_Diff` | 420.37 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 84.554 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 130.545 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 146.073 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 9.041 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 8.654 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 8139.346 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 16182.414 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 24213.487 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 48979.257 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 100431.338 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 30958.835 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 92.532 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.257 ms |  |  |  |  |  | 795466.522 |  |
| `BM_MetaLogCompress/10000/16` | 4.563 ms |  |  |  |  |  | 2.192e+06 |  |
| `BM_MetaLogCompress/100000/16` | 22.487 ms |  |  |  |  |  | 4.447e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.258 ms |  |  |  |  |  | 794694.35 |  |
| `BM_MetaLogCompress/10000/32` | 4.56 ms |  |  |  |  |  | 2.193e+06 |  |
| `BM_MetaLogCompress/100000/32` | 22.645 ms |  |  |  |  |  | 4.416e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.269 ms |  |  |  |  |  | 788346.133 |  |
| `BM_MetaLogCompress/10000/64` | 4.567 ms |  |  |  |  |  | 2.190e+06 |  |
| `BM_MetaLogCompress/100000/64` | 22.524 ms |  |  |  |  |  | 4.440e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 53.745 us |  |  |  |  |  | 1.861e+07 | 5.374e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 118.196 us |  |  |  |  |  | 8.461e+06 | 1.182e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 247.377 us |  |  |  |  |  | 4.043e+06 | 2.473e-07 |
| `BM_MetaLogIngest_Where` | 121.534 us |  |  |  |  |  | 8.229e+06 | 1.215e-07 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 4031.798 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4977.519 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 12403.926 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 31121.787 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 244.85 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 317.364 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3746.779 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4453.246 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 8663.481 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 543.864 us |  |  |  |  |  | 0.6 | 0 | 40453.163 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1348.924 us |  |  |  |  |  | 0.857 | 0 | 22833.888 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 5454.227 us |  |  |  |  |  | 0.857 | 0 | 5647.155 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7936.246 us |  |  |  |  |  | 0.857 | 0 | 3881.233 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 89680.492 us |  |  |  |  |  | 0.98 | 0 | 2404.129 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 99276.704 us |  |  |  |  |  | 0.98 | 0 | 2171.789 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 145827.615 us |  |  |  |  |  | 0.98 | 6 | 1478.553 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 444901.34 us |  |  |  |  |  | 0.98 | 0 | 484.615 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 368.585 ns | 2.983e+06 |
| `BM_Pipeline_IngestBatch/64` | 31449.666 ns | 2.245e+06 |
| `BM_Pipeline_IngestBatch/1024` | 404902.355 ns | 2.781e+06 |
| `BM_Pipeline_CloseWindow/1000` | 20445.922 ns | 54409.88 |
| `BM_Pipeline_CloseWindow/10000` | 32026.691 ns | 35161.439 |
| `BM_Pipeline_FullWindow/1000` | 471492.389 ns | 2.333e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.916e+06 ns | 2.809e+06 |

### `logcraft-core` — the deterministic log simulator core

_61 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | asio_ns_per_event | events_per_iter | interval_us | scheduler_ns_per_event | scheduler_overhead_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 6.859 ms | 1 | 874718.504 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 28.112 ms | 4 | 853724.521 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 156.667 ms | 16 | 612765.28 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 29.053 ms | 4 | 826064.759 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 155.312 ms | 16 | 618110.118 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 1.046 ms | 1 | 477833.339 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 3.526 ms | 4 | 567201.02 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 15.208 ms | 16 | 526043.591 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 82.892 ms | 64 | 386043.942 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 760.365 ms | 256 | 168340.216 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 8.251 ms | 32 | 1.939e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 14.304 ms | 32 | 1.119e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 22.196 ms | 32 | 720866.757 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 32.272 ms | 32 | 495784.412 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 32.795 ms | 32 | 487883.634 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 14.977 ms | 16 | 534160.253 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 15.284 ms | 16 | 523437.197 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 15.233 ms | 16 | 525180.764 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 15.035 ms | 16 | 532083.759 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 14.765 ms | 16 | 541829.881 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 15.032 ms | 16 | 532211.747 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.71 ns |  | 9.394e+07 |  |  | 2.715e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.17 ns |  | 1.172e+08 |  |  | 6.096e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 18.628 ns |  | 5.773e+07 |  |  | 5.773e+07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 15.564 ns |  | 6.922e+07 |  |  | 8.143e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.436 ns |  | 2.429e+08 |  |  | 1.943e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 102.078 ns |  | 1.055e+07 |  |  | 2.005e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 229.382 ns |  | 4.682e+06 |  |  | 2.575e+07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 408.22 ns |  | 2.631e+06 |  |  | 7.209e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 188.063 ns |  | 5.849e+06 |  |  | 1.065e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 275.974 ns |  | 3.986e+06 |  |  | 2.950e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 97.632 ns |  | 1.101e+07 |  |  | 5.947e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 135.349 ns |  | 7.944e+06 |  |  | 5.641e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 301.49 ns |  | 3.559e+06 |  |  | 7.117e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 424.302 ns |  | 2.529e+06 |  |  | 8.142e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 413.154 ns |  | 2.616e+06 |  |  | 1.820e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 339.039 ns |  | 3.187e+06 |  |  | 8.733e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 132.813 ns |  | 8.268e+06 |  |  | 1.505e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 243.583 ns |  | 4.516e+06 |  |  | 3.342e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 73.238 ns |  | 1.487e+07 |  |  | 8.030e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 99.821 ns |  | 1.091e+07 |  |  | 7.746e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 252.585 ns |  | 4.312e+06 |  |  | 8.623e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 339.928 ns |  | 3.125e+06 |  |  | 1.006e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 334.589 ns |  | 3.179e+06 |  |  | 2.213e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2977.806 us |  | 3.701e+06 |  |  |  | 8192 | 2.702e-07 |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2749.774 us |  | 4.008e+06 |  |  |  | 32768 | 2.495e-07 |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 225.58 us |  | 3.914e+07 |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 896.976 us |  | 3.927e+07 |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 6.291 ms |  | 3.179e+06 |  | 1 |  |  |  | 0 | 101521 | 1 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.72 ms |  | 4.785e+06 |  | 1 |  |  |  | 0 | 58534 | 4 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 22.127 ms |  | 3.615e+06 |  | 4 |  |  |  | 0 | 23733 | 4 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 44.74 ms |  | 7.152e+06 |  | 4 |  |  |  | 0 | 67454 | 16 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 50.505 ms |  | 6.336e+06 |  | 16 |  |  |  | 0 | 250839 | 16 | 0 |  |  |  |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 7.181 ms |  | 2.785e+06 |  | 1 |  |  |  | 82 | 0 | 1 | 7.472e+06 |  |  |  |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 19.712 ms |  | 4.059e+06 |  | 1 |  |  |  | 146 | 0 | 4 | 2.012e+07 |  |  |  |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 23.356 ms |  | 3.425e+06 |  | 4 |  |  |  | 102 | 0 | 4 | 1.248e+07 |  |  |  |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 45.743 ms |  | 6.996e+06 |  | 4 |  |  |  | 1336 | 0 | 16 | 3.668e+08 |  |  |  |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 57.545 ms |  | 5.561e+06 |  | 16 |  |  |  | 961 | 0 | 16 | 4.859e+08 |  |  |  |  |  |
| `BM_SimulationScheduler_TimerDrivenOverhead/250/real_time` | 36.16 ms |  | 1769.927 |  |  |  |  |  |  |  |  |  | 309404.977 | 64 | 250 | 251464.287 | -18.785 |
| `BM_SimulationScheduler_TimerDrivenOverhead/1000/real_time` | 137.454 ms |  | 465.61 |  |  |  |  |  |  |  |  |  | 1.141e+06 | 64 | 1000 | 1.002e+06 | -12.138 |
| `BM_SimulationScheduler_TimerDrivenOverhead/5000/real_time` | 670.545 ms |  | 95.445 |  |  |  |  |  |  |  |  |  | 5.463e+06 | 64 | 5000 | 5.008e+06 | -8.32 |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 40.682 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 40.922 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 41.687 ns | 65536 |
