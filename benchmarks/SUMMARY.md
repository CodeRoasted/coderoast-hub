# benchmark summary — v1.9.4

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_5 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1765.692 us | 566346.64 | 1.766e-06 |
| `BM_TokenizationThroughput/8` | 1638.003 us | 610516.745 | 1.638e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1705.666 us | 586275.952 | 1.706e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1584.068 us | 631288.201 | 1.584e-06 |
| `BM_TokenizationThroughputNestedJson` | 2666.006 us | 375098.231 | 2.666e-06 |

### `insight-metalog` — compression / MetaLog-document build

_31 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 261.972 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 434.347 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 78.418 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 120.797 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 128.811 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 9.971 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 7.571 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 8881.985 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 17641.531 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 26380.445 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 53590.37 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 108838.714 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 37462.238 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 89.606 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 46.313 us |  |  |  |  |  | 0 | 2.163e+07 | 4.622e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 63.499 us |  |  |  |  |  | 0 | 1.577e+07 | 6.341e-08 |
| `BM_CubeKeyAlloc_MidBand` | 64.635 us |  |  |  |  |  | 0 | 1.549e+07 | 6.455e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 66.564 us |  |  |  |  |  | 0 | 1.504e+07 | 6.647e-08 |
| `BM_MetaLogCompress/1000/16` | 1.284 ms |  |  |  |  |  |  | 778801.55 |  |
| `BM_MetaLogCompress/10000/16` | 4.55 ms |  |  |  |  |  |  | 2.198e+06 |  |
| `BM_MetaLogCompress/100000/16` | 21.68 ms |  |  |  |  |  |  | 4.613e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.288 ms |  |  |  |  |  |  | 776559.432 |  |
| `BM_MetaLogCompress/10000/32` | 4.557 ms |  |  |  |  |  |  | 2.195e+06 |  |
| `BM_MetaLogCompress/100000/32` | 21.706 ms |  |  |  |  |  |  | 4.608e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.294 ms |  |  |  |  |  |  | 772838.688 |  |
| `BM_MetaLogCompress/10000/64` | 4.569 ms |  |  |  |  |  |  | 2.189e+06 |  |
| `BM_MetaLogCompress/100000/64` | 21.675 ms |  |  |  |  |  |  | 4.614e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 43.504 us |  |  |  |  |  |  | 2.299e+07 | 4.350e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 103.96 us |  |  |  |  |  |  | 9.620e+06 | 1.040e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 236.301 us |  |  |  |  |  |  | 4.232e+06 | 2.363e-07 |
| `BM_MetaLogIngest_Where` | 86.164 us |  |  |  |  |  |  | 1.161e+07 | 8.616e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3546.05 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4289.214 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 10937.682 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 26961.52 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 219.604 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 277.324 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3252.198 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 3986.739 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7689.583 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 489.105 us |  |  |  |  |  | 0.6 | 0 | 40893.296 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1222.533 us |  |  |  |  |  | 0.857 | 0 | 22903.766 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 4917.311 us |  |  |  |  |  | 0.857 | 0 | 5694.272 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7200.657 us |  |  |  |  |  | 0.857 | 0 | 3888.569 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 80627.81 us |  |  |  |  |  | 0.98 | 0 | 2430.921 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 89473.35 us |  |  |  |  |  | 0.98 | 0 | 2190.649 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 133290.533 us |  |  |  |  |  | 0.98 | 6 | 1470.47 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 401009.952 us |  |  |  |  |  | 0.98 | 0 | 488.77 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 343.446 ns | 2.910e+06 |
| `BM_Pipeline_IngestBatch/64` | 28037.123 ns | 2.283e+06 |
| `BM_Pipeline_IngestBatch/1024` | 362881.529 ns | 2.820e+06 |
| `BM_Pipeline_CloseWindow/1000` | 19022.47 ns | 53124.524 |
| `BM_Pipeline_CloseWindow/10000` | 33561.434 ns | 30448.913 |
| `BM_Pipeline_FullWindow/1000` | 413060.381 ns | 2.421e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.458e+06 ns | 2.892e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.401 ms | 1 | 714222.034 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 17.075 ms | 4 | 1.406e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 49.56 ms | 16 | 1.937e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 16.881 ms | 4 | 1.422e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 49.187 ms | 16 | 1.952e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.557 ms | 1 | 897110.768 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.688 ms | 4 | 2.909e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.543 ms | 16 | 5.186e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.263 ms | 64 | 6.080e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 17.829 ms | 256 | 7.179e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.466 ms | 32 | 3.582e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.864 ms | 32 | 5.586e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.727 ms | 32 | 5.867e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 2.865 ms | 32 | 5.584e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.605 ms | 32 | 4.438e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.545 ms | 16 | 5.177e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.689 ms | 16 | 4.735e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.596 ms | 16 | 5.013e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.023 ms | 16 | 3.954e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.778 ms | 16 | 2.879e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.03 ms | 16 | 1.985e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 10.895 ns |  | 9.178e+07 |  |  | 2.653e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.489 ns |  | 1.054e+08 |  |  | 5.480e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 17.771 ns |  | 5.627e+07 |  |  | 5.627e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.953 ns |  | 6.688e+07 |  |  | 7.870e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 5.01 ns |  | 1.996e+08 |  |  | 1.597e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 85.945 ns |  | 1.164e+07 |  |  | 2.211e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 82.195 ns |  | 1.217e+07 |  |  | 6.691e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 393.284 ns |  | 2.543e+06 |  |  | 6.687e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 179.833 ns |  | 5.561e+06 |  |  | 1.012e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 265.696 ns |  | 3.764e+06 |  |  | 2.785e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 88.601 ns |  | 1.129e+07 |  |  | 6.095e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 128.353 ns |  | 7.791e+06 |  |  | 5.532e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 292.083 ns |  | 3.424e+06 |  |  | 6.847e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 436.126 ns |  | 2.293e+06 |  |  | 7.383e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 426.78 ns |  | 2.343e+06 |  |  | 1.631e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 352.821 ns |  | 2.834e+06 |  |  | 7.454e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 124.642 ns |  | 8.023e+06 |  |  | 1.460e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 239.316 ns |  | 4.179e+06 |  |  | 3.092e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 66.395 ns |  | 1.506e+07 |  |  | 8.133e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 93.42 ns |  | 1.070e+07 |  |  | 7.600e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 262.159 ns |  | 3.815e+06 |  |  | 7.629e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 379.145 ns |  | 2.638e+06 |  |  | 8.493e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 348.895 ns |  | 2.866e+06 |  |  | 1.995e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.184 ms | 1 |  | 6000 |  |  | 5.078 | 1.765 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 17.013 ms | 4 |  | 24000 |  |  | 3.652 | 8.106 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 47.711 ms | 16 |  | 96000 |  |  | 10.136 | 15.262 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2686.765 us |  | 3.756e+06 |  |  |  |  |  | 8192 | 2.662e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2474.595 us |  | 4.098e+06 |  |  |  |  |  | 32768 | 2.440e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 210.523 us |  | 3.893e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 841.343 us |  | 3.895e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.607 ms |  | 3.567e+06 |  | 1 |  |  |  |  |  | 0 | 110715 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 15.51 ms |  | 5.158e+06 |  | 1 |  |  |  |  |  | 0 | 64252 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 19.34 ms |  | 4.136e+06 |  | 4 |  |  |  |  |  | 0 | 47899 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 42.955 ms |  | 7.450e+06 |  | 4 |  |  |  |  |  | 0 | 426674 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 63.265 ms |  | 5.058e+06 |  | 16 |  |  |  |  |  | 0 | 380739 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 7.415 ms |  | 2.697e+06 |  | 1 |  |  |  |  |  | 299 | 0 | 1 | 8.007e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 16.501 ms |  | 4.848e+06 |  | 1 |  |  |  |  |  | 495 | 0 | 4 | 3.334e+07 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 52.414 ms |  | 1.526e+06 |  | 4 |  |  |  |  |  | 554 | 0 | 4 | 3.177e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 51.494 ms |  | 6.214e+06 |  | 4 |  |  |  |  |  | 10482 | 0 | 16 | 1.862e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 61.677 ms |  | 5.188e+06 |  | 16 |  |  |  |  |  | 1589 | 0 | 16 | 9.449e+08 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 5.489 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 4.837 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 35.914 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 36.33 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 36.998 ns | 65536 |
