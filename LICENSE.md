# License scope / Область лицензирования

This release candidate has **no blanket license**. Translation, tools and fonts have separate rights.
Этот релиз-кандидат не имеет общей лицензии на весь пакет. Нельзя считать лицензию кода/шрифта разрешением на оригинальную игру.

## Fonts — confirmed / Шрифты — подтверждено

The 11 LOFONT glyph additions are raster derivatives of Noto Sans 2.015.
Copyright 2022 The Noto Project Authors (https://github.com/notofonts/latin-greek-cyrillic).
They are provided under SIL Open Font License 1.1; the complete unchanged notice is
`mods/ru/licenses/NotoSans-OFL.txt` in installation ZIPs
(in the source tree: `package/mods/ru/licenses/NotoSans-OFL.txt`). Original game font packages are excluded.
Resource names such as Maiandra/Abc identify game routes; this does not grant rights to the game's typefaces.

## Russian text — legal review required / Русский текст — требуется правовая проверка

Russian edition: the Sanya1988 translation project and its contributors; final authorship/contributor permissions need maintainer confirmation.
The translation is derived from Lost Odyssey. No MIT, GPL, CC or other open license is assigned to its text here.
No written rightsholder authorization for this fan translation has been supplied or identified in the audited materials.
Rights in the original expression, stories, names and other game content remain with the relevant rightsholders.
No permission from Microsoft, Mistwalker, feelplus or FreeFrank is claimed. Possession of game discs alone does not establish translation-distribution rights.

Русская редакция связана с оригинальным произведением. Письменное разрешение правообладателей
на распространение перевода не подтверждено. Открытая лицензия переводчика или уведомление об ответственности
не устраняют права на оригинал. Публикация требует отдельного решения по правовому основанию и правам участников.

## New packaging tool and documentation / Новый инструмент упаковки и документация

`tools/release.py`, the CI definition and release documentation were newly prepared for this candidate.
They do not incorporate FreeFrank source or private converter code and use only Python's standard library.
Their public license is intentionally **pending owner approval**; no open grant is made in this candidate.
A narrowly scoped MIT license for these independently authored files is a proposed option, subject to ownership confirmation.
This pending choice does not change the separate OFL grant for the fonts.

## Gameplay screenshots — legal review required / Игровые кадры — требуется проверка

The four PNG files in `docs/screenshots/` are game-window crops supplied by the project owner.
They show Lost Odyssey rendered in official FreeFrank, not independently authored free artwork.
Their capture provenance and versions are recorded in [the screenshot guide](docs/screenshots/README.md).
Capture ownership does not establish permission to distribute the underlying game content.
No open license or rightsholder endorsement is assigned to these screenshots.
Public placement remains **LEGAL_REVIEW_REQUIRED / OWNER_APPROVAL_REQUIRED**.
The screenshots are repository documentation only and are excluded from both installation ZIPs.

Предоставление кадров владельцем разрешает локальную подготовку страницы, но не подтверждает права
на публичное распространение игровых изображений. Этот вопрос рассматривается отдельно от OFL-шрифтов,
собственного кода и производного текста перевода.

## External FreeFrank / Внешний FreeFrank

FreeFrank is a separate GPL-3.0-licensed program, obtained from its official repository.
No FreeFrank executable, GPL implementation, headers or compiled validation probes are distributed here.
Its GPL does not grant permission to distribute Lost Odyssey story text or artwork.
If GPL-derived tools are added later, their source/notices and applicable GPL obligations must be handled separately.
