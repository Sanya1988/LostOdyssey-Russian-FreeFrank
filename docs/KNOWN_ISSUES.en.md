# Known issues — v0.2.0 Beta

## Major limitations

- **Dreams:** the separate 34-story EXPERIMENTAL add-on retains severe overlap, broken wrapping/words and animation problems. Some pages are hard to read. The base ZIP uses original Dream fallback. Rejected geometry experiments, Reading Mode and Dream TimePitch API are excluded.
- **UI:** Type Info/Scroll (121/153), equipment Attack Speed (10221), long weapon/item names including the Magic Rifle of Aneira still have overflow problems. Compact statistics and headings are improved but not tested in every state.
- **Magic layout:** component-left names 102/121 (Поток жизни III / Слабость стихий) measure 191.7/211.5px against a 188px gap including a 2px guard. Approved Russian wording is retained with visual review still pending. Five names 156–160 use longer canonical full forms because their short forms contain the composite parser's colon delimiter.

## Incomplete coverage

- **Magic:** 152 of 153 nonblank native IDs now have Russian names. There are 152 distinct school/name-pool identities; IDs 110/132 share the Powera pool. These counts include auxiliary/alias records and are not a count of unique player-accessible spells or completion percentage. 64 of the previous 65 English full/short conflicts now receive Russian text. All-Stonus (45) remains English because its compact name collides with All-Stone (180), which has a different effect. All 50 native composite recipes have Russian results and both component columns. A shared stock key cannot supply a different full/short form for each screen.
- Existing duplicate Russian labels for Vanish/Lost belong to different schools; Powera IDs 110/132 share one native name pool. No new independent wording has been assigned.
- **Host UI:** six native TITLE labels are translated; Settings, first-run setup and some FreeFrank host UI remain English. Select **Russian** in Game language: the Cyrillic selector name is not supported by the stock v1.0.4 settings font. Game LOFONT does not patch that host font.
- **Save/load:** 15 native messages are added. Some profile notifications may be hidden by stock menu acceleration. Two Lv labels lack a separately reviewed mapping. Old save slots can retain an English location-name snapshot; saves are not rewritten.
- **XMB:** 387 keys fit; 550 further bindings remain deferred. Full coverage needs 74,141 bytes above the 65,536 pool limit; the selected pool uses 64,990 bytes. Some locations remain English.
- The observed main-battle **Special** consumer still lacks a proven binding. Similar text in other contexts is not substituted by dictionary matching.
- **Graphics excluded:** Perfect/Good/Bad, MISS/GUARD/DAMAGE GUARD/DELAY/DAMAGE UP, BATTLE-LOG and Loading. Native-derived ru-local-artwork is not distributed.
- Modified JSON can retain names, Latin text and original fragments; this is not a full English export or complete localization. Dream italics currently use upright Cyrillic; not every subtitle timing or late-game scene was checked individually.

The `%` skill-name issue was fixed in RU 0.5.1 and selectively owner-verified. TITLE labels were accepted, UI-FIT selectively accepted, and new magic approved for Beta. This is not a complete gameplay PASS: four-disc offline checks do not replace visual testing of every string.

Official FreeFrank v1.0.4 / Windows x64 is the tested version. v1.0.6 and newer versions may be compatible but still require separate runtime testing. This pack does not automatically update the game.
