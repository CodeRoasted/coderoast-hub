# benchmark summary — v1.10.2

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_5 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1722.823 us | 580441.323 | 1.723e-06 |
| `BM_TokenizationThroughput/8` | 1608.124 us | 621852.271 | 1.608e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1686.769 us | 592836.319 | 1.687e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1567.386 us | 637988.423 | 1.567e-06 |
| `BM_TokenizationThroughputNestedJson` | 2801.112 us | 357000.896 | 2.801e-06 |

### `insight-metalog` — compression / MetaLog-document build

_31 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 269.276 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 418.968 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 83.009 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 129.199 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 151.062 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 9.257 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 7.95 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 8118.381 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 16130.006 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 24129.119 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 48229.446 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 98485.963 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 34152.344 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 91.32 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 44.406 us |  |  |  |  |  | 0 | 2.259e+07 | 4.426e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 59.623 us |  |  |  |  |  | 0 | 1.681e+07 | 5.948e-08 |
| `BM_CubeKeyAlloc_MidBand` | 61.625 us |  |  |  |  |  | 0 | 1.627e+07 | 6.148e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 64.97 us |  |  |  |  |  | 0 | 1.542e+07 | 6.483e-08 |
| `BM_MetaLogCompress/1000/16` | 1.23 ms |  |  |  |  |  |  | 813088.453 |  |
| `BM_MetaLogCompress/10000/16` | 4.355 ms |  |  |  |  |  |  | 2.296e+06 |  |
| `BM_MetaLogCompress/100000/16` | 20.735 ms |  |  |  |  |  |  | 4.823e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.235 ms |  |  |  |  |  |  | 809603.239 |  |
| `BM_MetaLogCompress/10000/32` | 4.361 ms |  |  |  |  |  |  | 2.294e+06 |  |
| `BM_MetaLogCompress/100000/32` | 20.72 ms |  |  |  |  |  |  | 4.827e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.244 ms |  |  |  |  |  |  | 804000.749 |  |
| `BM_MetaLogCompress/10000/64` | 4.365 ms |  |  |  |  |  |  | 2.291e+06 |  |
| `BM_MetaLogCompress/100000/64` | 20.824 ms |  |  |  |  |  |  | 4.803e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 42.398 us |  |  |  |  |  |  | 2.361e+07 | 4.236e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 104.609 us |  |  |  |  |  |  | 9.559e+06 | 1.046e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 233.691 us |  |  |  |  |  |  | 4.280e+06 | 2.337e-07 |
| `BM_MetaLogIngest_Where` | 91.764 us |  |  |  |  |  |  | 1.090e+07 | 9.176e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 2021.684 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2426.067 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 6339.055 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 15948.41 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 232.253 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 292.622 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1788.998 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 2174.333 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 5530.186 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 800.235 us |  |  |  |  |  | 0.609 | 0 | 28742.071 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1519.988 us |  |  |  |  |  | 0.857 | 0 | 18421.169 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 6232.3 us |  |  |  |  |  | 0.857 | 0 | 4492.712 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 6239.052 us |  |  |  |  |  | 0.857 | 0 | 4487.901 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 73875.868 us |  |  |  |  |  | 0.98 | 0 | 2653.122 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 74230.884 us |  |  |  |  |  | 0.98 | 0 | 2640.463 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 169877.432 us |  |  |  |  |  | 0.971 | 6 | 1230.337 | 6 | 7 | 193 | 20 | 209 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 331437.191 us |  |  |  |  |  | 0.98 | 0 | 591.364 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 349.178 ns | 2.863e+06 |
| `BM_Pipeline_IngestBatch/64` | 28759.222 ns | 2.227e+06 |
| `BM_Pipeline_IngestBatch/1024` | 370458.419 ns | 2.763e+06 |
| `BM_Pipeline_CloseWindow/1000` | 19723.977 ns | 51275.135 |
| `BM_Pipeline_CloseWindow/10000` | 31361.394 ns | 32730.288 |
| `BM_Pipeline_FullWindow/1000` | 389750.429 ns | 2.566e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.568e+06 ns | 2.802e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.327 ms | 1 | 720582.325 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 17.119 ms | 4 | 1.402e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 50.304 ms | 16 | 1.908e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 16.827 ms | 4 | 1.426e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 49.571 ms | 16 | 1.937e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.532 ms | 1 | 940177.281 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.678 ms | 4 | 2.949e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.579 ms | 16 | 5.067e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.339 ms | 64 | 5.994e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 17.69 ms | 256 | 7.236e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.423 ms | 32 | 3.617e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.816 ms | 32 | 5.681e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.757 ms | 32 | 5.803e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 2.849 ms | 32 | 5.615e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.57 ms | 32 | 4.482e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.536 ms | 16 | 5.208e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.697 ms | 16 | 4.713e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.608 ms | 16 | 4.975e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.096 ms | 16 | 3.816e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.827 ms | 16 | 2.830e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.061 ms | 16 | 1.970e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.014 ns |  | 9.079e+07 |  |  | 2.624e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.679 ns |  | 1.033e+08 |  |  | 5.372e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 17.79 ns |  | 5.621e+07 |  |  | 5.621e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 15.161 ns |  | 6.596e+07 |  |  | 7.759e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 5.038 ns |  | 1.985e+08 |  |  | 1.588e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 88.423 ns |  | 1.131e+07 |  |  | 2.149e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 83.2 ns |  | 1.202e+07 |  |  | 6.610e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 397.576 ns |  | 2.515e+06 |  |  | 6.615e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 181.783 ns |  | 5.501e+06 |  |  | 1.001e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 270.033 ns |  | 3.703e+06 |  |  | 2.740e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 90.588 ns |  | 1.104e+07 |  |  | 5.961e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 131.318 ns |  | 7.615e+06 |  |  | 5.407e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 297.448 ns |  | 3.362e+06 |  |  | 6.724e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 444.271 ns |  | 2.251e+06 |  |  | 7.248e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 435.115 ns |  | 2.298e+06 |  |  | 1.600e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 356.567 ns |  | 2.805e+06 |  |  | 7.376e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 126.981 ns |  | 7.876e+06 |  |  | 1.433e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 238.061 ns |  | 4.201e+06 |  |  | 3.109e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 65.99 ns |  | 1.515e+07 |  |  | 8.183e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 95.043 ns |  | 1.052e+07 |  |  | 7.470e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 258.725 ns |  | 3.865e+06 |  |  | 7.730e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 385.381 ns |  | 2.595e+06 |  |  | 8.356e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 352.944 ns |  | 2.833e+06 |  |  | 1.972e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.272 ms | 1 |  | 6000 |  |  | 5.212 | 1.708 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 16.324 ms | 4 |  | 24000 |  |  | 3.595 | 8.402 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 48.57 ms | 16 |  | 96000 |  |  | 10.758 | 15.04 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2654.482 us |  | 3.814e+06 |  |  |  |  |  | 8192 | 2.622e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2523.972 us |  | 4.011e+06 |  |  |  |  |  | 32768 | 2.493e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 210.672 us |  | 3.889e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 843.254 us |  | 3.886e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.771 ms |  | 3.466e+06 |  | 1 |  |  |  |  |  | 0 | 113524 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.515 ms |  | 4.844e+06 |  | 1 |  |  |  |  |  | 0 | 56973 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 22.122 ms |  | 3.616e+06 |  | 4 |  |  |  |  |  | 0 | 34695 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 43.056 ms |  | 7.432e+06 |  | 4 |  |  |  |  |  | 0 | 358399 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 59.131 ms |  | 5.412e+06 |  | 16 |  |  |  |  |  | 0 | 308775 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.503 ms |  | 3.075e+06 |  | 1 |  |  |  |  |  | 134 | 0 | 1 | 5.848e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 17.683 ms |  | 4.524e+06 |  | 1 |  |  |  |  |  | 309 | 0 | 4 | 2.266e+07 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 53.21 ms |  | 1.503e+06 |  | 4 |  |  |  |  |  | 306 | 0 | 4 | 1.640e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 49.528 ms |  | 6.461e+06 |  | 4 |  |  |  |  |  | 5496 | 0 | 16 | 1.418e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 72.39 ms |  | 4.420e+06 |  | 16 |  |  |  |  |  | 1843 | 0 | 16 | 1.086e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 5.697 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 9.793 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 35.704 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 36.632 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 37.575 ns | 65536 |
