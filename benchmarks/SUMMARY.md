# benchmark summary — v1.9.6

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_5 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1729.744 us | 578101.92 | 1.730e-06 |
| `BM_TokenizationThroughput/8` | 1624.404 us | 615709.639 | 1.624e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1684.734 us | 593555.261 | 1.685e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1583.251 us | 631599.112 | 1.583e-06 |
| `BM_TokenizationThroughputNestedJson` | 2847.983 us | 351111.506 | 2.848e-06 |

### `insight-metalog` — compression / MetaLog-document build

_31 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 233.537 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 429.726 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 82.873 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 151.166 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 236.71 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 7.264 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 6.163 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 7792.24 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 15679.8 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 43339.163 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 57673.822 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 179618.004 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 33871.526 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 96.977 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 30.057 us |  |  |  |  |  | 0 | 3.330e+07 | 3.003e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 45.059 us |  |  |  |  |  | 0 | 2.221e+07 | 4.503e-08 |
| `BM_CubeKeyAlloc_MidBand` | 45.243 us |  |  |  |  |  | 0 | 2.212e+07 | 4.522e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 46.923 us |  |  |  |  |  | 0 | 2.132e+07 | 4.690e-08 |
| `BM_MetaLogCompress/1000/16` | 1.026 ms |  |  |  |  |  |  | 974724.978 |  |
| `BM_MetaLogCompress/10000/16` | 3.527 ms |  |  |  |  |  |  | 2.835e+06 |  |
| `BM_MetaLogCompress/100000/16` | 16.306 ms |  |  |  |  |  |  | 6.133e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.03 ms |  |  |  |  |  |  | 971125.076 |  |
| `BM_MetaLogCompress/10000/32` | 3.525 ms |  |  |  |  |  |  | 2.837e+06 |  |
| `BM_MetaLogCompress/100000/32` | 16.253 ms |  |  |  |  |  |  | 6.153e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.031 ms |  |  |  |  |  |  | 969776.483 |  |
| `BM_MetaLogCompress/10000/64` | 3.525 ms |  |  |  |  |  |  | 2.837e+06 |  |
| `BM_MetaLogCompress/100000/64` | 16.283 ms |  |  |  |  |  |  | 6.142e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 30.449 us |  |  |  |  |  |  | 3.284e+07 | 3.045e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 84.952 us |  |  |  |  |  |  | 1.177e+07 | 8.495e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 201.769 us |  |  |  |  |  |  | 4.956e+06 | 2.018e-07 |
| `BM_MetaLogIngest_Where` | 72.039 us |  |  |  |  |  |  | 1.388e+07 | 7.204e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 2003.077 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2425.383 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 6270.939 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 15950.056 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 219.547 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 276.857 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1789.424 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 2154.652 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 5720.477 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 772.703 us |  |  |  |  |  | 0.609 | 0 | 29766.264 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1451.741 us |  |  |  |  |  | 0.857 | 0 | 19287.142 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 5942.539 us |  |  |  |  |  | 0.857 | 0 | 4711.785 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 5939.335 us |  |  |  |  |  | 0.857 | 0 | 4714.482 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 71305.02 us |  |  |  |  |  | 0.98 | 0 | 2748.779 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 71193.574 us |  |  |  |  |  | 0.98 | 0 | 2753.053 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 113111.778 us |  |  |  |  |  | 0.98 | 6 | 1732.816 | 6 | 1 | 7 | 14 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 322590.622 us |  |  |  |  |  | 0.98 | 0 | 607.606 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 359.396 ns | 2.782e+06 |
| `BM_Pipeline_IngestBatch/64` | 29553.298 ns | 2.164e+06 |
| `BM_Pipeline_IngestBatch/1024` | 379088.687 ns | 2.700e+06 |
| `BM_Pipeline_CloseWindow/1000` | 19447.34 ns | 52049.649 |
| `BM_Pipeline_CloseWindow/10000` | 31127.176 ns | 33069.937 |
| `BM_Pipeline_FullWindow/1000` | 433108.263 ns | 2.309e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.681e+06 ns | 2.717e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.841 ms | 1 | 678692.692 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 19.072 ms | 4 | 1.258e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 57.812 ms | 16 | 1.661e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 19.102 ms | 4 | 1.256e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 56.59 ms | 16 | 1.696e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.555 ms | 1 | 901613.7 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.741 ms | 4 | 2.699e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.842 ms | 16 | 4.343e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 7.61 ms | 64 | 4.205e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 27.335 ms | 256 | 4.683e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 5.096 ms | 32 | 3.140e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 3.92 ms | 32 | 4.081e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 3.472 ms | 32 | 4.608e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 4.058 ms | 32 | 3.943e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 4.91 ms | 32 | 3.259e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.997 ms | 16 | 4.006e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 2.214 ms | 16 | 3.613e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 2.177 ms | 16 | 3.675e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.515 ms | 16 | 3.181e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 3.464 ms | 16 | 2.310e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 5.378 ms | 16 | 1.488e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.844 ns |  | 8.444e+07 |  |  | 2.440e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 10.15 ns |  | 9.852e+07 |  |  | 5.123e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 19.226 ns |  | 5.201e+07 |  |  | 5.201e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 16.004 ns |  | 6.248e+07 |  |  | 7.341e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 5.348 ns |  | 1.870e+08 |  |  | 1.496e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 90.149 ns |  | 1.109e+07 |  |  | 2.108e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 89.313 ns |  | 1.120e+07 |  |  | 6.158e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 425.922 ns |  | 2.348e+06 |  |  | 6.175e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 193.565 ns |  | 5.166e+06 |  |  | 9.403e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 286.894 ns |  | 3.486e+06 |  |  | 2.579e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 96.754 ns |  | 1.034e+07 |  |  | 5.581e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 139.849 ns |  | 7.151e+06 |  |  | 5.077e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 313.323 ns |  | 3.192e+06 |  |  | 6.383e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 474.966 ns |  | 2.105e+06 |  |  | 6.780e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 464.547 ns |  | 2.153e+06 |  |  | 1.498e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 385.094 ns |  | 2.597e+06 |  |  | 6.830e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 137.746 ns |  | 7.260e+06 |  |  | 1.321e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 252.166 ns |  | 3.966e+06 |  |  | 2.935e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 69.365 ns |  | 1.442e+07 |  |  | 7.785e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 98.661 ns |  | 1.014e+07 |  |  | 7.196e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 280.634 ns |  | 3.563e+06 |  |  | 7.127e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 410.847 ns |  | 2.434e+06 |  |  | 7.838e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 379.271 ns |  | 2.637e+06 |  |  | 1.835e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 9.146 ms | 1 |  | 6000 |  |  | 5.602 | 1.928 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 20.341 ms | 4 |  | 24000 |  |  | 4.619 | 8.804 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 61.081 ms | 16 |  | 96000 |  |  | 14.848 | 18.788 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2706.94 us |  | 3.754e+06 |  |  |  |  |  | 8192 | 2.664e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2401.558 us |  | 4.230e+06 |  |  |  |  |  | 32768 | 2.364e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 225.714 us |  | 3.630e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 897.179 us |  | 3.654e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.723 ms |  | 3.495e+06 |  | 1 |  |  |  |  |  | 0 | 146837 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.804 ms |  | 4.761e+06 |  | 1 |  |  |  |  |  | 0 | 362134 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 36.71 ms |  | 2.179e+06 |  | 4 |  |  |  |  |  | 0 | 226139 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 52.046 ms |  | 6.148e+06 |  | 4 |  |  |  |  |  | 0 | 930097 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 87.823 ms |  | 3.644e+06 |  | 16 |  |  |  |  |  | 0 | 665930 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.65 ms |  | 3.008e+06 |  | 1 |  |  |  |  |  | 194 | 0 | 1 | 1.131e+07 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 20.385 ms |  | 3.924e+06 |  | 1 |  |  |  |  |  | 938 | 0 | 4 | 1.978e+08 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 49.576 ms |  | 1.614e+06 |  | 4 |  |  |  |  |  | 666 | 0 | 4 | 6.661e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 108.653 ms |  | 2.945e+06 |  | 4 |  |  |  |  |  | 4606 | 0 | 16 | 4.619e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 110.918 ms |  | 2.885e+06 |  | 16 |  |  |  |  |  | 2327 | 0 | 16 | 3.693e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 6.734 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 5.388 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 38.382 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 38.981 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 41.185 ns | 65536 |
