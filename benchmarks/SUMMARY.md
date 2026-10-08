# benchmark summary — v1.10.6

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_5 benchmark(s)._

| benchmark | real_time | items_per_second | s_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 2047.44 us | 488409.911 | 2.047e-06 |
| `BM_TokenizationThroughput/8` | 1920.95 us | 520547.262 | 1.921e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1947.166 us | 513546.744 | 1.947e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1829.231 us | 546673.056 | 1.829e-06 |
| `BM_TokenizationThroughputNestedJson` | 2838.193 us | 352320.44 | 2.838e-06 |

### `insight-metalog` — compression / MetaLog-document build

_38 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 288.115 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 415.848 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 77.721 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 119.944 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 128.795 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 8.326 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 7.674 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 8877.265 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 17637.306 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 26379.436 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 53739.814 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 108799.47 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 37496.046 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 85.677 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 45.29 us |  |  |  |  |  | 0 | 2.212e+07 | 4.522e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 63.885 us |  |  |  |  |  | 0 | 1.568e+07 | 6.377e-08 |
| `BM_CubeKeyAlloc_MidBand` | 64.501 us |  |  |  |  |  | 0 | 1.553e+07 | 6.441e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 68.263 us |  |  |  |  |  | 0 | 1.467e+07 | 6.816e-08 |
| `BM_MetaLogCompress/1000/16` | 1.409 ms |  |  |  |  |  |  | 709852.342 |  |
| `BM_MetaLogCompress/10000/16` | 4.606 ms |  |  |  |  |  |  | 2.172e+06 |  |
| `BM_MetaLogCompress/100000/16` | 20.593 ms |  |  |  |  |  |  | 4.856e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.435 ms |  |  |  |  |  |  | 697074.118 |  |
| `BM_MetaLogCompress/10000/32` | 4.634 ms |  |  |  |  |  |  | 2.158e+06 |  |
| `BM_MetaLogCompress/100000/32` | 20.638 ms |  |  |  |  |  |  | 4.846e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.486 ms |  |  |  |  |  |  | 673001.674 |  |
| `BM_MetaLogCompress/10000/64` | 4.683 ms |  |  |  |  |  |  | 2.136e+06 |  |
| `BM_MetaLogCompress/100000/64` | 20.731 ms |  |  |  |  |  |  | 4.824e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 42.566 us |  |  |  |  |  |  | 2.350e+07 | 4.256e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 72.111 us |  |  |  |  |  |  | 1.387e+07 | 7.210e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 127.184 us |  |  |  |  |  |  | 7.864e+06 | 1.272e-07 |
| `BM_MetaLogIngest_ParamSketch/0` | 48.769 ms |  |  |  |  |  |  | 2.051e+06 | 4.876e-07 |
| `BM_MetaLogIngest_ParamSketch/1` | 872.064 ms |  |  |  |  |  |  | 114693.166 | 8.719e-06 |
| `BM_MetaLogIngest_Where` | 92.513 us |  |  |  |  |  |  | 1.081e+07 | 9.250e-08 |
| `BM_OrdinalKeyAlloc_None` | 45.039 us |  |  |  |  |  | 0 | 2.225e+07 | 4.495e-08 |
| `BM_OrdinalKeyAlloc_Key15Sso` | 66.159 us |  |  |  |  |  | 0 | 1.514e+07 | 6.606e-08 |
| `BM_OrdinalKeyAlloc_Key16ShipLegOnly` | 64.159 us |  |  |  |  |  | 0 | 1.561e+07 | 6.407e-08 |
| `BM_OrdinalKeyAlloc_Key16TraceMix` | 68.998 us |  |  |  |  |  | 0 | 1.451e+07 | 6.890e-08 |
| `BM_OrdinalKeyAlloc_Key23OverBothSso` | 67.075 us |  |  |  |  |  | 0 | 1.493e+07 | 6.699e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 1836.19 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2269.761 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 5775.356 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 14682.513 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 218.173 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 271.732 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1574.139 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 1965.854 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 5211.195 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 724.853 us |  |  |  |  |  | 0.609 | 0 | 31730.771 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1373.849 us |  |  |  |  |  | 0.857 | 0 | 20380.893 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 5804.22 us |  |  |  |  |  | 0.857 | 0 | 4824.068 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 5652.846 us |  |  |  |  |  | 0.857 | 0 | 4953.328 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 67314.241 us |  |  |  |  |  | 0.98 | 0 | 2911.745 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 75503.38 us |  |  |  |  |  | 0.98 | 0 | 2595.908 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 156153.391 us |  |  |  |  |  | 0.971 | 6 | 1338.452 | 6 | 7 | 193 | 20 | 209 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 324420.525 us |  |  |  |  |  | 0.98 | 0 | 604.161 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 406.906 ns | 2.457e+06 |
| `BM_Pipeline_IngestBatch/64` | 33378.185 ns | 1.917e+06 |
| `BM_Pipeline_IngestBatch/1024` | 1.067e+06 ns | 959410.318 |
| `BM_Pipeline_CloseWindow/1000` | 20563.758 ns | 49110.492 |
| `BM_Pipeline_CloseWindow/10000` | 25274.114 ns | 40488.152 |
| `BM_Pipeline_FullWindow/1000` | 441902.404 ns | 2.263e+06 |
| `BM_Pipeline_FullWindow/10000` | 4.055e+06 ns | 2.466e+06 |

### `logcraft-core` — the deterministic log simulator core

_73 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | peak_frontier_window_frames | peak_window_frames | records | emit_ms | materialize_ms | capacity | ns_per_record | coordinates | ns_per_coordinate | discovered_knob_cap | build_coordinates | discovered_tower_cap | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.979 ms | 1 | 668217.139 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 16.753 ms | 4 | 1.433e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 40.195 ms | 16 | 2.388e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 17.116 ms | 4 | 1.402e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 40.142 ms | 16 | 2.392e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.506 ms | 1 | 988074.305 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.706 ms | 4 | 2.832e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.768 ms | 16 | 4.526e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.572 ms | 64 | 5.743e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 19.812 ms | 256 | 6.461e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.407 ms | 32 | 3.630e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.758 ms | 32 | 5.802e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.718 ms | 32 | 5.886e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 2.976 ms | 32 | 5.376e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 0.923 ms | 16 | 8.664e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.585 ms | 16 | 5.046e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.635 ms | 16 | 4.894e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.212 ms | 16 | 3.616e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 3.255 ms | 16 | 2.458e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.667 ms | 16 | 1.714e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 8.875 ns |  | 1.127e+08 |  |  | 3.254e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 7.102 ns |  | 1.408e+08 |  |  | 7.322e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 7.407 ns |  | 1.350e+08 |  |  | 1.350e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 13.475 ns |  | 7.421e+07 |  |  | 8.753e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.609 ns |  | 2.170e+08 |  |  | 1.736e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 79.851 ns |  | 1.252e+07 |  |  | 2.379e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 57.515 ns |  | 1.739e+07 |  |  | 9.565e+07 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_IndexPass_Unmetered/iterations:1/real_time` | 388.744 ms |  |  |  |  |  | 25001 | 25000 | 1.800e+06 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_IndexPass_Metered/iterations:1/real_time` | 401.773 ms |  |  |  |  |  | 25001 | 25000 | 1.800e+06 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 368.302 ns |  | 2.715e+06 |  |  | 7.141e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 166.065 ns |  | 6.022e+06 |  |  | 1.096e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 246.035 ns |  | 4.064e+06 |  |  | 3.008e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 81.752 ns |  | 1.223e+07 |  |  | 6.605e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 118.286 ns |  | 8.454e+06 |  |  | 6.002e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 276.687 ns |  | 3.614e+06 |  |  | 7.228e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 408.552 ns |  | 2.448e+06 |  |  | 7.881e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 398.574 ns |  | 2.509e+06 |  |  | 1.746e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 316.942 ns |  | 3.155e+06 |  |  | 8.298e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 117.702 ns |  | 8.496e+06 |  |  | 1.546e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 216.275 ns |  | 4.624e+06 |  |  | 3.422e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 60.795 ns |  | 1.645e+07 |  |  | 8.882e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 85.087 ns |  | 1.175e+07 |  |  | 8.344e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 246.497 ns |  | 4.057e+06 |  |  | 8.114e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 347.504 ns |  | 2.878e+06 |  |  | 9.266e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 328.416 ns |  | 3.045e+06 |  |  | 2.119e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.729 ms | 1 |  | 6000 |  |  |  |  |  | 5.847 | 1.671 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 16.316 ms | 4 |  | 24000 |  |  |  |  |  | 9.013 | 5.155 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 35.288 ms | 16 |  | 96000 |  |  |  |  |  | 16.164 | 12.573 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2703.913 us |  | 3.735e+06 |  |  |  |  |  |  |  |  | 8192 | 2.677e-07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2626.876 us |  | 3.836e+06 |  |  |  |  |  |  |  |  | 32768 | 2.607e-07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 206.418 us |  | 3.969e+07 |  |  |  |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 817.968 us |  | 4.007e+07 |  |  |  |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate/real_time` | 145.603 us |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 1.456e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate_CiWorld/real_time` | 286.827 us |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 2.868e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisAtCap/real_time` | 28.364 ms |  |  |  |  |  |  |  |  |  |  |  |  | 64 | 4.432e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_TowerAtProductCap/real_time` | 158.591 ms |  |  |  |  |  |  |  |  |  |  |  |  | 256 | 6.195e-04 | 64 | 4 | 256 |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/2/real_time` | 383.573 us |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 1.918e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/4/real_time` | 798.323 us |  |  |  |  |  |  |  |  |  |  |  |  | 4 | 1.996e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/8/real_time` | 1671.258 us |  |  |  |  |  |  |  |  |  |  |  |  | 8 | 2.089e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/16/real_time` | 4018.262 us |  |  |  |  |  |  |  |  |  |  |  |  | 16 | 2.511e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/32/real_time` | 9896.568 us |  |  |  |  |  |  |  |  |  |  |  |  | 32 | 3.093e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/64/real_time` | 28403.2 us |  |  |  |  |  |  |  |  |  |  |  |  | 64 | 4.438e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.827 ms |  | 3.432e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 44248 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 15.893 ms |  | 5.034e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 19081 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 18.847 ms |  | 4.245e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 3405 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 35.778 ms |  | 8.944e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 | 23363 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.354 ms |  | 3.147e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 38 | 0 | 1 | 4.852e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 16.939 ms |  | 4.723e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 121 | 0 | 4 | 1.963e+07 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 20.697 ms |  | 3.865e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 46 | 0 | 4 | 8.228e+06 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 36.973 ms |  | 8.655e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  | 495 | 0 | 16 | 1.023e+08 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 4.746 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 4.8 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.005 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 25.578 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 25.538 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 36.78 ns | 65536 |
