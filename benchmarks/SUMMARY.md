# benchmark summary — v1.7.4

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_2 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1559.85 us | 641210.663 | 1.560e-06 |
| `BM_TokenizationThroughput/8` | 1448.614 us | 690357.494 | 1.449e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 253.836 us |  |  |  |  |  |  |  |
| `BM_Diff` | 421.404 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 82.471 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 128.744 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 148.797 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 9.582 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 8.67 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 8150.654 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 16313.579 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 24239.924 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 48874.06 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 100763.496 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 30914.423 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 85.01 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.261 ms |  |  |  |  |  | 793251.593 |  |
| `BM_MetaLogCompress/10000/16` | 4.581 ms |  |  |  |  |  | 2.183e+06 |  |
| `BM_MetaLogCompress/100000/16` | 22.949 ms |  |  |  |  |  | 4.358e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.272 ms |  |  |  |  |  | 786276.621 |  |
| `BM_MetaLogCompress/10000/32` | 4.615 ms |  |  |  |  |  | 2.167e+06 |  |
| `BM_MetaLogCompress/100000/32` | 23.02 ms |  |  |  |  |  | 4.345e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.279 ms |  |  |  |  |  | 782222.813 |  |
| `BM_MetaLogCompress/10000/64` | 4.606 ms |  |  |  |  |  | 2.171e+06 |  |
| `BM_MetaLogCompress/100000/64` | 23.089 ms |  |  |  |  |  | 4.331e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 56.49 us |  |  |  |  |  | 1.771e+07 | 5.648e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 121.001 us |  |  |  |  |  | 8.266e+06 | 1.210e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 249.581 us |  |  |  |  |  | 4.007e+06 | 2.496e-07 |
| `BM_MetaLogIngest_Where` | 123.547 us |  |  |  |  |  | 8.095e+06 | 1.235e-07 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 4052.659 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4762.593 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 12182.804 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 30420.11 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 244.609 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 310.611 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3658.946 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4537.52 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7348.679 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 535.537 us |  |  |  |  |  | 0.6 | 0 | 36771.744 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1325.832 us |  |  |  |  |  | 0.857 | 0 | 21030.751 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 5408.005 us |  |  |  |  |  | 0.857 | 0 | 5190.897 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7850.533 us |  |  |  |  |  | 0.857 | 0 | 3589.153 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 89228.333 us |  |  |  |  |  | 0.98 | 0 | 2216.675 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 100003.407 us |  |  |  |  |  | 0.98 | 0 | 1987.791 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 146732.552 us |  |  |  |  |  | 0.98 | 6 | 1350.82 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 441108.37 us |  |  |  |  |  | 0.98 | 0 | 449.266 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 330.828 ns | 3.058e+06 |
| `BM_Pipeline_IngestBatch/64` | 27240.321 ns | 2.374e+06 |
| `BM_Pipeline_IngestBatch/1024` | 342734.919 ns | 3.022e+06 |
| `BM_Pipeline_CloseWindow/1000` | 20676.967 ns | 48739.776 |
| `BM_Pipeline_CloseWindow/10000` | 32211.979 ns | 32021.595 |
| `BM_Pipeline_FullWindow/1000` | 416094.802 ns | 2.433e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.362e+06 ns | 3.011e+06 |

### `logcraft-core` — the deterministic log simulator core

_61 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | asio_ns_per_event | events_per_iter | interval_us | scheduler_ns_per_event | scheduler_overhead_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 6.631 ms | 1 | 904818.602 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 29.474 ms | 4 | 814278.641 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 163.755 ms | 16 | 586241.615 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 28.932 ms | 4 | 829530.181 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 163.882 ms | 16 | 585786.271 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.948 ms | 1 | 527182.9 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 3.147 ms | 4 | 635547.628 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 14.616 ms | 16 | 547335.983 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 78.084 ms | 64 | 409816.036 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 764.647 ms | 256 | 167397.606 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 7.399 ms | 32 | 2.163e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 13.598 ms | 32 | 1.177e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 22.046 ms | 32 | 725758.84 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 30.956 ms | 32 | 516860.123 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 32.667 ms | 32 | 489792.453 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 13.548 ms | 16 | 590514.408 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 14.097 ms | 16 | 567504.814 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 14.352 ms | 16 | 557415.387 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 14.702 ms | 16 | 544151.19 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 14.584 ms | 16 | 548564.141 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 15.245 ms | 16 | 524755.865 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.356 ns |  | 8.806e+07 |  |  | 2.545e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.408 ns |  | 1.063e+08 |  |  | 5.528e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 17.96 ns |  | 5.568e+07 |  |  | 5.568e+07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 15.558 ns |  | 6.428e+07 |  |  | 7.557e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.636 ns |  | 2.157e+08 |  |  | 1.725e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 101.143 ns |  | 9.887e+06 |  |  | 1.879e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 231.469 ns |  | 4.320e+06 |  |  | 2.376e+07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 407.77 ns |  | 2.452e+06 |  |  | 6.720e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 188.345 ns |  | 5.310e+06 |  |  | 9.664e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 266.369 ns |  | 3.754e+06 |  |  | 2.778e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 106.382 ns |  | 9.400e+06 |  |  | 5.076e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 137.373 ns |  | 7.280e+06 |  |  | 5.169e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 321.192 ns |  | 3.113e+06 |  |  | 6.227e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 399.955 ns |  | 2.500e+06 |  |  | 8.051e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 396.613 ns |  | 2.521e+06 |  |  | 1.755e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 330.179 ns |  | 3.029e+06 |  |  | 8.299e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 131.164 ns |  | 7.624e+06 |  |  | 1.388e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 234.964 ns |  | 4.256e+06 |  |  | 3.150e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 72.589 ns |  | 1.378e+07 |  |  | 7.439e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 99.717 ns |  | 1.003e+07 |  |  | 7.120e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 269.061 ns |  | 3.717e+06 |  |  | 7.434e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 332.708 ns |  | 3.006e+06 |  |  | 9.678e+08 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 320.202 ns |  | 3.123e+06 |  |  | 2.174e+09 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2573.469 us |  | 3.955e+06 |  |  |  | 8192 | 2.529e-07 |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2365.458 us |  | 4.320e+06 |  |  |  | 32768 | 2.315e-07 |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 204.805 us |  | 4.002e+07 |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 821.028 us |  | 3.992e+07 |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.499 ms |  | 3.637e+06 |  | 1 |  |  |  | 0 | 168438 | 1 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.219 ms |  | 4.933e+06 |  | 1 |  |  |  | 0 | 191665 | 4 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 24.409 ms |  | 3.278e+06 |  | 4 |  |  |  | 0 | 99057 | 4 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 44.865 ms |  | 7.133e+06 |  | 4 |  |  |  | 0 | 583387 | 16 | 0 |  |  |  |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 67.933 ms |  | 4.711e+06 |  | 16 |  |  |  | 0 | 656257 | 16 | 0 |  |  |  |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.306 ms |  | 3.172e+06 |  | 1 |  |  |  | 171 | 0 | 1 | 8.528e+06 |  |  |  |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 19.113 ms |  | 4.186e+06 |  | 1 |  |  |  | 597 | 0 | 4 | 9.822e+07 |  |  |  |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 27.774 ms |  | 2.880e+06 |  | 4 |  |  |  | 535 | 0 | 4 | 5.541e+07 |  |  |  |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 58.309 ms |  | 5.488e+06 |  | 4 |  |  |  | 3271 | 0 | 16 | 1.911e+09 |  |  |  |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 79.751 ms |  | 4.013e+06 |  | 16 |  |  |  | 2076 | 0 | 16 | 1.833e+09 |  |  |  |  |  |
| `BM_SimulationScheduler_TimerDrivenOverhead/250/real_time` | 34.331 ms |  | 1864.199 |  |  |  |  |  |  |  |  |  | 281265.175 | 64 | 250 | 250769.378 | -10.838 |
| `BM_SimulationScheduler_TimerDrivenOverhead/1000/real_time` | 130.613 ms |  | 489.996 |  |  |  |  |  |  |  |  |  | 1.035e+06 | 64 | 1000 | 1.001e+06 | -3.302 |
| `BM_SimulationScheduler_TimerDrivenOverhead/5000/real_time` | 642.739 ms |  | 99.574 |  |  |  |  |  |  |  |  |  | 5.036e+06 | 64 | 5000 | 5.001e+06 | -0.704 |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 49.925 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 49.894 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 51.879 ns | 65536 |
