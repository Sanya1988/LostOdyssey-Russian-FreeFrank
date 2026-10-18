# Validate and package

Python 3.10+ standard library only; no game data is needed to validate this reviewed public data tree.

```sh
python -X utf8 -B tools/release.py validate
python -X utf8 -B tools/release.py package --output dist
```

ZIP entry order, timestamps and attributes are fixed. Identical inputs and the same Python/zlib version produce identical ZIPs.
Each ZIP is reopened and CRC/content checked. The source archive can be made from the clean root commit with `git archive`.
This public tree contains reviewed JSON source data and a new packaging tool. It does not contain the private canonical
editorial corpus, development history, converter, game exports or build dependencies. It cannot independently regenerate
the translation from that private corpus. Source archive means this exact reviewed public tree, not the entire private toolchain.
Native four-disc/format testing and prior selective gameplay results are documented in the maintainer's audit;
the lightweight public CI is not a substitute for those tests or new gameplay testing.
