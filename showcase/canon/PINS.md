# Pins — what a re-run needs to reproduce these bytes

These renders are deterministic **for a fixed tool and fixed inputs**. That is narrower than
"deterministic", and the difference is the reason this file exists: the same tool over the
same-named inputs has already produced different bytes at two different acts. If you re-run
and your class set differs from the one declared beside these artifacts, check these pins
first — you are almost certainly not holding the same inputs or the same build.

## Tool

- `det_proof` sha256: `a2c2e0f65a0d283f0c8321db0ba0e2aefcc3eb2094d5d01079b23ef0db032bb1`
- canon ruleset: `semantic_identity d5175c869368cab9ad28804e4ad0d8ce`
- canon packages: github@1.4.0 gitlab@1.0.0 jenkins@1.1.0 test_frameworks@1.0.0

## Inputs

- source repository commit: `ef2f2a12efe2e0873fc9faafdf78d285328ff498`

Per corpus, the SHA-256 of every input log actually read by this run, in the order it was
read. A corpus anchor is the SHA-256 of that list, so one line identifies the whole input set.

### `loghub` — 16 log(s)

```
15734be6ee4bcfca99c7788774d17d97d652ab2852135688ef63125cbf4ce5f0  ./Android_2k.log
0e51c532c9b82b49234f5691ed96d7b584eaeef9f35839b9c365769a80294705  ./Apache_2k.log
5adca4dadb7cf162bf220e4f0605faa2fdcfd8645c7547d2cf312dac3d42fee7  ./BGL_2k.log
6fe25449e79d75e35bb223ead9729fa02c00b7abb23e4e8ec0f3bb2addec6e3a  ./HDFS_2k.log
531ff6f67fc9c1228f1f004e3a1b529f395cca8bae5d3b36a2cb5beb226d2386  ./HPC_2k.log
dc0e343fc230bce6fd8be4c0cbb05cfaecdaf5fdcf88e029b584f0346fb60312  ./Hadoop_2k.log
205728b6583de25cf9d9a9fd15366591a6b79b634679cd04ec8e6531127e6d06  ./HealthApp_2k.log
6d50cefa82380651f910df35fda0995a237a3c788b7b2e3d2d37e51fb9debca9  ./Linux_2k.log
46944eb852979f1c6311742cd53e8a0abd19f7583e35c9f5eabe37470ca58fc1  ./Mac_2k.log
16da02f37eb00cec9ec65c4d71175897be45b266aa7d6e01b26186678e2288b8  ./OpenSSH_2k.log
6ea7e03648d7bd6231cae427cb509073a9fbc71f49ded5301673495902edab17  ./OpenStack_2k.log
94b6a9d98d76e7ad7841ed10caa463cd4e638a229b92a220a2bf1707552adbb9  ./Proxifier_2k.log
87e9715f97f193135d807226b0949c129035df0842cc141f48332fa712eaf81b  ./Spark_2k.log
e92e8a6af2a545067ea34b5cd97c05eb27c8274053f7fc22e34c15dc80309bb0  ./Thunderbird_2k.log
2f7677ba753b9af3abf5cbaa7279c133120544cddb9d09d6700a044c886e114e  ./Windows_2k.log
ca38c8b373c693760a86dea60ad73ea69cee2c260576f8bb329a1b1e068c2949  ./Zookeeper_2k.log
```

corpus anchor: `baa12921c7e72d00415c3403ceba2211593fa12c3fd9246cc1f87f2fb15a6967`

### `marker_corpus` — 5 log(s)

```
bd5cec93febdc8943a7506c0ecb39e32dbf00ba446d74cb8373d5a91fa68980d  ./logs/acme__widget__PR-7__build11.log
6a7b44cad236d8cec6ce0270916beb2b01e777cbc9a3335730ed7881518d58e5  ./logs/acme__widget__main__build42.log
3f7f8df95cf9bb5946e7ec2d802db06167e0824800c970f9936ecd09fdf082c6  ./logs/demo__engine__main__build205.log
9c79e02229215e0b1c862013b1f2ee25da91e9a1219b15fb1d9bb611240e33f7  ./logs/demo__toolkit__master__build88.log
106adc25f010b378b555e9264e748d74c827b7ba689738c0c4eafabc57274bcc  ./logs/sample__service__build513.log
```

corpus anchor: `dbd7c0028f0174de268d58faf9dc5b9490984d6b54f98c31ee88c833a1282018`

### `revert_corpus` — 10 log(s)

```
73bf1631d3c2dd4388b7f71e1ba9d6418eaa92ce4068ee6e0a3f8bf3c7b1f9b6  ./log_annotated/acme__widget__pr101__run900000101.log
5b5fd5de022838e70b3393b998a7258ab4f1d220d717255c05bb8cb07ea61f91  ./log_annotated/acme__widget__pr102__run900000102.log
a338811bd0c098e03e1d6d9b1b3af7710086a97cf153fc8a4e2a13712ecc62be  ./log_annotated/demo__toolkit__pr55__run900000055.log
5c0263d50b154d65ab55b7b6d3cc375e3f2e59d312170fc3a700cfa10da34349  ./log_annotated/demo__toolkit__pr56__run900000056.log
a03cbb758517df63f4435296d4cb3c60e7da839a011d30ea33596db4ba3d2ff1  ./log_annotated/sample__service__pr7__run900000007.log
f825978bbc3887457f3f3b3f0960a63be96b9ff4583fa630c0da9d41f5f676bb  ./log_stripped/acme__widget__pr101__run900000101.log
af8e33481f9b400948f290144e5a05fde7d69f79f76311e6d2234b3cef7a11c1  ./log_stripped/acme__widget__pr102__run900000102.log
b16f98f0b0038d19fe6efa0897fd331e6ba7407b5464d6e492b636f83316087b  ./log_stripped/demo__toolkit__pr55__run900000055.log
030e520780d66368a1e3ccaf7d1c71e9c6746e23a93a3e0a5179cc8b0529d155  ./log_stripped/demo__toolkit__pr56__run900000056.log
33481126946a21f65b6c2628b36752e2fac84db7559929ea2a24a256b339ed80  ./log_stripped/sample__service__pr7__run900000007.log
```

corpus anchor: `825bca7a6ff149f08abc29cb545c965b02555ebb3e5c54280ba1890f713f68c7`
