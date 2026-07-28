# benchmark summary — v1.8.6

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1196.133 us | 836049.682 | 1.196e-06 |
| `BM_TokenizationThroughput/8` | 1121.801 us | 891482.138 | 1.122e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1161.433 us | 861024.99 | 1.161e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1078.137 us | 927507.474 | 1.078e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 236.868 us |  |  |  |  |  |  |  |
| `BM_Diff` | 437.253 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 63.68 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 150.549 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 237.313 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 6.696 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 6.336 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 7664.374 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 15395.537 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 40403.437 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 73912.267 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 185135.132 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 28913.145 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 103.276 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.056 ms |  |  |  |  |  | 946951.558 |  |
| `BM_MetaLogCompress/10000/16` | 3.698 ms |  |  |  |  |  | 2.705e+06 |  |
| `BM_MetaLogCompress/100000/16` | 17.795 ms |  |  |  |  |  | 5.620e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.059 ms |  |  |  |  |  | 944125.906 |  |
| `BM_MetaLogCompress/10000/32` | 3.696 ms |  |  |  |  |  | 2.706e+06 |  |
| `BM_MetaLogCompress/100000/32` | 17.792 ms |  |  |  |  |  | 5.620e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.061 ms |  |  |  |  |  | 942282.999 |  |
| `BM_MetaLogCompress/10000/64` | 3.7 ms |  |  |  |  |  | 2.702e+06 |  |
| `BM_MetaLogCompress/100000/64` | 17.788 ms |  |  |  |  |  | 5.622e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 37.124 us |  |  |  |  |  | 2.694e+07 | 3.712e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 86.323 us |  |  |  |  |  | 1.158e+07 | 8.632e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 201.294 us |  |  |  |  |  | 4.968e+06 | 2.013e-07 |
| `BM_MetaLogIngest_Where` | 90.669 us |  |  |  |  |  | 1.103e+07 | 9.067e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3744.421 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4573.096 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 11609.238 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 29350.548 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 238.045 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 288.118 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3450.414 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4212.437 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7612.4 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 509.752 us |  |  |  |  |  | 0.6 | 0 | 39253.597 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1255.45 us |  |  |  |  |  | 0.857 | 0 | 22310.095 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 5124.83 us |  |  |  |  |  | 0.857 | 0 | 5464.971 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7407.099 us |  |  |  |  |  | 0.857 | 0 | 3780.87 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 84185.737 us |  |  |  |  |  | 0.98 | 0 | 2328.773 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 92533.675 us |  |  |  |  |  | 0.98 | 0 | 2118.653 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 136532.74 us |  |  |  |  |  | 0.98 | 6 | 1435.969 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 413142.35 us |  |  |  |  |  | 0.98 | 0 | 474.527 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 341.913 ns | 2.924e+06 |
| `BM_Pipeline_IngestBatch/64` | 28125.112 ns | 2.274e+06 |
| `BM_Pipeline_IngestBatch/1024` | 363190.216 ns | 2.818e+06 |
| `BM_Pipeline_CloseWindow/1000` | 19763.105 ns | 51167.521 |
| `BM_Pipeline_CloseWindow/10000` | 32388.718 ns | 31594.853 |
| `BM_Pipeline_FullWindow/1000` | 412337.417 ns | 2.425e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.525e+06 ns | 2.837e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.429 ms | 1 | 711811.837 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 17.248 ms | 4 | 1.391e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 49.929 ms | 16 | 1.923e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 16.98 ms | 4 | 1.413e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 49.168 ms | 16 | 1.952e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.563 ms | 1 | 888340.382 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.709 ms | 4 | 2.823e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.622 ms | 16 | 4.933e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.49 ms | 64 | 5.828e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 19.045 ms | 256 | 6.721e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.646 ms | 32 | 3.444e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.971 ms | 32 | 5.385e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.842 ms | 32 | 5.630e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 3.051 ms | 32 | 5.244e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.781 ms | 32 | 4.232e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.589 ms | 16 | 5.035e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.757 ms | 16 | 4.553e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.679 ms | 16 | 4.765e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.189 ms | 16 | 3.655e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.878 ms | 16 | 2.779e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.141 ms | 16 | 1.932e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 10.364 ns |  | 8.845e+07 |  |  | 2.556e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 8.68 ns |  | 1.056e+08 |  |  | 5.492e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 16.247 ns |  | 5.642e+07 |  |  | 5.642e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 13.93 ns |  | 6.581e+07 |  |  | 7.745e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.188 ns |  | 2.189e+08 |  |  | 1.751e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 92.319 ns |  | 9.930e+06 |  |  | 1.887e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 78.984 ns |  | 1.161e+07 |  |  | 6.383e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 350.073 ns |  | 2.619e+06 |  |  | 6.887e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 187.825 ns |  | 5.307e+06 |  |  | 9.660e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 256.266 ns |  | 3.902e+06 |  |  | 2.888e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 94.322 ns |  | 1.060e+07 |  |  | 5.725e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 130.802 ns |  | 7.645e+06 |  |  | 5.428e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 304.997 ns |  | 3.279e+06 |  |  | 6.558e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 409.616 ns |  | 2.441e+06 |  |  | 7.861e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 398.285 ns |  | 2.511e+06 |  |  | 1.748e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 344.341 ns |  | 2.904e+06 |  |  | 7.638e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 128.334 ns |  | 7.792e+06 |  |  | 1.418e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 236 ns |  | 4.237e+06 |  |  | 3.136e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 71.405 ns |  | 1.400e+07 |  |  | 7.563e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 98.558 ns |  | 1.015e+07 |  |  | 7.204e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 255.168 ns |  | 3.919e+06 |  |  | 7.838e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 336.854 ns |  | 2.969e+06 |  |  | 9.559e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 320.322 ns |  | 3.122e+06 |  |  | 2.173e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.309 ms | 1 |  | 6000 |  |  | 5.184 | 1.751 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 17.159 ms | 4 |  | 24000 |  |  | 3.725 | 8.234 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 49.177 ms | 16 |  | 96000 |  |  | 11.023 | 15.274 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2763.028 us |  | 3.661e+06 |  |  |  |  |  | 8192 | 2.731e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2623.714 us |  | 3.867e+06 |  |  |  |  |  | 32768 | 2.586e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 223.754 us |  | 3.662e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 867.79 us |  | 3.776e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.613 ms |  | 3.563e+06 |  | 1 |  |  |  |  |  | 0 | 131619 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.849 ms |  | 4.748e+06 |  | 1 |  |  |  |  |  | 0 | 71925 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 24.638 ms |  | 3.247e+06 |  | 4 |  |  |  |  |  | 0 | 53482 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 44.455 ms |  | 7.198e+06 |  | 4 |  |  |  |  |  | 0 | 377237 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 64.219 ms |  | 4.983e+06 |  | 16 |  |  |  |  |  | 0 | 489446 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 7.519 ms |  | 2.660e+06 |  | 1 |  |  |  |  |  | 402 | 0 | 1 | 9.643e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 18.463 ms |  | 4.333e+06 |  | 1 |  |  |  |  |  | 398 | 0 | 4 | 3.070e+07 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 49.209 ms |  | 1.626e+06 |  | 4 |  |  |  |  |  | 254 | 0 | 4 | 1.836e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 53.033 ms |  | 6.034e+06 |  | 4 |  |  |  |  |  | 5414 | 0 | 16 | 1.401e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 68.014 ms |  | 4.705e+06 |  | 16 |  |  |  |  |  | 1868 | 0 | 16 | 1.033e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 5.614 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 4.887 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 82.011 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 81.986 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 81.944 ns | 65536 |
