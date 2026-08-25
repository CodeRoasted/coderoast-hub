# benchmark summary — v1.10.0

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_5 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1269.935 us | 787530.115 | 1.270e-06 |
| `BM_TokenizationThroughput/8` | 1173.872 us | 851836.596 | 1.174e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1229.126 us | 813608.534 | 1.229e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1132.89 us | 882628.656 | 1.133e-06 |
| `BM_TokenizationThroughputNestedJson` | 2038.063 us | 490653.558 | 2.038e-06 |

### `insight-metalog` — compression / MetaLog-document build

_31 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 270.054 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 418.564 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 82.992 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 128.903 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 151.907 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 9.465 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 7.941 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 8115.872 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 16126.976 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 24126.642 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 48039.729 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 98048.056 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 34120.308 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 89.637 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 43.732 us |  |  |  |  |  | 0 | 2.293e+07 | 4.361e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 59.135 us |  |  |  |  |  | 0 | 1.695e+07 | 5.901e-08 |
| `BM_CubeKeyAlloc_MidBand` | 61.525 us |  |  |  |  |  | 0 | 1.629e+07 | 6.140e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 64.497 us |  |  |  |  |  | 0 | 1.554e+07 | 6.437e-08 |
| `BM_MetaLogCompress/1000/16` | 1.224 ms |  |  |  |  |  |  | 817019.028 |  |
| `BM_MetaLogCompress/10000/16` | 4.322 ms |  |  |  |  |  |  | 2.314e+06 |  |
| `BM_MetaLogCompress/100000/16` | 20.518 ms |  |  |  |  |  |  | 4.874e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.227 ms |  |  |  |  |  |  | 814860.89 |  |
| `BM_MetaLogCompress/10000/32` | 4.333 ms |  |  |  |  |  |  | 2.308e+06 |  |
| `BM_MetaLogCompress/100000/32` | 20.521 ms |  |  |  |  |  |  | 4.874e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.232 ms |  |  |  |  |  |  | 811483.669 |  |
| `BM_MetaLogCompress/10000/64` | 4.329 ms |  |  |  |  |  |  | 2.310e+06 |  |
| `BM_MetaLogCompress/100000/64` | 20.465 ms |  |  |  |  |  |  | 4.887e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 42.313 us |  |  |  |  |  |  | 2.364e+07 | 4.231e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 104.117 us |  |  |  |  |  |  | 9.606e+06 | 1.041e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 232.556 us |  |  |  |  |  |  | 4.301e+06 | 2.325e-07 |
| `BM_MetaLogIngest_Where` | 92.317 us |  |  |  |  |  |  | 1.083e+07 | 9.230e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 2132.91 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2549.007 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 6673.114 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 16592.943 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 244.381 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 304.2 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1853.749 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 2273.341 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 6497.346 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 864.34 us |  |  |  |  |  | 0.609 | 0 | 26609.844 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1589.207 us |  |  |  |  |  | 0.857 | 0 | 17618.802 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 6401.604 us |  |  |  |  |  | 0.857 | 0 | 4374.016 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 6469.115 us |  |  |  |  |  | 0.857 | 0 | 4328.4 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 77279.754 us |  |  |  |  |  | 0.98 | 0 | 2536.233 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 77249.047 us |  |  |  |  |  | 0.98 | 0 | 2537.245 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 175539.817 us |  |  |  |  |  | 0.971 | 6 | 1190.699 | 6 | 7 | 193 | 20 | 209 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 343038.608 us |  |  |  |  |  | 0.98 | 0 | 571.371 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 355.057 ns | 2.815e+06 |
| `BM_Pipeline_IngestBatch/64` | 30534.485 ns | 2.096e+06 |
| `BM_Pipeline_IngestBatch/1024` | 383882.542 ns | 2.666e+06 |
| `BM_Pipeline_CloseWindow/1000` | 21204.3 ns | 47680.417 |
| `BM_Pipeline_CloseWindow/10000` | 37329.602 ns | 27458.699 |
| `BM_Pipeline_FullWindow/1000` | 525553.529 ns | 1.903e+06 |
| `BM_Pipeline_FullWindow/10000` | 7.517e+06 ns | 1.330e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 9.546 ms | 1 | 628516.43 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 20.153 ms | 4 | 1.191e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 59.438 ms | 16 | 1.615e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 20.289 ms | 4 | 1.183e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 61.508 ms | 16 | 1.561e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.627 ms | 1 | 797597.106 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.907 ms | 4 | 2.204e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 2.229 ms | 16 | 3.590e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 8.462 ms | 64 | 3.782e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 29.458 ms | 256 | 4.345e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 5.531 ms | 32 | 2.893e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 4.006 ms | 32 | 3.994e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 3.984 ms | 32 | 4.016e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 4.582 ms | 32 | 3.492e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 5.61 ms | 32 | 2.852e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 2.283 ms | 16 | 3.503e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 2.523 ms | 16 | 3.171e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 2.301 ms | 16 | 3.476e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.563 ms | 16 | 3.121e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 3.146 ms | 16 | 2.543e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.218 ms | 16 | 1.897e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.016 ns |  | 9.078e+07 |  |  | 2.624e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.506 ns |  | 1.052e+08 |  |  | 5.471e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 17.796 ns |  | 5.619e+07 |  |  | 5.619e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.937 ns |  | 6.695e+07 |  |  | 7.879e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 5.06 ns |  | 1.976e+08 |  |  | 1.581e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 86.342 ns |  | 1.158e+07 |  |  | 2.201e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 82.917 ns |  | 1.206e+07 |  |  | 6.633e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 397.026 ns |  | 2.519e+06 |  |  | 6.624e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 181.448 ns |  | 5.511e+06 |  |  | 1.003e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 266.492 ns |  | 3.753e+06 |  |  | 2.777e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 89.936 ns |  | 1.112e+07 |  |  | 6.004e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 128.704 ns |  | 7.770e+06 |  |  | 5.517e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 296.131 ns |  | 3.377e+06 |  |  | 6.754e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 446.282 ns |  | 2.241e+06 |  |  | 7.215e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 435.289 ns |  | 2.297e+06 |  |  | 1.599e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 359.983 ns |  | 2.778e+06 |  |  | 7.306e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 125.942 ns |  | 7.940e+06 |  |  | 1.445e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 236.738 ns |  | 4.224e+06 |  |  | 3.126e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 66.277 ns |  | 1.509e+07 |  |  | 8.148e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 93.86 ns |  | 1.065e+07 |  |  | 7.564e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 263.713 ns |  | 3.792e+06 |  |  | 7.584e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 384.359 ns |  | 2.602e+06 |  |  | 8.378e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 360.42 ns |  | 2.775e+06 |  |  | 1.931e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.61 ms | 1 |  | 6000 |  |  | 5.32 | 1.835 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 17.76 ms | 4 |  | 24000 |  |  | 4.017 | 8.327 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 55.829 ms | 16 |  | 96000 |  |  | 12.76 | 17.548 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2650.113 us |  | 3.820e+06 |  |  |  |  |  | 8192 | 2.618e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2484.687 us |  | 4.086e+06 |  |  |  |  |  | 32768 | 2.448e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 220.236 us |  | 3.721e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 875.734 us |  | 3.742e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.653 ms |  | 3.538e+06 |  | 1 |  |  |  |  |  | 0 | 172454 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.416 ms |  | 4.873e+06 |  | 1 |  |  |  |  |  | 0 | 302653 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 25.64 ms |  | 3.120e+06 |  | 4 |  |  |  |  |  | 0 | 224500 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 62.179 ms |  | 5.146e+06 |  | 4 |  |  |  |  |  | 0 | 842809 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 71.289 ms |  | 4.489e+06 |  | 16 |  |  |  |  |  | 0 | 767543 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.638 ms |  | 3.013e+06 |  | 1 |  |  |  |  |  | 161 | 0 | 1 | 1.162e+07 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 19.51 ms |  | 4.100e+06 |  | 1 |  |  |  |  |  | 716 | 0 | 4 | 1.672e+08 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 45.987 ms |  | 1.740e+06 |  | 4 |  |  |  |  |  | 1102 | 0 | 4 | 1.374e+08 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 98.124 ms |  | 3.261e+06 |  | 4 |  |  |  |  |  | 6381 | 0 | 16 | 3.683e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 102.99 ms |  | 3.107e+06 |  | 16 |  |  |  |  |  | 2295 | 0 | 16 | 2.767e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 6.576 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 5.436 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 28.287 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 29.453 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 29.69 ns | 65536 |
