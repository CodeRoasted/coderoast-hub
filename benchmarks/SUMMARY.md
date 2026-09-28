# benchmark summary — v1.10.5

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_5 benchmark(s)._

| benchmark | real_time | items_per_second | s_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1753.607 us | 570396.285 | 1.753e-06 |
| `BM_TokenizationThroughput/8` | 1648.799 us | 606465.029 | 1.649e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1706.11 us | 586090.26 | 1.706e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1609.256 us | 621359.807 | 1.609e-06 |
| `BM_TokenizationThroughputNestedJson` | 2711.186 us | 368801.261 | 2.711e-06 |

### `insight-metalog` — compression / MetaLog-document build

_36 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 278.668 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 418.355 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 84.862 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 131.889 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 157.587 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 9.347 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 7.91 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 8119.705 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 16140.664 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 24141.285 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 48248.009 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 135607.609 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 34034.597 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 96.199 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 48.742 us |  |  |  |  |  | 0 | 2.056e+07 | 4.864e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 64.448 us |  |  |  |  |  | 0 | 1.554e+07 | 6.434e-08 |
| `BM_CubeKeyAlloc_MidBand` | 66.264 us |  |  |  |  |  | 0 | 1.511e+07 | 6.616e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 72.103 us |  |  |  |  |  | 0 | 1.389e+07 | 7.198e-08 |
| `BM_MetaLogCompress/1000/16` | 1.322 ms |  |  |  |  |  |  | 756510.86 |  |
| `BM_MetaLogCompress/10000/16` | 4.302 ms |  |  |  |  |  |  | 2.325e+06 |  |
| `BM_MetaLogCompress/100000/16` | 19.17 ms |  |  |  |  |  |  | 5.217e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.346 ms |  |  |  |  |  |  | 743213.087 |  |
| `BM_MetaLogCompress/10000/32` | 4.325 ms |  |  |  |  |  |  | 2.312e+06 |  |
| `BM_MetaLogCompress/100000/32` | 19.201 ms |  |  |  |  |  |  | 5.208e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.39 ms |  |  |  |  |  |  | 719500.51 |  |
| `BM_MetaLogCompress/10000/64` | 4.379 ms |  |  |  |  |  |  | 2.284e+06 |  |
| `BM_MetaLogCompress/100000/64` | 19.324 ms |  |  |  |  |  |  | 5.175e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 45.716 us |  |  |  |  |  |  | 2.187e+07 | 4.572e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 103.782 us |  |  |  |  |  |  | 9.637e+06 | 1.038e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 221.725 us |  |  |  |  |  |  | 4.510e+06 | 2.217e-07 |
| `BM_MetaLogIngest_Where` | 95.473 us |  |  |  |  |  |  | 1.047e+07 | 9.547e-08 |
| `BM_OrdinalKeyAlloc_None` | 47.332 us |  |  |  |  |  | 0 | 2.117e+07 | 4.724e-08 |
| `BM_OrdinalKeyAlloc_Key15Sso` | 69.55 us |  |  |  |  |  | 0 | 1.440e+07 | 6.945e-08 |
| `BM_OrdinalKeyAlloc_Key16ShipLegOnly` | 66.776 us |  |  |  |  |  | 0 | 1.500e+07 | 6.667e-08 |
| `BM_OrdinalKeyAlloc_Key16TraceMix` | 77.206 us |  |  |  |  |  | 0 | 1.297e+07 | 7.710e-08 |
| `BM_OrdinalKeyAlloc_Key23OverBothSso` | 70.404 us |  |  |  |  |  | 0 | 1.423e+07 | 7.030e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 1961.217 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2375.463 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 6145.715 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 15735 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 230.917 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 289.926 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1715.016 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 2098.373 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 5393.048 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 771 us |  |  |  |  |  | 0.609 | 0 | 29832.213 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1478.497 us |  |  |  |  |  | 0.857 | 0 | 18938.33 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 5958.947 us |  |  |  |  |  | 0.857 | 0 | 4698.807 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 6053.692 us |  |  |  |  |  | 0.857 | 0 | 4625.416 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 70468.38 us |  |  |  |  |  | 0.98 | 0 | 2781.459 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 71147.294 us |  |  |  |  |  | 0.98 | 0 | 2754.916 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 162805.032 us |  |  |  |  |  | 0.971 | 6 | 1283.756 | 6 | 7 | 193 | 20 | 209 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 320631.922 us |  |  |  |  |  | 0.98 | 0 | 611.299 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 336.854 ns | 2.968e+06 |
| `BM_Pipeline_IngestBatch/64` | 27832.42 ns | 2.300e+06 |
| `BM_Pipeline_IngestBatch/1024` | 355469.468 ns | 2.880e+06 |
| `BM_Pipeline_CloseWindow/1000` | 16632.296 ns | 60654.725 |
| `BM_Pipeline_CloseWindow/10000` | 29592.189 ns | 34600.219 |
| `BM_Pipeline_FullWindow/1000` | 369789.74 ns | 2.704e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.388e+06 ns | 2.952e+06 |

### `logcraft-core` — the deterministic log simulator core

_71 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | coordinates | ns_per_coordinate | discovered_knob_cap | build_coordinates | discovered_tower_cap | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 9.61 ms | 1 | 624332.409 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 14.836 ms | 4 | 1.618e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 36.22 ms | 16 | 2.650e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 14.834 ms | 4 | 1.618e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 36.394 ms | 16 | 2.638e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.505 ms | 1 | 990397.985 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.643 ms | 4 | 3.110e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.489 ms | 16 | 5.374e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.075 ms | 64 | 6.306e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 16.403 ms | 256 | 7.804e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.397 ms | 32 | 3.639e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.75 ms | 32 | 5.818e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.654 ms | 32 | 6.028e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 2.737 ms | 32 | 5.845e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.132 ms | 16 | 7.067e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.429 ms | 16 | 5.596e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.435 ms | 16 | 5.574e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 1.859 ms | 16 | 4.304e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.721 ms | 16 | 2.940e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 3.872 ms | 16 | 2.066e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 10.887 ns |  | 9.185e+07 |  |  | 2.655e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.121 ns |  | 1.096e+08 |  |  | 5.701e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 17.341 ns |  | 5.767e+07 |  |  | 5.767e+07 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.314 ns |  | 6.986e+07 |  |  | 8.227e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.514 ns |  | 2.216e+08 |  |  | 1.772e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 85.683 ns |  | 1.167e+07 |  |  | 2.217e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 80.409 ns |  | 1.244e+07 |  |  | 6.840e+07 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 386.326 ns |  | 2.589e+06 |  |  | 6.808e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 172.945 ns |  | 5.782e+06 |  |  | 1.052e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 240.836 ns |  | 4.152e+06 |  |  | 3.073e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 84.4 ns |  | 1.185e+07 |  |  | 6.398e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 125.975 ns |  | 7.938e+06 |  |  | 5.636e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 285.179 ns |  | 3.507e+06 |  |  | 7.013e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 430.936 ns |  | 2.321e+06 |  |  | 7.472e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 430.129 ns |  | 2.325e+06 |  |  | 1.618e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 341.293 ns |  | 2.930e+06 |  |  | 7.706e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 123.182 ns |  | 8.118e+06 |  |  | 1.478e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 214.158 ns |  | 4.669e+06 |  |  | 3.455e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 65.29 ns |  | 1.532e+07 |  |  | 8.271e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 90.235 ns |  | 1.108e+07 |  |  | 7.868e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 249.804 ns |  | 4.003e+06 |  |  | 8.006e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 352.558 ns |  | 2.836e+06 |  |  | 9.133e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 354.148 ns |  | 2.824e+06 |  |  | 1.965e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.994 ms | 1 |  | 6000 |  |  | 6.028 | 1.777 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 14.514 ms | 4 |  | 24000 |  |  | 7.025 | 5.342 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 34.028 ms | 16 |  | 96000 |  |  | 15.588 | 11.124 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2678.643 us |  | 3.761e+06 |  |  |  |  |  | 8192 | 2.659e-07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2522.784 us |  | 4.002e+06 |  |  |  |  |  | 32768 | 2.499e-07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 210.844 us |  | 3.886e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 842.979 us |  | 3.888e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate/real_time` | 142.727 us |  |  |  |  |  |  |  |  |  | 1 | 1.427e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate_CiWorld/real_time` | 285.047 us |  |  |  |  |  |  |  |  |  | 1 | 2.850e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisAtCap/real_time` | 27.754 ms |  |  |  |  |  |  |  |  |  | 64 | 4.337e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_TowerAtProductCap/real_time` | 156.967 ms |  |  |  |  |  |  |  |  |  | 256 | 6.132e-04 | 64 | 4 | 256 |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/2/real_time` | 378.619 us |  |  |  |  |  |  |  |  |  | 2 | 1.893e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/4/real_time` | 782.024 us |  |  |  |  |  |  |  |  |  | 4 | 1.955e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/8/real_time` | 1674.212 us |  |  |  |  |  |  |  |  |  | 8 | 2.093e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/16/real_time` | 3920.966 us |  |  |  |  |  |  |  |  |  | 16 | 2.451e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/32/real_time` | 9848.847 us |  |  |  |  |  |  |  |  |  | 32 | 3.078e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/64/real_time` | 27735.261 us |  |  |  |  |  |  |  |  |  | 64 | 4.334e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.889 ms |  | 3.396e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  | 0 | 118654 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.285 ms |  | 4.913e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  | 0 | 39396 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 18.004 ms |  | 4.443e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  | 0 | 26146 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 41.066 ms |  | 7.792e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  | 0 | 196251 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.627 ms |  | 3.018e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  | 72 | 0 | 1 | 7.538e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 17.49 ms |  | 4.574e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  | 252 | 0 | 4 | 1.487e+07 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 45.165 ms |  | 1.771e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  | 93 | 0 | 4 | 4.451e+06 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 45.251 ms |  | 7.072e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  | 5415 | 0 | 16 | 6.443e+08 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 4.665 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 4.777 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.005 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 35.689 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 36.633 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 36.782 ns | 65536 |
