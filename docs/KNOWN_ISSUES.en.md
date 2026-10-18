# Known issues

## Major limitations

- **DREAM_LAYOUT_POLISH_REQUIRED:** the optional 34-Dream add-on has confirmed overlapping fragments,
  broken wrapping/words and animation limitations. Some pages can be hard to read.
  Stock `.x/.y/.w/.h/.scale` cannot reproduce every per-character effect. The default ZIP uses original Dream fallback.
  No layout fix is claimed; all canonical Russian Dream text remains preserved.
- **UI layout:** MenuDat 121/153 labels and 10221 have confirmed overlaps. Heading 3045, value 21037 and other long strings
  need visual checks. Global metrics and the executable are unchanged; compact stats are not checked for every value combination.

## Incomplete coverage and cosmetic issues

- **Magic full/short:** 69 conflicting spell IDs have different canonical full/short names but one shared stock key.
  Some names therefore remain English; other context-dependent exceptions are retained.
- **XMB:** 387 keys fit; 550 further bindings are deferred. Full coverage needs a 74,141-byte pool, above the 65,536 limit;
  the selected pool is 64,990 bytes. Some locations remain English.
- Old saves can retain an English location-name snapshot in save/load. The pack does not rewrite save files.
- **HOST_UI_UNTRANSLATED:** Press Start, New Game, first-run setup and language-selection host UI still need canonical wording.
  The Russian language option does not imply that its host menu is translated.
- The observed main-battle `Special` label still lacks a proven consumer binding.
- **Graphics excluded:** Perfect/Good/Bad, MISS/GUARD/DAMAGE GUARD/DELAY/DAMAGE UP, BATTLE-LOG and Loading.
  Native-derived atlases are not distributed; a stock Loading replacement route is not proven.
- Modified JSON may retain names, Latin text and original fragments. This is not a complete original export or complete localization.
- Dream italics currently use upright Cyrillic. Not every subtitle timing or late-game scene was individually checked.

Missing skill names containing `%` were fixed in RU 0.5.1 and selectively owner-verified;
this is not a claim to fix every possible blank label. Automated format PASS is not complete gameplay PASS.

## Language name in settings

Select **Russian** in Game language. The Cyrillic name renders as question marks in official v1.0.4 because its host UI font lacks Cyrillic and does not use game LOFONT additions. This is a settings-font limitation; pack ID `ru`, base `int` and Russian game text are unchanged.
