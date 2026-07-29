# benchmark summary — v1.8.7

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1719.462 us | 581727.102 | 1.719e-06 |
| `BM_TokenizationThroughput/8` | 1602.795 us | 623871.925 | 1.603e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1669.965 us | 598796.905 | 1.670e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1554.585 us | 643269.828 | 1.555e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 253.248 us |  |  |  |  |  |  |  |
| `BM_Diff` | 419.662 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 82.28 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 127.683 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 146.7 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 8.993 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 8.637 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 8136.475 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 16157.219 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 24172.714 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 48869.2 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 99410.774 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 31050.217 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 84.457 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.251 ms |  |  |  |  |  | 799676.603 |  |
| `BM_MetaLogCompress/10000/16` | 4.469 ms |  |  |  |  |  | 2.238e+06 |  |
| `BM_MetaLogCompress/100000/16` | 21.913 ms |  |  |  |  |  | 4.564e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.258 ms |  |  |  |  |  | 795067.513 |  |
| `BM_MetaLogCompress/10000/32` | 4.478 ms |  |  |  |  |  | 2.233e+06 |  |
| `BM_MetaLogCompress/100000/32` | 21.879 ms |  |  |  |  |  | 4.571e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.263 ms |  |  |  |  |  | 791786.221 |  |
| `BM_MetaLogCompress/10000/64` | 4.478 ms |  |  |  |  |  | 2.233e+06 |  |
| `BM_MetaLogCompress/100000/64` | 21.777 ms |  |  |  |  |  | 4.592e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 53.475 us |  |  |  |  |  | 1.870e+07 | 5.347e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 117.655 us |  |  |  |  |  | 8.500e+06 | 1.177e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 247.842 us |  |  |  |  |  | 4.035e+06 | 2.478e-07 |
| `BM_MetaLogIngest_Where` | 122.665 us |  |  |  |  |  | 8.152e+06 | 1.227e-07 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3847.588 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4692.016 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 12324.498 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 29634.292 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 232.198 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 292.005 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3484.093 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4273.449 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 8803.689 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 522.92 us |  |  |  |  |  | 0.6 | 0 | 38247.008 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1299.493 us |  |  |  |  |  | 0.857 | 0 | 21547.098 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 5172.245 us |  |  |  |  |  | 0.857 | 0 | 5413.622 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7493.17 us |  |  |  |  |  | 0.857 | 0 | 3736.729 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 84824.773 us |  |  |  |  |  | 0.98 | 0 | 2310.643 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 94344.598 us |  |  |  |  |  | 0.98 | 0 | 2077.517 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 137662.496 us |  |  |  |  |  | 0.98 | 6 | 1423.768 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 416394.087 us |  |  |  |  |  | 0.98 | 0 | 470.716 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 343.925 ns | 2.907e+06 |
| `BM_Pipeline_IngestBatch/64` | 28176.245 ns | 2.270e+06 |
| `BM_Pipeline_IngestBatch/1024` | 363241.519 ns | 2.817e+06 |
| `BM_Pipeline_CloseWindow/1000` | 20167.247 ns | 50164.96 |
| `BM_Pipeline_CloseWindow/10000` | 36033.05 ns | 29066.259 |
| `BM_Pipeline_FullWindow/1000` | 427550.594 ns | 2.339e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.508e+06 ns | 2.851e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.77 ms | 1 | 684140.756 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 18.302 ms | 4 | 1.311e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 54.318 ms | 16 | 1.767e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 18.239 ms | 4 | 1.316e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 55.089 ms | 16 | 1.743e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.576 ms | 1 | 868329.28 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.702 ms | 4 | 2.847e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.663 ms | 16 | 4.811e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 6.007 ms | 64 | 5.327e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 21.602 ms | 256 | 5.925e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.781 ms | 32 | 3.346e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 3.178 ms | 32 | 5.035e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 3.016 ms | 32 | 5.305e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 3.232 ms | 32 | 4.950e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.894 ms | 32 | 4.109e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.712 ms | 16 | 4.672e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.849 ms | 16 | 4.327e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.769 ms | 16 | 4.521e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.232 ms | 16 | 3.584e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.957 ms | 16 | 2.706e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.454 ms | 16 | 1.796e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.2 ns |  | 8.928e+07 |  |  | 2.580e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.39 ns |  | 1.065e+08 |  |  | 5.538e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 17.676 ns |  | 5.657e+07 |  |  | 5.657e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.951 ns |  | 6.689e+07 |  |  | 7.868e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.53 ns |  | 2.207e+08 |  |  | 1.766e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 97.342 ns |  | 1.027e+07 |  |  | 1.952e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 84.261 ns |  | 1.187e+07 |  |  | 6.527e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 380.617 ns |  | 2.627e+06 |  |  | 6.910e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 181.673 ns |  | 5.505e+06 |  |  | 1.002e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 279.577 ns |  | 3.577e+06 |  |  | 2.647e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 96.852 ns |  | 1.033e+07 |  |  | 5.576e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 130.821 ns |  | 7.644e+06 |  |  | 5.427e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 305.19 ns |  | 3.277e+06 |  |  | 6.554e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 425.277 ns |  | 2.351e+06 |  |  | 7.572e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 396.686 ns |  | 2.521e+06 |  |  | 1.755e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 341.584 ns |  | 2.928e+06 |  |  | 7.700e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 126.733 ns |  | 7.891e+06 |  |  | 1.436e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 254.234 ns |  | 3.933e+06 |  |  | 2.911e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 71.446 ns |  | 1.400e+07 |  |  | 7.558e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 98.255 ns |  | 1.018e+07 |  |  | 7.226e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 249.227 ns |  | 4.012e+06 |  |  | 8.025e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 335.314 ns |  | 2.982e+06 |  |  | 9.603e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 318.662 ns |  | 3.138e+06 |  |  | 2.184e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.385 ms | 1 |  | 6000 |  |  | 5.215 | 1.716 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 17.638 ms | 4 |  | 24000 |  |  | 3.969 | 8.077 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 52.947 ms | 16 |  | 96000 |  |  | 12.176 | 16.673 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2346.578 us |  | 4.315e+06 |  |  |  |  |  | 8192 | 2.318e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2178.605 us |  | 4.650e+06 |  |  |  |  |  | 32768 | 2.151e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 215.646 us |  | 3.801e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 862.773 us |  | 3.798e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.636 ms |  | 3.549e+06 |  | 1 |  |  |  |  |  | 0 | 134001 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.607 ms |  | 4.817e+06 |  | 1 |  |  |  |  |  | 0 | 113381 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 29.249 ms |  | 2.735e+06 |  | 4 |  |  |  |  |  | 0 | 161722 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 50.278 ms |  | 6.365e+06 |  | 4 |  |  |  |  |  | 0 | 597863 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 61.811 ms |  | 5.177e+06 |  | 16 |  |  |  |  |  | 0 | 597407 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 8.597 ms |  | 2.326e+06 |  | 1 |  |  |  |  |  | 274 | 0 | 1 | 6.525e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 18.733 ms |  | 4.270e+06 |  | 1 |  |  |  |  |  | 659 | 0 | 4 | 4.777e+07 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 38.175 ms |  | 2.096e+06 |  | 4 |  |  |  |  |  | 500 | 0 | 4 | 4.005e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 66.25 ms |  | 4.830e+06 |  | 4 |  |  |  |  |  | 4755 | 0 | 16 | 2.677e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 69.159 ms |  | 4.627e+06 |  | 16 |  |  |  |  |  | 1685 | 0 | 16 | 1.125e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 6.038 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 10.544 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 67.595 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 68.359 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 67.791 ns | 65536 |
