# benchmark summary — v1.8.3

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 783.904 us | 1.276e+06 | 7.839e-07 |
| `BM_TokenizationThroughput/8` | 745.843 us | 1.341e+06 | 7.458e-07 |
| `BM_TokenizationThroughputDegenerate/4` | 775.092 us | 1.290e+06 | 7.751e-07 |
| `BM_TokenizationThroughputDegenerate/8` | 719.708 us | 1.389e+06 | 7.197e-07 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 206.275 us |  |  |  |  |  |  |  |
| `BM_Diff` | 363.165 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 63.214 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 114.51 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 184.384 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 5.006 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 5.421 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 6618.381 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 13243.658 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 33413.905 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 61279.828 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 156205.153 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 24802.369 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 79.791 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 0.892 ms |  |  |  |  |  | 1.121e+06 |  |
| `BM_MetaLogCompress/10000/16` | 3.186 ms |  |  |  |  |  | 3.139e+06 |  |
| `BM_MetaLogCompress/100000/16` | 15.178 ms |  |  |  |  |  | 6.589e+06 |  |
| `BM_MetaLogCompress/1000/32` | 0.918 ms |  |  |  |  |  | 1.090e+06 |  |
| `BM_MetaLogCompress/10000/32` | 3.107 ms |  |  |  |  |  | 3.218e+06 |  |
| `BM_MetaLogCompress/100000/32` | 14.895 ms |  |  |  |  |  | 6.715e+06 |  |
| `BM_MetaLogCompress/1000/64` | 0.899 ms |  |  |  |  |  | 1.112e+06 |  |
| `BM_MetaLogCompress/10000/64` | 3.108 ms |  |  |  |  |  | 3.218e+06 |  |
| `BM_MetaLogCompress/100000/64` | 14.888 ms |  |  |  |  |  | 6.717e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 31.338 us |  |  |  |  |  | 3.191e+07 | 3.133e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 75.873 us |  |  |  |  |  | 1.318e+07 | 7.587e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 176.34 us |  |  |  |  |  | 5.671e+06 | 1.763e-07 |
| `BM_MetaLogIngest_Where` | 75.471 us |  |  |  |  |  | 1.325e+07 | 7.547e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3924.893 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4650.99 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 12271.78 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 29720.861 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 233.032 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 297.659 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3522.733 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 4311.206 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7755.6 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 542.321 us |  |  |  |  |  | 0.6 | 0 | 36878.416 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1304.989 us |  |  |  |  |  | 0.857 | 0 | 21456.521 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 5218.228 us |  |  |  |  |  | 0.857 | 0 | 5365.929 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 7633.225 us |  |  |  |  |  | 0.857 | 0 | 3668.216 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 88478.587 us |  |  |  |  |  | 0.98 | 0 | 2215.223 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 94879.357 us |  |  |  |  |  | 0.98 | 0 | 2065.805 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 139652.499 us |  |  |  |  |  | 0.98 | 6 | 1403.534 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 419810.298 us |  |  |  |  |  | 0.98 | 0 | 466.887 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 341.917 ns | 2.924e+06 |
| `BM_Pipeline_IngestBatch/64` | 28189.184 ns | 2.271e+06 |
| `BM_Pipeline_IngestBatch/1024` | 372795.082 ns | 2.745e+06 |
| `BM_Pipeline_CloseWindow/1000` | 20986.627 ns | 48171.6 |
| `BM_Pipeline_CloseWindow/10000` | 34525.632 ns | 29617.68 |
| `BM_Pipeline_FullWindow/1000` | 423948.435 ns | 2.359e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.454e+06 ns | 2.895e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.921 ms | 1 | 672589.387 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 18.953 ms | 4 | 1.266e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 54.813 ms | 16 | 1.751e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 18.936 ms | 4 | 1.267e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 54.538 ms | 16 | 1.760e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.595 ms | 1 | 840801.249 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.764 ms | 4 | 2.616e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.777 ms | 16 | 4.502e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 6.268 ms | 64 | 5.105e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 22.537 ms | 256 | 5.680e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.834 ms | 32 | 3.310e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 3.236 ms | 32 | 4.945e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 3.144 ms | 32 | 5.090e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 3.389 ms | 32 | 4.722e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 4.085 ms | 32 | 3.917e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.727 ms | 16 | 4.631e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.913 ms | 16 | 4.183e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.85 ms | 16 | 4.324e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.332 ms | 16 | 3.431e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 3.122 ms | 16 | 2.562e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.711 ms | 16 | 1.698e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.466 ns |  | 8.722e+07 |  |  | 2.521e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.637 ns |  | 1.038e+08 |  |  | 5.396e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 18.139 ns |  | 5.513e+07 |  |  | 5.513e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 15.05 ns |  | 6.644e+07 |  |  | 7.818e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.436 ns |  | 2.255e+08 |  |  | 1.804e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 98.281 ns |  | 1.018e+07 |  |  | 1.933e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 84.517 ns |  | 1.183e+07 |  |  | 6.507e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 385.251 ns |  | 2.596e+06 |  |  | 6.827e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 184.219 ns |  | 5.428e+06 |  |  | 9.880e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 274.295 ns |  | 3.646e+06 |  |  | 2.698e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 95.248 ns |  | 1.050e+07 |  |  | 5.669e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 131.561 ns |  | 7.601e+06 |  |  | 5.397e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 305.532 ns |  | 3.273e+06 |  |  | 6.546e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 412.248 ns |  | 2.426e+06 |  |  | 7.811e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 401.246 ns |  | 2.492e+06 |  |  | 1.735e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 344.851 ns |  | 2.900e+06 |  |  | 7.627e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 127.659 ns |  | 7.833e+06 |  |  | 1.426e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 249.449 ns |  | 4.009e+06 |  |  | 2.967e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 72.214 ns |  | 1.385e+07 |  |  | 7.478e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 97.226 ns |  | 1.029e+07 |  |  | 7.303e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 259.909 ns |  | 3.848e+06 |  |  | 7.695e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 338.99 ns |  | 2.950e+06 |  |  | 9.499e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 324.576 ns |  | 3.081e+06 |  |  | 2.144e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.667 ms | 1 |  | 6000 |  |  | 5.362 | 1.891 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 17.989 ms | 4 |  | 24000 |  |  | 4.296 | 8.065 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 52.684 ms | 16 |  | 96000 |  |  | 12.772 | 17.021 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2827.634 us |  | 3.570e+06 |  |  |  |  |  | 8192 | 2.801e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2641.53 us |  | 3.836e+06 |  |  |  |  |  | 32768 | 2.607e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 216.296 us |  | 3.789e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 862.512 us |  | 3.800e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.713 ms |  | 3.501e+06 |  | 1 |  |  |  |  |  | 0 | 170628 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.682 ms |  | 4.796e+06 |  | 1 |  |  |  |  |  | 0 | 247852 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 35.041 ms |  | 2.283e+06 |  | 4 |  |  |  |  |  | 0 | 160673 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 53.544 ms |  | 5.976e+06 |  | 4 |  |  |  |  |  | 0 | 726215 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 76.366 ms |  | 4.190e+06 |  | 16 |  |  |  |  |  | 0 | 821263 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 6.779 ms |  | 2.950e+06 |  | 1 |  |  |  |  |  | 125 | 0 | 1 | 7.299e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 19.482 ms |  | 4.106e+06 |  | 1 |  |  |  |  |  | 755 | 0 | 4 | 1.411e+08 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 42.755 ms |  | 1.871e+06 |  | 4 |  |  |  |  |  | 780 | 0 | 4 | 7.523e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 94.51 ms |  | 3.386e+06 |  | 4 |  |  |  |  |  | 8822 | 0 | 16 | 6.342e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 94.212 ms |  | 3.397e+06 |  | 16 |  |  |  |  |  | 1925 | 0 | 16 | 2.173e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 5.836 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 4.886 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 68.136 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 67.085 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 70.228 ns | 65536 |
