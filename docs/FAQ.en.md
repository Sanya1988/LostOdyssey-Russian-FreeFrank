# Frequently asked questions

## Which file should I download?

Install `LostOdyssey-Russian-Language-Pack-v0.1.0-beta.zip` from the GitHub Pre-release.
GitHub's automatic Source code archive is a repository snapshot, not the ready-to-install package.
Obtain official [FreeFrank for Windows x64](https://github.com/freefrank/LostOdysseyRecomp/releases/latest) and your own original Lost Odyssey data separately.

This language pack is intended for the official LostOdysseyRecomp from FreeFrank (Windows x64). It has been tested on v1.0.4. Newer versions may be compatible but have not yet been tested. FreeFrank updates may require the language pack to be adapted.

## Where do I extract it, and how do I select Russian?

Extract into the folder containing `LostOdysseyRecomp.exe`, producing `mods/ru/language.ini`.
All archive entries are under `mods/ru`; avoid `mods/mods` or an extra archive-name folder.
Move any old `mods/ru` outside `mods` first. Then select Settings → System → Game language → Русский,
save and fully restart. Startup/first-run host UI remains partly English.

## Can I use existing saves?

Yes. Load your existing save. The language pack does not change save format/location or achievements.
An old location-name snapshot in a save can remain English.

## What about Dreams?

All 34 stories have translated text, but severe layout problems keep them out of the main ZIP.
The separate EXPERIMENTAL Dream ZIP requires the same base version. Overlaps, wrapping/word breaks and
animation/presentation issues remain. Optional add-on sources are also present in the repository;
source downloads do not replace the installation ZIP.

## How do I remove the add-on or the whole translation?

Close the game and move the entire `mods/ru` outside `mods`.
To remove only experimental Dreams, extract a fresh base ZIP; all base translations return and Dream overrides disappear.
Do not overlay base files onto the add-on: that cannot remove leftover Dream files.
To uninstall everything, leave ru removed, choose another available language and restart.
Do not delete saves, achievements or engine files.

## Why is some text still English?

Magic full/short conflicts, XMB pool limits, an unresolved Special consumer and some UI overflow remain.
See KNOWN_ISSUES. Blank skill names containing `%` were fixed in RU 0.5.1; that old issue is not claimed as an unfixed general Beta problem.

## Does this include an EXE, voices, textures or the game?

No. It is language.ini, JSON, LOFONT and documentation. Native-derived ru-local-artwork is excluded.
Other FreeFrank versions/platforms require separate tests. Existing gameplay checks were selective, not a full playthrough.

## Reporting and licensing

Use this project's Issues after publication: include versions, disc/location, exact screen and reproduction steps.
Redact personal data from any evidence. Do not upload game files, saves, tokens or complete dumps.
Noto additions retain SIL OFL 1.1. Translation/tooling rights are separate. Russian language pack author: **Sanya1988**. Authorization from the original rightsholders to distribute
the derivative text remains LEGAL_REVIEW_REQUIRED. A disclaimer does not clear them. See LICENSE.md.
