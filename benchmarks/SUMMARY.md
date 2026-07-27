# benchmark summary — v1.8.4

Per-stage measurements, taken fresh on the release runner at this tag. Each table lists the benchmark, its median `real_time`, and the domain counters the cost scales with (template / n-gram cardinality, throughput). **Read the shape, not the absolute time** — wall-time is machine-relative; the invariant we hold is the *ordering* (see METHODOLOGY.md).

### `insight-canon` — ingestion / tokenization throughput (O(lines) — the pipeline's largest stage)

_4 benchmark(s)._

| benchmark | real_time | items_per_second | ns_per_line |
| --- | --- | --- | --- |
| `BM_TokenizationThroughput/4` | 1696.049 us | 589733.463 | 1.696e-06 |
| `BM_TokenizationThroughput/8` | 1583.755 us | 631427.879 | 1.584e-06 |
| `BM_TokenizationThroughputDegenerate/4` | 1656.099 us | 603849.977 | 1.656e-06 |
| `BM_TokenizationThroughputDegenerate/8` | 1525.928 us | 655347.913 | 1.526e-06 |

### `insight-metalog` — compression / MetaLog-document build

_27 benchmark(s)._

| benchmark | real_time | base_rows | lhs_cells | prev_cells | cells | n | items_per_second | ns_per_event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_Compose` | 217.948 us |  |  |  |  |  |  |  |
| `BM_Diff` | 415.545 us |  |  |  |  |  |  |  |
| `BM_BuildClosedCube` | 55.939 us | 113 |  |  |  |  |  |  |
| `BM_ComposeCubes` | 120.878 us |  | 253 |  |  |  |  |  |
| `BM_CubeDiffOf` | 189.652 us |  |  | 253 |  |  |  |  |
| `BM_CoordParse` | 5.057 us |  |  |  | 225 |  |  |  |
| `BM_CoordStringify` | 5.451 us |  |  |  | 225 |  |  |  |
| `BM_ShannonEntropy/64` | 6644.109 ns |  |  |  |  | 64 |  |  |
| `BM_ShannonEntropy/128` | 13168.254 ns |  |  |  |  | 128 |  |  |
| `BM_ShannonEntropy/192` | 28890.748 ns |  |  |  |  | 192 |  |  |
| `BM_Divergences/64` | 66652.105 ns |  |  |  |  | 64 |  |  |
| `BM_Divergences/128` | 156907.641 ns |  |  |  |  | 128 |  |  |
| `BM_HistogramJs/64` | 24876.381 ns |  |  |  |  | 64 |  |  |
| `BM_StageCube_Determinism/iterations:1` | 76.385 us |  |  |  |  |  |  |  |
| `BM_MetaLogCompress/1000/16` | 0.894 ms |  |  |  |  |  | 1.119e+06 |  |
| `BM_MetaLogCompress/10000/16` | 3.105 ms |  |  |  |  |  | 3.221e+06 |  |
| `BM_MetaLogCompress/100000/16` | 14.918 ms |  |  |  |  |  | 6.704e+06 |  |
| `BM_MetaLogCompress/1000/32` | 0.897 ms |  |  |  |  |  | 1.115e+06 |  |
| `BM_MetaLogCompress/10000/32` | 3.103 ms |  |  |  |  |  | 3.223e+06 |  |
| `BM_MetaLogCompress/100000/32` | 15.828 ms |  |  |  |  |  | 6.318e+06 |  |
| `BM_MetaLogCompress/1000/64` | 0.899 ms |  |  |  |  |  | 1.113e+06 |  |
| `BM_MetaLogCompress/10000/64` | 3.109 ms |  |  |  |  |  | 3.217e+06 |  |
| `BM_MetaLogCompress/100000/64` | 14.908 ms |  |  |  |  |  | 6.708e+06 |  |
| `BM_MetaLogIngest_FieldHistograms/0` | 32.38 us |  |  |  |  |  | 3.089e+07 | 3.238e-08 |
| `BM_MetaLogIngest_FieldHistograms/1` | 77.277 us |  |  |  |  |  | 1.294e+07 | 7.727e-08 |
| `BM_MetaLogIngest_FieldHistograms/3` | 169.806 us |  |  |  |  |  | 5.889e+06 | 1.698e-07 |
| `BM_MetaLogIngest_Where` | 79.504 us |  |  |  |  |  | 1.258e+07 | 7.950e-08 |

### `insight-eidos-detection` — eidos detection stage

_17 benchmark(s)._

| benchmark | real_time | components | composes_per_tick | cube_cells | diffs_per_tick | window_size | avg_composes/adv | disjoint | items_per_second | max_composes/adv | scales | windows_per_iter |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_CubeTick/2000/16` | 3500.281 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/16` | 4260.759 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/64` | 10984.716 us | 64 | 0.917 | 965 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick/8000/256` | 27254.522 us | 256 | 0.917 | 2198 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/2000/16` | 214.641 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_AdvancePhase/8000/16` | 273.766 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/2000/16` | 3205.149 us | 16 | 0.917 | 269 | 10 | 2000 |  |  |  |  |  |  |
| `BM_CubeTick_DiffPhase/8000/16` | 3943.931 us | 16 | 0.917 | 392 | 10 | 8000 |  |  |  |  |  |  |
| `BM_CubeTick_Determinism/iterations:1` | 7385.8 us |  |  |  |  |  |  |  |  |  |  |  |
| `BM_PyramidAdvanceAndDiff/16/1/0/0` | 473.959 us |  |  |  |  |  | 0.6 | 0 | 42197.661 | 1 | 2 | 20 |
| `BM_PyramidAdvanceAndDiff/16/3/0/0` | 1170.808 us |  |  |  |  |  | 0.857 | 0 | 23915.627 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/0/0` | 4747.676 us |  |  |  |  |  | 0.857 | 0 | 5897.695 | 3 | 4 | 28 |
| `BM_PyramidAdvanceAndDiff/64/3/2/0` | 6910.964 us |  |  |  |  |  | 0.857 | 0 | 4051.554 | 3 | 6 | 28 |
| `BM_PyramidAdvanceAndDiff/64/6/2/0` | 77827.544 us |  |  |  |  |  | 0.98 | 0 | 2518.385 | 6 | 9 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/0` | 86143.913 us |  |  |  |  |  | 0.98 | 0 | 2275.282 | 6 | 10 | 196 |
| `BM_PyramidAdvanceAndDiff/64/6/3/6` | 127322.833 us |  |  |  |  |  | 0.98 | 6 | 1539.439 | 6 | 16 | 196 |
| `BM_PyramidAdvanceAndDiff/256/6/3/0` | 387280.548 us |  |  |  |  |  | 0.98 | 0 | 506.108 | 6 | 10 | 196 |

### `insight-eidos-engine` — eidos engine / diff stage

_7 benchmark(s)._

| benchmark | real_time | items_per_second |
| --- | --- | --- |
| `BM_Pipeline_IngestLine` | 324.525 ns | 3.081e+06 |
| `BM_Pipeline_IngestBatch/64` | 25727.592 ns | 2.488e+06 |
| `BM_Pipeline_IngestBatch/1024` | 335402.569 ns | 3.052e+06 |
| `BM_Pipeline_CloseWindow/1000` | 15658.79 ns | 64353.652 |
| `BM_Pipeline_CloseWindow/10000` | 32833.406 ns | 31548.835 |
| `BM_Pipeline_FullWindow/1000` | 407200.355 ns | 2.456e+06 |
| `BM_Pipeline_FullWindow/10000` | 3.436e+06 ns | 2.910e+06 |

### `logcraft-core` — the deterministic log simulator core

_64 benchmark(s)._

| benchmark | real_time | agents | items_per_second | records_per_iter | shards | bytes_per_second | emit_ms | materialize_ms | capacity | ns_per_record | blocked_events | dropped | producers | wait_ns_total | epochs_per_reunfold | records_per_reunfold |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BM_DeterministicReplay_AgentScaling/1/real_time` | 8.908 ms | 1 | 673542.229 | 6000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/4/real_time` | 18.012 ms | 4 | 1.332e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_AgentScaling/16/real_time` | 53.255 ms | 16 | 1.803e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/4/real_time` | 17.943 ms | 4 | 1.338e+06 | 24000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_DeterministicReplay_RuntimeTimerBarriers/16/real_time` | 52.024 ms | 16 | 1.845e+06 | 96000 |  |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/1/real_time` | 0.593 ms | 1 | 843584.981 | 500 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/4/real_time` | 0.745 ms | 4 | 2.685e+06 | 2000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/16/real_time` | 1.675 ms | 16 | 4.776e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/64/real_time` | 5.848 ms | 64 | 5.472e+06 | 32000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_AgentScaling/256/real_time` | 20.517 ms | 256 | 6.239e+06 | 128000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/1/real_time` | 4.796 ms | 32 | 3.336e+06 | 16000 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/2/real_time` | 3.106 ms | 32 | 5.152e+06 | 16000 | 2 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/4/real_time` | 2.951 ms | 32 | 5.422e+06 | 16000 | 4 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/8/real_time` | 3.136 ms | 32 | 5.101e+06 | 16000 | 8 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_ShardScaling/16/real_time` | 3.817 ms | 32 | 4.192e+06 | 16000 | 16 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/0/real_time` | 1.649 ms | 16 | 4.850e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/2/real_time` | 1.828 ms | 16 | 4.375e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/4/real_time` | 1.755 ms | 16 | 4.559e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/8/real_time` | 2.226 ms | 16 | 3.594e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/16/real_time` | 2.982 ms | 16 | 2.683e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_EngineThroughput_FieldScaling/32/real_time` | 4.405 ms | 16 | 1.816e+06 | 8000 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Range` | 11.537 ns |  | 8.670e+07 |  |  | 2.506e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Choice` | 9.331 ns |  | 1.072e+08 |  |  | 5.574e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_WeightedChoice` | 18.006 ns |  | 5.554e+07 |  |  | 5.554e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Sequence` | 15.104 ns |  | 6.621e+07 |  |  | 7.790e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_StaticValue` | 4.765 ns |  | 2.099e+08 |  |  | 1.679e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Timestamp` | 98.237 ns |  | 1.018e+07 |  |  | 1.935e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Generator_Normal` | 84.867 ns |  | 1.178e+07 |  |  | 6.481e+07 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json` | 392.138 ns |  | 2.550e+06 |  |  | 6.707e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text` | 181.271 ns |  | 5.517e+06 |  |  | 1.004e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf` | 277.745 ns |  | 3.601e+06 |  |  | 2.665e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog` | 93.64 ns |  | 1.068e+07 |  |  | 5.767e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424` | 133.382 ns |  | 7.498e+06 |  |  | 5.324e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv` | 305.961 ns |  | 3.270e+06 |  |  | 6.540e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs` | 429.952 ns |  | 2.326e+06 |  |  | 7.489e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson` | 410.759 ns |  | 2.435e+06 |  |  | 1.694e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Json_Into` | 345.591 ns |  | 2.895e+06 |  |  | 7.613e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Text_Into` | 128.913 ns |  | 7.758e+06 |  |  | 1.412e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Clf_Into` | 246.793 ns |  | 4.052e+06 |  |  | 2.999e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Syslog_Into` | 72.861 ns |  | 1.373e+07 |  |  | 7.412e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Rfc5424_Into` | 96.374 ns |  | 1.038e+07 |  |  | 7.368e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Kv_Into` | 263.42 ns |  | 3.797e+06 |  |  | 7.593e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_Ecs_Into` | 358.622 ns |  | 2.789e+06 |  |  | 8.979e+08 |  |  |  |  |  |  |  |  |  |  |
| `BM_Formatter_OtelJson_Into` | 336.969 ns |  | 2.968e+06 |  |  | 2.066e+09 |  |  |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/1/real_time` | 8.673 ms | 1 |  | 6000 |  |  | 5.348 | 1.932 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/4/real_time` | 17.783 ms | 4 |  | 24000 |  |  | 3.973 | 8.336 |  |  |  |  |  |  |  |  |
| `BM_PlayToTarget_PhaseSplit/16/real_time` | 50.494 ms | 16 |  | 96000 |  |  | 11.16 | 16.172 |  |  |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/8192` | 2739.069 us |  | 3.689e+06 |  |  |  |  |  | 8192 | 2.711e-07 |  |  |  |  |  |  |
| `BM_RingSteadyState_SingleProducer/32768` | 2676.909 us |  | 3.773e+06 |  |  |  |  |  | 32768 | 2.651e-07 |  |  |  |  |  |  |
| `BM_RingBulkPop/8192` | 217.482 us |  | 3.768e+07 |  |  |  |  |  | 8192 |  |  |  |  |  |  |  |
| `BM_RingBulkPop/32768` | 878.485 us |  | 3.730e+07 |  |  |  |  |  | 32768 |  |  |  |  |  |  |  |
| `BM_Pipeline_Drop/1/1/real_time` | 5.825 ms |  | 3.434e+06 |  | 1 |  |  |  |  |  | 0 | 117406 | 1 | 0 |  |  |
| `BM_Pipeline_Drop/4/1/real_time` | 16.841 ms |  | 4.750e+06 |  | 1 |  |  |  |  |  | 0 | 128148 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/4/4/real_time` | 25.608 ms |  | 3.124e+06 |  | 4 |  |  |  |  |  | 0 | 107242 | 4 | 0 |  |  |
| `BM_Pipeline_Drop/16/4/real_time` | 50.224 ms |  | 6.371e+06 |  | 4 |  |  |  |  |  | 0 | 392301 | 16 | 0 |  |  |
| `BM_Pipeline_Drop/16/16/real_time` | 68.167 ms |  | 4.694e+06 |  | 16 |  |  |  |  |  | 0 | 650453 | 16 | 0 |  |  |
| `BM_Pipeline_Block/1/1/real_time` | 7.683 ms |  | 2.603e+06 |  | 1 |  |  |  |  |  | 309 | 0 | 1 | 8.736e+06 |  |  |
| `BM_Pipeline_Block/4/1/real_time` | 18.752 ms |  | 4.266e+06 |  | 1 |  |  |  |  |  | 929 | 0 | 4 | 8.522e+07 |  |  |
| `BM_Pipeline_Block/4/4/real_time` | 47.832 ms |  | 1.673e+06 |  | 4 |  |  |  |  |  | 335 | 0 | 4 | 3.562e+07 |  |  |
| `BM_Pipeline_Block/16/4/real_time` | 62.672 ms |  | 5.106e+06 |  | 4 |  |  |  |  |  | 4617 | 0 | 16 | 1.950e+09 |  |  |
| `BM_Pipeline_Block/16/16/real_time` | 79.668 ms |  | 4.017e+06 |  | 16 |  |  |  |  |  | 1515 | 0 | 16 | 1.053e+09 |  |  |
| `BM_TimelineSeek_EvictedColdWindow/real_time` | 5.871 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineReunfoldOneInterval/real_time` | 4.898 ms |  |  |  |  |  |  |  |  |  |  |  |  |  | 30 | 24000 |
| `BM_TimelineSeek_Resident/real_time` | 0.003 us |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `coderoast-ipc-core` — the shared-memory transport core

_3 benchmark(s)._

| benchmark | real_time | slots |
| --- | --- | --- |
| `BM_SharedMemoryPushPop/1024` | 68.065 ns | 1024 |
| `BM_SharedMemoryPushPop/8192` | 68.286 ns | 8192 |
| `BM_SharedMemoryPushPop/65536` | 71.35 ns | 65536 |
