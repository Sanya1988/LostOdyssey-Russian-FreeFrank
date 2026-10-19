# Validate and package

Python 3.10+ standard library only; no game data is needed to validate this reviewed public data tree.

```sh
python -X utf8 -B tools/release.py validate
python -X utf8 -B tools/release.py package --output dist
```

ZIP entry order, timestamps and attributes are fixed. Identical inputs and the same Python/zlib version produce identical ZIPs.
Each ZIP is reopened and CRC/content checked. The source archive can be made from the release tag with `git archive v0.2.0-beta`.
This public tree contains reviewed JSON source data and a new packaging tool. It does not contain the private canonical
editorial corpus, development history, converter, game exports or build dependencies. It cannot independently regenerate
the translation from that private corpus. Source archive means this exact reviewed public tree, not the entire private toolchain.
Native four-disc/format testing and prior selective gameplay results are documented in the maintainer's audit;
the lightweight public CI is not a substitute for those tests or new gameplay testing.

## Website documentation and frozen installation documents

The root README files and `docs/screenshots/` are GitHub documentation. Screenshots have a separate
unresolved publication-rights status; they are not installation payload.
`release-docs/` preserves the six root-level documents embedded in the versioned v0.2.0-beta ZIPs,
for this release. The packager reads those snapshots rather than the GitHub page, so gallery changes
do not add images or broken gallery links to the installed pack and do not change the frozen ZIP hashes.
The bilingual INSTALL, FAQ and KNOWN_ISSUES files in `docs/` also remain included, unchanged.
Future critical installation-document changes need an explicit repack and updated checksums.
