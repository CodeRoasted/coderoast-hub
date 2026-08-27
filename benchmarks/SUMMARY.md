# benchmark summary — v1.10.1

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_5 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1740.267 us | 574811.83 | 1.740e-06 |
| `BM_TokenizationThroughput/8` | 1624.476 us | 615622.875 | 1.624e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1692.544 us | 590853.075 | 1.692e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1582.054 us | 632084.134 | 1.582e-06 |
| `BM_TokenizationThroughputNestedJson` | 2801.608 us | 356960.422 | 2.801e-06 |

### `insight-metalog` — compression / MetaLog-document build

_31 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 277.377 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 432.482 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 78.19 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 121.265 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 128.42 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 9.91 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 8.387 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 9062.746 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 18015.249 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 26939.903 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 53852.043 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 109058.717 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 37845.755 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 90.955 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 45.824 us |  |  |  |  |  | 0 | 2.188e+07 | 4.571e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 62.301 us |  |  |  |  |  | 0 | 1.608e+07 | 6.218e-08 |
| `BM_CubeKeyAlloc_MidBand` | 63.549 us |  |  |  |  |  | 0 | 1.576e+07 | 6.346e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 65.235 us |  |  |  |  |  | 0 | 1.536e+07 | 6.511e-08 |
| `BM_MetaLogCompress/1000/16` | 1.288 ms |  |  |  |  |  |  | 776491.518 |  |
| `BM_MetaLogCompress/10000/16` | 4.573 ms |  |  |  |  |  |  | 2.187e+06 |  |
| `BM_MetaLogCompress/100000/16` | 21.647 ms |  |  |  |  |  |  | 4.620e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.294 ms |  |  |  |  |  |  | 772759.713 |  |
| `BM_MetaLogCompress/10000/32` | 4.573 ms |  |  |  |  |  |  | 2.187e+06 |  |
| `BM_MetaLogCompress/100000/32` | 21.642 ms |  |  |  |  |  |  | 4.621e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.298 ms |  |  |  |  |  |  | 770425.984 |  |
| `BM_MetaLogCompress/10000/64` | 4.585 ms |  |  |  |  |  |  | 2.181e+06 |  |
| `BM_MetaLogCompress/100000/64` | 21.627 ms |  |  |  |  |  |  | 4.624e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 42.166 us |  |  |  |  |  |  | 2.372e+07 | 4.216e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 101.958 us |  |  |  |  |  |  | 9.809e+06 | 1.019e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 232.924 us |  |  |  |  |  |  | 4.294e+06 | 2.329e-07 |
| `BM_MetaLogIngest_Where` | 88.877 us |  |  |  |  |  |  | 1.125e+07 | 8.886e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 2207.39 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2609.985 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 6805.442 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 16706.117 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 245.994 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 311.352 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1898.491 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 2315.866 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7560.774 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 839.256 us |  |  |  |  |  | 0.609 | 0 | 27406.088 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1610.874 us |  |  |  |  |  | 0.857 | 0 | 17381.805 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 6565.702 us |  |  |  |  |  | 0.857 | 0 | 4264.639 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 6547.745 us |  |  |  |  |  | 0.857 | 0 | 4276.374 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 77491.185 us |  |  |  |  |  | 0.98 | 0 | 2529.376 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 78427.902 us |  |  |  |  |  | 0.98 | 0 | 2499.107 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 179167.266 us |  |  |  |  |  | 0.971 | 6 | 1166.523 | 6 | 7 | 193 | 20 | 209 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 354601.067 us |  |  |  |  |  | 0.98 | 0 | 552.921 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 363.194 ns | 2.752e+06 |
| `BM_Pipeline_IngestBatch/64` | 30544.504 ns | 2.092e+06 |
| `BM_Pipeline_IngestBatch/1024` | 388915.489 ns | 2.629e+06 |
| `BM_Pipeline_CloseWindow/1000` | 21365.373 ns | 47351.273 |
| `BM_Pipeline_CloseWindow/10000` | 36457.896 ns | 28049.071 |
| `BM_Pipeline_FullWindow/1000` | 796576.851 ns | 1.255e+06 |
| `BM_Pipeline_FullWindow/10000` | 8.567e+06 ns | 1.167e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.776 ms | 1 | 683680.054 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 17.919 ms | 4 | 1.339e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 49.644 ms | 16 | 1.934e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 17.189 ms | 4 | 1.396e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 51.039 ms | 16 | 1.881e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.576 ms | 1 | 867895.351 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.711 ms | 4 | 2.812e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.701 ms | 16 | 4.704e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 7.845 ms | 64 | 4.079e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 31.204 ms | 256 | 4.102e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 5.424 ms | 32 | 2.950e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 4.094 ms | 32 | 3.908e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 3.822 ms | 32 | 4.186e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 4.895 ms | 32 | 3.268e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 5.603 ms | 32 | 2.855e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 2.361 ms | 16 | 3.388e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 2.569 ms | 16 | 3.115e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 2.689 ms | 16 | 2.975e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.702 ms | 16 | 2.961e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 3.781 ms | 16 | 2.116e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 5.767 ms | 16 | 1.387e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.719 ns |  | 8.533e+07 |  |  | 2.466e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 10.125 ns |  | 9.878e+07 |  |  | 5.136e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 19.385 ns |  | 5.159e+07 |  |  | 5.159e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 16.19 ns |  | 6.177e+07 |  |  | 7.257e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 5.392 ns |  | 1.855e+08 |  |  | 1.484e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 91.751 ns |  | 1.090e+07 |  |  | 2.071e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 89.522 ns |  | 1.117e+07 |  |  | 6.144e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 431.954 ns |  | 2.315e+06 |  |  | 6.089e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 195.661 ns |  | 5.111e+06 |  |  | 9.302e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 291.347 ns |  | 3.432e+06 |  |  | 2.540e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 96.03 ns |  | 1.041e+07 |  |  | 5.623e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 140.022 ns |  | 7.142e+06 |  |  | 5.071e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 316.894 ns |  | 3.156e+06 |  |  | 6.311e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 485.726 ns |  | 2.059e+06 |  |  | 6.629e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 460.746 ns |  | 2.170e+06 |  |  | 1.511e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 383.419 ns |  | 2.608e+06 |  |  | 6.859e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 133.269 ns |  | 7.504e+06 |  |  | 1.366e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 256.247 ns |  | 3.902e+06 |  |  | 2.888e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 70.205 ns |  | 1.424e+07 |  |  | 7.692e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 98.231 ns |  | 1.018e+07 |  |  | 7.228e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 288.033 ns |  | 3.472e+06 |  |  | 6.944e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 411.313 ns |  | 2.431e+06 |  |  | 7.829e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 382.028 ns |  | 2.618e+06 |  |  | 1.822e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 9.132 ms | 1 |  | 6000 |  |  | 5.599 | 1.886 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 21.485 ms | 4 |  | 24000 |  |  | 5.343 | 9.005 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 65.675 ms | 16 |  | 96000 |  |  | 16.016 | 21.594 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2799.306 us |  | 3.639e+06 |  |  |  |  |  | 8192 | 2.748e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2475.408 us |  | 4.134e+06 |  |  |  |  |  | 32768 | 2.419e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 229.986 us |  | 3.562e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 916.384 us |  | 3.576e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.769 ms |  | 3.467e+06 |  | 1 |  |  |  |  |  | 0 | 173151 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.506 ms |  | 4.847e+06 |  | 1 |  |  |  |  |  | 0 | 656740 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 38.842 ms |  | 2.060e+06 |  | 4 |  |  |  |  |  | 0 | 293556 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 58.71 ms |  | 5.451e+06 |  | 4 |  |  |  |  |  | 0 | 1.242e+06 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 68.299 ms |  | 4.685e+06 |  | 16 |  |  |  |  |  | 0 | 887767 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.459 ms |  | 3.096e+06 |  | 1 |  |  |  |  |  | 190 | 0 | 1 | 1.294e+07 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 21.969 ms |  | 3.642e+06 |  | 1 |  |  |  |  |  | 1043 | 0 | 4 | 3.903e+08 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 34.993 ms |  | 2.286e+06 |  | 4 |  |  |  |  |  | 995 | 0 | 4 | 1.783e+08 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 135.77 ms |  | 2.357e+06 |  | 4 |  |  |  |  |  | 4879 | 0 | 16 | 6.823e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 107.294 ms |  | 2.982e+06 |  | 16 |  |  |  |  |  | 1902 | 0 | 16 | 3.042e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 6.553 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 11.357 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 36.108 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 36.519 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 36.909 ns | 65536 |
