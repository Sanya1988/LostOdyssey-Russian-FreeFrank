# Lost Odyssey — Russian Language Pack

**Unofficial Russian text translation for [FreeFrank LostOdysseyRecomp](https://github.com/freefrank/LostOdysseyRecomp).**

**v0.1.0 Beta | Windows x64**

This language pack is intended for the official LostOdysseyRecomp from FreeFrank (Windows x64). It has been tested on v1.0.4. Newer versions may be compatible but have not yet been tested. FreeFrank updates may require the language pack to be adapted.

Translation is in development. No original game or modified EXE is included. Gameplay checks were selective;
no complete playthrough or review of every string is claimed. **All 34 Russian Dreams are a separate experimental add-on.**

[Русская главная страница](README.md) · [Full installation guide](docs/INSTALL.en.md) · [FAQ](docs/FAQ.en.md)

## Download

**The release is not published yet.** After publication, use this project's GitHub Releases:

| File | Purpose |
| --- | --- |
| **`LostOdyssey-Russian-Language-Pack-v0.1.0-beta.zip`** | **Start here:** the ready-to-install main pack, which works without the Dream add-on. |
| `LostOdyssey-Russian-Dreams-v0.1.0-beta-EXPERIMENTAL.zip` | Optional 34-Dream add-on for the same base version. Serious layout issues remain. |
| `SHA256SUMS.txt` | Checksums for both installation ZIPs. |

GitHub's **Source code** and **Code → Download ZIP** are repository snapshots, not the installation ZIP.
The [Russian main page](README.md#скачать--download) records the planned release/asset addresses for verification after publication.

## Quick start

Installation is ZIP extraction; compilation is not required.

1. Get official **[FreeFrank for Windows x64](https://github.com/freefrank/LostOdysseyRecomp/releases/latest)**.
2. Set it up with your own original Lost Odyssey game data, following FreeFrank's instructions. Confirm the game starts.
3. Close the game. Move any existing **entire `mods/ru` folder outside `mods`** as a backup. Do not merge old and new base packs.
4. Once published, download **`LostOdyssey-Russian-Language-Pack-v0.1.0-beta.zip`** from this project's Releases.
5. Extract it into the folder containing **`LostOdysseyRecomp.exe`**, keeping the archive's directory structure.
6. Confirm **`mods/ru/language.ini`** exists. Avoid `mods/mods/ru` or an extra archive-name folder.
7. Start FreeFrank → **Settings → System → Game language → Russian**.
8. Choose **Save settings**, fully restart the game, then load your save.

The selector label is **Russian** (pack ID `ru`). This ASCII label avoids the missing Cyrillic glyphs in the v1.0.4 settings-menu font; in-game text remains Russian.

Choose **Game language**; **Settings language** controls FreeFrank's own settings UI.
If Russian is missing, check the path, duplicate `id=ru` packs inside `mods`, the target version and restart.
Installing this pack does not require moving or overwriting saves or achievements.

### Optional Russian Dreams

Close the game and extract **`LostOdyssey-Russian-Dreams-v0.1.0-beta-EXPERIMENTAL.zip`** into the same EXE folder,
merging `mods/ru` with the installed base pack of the same version. Restart afterward.
All 34 stories have Russian text, but **severe overlaps, bad wrapping, broken words and animation/presentation issues** remain.
Some pages are difficult to read. The main ZIP keeps the original Dream fallback and works independently.

### Removal

Close the game and move only this pack's **`mods/ru` outside `mods`**. Select another available game language and restart.
Restore your previous `ru` backup if applicable. Keep saves, achievements, other mods and original game files.

To remove **only experimental Dreams**, move the entire current `mods/ru` outside `mods`, then extract a fresh base ZIP.
Overlaying base files alone cannot delete leftover Dream overrides.

## Coverage and limitations

Russian dialogue and story subtitles; main in-game menus and some system messages; items/descriptions;
supported spell names and skills; combat messages/actions; selected locations and tutorials; Cyrillic glyph additions.
No Russian voice-over or graphical replacement mod is included.

The existing **RU 0.5.1** translation is the source. The base pack has **27,951 JSON keys / 536 text resources / 11 LOFONT**.
The optional 34 Dreams add 7,802 keys; combined scope is 35,753 keys / 570 resources.
Nine opening-story captions are separate and stay in the base. Counts are not a completion percentage.

The owner selectively checked launch/save loading, `%` skill names, dialogue/subtitles, items, some magic,
actions, locations and sampled Dreams on v1.0.4. Format checks covered all four discs.
Other versions/platforms require separate testing.

- Long UI labels may overlap or overflow.
- Some spells remain English because canonical full/short names conflict.
- XMB string-pool limits leave some locations untranslated.
- Old save slots can retain stored English location names.
- Startup/first-run/settings host UI remains partly English.
- Original combat artwork and Loading graphics are not replaced.
- Optional Dreams have serious layout problems, described above.

Missing skill names containing `%` were **fixed in RU 0.5.1** and selectively verified by the owner;
this does not claim to fix every possible blank label.

[Full known issues](docs/KNOWN_ISSUES.en.md) · [Release notes](RELEASE_NOTES.md) · [Screenshot gallery](README.md#скриншоты).
The gallery has three v1.0.4 captures and one earlier **v1.0.0** dialogue capture, which is not v1.0.4 validation.
Visible UI overflow is acknowledged in its captions.

## Reporting issues

After publication, use this project's Issues. Until then, send findings to the maintainer.
Include FreeFrank/pack versions, disc, location, screen, nearby text and reproduction steps.
Redact personal information from evidence; do not upload game files, saves, tokens or full dumps.

## Credits and rights

Russian language pack author: **Sanya1988**. This credits the Russian edition and language pack, not the original Lost Odyssey.
FreeFrank and its contributors created the separate LostOdysseyRecomp port;
thanks for its stock language-pack system. Their endorsement of this translation is not claimed.
Lost Odyssey and its game content belong to the respective rightsholders; Microsoft is the publisher,
Mistwalker / feelplus are developers. This fan project has no official affiliation with them.

Noto Sans additions retain SIL OFL 1.1. The owner-supplied screenshots depict copyrighted game content;
capture ownership does not establish permission to publish it. No blanket open license is assigned to text or images.
**Publication: OWNER_APPROVAL_REQUIRED. Derivative translation and screenshot rights: LEGAL_REVIEW_REQUIRED.**
Notices do not replace rightsholder permission.

[License scope](LICENSE.md) · [Third-party notices](THIRD_PARTY_NOTICES.md) · [Screenshot provenance](docs/screenshots/README.md).
