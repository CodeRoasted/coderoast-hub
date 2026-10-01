# Corrections

## LogHub samples and the canon showcase — withdrawn

**Ruling:** Founder, Emmanuel Prunet, 2026-10-01

**What was published.** From 2026-07-09, `samples/loghub/samples/` held 16 `*_2k.log` files from the
LogHub collection (LOGPAI): logpai/loghub's own sample files, at its commit
`dd61d0952749ee7963bde24220d1be5ede023033`, with the carriage return of every CRLF line end stripped
in 15 of the 16. From 2026-07-10, `showcase/canon/` held canon's rendering over them
(`loghub.canon.txt`), beside two renderings over our synthetic samples.

**Why they are withdrawn.** They were labelled CC-BY-4.0, as members of Zenodo record `8196385`.
They are not: the record holds only full logs, and logpai/loghub's files are under its own notice
(free for research or academic work, on condition that any use or distribution refers to
https://github.com/logpai/loghub, cites the loghub paper and includes the notice), which these
copies did not carry. And CodeRoast now publishes only its own logs: logs our own instruments
generate, and logs of our own systems. No third-party log byte, excerpt or rendering stays here.

**What remains.** Git history is not rewritten. The files remain in this repository's history and
in its tags `v1.7.6` to `v1.10.5`, each of which also carries the disclosure signed on 2026-08-21.
That disclosure's licence and byte-identity statements are wrong for the reasons above; its
identifying-content classes and counts were measured on the bytes it described.
