# benchmark summary — v1.7.1

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_2 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1601.689 us | 624323.739 | 1.602e-06 |
| `BM_TokenizationThroughput/8` | 1474.914 us | 678011.255 | 1.475e-06 |

### `insight-metalog` — compression / MetaLog-document build

_30 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose/0` | 34.104 us |  |  |  |  |  |  |  |
| `BM_Compose/1` | 262.502 us |  |  |  |  |  |  |  |
| `BM_Diff/0` | 131.705 us |  |  |  |  |  |  |  |
| `BM_Diff/1` | 408.684 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 71.331 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 107.867 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 112.387 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 9.848 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 8.309 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 8906.376 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 17685.682 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 26447.945 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 54466.223 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 110639.104 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 35031.279 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 79.63 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.288 ms |  |  |  |  |  | 776289.606 |  |
| `BM_MetaLogCompress/10000/16` | 4.576 ms |  |  |  |  |  | 2.185e+06 |  |
| `BM_MetaLogCompress/100000/16` | 21.73 ms |  |  |  |  |  | 4.602e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.288 ms |  |  |  |  |  | 776505.307 |  |
| `BM_MetaLogCompress/10000/32` | 4.583 ms |  |  |  |  |  | 2.182e+06 |  |
| `BM_MetaLogCompress/100000/32` | 21.84 ms |  |  |  |  |  | 4.580e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.296 ms |  |  |  |  |  | 771445.898 |  |
| `BM_MetaLogCompress/10000/64` | 4.587 ms |  |  |  |  |  | 2.180e+06 |  |
| `BM_MetaLogCompress/100000/64` | 21.788 ms |  |  |  |  |  | 4.590e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 39.391 us |  |  |  |  |  | 2.539e+07 | 3.938e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 99.74 us |  |  |  |  |  | 1.003e+07 | 9.973e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 232.11 us |  |  |  |  |  | 4.309e+06 | 2.321e-07 |
| `BM_MetaLogIngest_Where/0` | 53.039 us |  |  |  |  |  | 1.886e+07 | 5.303e-08 |
| `BM_MetaLogIngest_Where/1` | 69.825 us |  |  |  |  |  | 1.432e+07 | 6.982e-08 |

### `insight-eidos-detection` — eidos detection stage

_25 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | emit_cube | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/0/16` | 1007.947 us | 16 | 0.917 | 0 | 10 | 0 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/2000/1/16` | 3427.797 us | 16 | 0.917 | 269 | 10 | 1 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/0/16` | 992.999 us | 16 | 0.917 | 0 | 10 | 0 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/1/16` | 4064.753 us | 16 | 0.917 | 392 | 10 | 1 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/0/64` | 986.565 us | 64 | 0.917 | 0 | 10 | 0 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/1/64` | 10458.597 us | 64 | 0.917 | 965 | 10 | 1 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/0/256` | 987.572 us | 256 | 0.917 | 0 | 10 | 0 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/1/256` | 26174.039 us | 256 | 0.917 | 2198 | 10 | 1 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/0/16` | 33.825 us | 16 | 0.917 | 0 | 10 | 0 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/1/16` | 209.984 us | 16 | 0.917 | 269 | 10 | 1 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/0/16` | 29.322 us | 16 | 0.917 | 0 | 10 | 0 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/1/16` | 262.417 us | 16 | 0.917 | 392 | 10 | 1 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/0/16` | 874.947 us | 16 | 0.917 | 0 | 10 | 0 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/1/16` | 3077.805 us | 16 | 0.917 | 269 | 10 | 1 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/0/16` | 857.565 us | 16 | 0.917 | 0 | 10 | 0 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/1/16` | 3758.996 us | 16 | 0.917 | 392 | 10 | 1 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7395.888 us |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 454.084 us |  |  |  |  |  |  | 0.6 | 0 | 46528.915 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1122.395 us |  |  |  |  |  |  | 0.857 | 0 | 26354.736 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 4566.678 us |  |  |  |  |  |  | 0.857 | 0 | 6482.02 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 6605.501 us |  |  |  |  |  |  | 0.857 | 0 | 4481.424 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 73571.937 us |  |  |  |  |  |  | 0.98 | 0 | 2819.422 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 81934.882 us |  |  |  |  |  |  | 0.98 | 0 | 2533.137 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 120399.591 us |  |  |  |  |  |  | 0.98 | 6 | 1723.89 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 371405.449 us |  |  |  |  |  |  | 0.98 | 0 | 557.991 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 269.474 ns | 3.922e+06 |
| `BM_Pipeline_IngestBatch/64` | 22599.619 ns | 2.990e+06 |
| `BM_Pipeline_IngestBatch/1024` | 287208.624 ns | 3.763e+06 |
| `BM_Pipeline_CloseWindow/1000` | 10422.798 ns | 102710.673 |
| `BM_Pipeline_CloseWindow/10000` | 17562.107 ns | 62936.376 |
| `BM_Pipeline_FullWindow/1000` | 327938.865 ns | 3.223e+06 |
| `BM_Pipeline_FullWindow/10000` | 2.824e+06 ns | 3.758e+06 |

### `logcraft-core` — the deterministic log simulator core

_61 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | asio_ns_per_event | events_per_iter | interval_us | scheduler_ns_per_event | scheduler_overhead_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 6.787 ms | 1 | 884055.421 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 28.349 ms | 4 | 846599.363 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 162.68 ms | 16 | 590115.543 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 28.63 ms | 4 | 838278.105 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 160.876 ms | 16 | 596734.227 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.66 ms | 1 | 757700.177 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 3.299 ms | 4 | 606184.343 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 14.393 ms | 16 | 555816.405 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 87.059 ms | 64 | 367565.44 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 870.783 ms | 256 | 146994.076 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 7.819 ms | 32 | 2.046e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 13.951 ms | 32 | 1.147e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 21.47 ms | 32 | 745226.946 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 31.51 ms | 32 | 507774.1 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 33.184 ms | 32 | 482166.531 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 13.863 ms | 16 | 577072.785 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 13.951 ms | 16 | 573418.633 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 14.305 ms | 16 | 559256.612 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 14.314 ms | 16 | 558879.658 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 14.036 ms | 16 | 569959.022 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 13.975 ms | 16 | 572462.453 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.727 ns |  | 9.215e+07 |  |  | 2.663e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.624 ns |  | 1.123e+08 |  |  | 5.839e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 18.586 ns |  | 5.918e+07 |  |  | 5.918e+07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 16.21 ns |  | 6.786e+07 |  |  | 7.988e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.971 ns |  | 2.162e+08 |  |  | 1.730e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 103.838 ns |  | 1.033e+07 |  |  | 1.962e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 233.761 ns |  | 4.587e+06 |  |  | 2.523e+07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 419.847 ns |  | 2.560e+06 |  |  | 7.015e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 190.64 ns |  | 5.638e+06 |  |  | 1.026e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 289.276 ns |  | 3.788e+06 |  |  | 2.803e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 101.351 ns |  | 1.065e+07 |  |  | 5.753e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 142.51 ns |  | 7.557e+06 |  |  | 5.366e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 315.869 ns |  | 3.410e+06 |  |  | 6.819e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 431.351 ns |  | 2.505e+06 |  |  | 8.065e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 428.157 ns |  | 2.523e+06 |  |  | 1.756e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 354.855 ns |  | 3.028e+06 |  |  | 8.297e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 135.952 ns |  | 7.904e+06 |  |  | 1.439e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 265.997 ns |  | 4.120e+06 |  |  | 3.049e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 77.055 ns |  | 1.422e+07 |  |  | 7.680e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 101.656 ns |  | 1.059e+07 |  |  | 7.521e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 262.144 ns |  | 4.099e+06 |  |  | 8.198e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 357.005 ns |  | 3.014e+06 |  |  | 9.705e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 370.027 ns |  | 2.910e+06 |  |  | 2.025e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2749.149 us |  | 3.971e+06 |  |  |  | 8192 | 2.519e-07 |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2762.571 us |  | 3.969e+06 |  |  |  | 32768 | 2.520e-07 |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 210.199 us |  | 4.288e+07 |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 826.454 us |  | 4.248e+07 |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 6.252 ms |  | 3.199e+06 |  | 1 |  |  |  | 0 | 84942 | 1 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 17.022 ms |  | 4.700e+06 |  | 1 |  |  |  | 0 | 30657 | 4 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 22.646 ms |  | 3.533e+06 |  | 4 |  |  |  | 0 | 43360 | 4 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 44.666 ms |  | 7.164e+06 |  | 4 |  |  |  | 0 | 128130 | 16 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 54.21 ms |  | 5.903e+06 |  | 16 |  |  |  | 0 | 243980 | 16 | 0 |  |  |  |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 7.97 ms |  | 2.509e+06 |  | 1 |  |  |  | 72 | 0 | 1 | 9.693e+06 |  |  |  |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 19.569 ms |  | 4.088e+06 |  | 1 |  |  |  | 187 | 0 | 4 | 2.330e+07 |  |  |  |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 24.271 ms |  | 3.296e+06 |  | 4 |  |  |  | 154 | 0 | 4 | 8.701e+06 |  |  |  |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 47.41 ms |  | 6.750e+06 |  | 4 |  |  |  | 1792 | 0 | 16 | 4.893e+08 |  |  |  |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 58.709 ms |  | 5.451e+06 |  | 16 |  |  |  | 1529 | 0 | 16 | 7.188e+08 |  |  |  |  |  |
| `BM_SimulationScheduler_TimerDrivenOverhead/250/real_time` | 35.704 ms |  | 1792.495 |  |  |  |  |  |  |  |  |  | 302273.597 | 64 | 250 | 251130.164 | -16.629 |
| `BM_SimulationScheduler_TimerDrivenOverhead/1000/real_time` | 135.595 ms |  | 471.994 |  |  |  |  |  |  |  |  |  | 1.113e+06 | 64 | 1000 | 1.002e+06 | -9.966 |
| `BM_SimulationScheduler_TimerDrivenOverhead/5000/real_time` | 673.043 ms |  | 95.09 |  |  |  |  |  |  |  |  |  | 5.504e+06 | 64 | 5000 | 5.008e+06 | -9.023 |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 80.554 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 80.527 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 80.554 ns | 65536 |
