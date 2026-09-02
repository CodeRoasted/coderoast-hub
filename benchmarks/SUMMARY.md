# benchmark summary — v1.10.3

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_5 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1688.995 us | 592270.865 | 1.688e-06 |
| `BM_TokenizationThroughput/8` | 1564.403 us | 639182.41 | 1.564e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1646.209 us | 607457.628 | 1.646e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1525.797 us | 655405.054 | 1.526e-06 |
| `BM_TokenizationThroughputNestedJson` | 2529.299 us | 395350.067 | 2.529e-06 |

### `insight-metalog` — compression / MetaLog-document build

_31 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | allocs_per_event | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 278.731 us |  |  |  |  |  |  |  |  |
| `BM_Diff` | 433.32 us |  |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 77.809 us | 113 |  |  |  |  |  |  |  |
| `BM_ComposeCubes` | 121.385 us |  | 253 |  |  |  |  |  |  |
| `BM_CubeDiffOf` | 129.042 us |  |  | 253 |  |  |  |  |  |
| `BM_CoordParse` | 10.119 us |  |  |  | 225 |  |  |  |  |
| `BM_CoordStringify` | 8.321 us |  |  |  | 225 |  |  |  |  |
| `BM_ShannonEntropy/64` | 9074.304 ns |  |  |  |  | 64 |  |  |  |
| `BM_ShannonEntropy/128` | 18008.764 ns |  |  |  |  | 128 |  |  |  |
| `BM_ShannonEntropy/192` | 26938.672 ns |  |  |  |  | 192 |  |  |  |
| `BM_Divergences/64` | 53859.773 ns |  |  |  |  | 64 |  |  |  |
| `BM_Divergences/128` | 109305.096 ns |  |  |  |  | 128 |  |  |  |
| `BM_HistogramJs/64` | 37895.96 ns |  |  |  |  | 64 |  |  |  |
| `BM_StageCube_Determinism/iterations:1` | 89.055 us |  |  |  |  |  |  |  |  |
| `BM_CubeKeyAlloc_Empty` | 45.375 us |  |  |  |  |  | 0 | 2.209e+07 | 4.527e-08 |
| `BM_CubeKeyAlloc_ShortSSO` | 62.694 us |  |  |  |  |  | 0 | 1.598e+07 | 6.259e-08 |
| `BM_CubeKeyAlloc_MidBand` | 63.157 us |  |  |  |  |  | 0 | 1.586e+07 | 6.305e-08 |
| `BM_CubeKeyAlloc_LongOverSSO` | 65.529 us |  |  |  |  |  | 0 | 1.529e+07 | 6.541e-08 |
| `BM_MetaLogCompress/1000/16` | 1.298 ms |  |  |  |  |  |  | 770263.975 |  |
| `BM_MetaLogCompress/10000/16` | 4.569 ms |  |  |  |  |  |  | 2.189e+06 |  |
| `BM_MetaLogCompress/100000/16` | 21.739 ms |  |  |  |  |  |  | 4.600e+06 |  |
| `BM_MetaLogCompress/1000/32` | 1.312 ms |  |  |  |  |  |  | 762555.492 |  |
| `BM_MetaLogCompress/10000/32` | 4.593 ms |  |  |  |  |  |  | 2.177e+06 |  |
| `BM_MetaLogCompress/100000/32` | 21.746 ms |  |  |  |  |  |  | 4.599e+06 |  |
| `BM_MetaLogCompress/1000/64` | 1.31 ms |  |  |  |  |  |  | 763276.794 |  |
| `BM_MetaLogCompress/10000/64` | 4.591 ms |  |  |  |  |  |  | 2.178e+06 |  |
| `BM_MetaLogCompress/100000/64` | 21.872 ms |  |  |  |  |  |  | 4.574e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 42.014 us |  |  |  |  |  |  | 2.380e+07 | 4.201e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 102.412 us |  |  |  |  |  |  | 9.765e+06 | 1.024e-07 |
| `BM_MetaLogIngest_FieldHistograms/3` | 234.237 us |  |  |  |  |  |  | 4.270e+06 | 2.342e-07 |
| `BM_MetaLogIngest_Where` | 91.316 us |  |  |  |  |  |  | 1.095e+07 | 9.130e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | raw_strides | ring_capacity | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 1903.951 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 2282.027 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 5994.033 us | 64 | 0.917 | 965 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 15342.134 us | 256 | 0.917 | 2198 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 217.487 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 275.095 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 1670.69 us | 16 | 0.917 | 269 | 5 | 2000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 2041.43 us | 16 | 0.917 | 392 | 5 | 8000 |  |  |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 5315.9 us |  |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/1/0` | 742.422 us |  |  |  |  |  | 0.609 | 0 | 30979.906 | 1 | 1 | 7 | 3 | 23 |
| `BM_PyramidAdvanceAndDiff/16/3/1/0` | 1423.353 us |  |  |  |  |  | 0.857 | 0 | 19673.28 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/1/0` | 5853.695 us |  |  |  |  |  | 0.857 | 0 | 4783.299 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/3/0` | 5793.346 us |  |  |  |  |  | 0.857 | 0 | 4833.214 | 3 | 1 | 7 | 5 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 69071.285 us |  |  |  |  |  | 0.98 | 0 | 2837.644 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/0` | 69283.258 us |  |  |  |  |  | 0.98 | 0 | 2828.985 | 6 | 1 | 7 | 8 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/4/6` | 157861.619 us |  |  |  |  |  | 0.971 | 6 | 1323.958 | 6 | 7 | 193 | 20 | 209 |
| `BM_PyramidAdvanceAndDiff/256/6/4/0` | 310832.489 us |  |  |  |  |  | 0.98 | 0 | 630.572 | 6 | 1 | 7 | 8 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 329.043 ns | 3.038e+06 |
| `BM_Pipeline_IngestBatch/64` | 26570.275 ns | 2.407e+06 |
| `BM_Pipeline_IngestBatch/1024` | 342218.242 ns | 2.991e+06 |
| `BM_Pipeline_CloseWindow/1000` | 15785.353 ns | 63911.833 |
| `BM_Pipeline_CloseWindow/10000` | 28108.837 ns | 36426.346 |
| `BM_Pipeline_FullWindow/1000` | 359099.102 ns | 2.785e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.317e+06 ns | 3.014e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 7.939 ms | 1 | 755719.29 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 15.712 ms | 4 | 1.528e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 42.481 ms | 16 | 2.260e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 15.597 ms | 4 | 1.539e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 42.825 ms | 16 | 2.242e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.857 ms | 1 | 583673.217 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.714 ms | 4 | 2.803e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.44 ms | 16 | 5.555e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 4.867 ms | 64 | 6.575e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 16.043 ms | 256 | 7.979e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.315 ms | 32 | 3.708e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 2.692 ms | 32 | 5.944e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.642 ms | 32 | 6.057e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 2.616 ms | 32 | 6.117e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.689 ms | 32 | 4.338e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.39 ms | 16 | 5.755e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.542 ms | 16 | 5.190e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.512 ms | 16 | 5.291e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 1.998 ms | 16 | 4.004e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.684 ms | 16 | 2.981e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 3.84 ms | 16 | 2.083e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 12.042 ns |  | 8.304e+07 |  |  | 2.400e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.047 ns |  | 1.105e+08 |  |  | 5.748e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 16.979 ns |  | 5.890e+07 |  |  | 5.890e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 14.124 ns |  | 7.080e+07 |  |  | 8.340e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.782 ns |  | 2.091e+08 |  |  | 1.673e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 83.616 ns |  | 1.196e+07 |  |  | 2.272e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 77.805 ns |  | 1.285e+07 |  |  | 7.069e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 384.513 ns |  | 2.601e+06 |  |  | 6.840e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 167.668 ns |  | 5.964e+06 |  |  | 1.085e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 243.117 ns |  | 4.113e+06 |  |  | 3.044e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 83.642 ns |  | 1.196e+07 |  |  | 6.456e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 127.13 ns |  | 7.866e+06 |  |  | 5.585e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 278.355 ns |  | 3.593e+06 |  |  | 7.185e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 426.206 ns |  | 2.346e+06 |  |  | 7.555e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 412.249 ns |  | 2.426e+06 |  |  | 1.688e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 342.924 ns |  | 2.916e+06 |  |  | 7.669e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 121.07 ns |  | 8.260e+06 |  |  | 1.503e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 212.979 ns |  | 4.695e+06 |  |  | 3.475e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 63.02 ns |  | 1.587e+07 |  |  | 8.569e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 96.681 ns |  | 1.034e+07 |  |  | 7.344e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 242.601 ns |  | 4.122e+06 |  |  | 8.244e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 361.821 ns |  | 2.764e+06 |  |  | 8.899e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 346.045 ns |  | 2.890e+06 |  |  | 2.011e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.03 ms | 1 |  | 6000 |  |  | 4.799 | 1.658 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 15.592 ms | 4 |  | 24000 |  |  | 3.57 | 7.617 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 41.849 ms | 16 |  | 96000 |  |  | 8.693 | 13.97 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2456.808 us |  | 4.085e+06 |  |  |  |  |  | 8192 | 2.448e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2559.572 us |  | 3.929e+06 |  |  |  |  |  | 32768 | 2.545e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 203.443 us |  | 4.028e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 823.989 us |  | 3.978e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 6.004 ms |  | 3.331e+06 |  | 1 |  |  |  |  |  | 0 | 11825 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.456 ms |  | 4.862e+06 |  | 1 |  |  |  |  |  | 0 | 1788 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 18.133 ms |  | 4.412e+06 |  | 4 |  |  |  |  |  | 0 | 8760 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 39.227 ms |  | 8.158e+06 |  | 4 |  |  |  |  |  | 0 | 142247 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 51.336 ms |  | 6.233e+06 |  | 16 |  |  |  |  |  | 0 | 271696 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.746 ms |  | 2.965e+06 |  | 1 |  |  |  |  |  | 2101 | 0 | 1 | 1.184e+07 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 17.257 ms |  | 4.636e+06 |  | 1 |  |  |  |  |  | 39 | 0 | 4 | 1.424e+06 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 40.961 ms |  | 1.953e+06 |  | 4 |  |  |  |  |  | 52 | 0 | 4 | 2.577e+06 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 43.544 ms |  | 7.349e+06 |  | 4 |  |  |  |  |  | 4916 | 0 | 16 | 4.015e+08 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 55.817 ms |  | 5.733e+06 |  | 16 |  |  |  |  |  | 1059 | 0 | 16 | 4.652e+08 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 4.731 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 9.742 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 36.458 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 36.511 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 37.321 ns | 65536 |
