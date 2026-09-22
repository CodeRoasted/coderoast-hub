# benchmark summary — v1.10.4

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_5 benchmark(s)._

| benchmark | real_time | items_per_second | s_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1831.116 us | 546149.555 | 1.831e-06 |
| `BM_TokenizationThroughput/8` | 1737.881 us | 575388.304 | 1.738e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1782.893 us | 560965.132 | 1.783e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1679.561 us | 595414.568 | 1.680e-06 |
| `BM_TokenizationThroughputNestedJson` | 2960.152 us | 337801.926 | 2.960e-06 |

### `insight-metalog` — compression / MetaLog-document build

_36 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 218.324 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 332.351 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 59.484 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 92.504 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 97.788 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 7.139 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 6.491 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 6885.782 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 13679.587 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 20455.72 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 41188.879 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 83661.139 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 28644.57 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 67.449 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 34.72 us |  |  |  |  |  | 0 | 2.886e+07 | 3.466e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 47.889 us |  |  |  |  |  | 0 | 2.091e+07 | 4.782e-08 |
| `BM_CubeKeyAlloc_MidBand` | 48.775 us |  |  |  |  |  | 0 | 2.053e+07 | 4.871e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 51.676 us |  |  |  |  |  | 0 | 1.937e+07 | 5.161e-08 |
| `BM_MetaLogCompress/1000/16` | 0.951 ms |  |  |  |  |  |  | 1.051e+06 |  |
| `BM_MetaLogCompress/10000/16` | 3.367 ms |  |  |  |  |  |  | 2.970e+06 |  |
| `BM_MetaLogCompress/100000/16` | 15.919 ms |  |  |  |  |  |  | 6.282e+06 |  |
| `BM_MetaLogCompress/1000/32` | 0.957 ms |  |  |  |  |  |  | 1.045e+06 |  |
| `BM_MetaLogCompress/10000/32` | 3.372 ms |  |  |  |  |  |  | 2.966e+06 |  |
| `BM_MetaLogCompress/100000/32` | 15.904 ms |  |  |  |  |  |  | 6.288e+06 |  |
| `BM_MetaLogCompress/1000/64` | 0.96 ms |  |  |  |  |  |  | 1.042e+06 |  |
| `BM_MetaLogCompress/10000/64` | 3.379 ms |  |  |  |  |  |  | 2.959e+06 |  |
| `BM_MetaLogCompress/100000/64` | 15.917 ms |  |  |  |  |  |  | 6.283e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 32.457 us |  |  |  |  |  |  | 3.081e+07 | 3.246e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 78.465 us |  |  |  |  |  |  | 1.274e+07 | 7.846e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 165.908 us |  |  |  |  |  |  | 6.028e+06 | 1.659e-07 |
| `BM_MetaLogIngest_Where` | 66.571 us |  |  |  |  |  |  | 1.502e+07 | 6.657e-08 |
| `BM_OrdinalKeyAlloc_None` | 34.363 us |  |  |  |  |  | 0 | 2.915e+07 | 3.431e-08 |
| `BM_OrdinalKeyAlloc_Key15Sso` | 51.003 us |  |  |  |  |  | 0 | 1.963e+07 | 5.093e-08 |
| `BM_OrdinalKeyAlloc_Key16ShipLegOnly` | 49.518 us |  |  |  |  |  | 0 | 2.022e+07 | 4.945e-08 |
| `BM_OrdinalKeyAlloc_Key16TraceMix` | 52.446 us |  |  |  |  |  | 0 | 1.909e+07 | 5.237e-08 |
| `BM_OrdinalKeyAlloc_Key23OverBothSso` | 51.188 us |  |  |  |  |  | 0 | 1.956e+07 | 5.112e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 2084.293 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2550.874 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 6537.247 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 16925.603 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 260.066 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 310.311 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1887.177 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 2242.659 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 6356.014 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 832.392 us |  |  |  |  |  | 0.609 | 0 | 27631.794 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1610.55 us |  |  |  |  |  | 0.857 | 0 | 17387.565 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 6381.912 us |  |  |  |  |  | 0.857 | 0 | 4387.578 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 6386.2 us |  |  |  |  |  | 0.857 | 0 | 4384.888 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 77092.573 us |  |  |  |  |  | 0.98 | 0 | 2542.394 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 76488.747 us |  |  |  |  |  | 0.98 | 0 | 2562.465 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 176104.305 us |  |  |  |  |  | 0.971 | 6 | 1186.793 | 6 | 7 | 193 | 20 | 209 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 341567.45 us |  |  |  |  |  | 0.98 | 0 | 573.835 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 365.565 ns | 2.733e+06 |
| `BM_Pipeline_IngestBatch/64` | 29731.664 ns | 2.151e+06 |
| `BM_Pipeline_IngestBatch/1024` | 377785.084 ns | 2.709e+06 |
| `BM_Pipeline_CloseWindow/1000` | 21195.337 ns | 47720.911 |
| `BM_Pipeline_CloseWindow/10000` | 36016.57 ns | 28786.189 |
| `BM_Pipeline_FullWindow/1000` | 410728.916 ns | 2.435e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.817e+06 ns | 2.620e+06 |

### `logcraft-core` — the deterministic log simulator core

_74 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | coordinates | ns_per_coordinate | discovered_knob_cap | build_coordinates | discovered_tower_cap | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 10.038 ms | 1 | 597706.15 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 16.172 ms | 4 | 1.484e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 45.694 ms | 16 | 2.101e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 16.374 ms | 4 | 1.466e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 45.205 ms | 16 | 2.124e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.568 ms | 1 | 880513.278 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.715 ms | 4 | 2.798e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.648 ms | 16 | 4.853e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.501 ms | 64 | 5.817e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 18.828 ms | 256 | 6.799e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.72 ms | 32 | 3.390e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.992 ms | 32 | 5.348e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.776 ms | 32 | 5.763e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 2.922 ms | 32 | 5.476e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.664 ms | 32 | 4.367e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.298 ms | 16 | 6.163e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.767 ms | 16 | 4.528e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.659 ms | 16 | 4.824e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.049 ms | 16 | 3.904e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.834 ms | 16 | 2.823e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.124 ms | 16 | 1.940e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.426 ns |  | 8.752e+07 |  |  | 2.529e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.625 ns |  | 1.039e+08 |  |  | 5.402e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 18.19 ns |  | 5.498e+07 |  |  | 5.498e+07 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 15.318 ns |  | 6.528e+07 |  |  | 7.665e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.579 ns |  | 2.184e+08 |  |  | 1.747e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 89.851 ns |  | 1.113e+07 |  |  | 2.115e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 84.574 ns |  | 1.182e+07 |  |  | 6.503e+07 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 404.574 ns |  | 2.472e+06 |  |  | 6.501e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 182.836 ns |  | 5.469e+06 |  |  | 9.954e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 255.663 ns |  | 3.911e+06 |  |  | 2.894e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 92.184 ns |  | 1.085e+07 |  |  | 5.858e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 129.88 ns |  | 7.699e+06 |  |  | 5.467e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 305.623 ns |  | 3.272e+06 |  |  | 6.544e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 445.489 ns |  | 2.245e+06 |  |  | 7.228e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 451.188 ns |  | 2.216e+06 |  |  | 1.543e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 370.024 ns |  | 2.703e+06 |  |  | 7.108e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 130.238 ns |  | 7.678e+06 |  |  | 1.397e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 231.881 ns |  | 4.313e+06 |  |  | 3.191e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 68.716 ns |  | 1.455e+07 |  |  | 7.859e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 97.86 ns |  | 1.022e+07 |  |  | 7.255e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 268.047 ns |  | 3.731e+06 |  |  | 7.461e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 384.124 ns |  | 2.603e+06 |  |  | 8.383e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 361.198 ns |  | 2.769e+06 |  |  | 1.927e+09 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 9.844 ms | 1 |  | 6000 |  |  | 6.465 | 1.988 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 16.221 ms | 4 |  | 24000 |  |  | 7.823 | 6.006 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 43.036 ms | 16 |  | 96000 |  |  | 20.084 | 12.272 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2787.693 us |  | 3.640e+06 |  |  |  |  |  | 8192 | 2.747e-07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2578.299 us |  | 3.941e+06 |  |  |  |  |  | 32768 | 2.538e-07 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 215.967 us |  | 3.795e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 857.977 us |  | 3.820e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate/real_time` | 154.064 us |  |  |  |  |  |  |  |  |  | 1 | 1.541e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_SingleCoordinate_CiWorld/real_time` | 316.135 us |  |  |  |  |  |  |  |  |  | 1 | 3.161e-04 |  |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisAtCap/real_time` | 29.968 ms |  |  |  |  |  |  |  |  |  | 64 | 4.683e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_TowerAtProductCap/real_time` | 174.026 ms |  |  |  |  |  |  |  |  |  | 256 | 6.798e-04 | 64 | 4 | 256 |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/2/real_time` | 402.314 us |  |  |  |  |  |  |  |  |  | 2 | 2.012e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/4/real_time` | 860.451 us |  |  |  |  |  |  |  |  |  | 4 | 2.151e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/8/real_time` | 1847.661 us |  |  |  |  |  |  |  |  |  | 8 | 2.310e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/16/real_time` | 4209.03 us |  |  |  |  |  |  |  |  |  | 16 | 2.631e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/32/real_time` | 10875.997 us |  |  |  |  |  |  |  |  |  | 32 | 3.399e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_ScenarioLoad_KnobAxisLadder/64/real_time` | 29748.874 us |  |  |  |  |  |  |  |  |  | 64 | 4.648e-04 | 64 |  |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.886 ms |  | 3.398e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  | 0 | 141284 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.622 ms |  | 4.813e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  | 0 | 156454 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 25.77 ms |  | 3.104e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  | 0 | 65929 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 51.598 ms |  | 6.202e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  | 0 | 424150 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 71.127 ms |  | 4.499e+06 |  | 16 |  |  |  |  |  |  |  |  |  |  | 0 | 381115 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 7.298 ms |  | 2.740e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  | 1252 | 0 | 1 | 1.686e+07 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 18.841 ms |  | 4.246e+06 |  | 1 |  |  |  |  |  |  |  |  |  |  | 732 | 0 | 4 | 6.189e+07 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 59.52 ms |  | 1.344e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  | 439 | 0 | 4 | 3.761e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 58.365 ms |  | 5.483e+06 |  | 4 |  |  |  |  |  |  |  |  |  |  | 4749 | 0 | 16 | 1.924e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 74.633 ms |  | 4.288e+06 |  | 16 |  |  |  |  |  |  |  |  |  |  | 1672 | 0 | 16 | 1.127e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 5.096 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 5.228 ms |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.004 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 17.96 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 17.71 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 28.875 ns | 65536 |
