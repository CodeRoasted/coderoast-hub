# benchmark summary — v1.8.8

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1736.254 us | 576140.235 | 1.736e-06 |
| `BM_TokenizationThroughput/8` | 1623.509 us | 615991.604 | 1.623e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1684.465 us | 593759.733 | 1.684e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1577.01 us | 634085.095 | 1.577e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 253.671 us |  |  |  |  |  |  |  |
| `BM_Diff` | 421.695 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 82.95 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 128.391 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 149.127 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 9.051 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 8.647 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 8135.183 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 16160.392 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 24173.985 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 48763.737 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 100170.296 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 31049.2 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 89.387 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 1.286 ms |  |  |  |  |  | 777464.436 |  |
| `BM_MetaLogCompress/10000/16` | 4.744 ms |  |  |  |  |  | 2.108e+06 |  |
| `BM_MetaLogCompress/100000/16` | 24.076 ms |  |  |  |  |  | 4.154e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.292 ms |  |  |  |  |  | 774315.921 |  |
| `BM_MetaLogCompress/10000/32` | 4.757 ms |  |  |  |  |  | 2.103e+06 |  |
| `BM_MetaLogCompress/100000/32` | 24.093 ms |  |  |  |  |  | 4.151e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.298 ms |  |  |  |  |  | 770622.744 |  |
| `BM_MetaLogCompress/10000/64` | 4.745 ms |  |  |  |  |  | 2.108e+06 |  |
| `BM_MetaLogCompress/100000/64` | 24.025 ms |  |  |  |  |  | 4.163e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 54.355 us |  |  |  |  |  | 1.840e+07 | 5.435e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 118.454 us |  |  |  |  |  | 8.444e+06 | 1.184e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 248.569 us |  |  |  |  |  | 4.023e+06 | 2.485e-07 |
| `BM_MetaLogIngest_Where` | 122.72 us |  |  |  |  |  | 8.149e+06 | 1.227e-07 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3696.394 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4466.18 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 11429.338 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 28582.22 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 224.511 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 287.819 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3389.861 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4145.214 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 8048.7 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 499.183 us |  |  |  |  |  | 0.6 | 0 | 40065.827 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1221.519 us |  |  |  |  |  | 0.857 | 0 | 22922.406 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 5014.545 us |  |  |  |  |  | 0.857 | 0 | 5583.927 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7351.942 us |  |  |  |  |  | 0.857 | 0 | 3808.412 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 81829.511 us |  |  |  |  |  | 0.98 | 0 | 2395.221 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 91575.27 us |  |  |  |  |  | 0.98 | 0 | 2140.314 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 134447.998 us |  |  |  |  |  | 0.98 | 6 | 1457.828 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 404622.701 us |  |  |  |  |  | 0.98 | 0 | 484.401 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 338.936 ns | 2.949e+06 |
| `BM_Pipeline_IngestBatch/64` | 27335.118 ns | 2.341e+06 |
| `BM_Pipeline_IngestBatch/1024` | 350866.733 ns | 2.917e+06 |
| `BM_Pipeline_CloseWindow/1000` | 18327.073 ns | 55191.987 |
| `BM_Pipeline_CloseWindow/10000` | 31246.89 ns | 32764.574 |
| `BM_Pipeline_FullWindow/1000` | 403505.49 ns | 2.478e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.415e+06 ns | 2.929e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.539 ms | 1 | 702625.168 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 16.975 ms | 4 | 1.414e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 49.023 ms | 16 | 1.958e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 16.53 ms | 4 | 1.452e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 50.642 ms | 16 | 1.896e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.556 ms | 1 | 898982.108 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.712 ms | 4 | 2.809e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.601 ms | 16 | 4.998e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.45 ms | 64 | 5.872e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 18.269 ms | 256 | 7.006e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.634 ms | 32 | 3.453e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.945 ms | 32 | 5.433e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.836 ms | 32 | 5.641e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 2.911 ms | 32 | 5.497e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.648 ms | 32 | 4.385e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.52 ms | 16 | 5.264e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.704 ms | 16 | 4.694e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.659 ms | 16 | 4.823e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.083 ms | 16 | 3.841e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.832 ms | 16 | 2.825e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.103 ms | 16 | 1.950e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.155 ns |  | 8.965e+07 |  |  | 2.591e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.349 ns |  | 1.070e+08 |  |  | 5.562e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 17.902 ns |  | 5.586e+07 |  |  | 5.586e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 15.045 ns |  | 6.647e+07 |  |  | 7.819e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.522 ns |  | 2.212e+08 |  |  | 1.769e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 98.649 ns |  | 1.014e+07 |  |  | 1.926e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 84.311 ns |  | 1.186e+07 |  |  | 6.523e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 394.257 ns |  | 2.536e+06 |  |  | 6.671e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 179.065 ns |  | 5.585e+06 |  |  | 1.016e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 291.626 ns |  | 3.429e+06 |  |  | 2.538e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 95.055 ns |  | 1.052e+07 |  |  | 5.681e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 131.178 ns |  | 7.623e+06 |  |  | 5.412e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 302.186 ns |  | 3.309e+06 |  |  | 6.618e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 413.518 ns |  | 2.418e+06 |  |  | 7.787e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 403.618 ns |  | 2.478e+06 |  |  | 1.724e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 343.368 ns |  | 2.912e+06 |  |  | 7.659e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 128.128 ns |  | 7.805e+06 |  |  | 1.420e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 256.669 ns |  | 3.896e+06 |  |  | 2.883e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 70.89 ns |  | 1.411e+07 |  |  | 7.617e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 97.103 ns |  | 1.030e+07 |  |  | 7.312e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 251.605 ns |  | 3.975e+06 |  |  | 7.949e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 339.854 ns |  | 2.942e+06 |  |  | 9.475e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 327.667 ns |  | 3.052e+06 |  |  | 2.124e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.438 ms | 1 |  | 6000 |  |  | 5.295 | 1.766 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 16.356 ms | 4 |  | 24000 |  |  | 3.655 | 7.998 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 48.607 ms | 16 |  | 96000 |  |  | 10.509 | 15.154 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2697.307 us |  | 3.753e+06 |  |  |  |  |  | 8192 | 2.664e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2581 us |  | 3.922e+06 |  |  |  |  |  | 32768 | 2.550e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 214.449 us |  | 3.822e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 860.495 us |  | 3.808e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.768 ms |  | 3.467e+06 |  | 1 |  |  |  |  |  | 0 | 123872 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.514 ms |  | 4.844e+06 |  | 1 |  |  |  |  |  | 0 | 79843 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 21.576 ms |  | 3.708e+06 |  | 4 |  |  |  |  |  | 0 | 56336 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 44.413 ms |  | 7.205e+06 |  | 4 |  |  |  |  |  | 0 | 400013 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 62.997 ms |  | 5.080e+06 |  | 16 |  |  |  |  |  | 0 | 407813 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.695 ms |  | 2.987e+06 |  | 1 |  |  |  |  |  | 115 | 0 | 1 | 4.848e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 18.93 ms |  | 4.226e+06 |  | 1 |  |  |  |  |  | 617 | 0 | 4 | 4.323e+07 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 56.945 ms |  | 1.405e+06 |  | 4 |  |  |  |  |  | 190 | 0 | 4 | 1.722e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 52.172 ms |  | 6.134e+06 |  | 4 |  |  |  |  |  | 5434 | 0 | 16 | 1.501e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 71.463 ms |  | 4.478e+06 |  | 16 |  |  |  |  |  | 2068 | 0 | 16 | 1.217e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 5.562 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 10.553 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 81.902 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 82.08 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 82.105 ns | 65536 |
