# Known issues — v0.3.0 Beta

## Major limitations

- **Dreams:** the separate 34-story EXPERIMENTAL add-on retains severe overlap, broken wrapping/words and animation problems. Some pages are hard to read. The base ZIP uses original Dream fallback. Rejected geometry experiments, Reading Mode and Dream TimePitch API are excluded.
- **UI:** v0.3.0 includes accepted long-name, Attack Speed, Type/Scroll, filter/sort and skill-slot fixes. Other states and screens may still overflow; complete visual verification is not claimed.
- **Magic layout:** accepted compact names for IDs 102/121/156–160 and ten further spell names are included, with full descriptions retained. Not every screen was checked.

## Incomplete coverage

- **Magic:** 152 of 153 nonblank native IDs now have Russian names. There are 152 distinct school/name-pool identities; IDs 110/132 share the Powera pool. These counts include auxiliary/alias records and are not a count of unique player-accessible spells or completion percentage. 64 of the previous 65 English full/short conflicts now receive Russian text. All-Stonus (45) remains English because its compact name collides with All-Stone (180), which has a different effect. All 50 native composite recipes have Russian results and both component columns. A shared stock key cannot supply a different full/short form for each screen.
- Existing duplicate Russian labels for Vanish/Lost belong to different schools; Powera IDs 110/132 share one native name pool. No new independent wording has been assigned.
- **Host UI:** six native TITLE labels are translated; Settings, first-run setup and some FreeFrank host UI remain English. Select **Russian** in Game language: the Cyrillic selector name is not supported by the stock v1.0.4 settings font. Game LOFONT does not patch that host font.
- **Save/load:** 15 native messages are added. Some profile notifications may be hidden by stock menu acceleration. Two Lv labels lack a separately reviewed mapping. Old save slots can retain an English location-name snapshot; saves are not rewritten.
- **XMB:** 398 keys are delivered; 539 further bindings remain deferred because of the 16-bit string pool. Some locations stay English; existing save snapshots are not rewritten.
- The observed main-battle **Special** consumer still lacks a proven binding. Similar text in other contexts is not substituted by dictionary matching.
- **Graphics excluded:** Perfect/Good/Bad, MISS/GUARD/DAMAGE GUARD/DELAY/DAMAGE UP, BATTLE-LOG and Loading. Native-derived ru-local-artwork is not distributed.
- Modified JSON can retain names, Latin text and original fragments; this is not a full English export or complete localization. Dream italics currently use upright Cyrillic; not every subtitle timing or late-game scene was checked individually.

The `%` skill-name issue was fixed in RU 0.5.1 and selectively owner-verified. TITLE labels were accepted, UI-FIT selectively accepted, and new magic approved for Beta. This is not a complete gameplay PASS: four-disc offline checks do not replace visual testing of every string.

This language pack is intended for the official LostOdysseyRecomp from FreeFrank (Windows x64). Tested in-game with the official FreeFrank v1.0.6 on Windows x64, based on selective verification by the project owner. A complete playthrough and verification of every translated string are not claimed. Newer versions have not yet been tested and may require the language pack to be adapted.

Enemy-name audit covers all 1,024 native slots: 511 name entries include 171 canonical "Monster NNN" placeholders. Not every slot is claimed to appear in gameplay; report a placeholder with its location if encountered.
