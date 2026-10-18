# Installation — Windows x64 / FreeFrank

This language pack is intended for the official LostOdysseyRecomp from FreeFrank (Windows x64). It has been tested on v1.0.4. Newer versions may be compatible but have not yet been tested. FreeFrank updates may require the language pack to be adapted.

1. Obtain official [FreeFrank for Windows x64](https://github.com/freefrank/LostOdysseyRecomp/releases/latest).
2. Prepare your own original game data using FreeFrank's instructions. No discs or copying rights are supplied here.
   Confirm the game works before adding the language pack.
3. Close the game. If `mods/ru` already exists, move the **entire folder outside `mods`** as a backup.
   Do not merge the default pack with an older pack: leftover Dream files would keep experimental overrides active.
   Do not leave another `language.ini` with `id=ru` in a second folder under `mods`.
4. Extract `LostOdyssey-Russian-Language-Pack-v0.1.0-beta.zip` into the folder containing `LostOdysseyRecomp.exe`.
   The resulting paths must be `mods/ru/language.ini`, `mods/ru/text`, `mods/ru/fonts`, `mods/ru/licenses`.
   Avoid `mods/mods` or an extra archive-name directory.
5. Start the game, open **Settings → System → Game language**, select **Русский**, and save the setting.
6. Fully restart the game so its added glyphs are loaded.
7. Load an existing save. Installing a language does not require moving or overwriting saves or achievements.

The default package uses original Dream fallback. The optional 34-Dream EXPERIMENTAL archive is an add-on for the
same base version, extracted into the same game folder. It has serious known layout problems and is not standalone.
Read `EXPERIMENTAL_DREAMS.md` in that archive.

If Russian is missing, check `mods/ru/language.ini`, duplicate IDs and restart.
If English text remains, check KNOWN_ISSUES; do not replace unrelated game files.
Uninstall with the game closed: move `mods/ru` outside `mods`, choose another language and restart.
To disable experimental Dreams, replace the **entire** folder with the clean default pack.
The pack does not change the save format. New-ZIP installation is validated offline, not by a complete gameplay run.
