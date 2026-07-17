# benchmark summary — v1.8.1

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1633.218 us | 612326.151 | 1.633e-06 |
| `BM_TokenizationThroughput/8` | 1522.726 us | 656738.34 | 1.523e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1589.458 us | 629148.154 | 1.589e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1481.692 us | 674886.416 | 1.482e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 253.668 us |  |  |  |  |  |  |  |
| `BM_Diff` | 419.004 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 83.422 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 128.137 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 150.302 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 9.093 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 8.658 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 8131.384 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 16153.857 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 24169.003 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 48923.183 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 100059.12 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 30975.458 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 87.624 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.255 ms |  |  |  |  |  | 796648.804 |  |
| `BM_MetaLogCompress/10000/16` | 4.558 ms |  |  |  |  |  | 2.194e+06 |  |
| `BM_MetaLogCompress/100000/16` | 22.507 ms |  |  |  |  |  | 4.444e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.262 ms |  |  |  |  |  | 792739.739 |  |
| `BM_MetaLogCompress/10000/32` | 4.565 ms |  |  |  |  |  | 2.191e+06 |  |
| `BM_MetaLogCompress/100000/32` | 22.426 ms |  |  |  |  |  | 4.459e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.27 ms |  |  |  |  |  | 787408.559 |  |
| `BM_MetaLogCompress/10000/64` | 4.572 ms |  |  |  |  |  | 2.187e+06 |  |
| `BM_MetaLogCompress/100000/64` | 22.498 ms |  |  |  |  |  | 4.445e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 54.692 us |  |  |  |  |  | 1.829e+07 | 5.469e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 123.594 us |  |  |  |  |  | 8.092e+06 | 1.236e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 254.79 us |  |  |  |  |  | 3.926e+06 | 2.547e-07 |
| `BM_MetaLogIngest_Where` | 123.828 us |  |  |  |  |  | 8.078e+06 | 1.238e-07 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3969.148 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4885.902 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 12249.6 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 31010.242 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 245.199 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 316.553 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3656.732 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4350.137 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 8604.181 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 553.69 us |  |  |  |  |  | 0.6 | 0 | 37653.012 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1369.302 us |  |  |  |  |  | 0.857 | 0 | 21315.649 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 5578.383 us |  |  |  |  |  | 0.857 | 0 | 5248.714 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 8012.768 us |  |  |  |  |  | 0.857 | 0 | 3653.695 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 88395.896 us |  |  |  |  |  | 0.98 | 0 | 2316.071 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 98284.263 us |  |  |  |  |  | 0.98 | 0 | 2083.052 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 146062.693 us |  |  |  |  |  | 0.98 | 6 | 1399.245 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 439053.473 us |  |  |  |  |  | 0.98 | 0 | 465.497 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 349.45 ns | 2.983e+06 |
| `BM_Pipeline_IngestBatch/64` | 29057.023 ns | 2.295e+06 |
| `BM_Pipeline_IngestBatch/1024` | 373699.97 ns | 2.865e+06 |
| `BM_Pipeline_CloseWindow/1000` | 20635.713 ns | 51125.352 |
| `BM_Pipeline_CloseWindow/10000` | 34944.305 ns | 30800.384 |
| `BM_Pipeline_FullWindow/1000` | 483365.404 ns | 2.169e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.600e+06 ns | 2.912e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 9.768 ms | 1 | 614232.027 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 18.048 ms | 4 | 1.330e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 58.194 ms | 16 | 1.650e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 18.747 ms | 4 | 1.280e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 54.513 ms | 16 | 1.761e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.609 ms | 1 | 820852.333 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.789 ms | 4 | 2.534e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.79 ms | 16 | 4.469e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 6.242 ms | 64 | 5.127e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 22.344 ms | 256 | 5.729e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 5.328 ms | 32 | 3.003e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 3.207 ms | 32 | 4.989e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 3.242 ms | 32 | 4.936e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 3.515 ms | 32 | 4.552e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 4.519 ms | 32 | 3.540e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.798 ms | 16 | 4.449e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.901 ms | 16 | 4.209e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.924 ms | 16 | 4.158e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.361 ms | 16 | 3.389e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 3.136 ms | 16 | 2.551e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.51 ms | 16 | 1.774e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 12.165 ns |  | 8.605e+07 |  |  | 2.487e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.53 ns |  | 1.051e+08 |  |  | 5.466e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 19.601 ns |  | 5.470e+07 |  |  | 5.470e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 16.043 ns |  | 6.753e+07 |  |  | 7.946e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 5.151 ns |  | 2.102e+08 |  |  | 1.682e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 98.764 ns |  | 1.013e+07 |  |  | 1.925e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 243.265 ns |  | 4.339e+06 |  |  | 2.386e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 402.204 ns |  | 2.486e+06 |  |  | 6.813e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 192.977 ns |  | 5.384e+06 |  |  | 9.798e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 310.946 ns |  | 3.358e+06 |  |  | 2.485e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 96.632 ns |  | 1.035e+07 |  |  | 5.588e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 147.306 ns |  | 7.354e+06 |  |  | 5.222e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 312.49 ns |  | 3.230e+06 |  |  | 6.461e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 455.452 ns |  | 2.350e+06 |  |  | 7.568e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 407.092 ns |  | 2.456e+06 |  |  | 1.710e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 349.237 ns |  | 3.005e+06 |  |  | 8.233e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 131.139 ns |  | 7.626e+06 |  |  | 1.388e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 267.842 ns |  | 3.878e+06 |  |  | 2.870e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 72.482 ns |  | 1.387e+07 |  |  | 7.489e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 105.36 ns |  | 1.018e+07 |  |  | 7.227e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 286.416 ns |  | 3.741e+06 |  |  | 7.483e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 372.777 ns |  | 2.887e+06 |  |  | 9.295e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 341.228 ns |  | 2.971e+06 |  |  | 2.068e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 9.302 ms | 1 |  | 6000 |  |  | 5.743 | 2.002 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 16.294 ms | 4 |  | 24000 |  |  | 4.107 | 8.024 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 50.359 ms | 16 |  | 96000 |  |  | 12.215 | 16.934 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2492.115 us |  | 4.398e+06 |  |  |  |  |  | 8192 | 2.274e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2170.901 us |  | 4.660e+06 |  |  |  |  |  | 32768 | 2.146e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 236.623 us |  | 3.654e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 936.303 us |  | 3.709e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.634 ms |  | 3.550e+06 |  | 1 |  |  |  |  |  | 0 | 131869 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 15.955 ms |  | 5.014e+06 |  | 1 |  |  |  |  |  | 0 | 220102 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 32.672 ms |  | 2.449e+06 |  | 4 |  |  |  |  |  | 0 | 127077 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 52.727 ms |  | 6.069e+06 |  | 4 |  |  |  |  |  | 0 | 755827 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 66.268 ms |  | 4.829e+06 |  | 16 |  |  |  |  |  | 0 | 944082 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.634 ms |  | 3.015e+06 |  | 1 |  |  |  |  |  | 149 | 0 | 1 | 7.176e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 20.48 ms |  | 3.906e+06 |  | 1 |  |  |  |  |  | 579 | 0 | 4 | 1.135e+08 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 31.206 ms |  | 2.564e+06 |  | 4 |  |  |  |  |  | 1078 | 0 | 4 | 1.109e+08 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 89.369 ms |  | 3.581e+06 |  | 4 |  |  |  |  |  | 5846 | 0 | 16 | 4.256e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 88.252 ms |  | 3.626e+06 |  | 16 |  |  |  |  |  | 1956 | 0 | 16 | 1.913e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 5.979 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 10.549 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 81.821 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 81.798 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 81.99 ns | 65536 |
