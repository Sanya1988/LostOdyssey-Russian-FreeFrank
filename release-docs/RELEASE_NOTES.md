# v0.2.0-beta — Release Notes / Примечания к выпуску

## Русский

Автор русификатора: **Sanya1988**. Неофициальный data-only language pack для официального LostOdysseyRecomp от FreeFrank / Windows x64. Проверена работа на v1.0.4; v1.0.6 и более новые сборки пока требуют отдельного runtime-теста. Спасибо FreeFrank и участникам его проекта за порт и поддержку language packs; их одобрение перевода не заявляется.

- 64 дополнительных русских названия магии и 15 native сообщений загрузки/сохранения, хранилища и профиля.
- Шесть принятых TITLE-подписей, UI-FIT-01/02, компактные характеристики и заголовки «Заклинания», «Ур.», «Вр.».
- Сохранены диалоги, субтитры, предметы, навыки с `%`, боевые команды, локации и действия из RU 0.5.1.
- Основной пакет: **28 040 ключей / 536 текстовых ресурсов / 12 LOFONT**; 34 сна — отдельное EXPERIMENTAL дополнение, **7 802 ключа / 34 ресурса**. Вместе 35 842 ключа / 570 ресурсов. Количество ключей не означает процент готовности.
- Native таблица содержит 153 непустых magic ID, из них 152 имеют русский текст. Все 50 составных рецептов получают русский результат и обе колонки компонентов; эти контексты не считаются отдельными заклинаниями.

В Settings → System → Game language выбирайте **Russian**, сохраните настройки и полностью перезапустите игру. Для обновления сначала перенесите старую `mods/ru` за пределы `mods`, затем установите чистый основной ZIP. Сны ставятся отдельно поверх пакета той же версии. Для их удаления полностью замените `mods/ru` чистым основным пакетом; не удаляйте сохранения или достижения.

**Ограничения:** All-Stonus остаётся английским; некоторые длинные имена и UI-поля переполняются. «Поток жизни III», «Слабость стихий» и пять длинных составных имён требуют особого внимания. Host UI не полностью переведён; XMB ограничивает часть локаций. В экспериментальных снах серьёзные наложения и проблемы анимации не исправлены. Неудачные новые geometry, Reading Mode, engine patches, EXE/DLL и графический мод не включены. Новая магия утверждена для Beta, но визуально проверены не все контексты. Полного прохождения нет.

Оригинальная игра не входит. Письменное разрешение правообладателей на производный текст и изображения не заявляется; LEGAL_REVIEW_REQUIRED сохраняется. Noto Sans additions — SIL OFL 1.1; см. LICENSE.md и THIRD_PARTY_NOTICES.md.

## English

Russian language pack author: **Sanya1988**. Unofficial data-only localization for official FreeFrank LostOdysseyRecomp / Windows x64. Tested with v1.0.4; v1.0.6 and later still need separate runtime testing. Thanks to FreeFrank and its contributors for the port and language-pack support; their endorsement is not claimed.

- 64 additional Russian spell names and 15 native save/load, storage and profile messages.
- Six accepted TITLE labels, UI-FIT-01/02, compact statistics and headings; dialogue, subtitles, items, `%` skill-name fixes, combat commands, locations and actions are retained.
- Base: **28,040 keys / 536 text resources / 12 LOFONT**. Optional 34-Dream EXPERIMENTAL add-on: **7,802 keys / 34 resources**. Combined: 35,842 keys / 570 resources, not a completion percentage.
- 152 of 153 nonblank native magic IDs have Russian names, including auxiliary/alias records. All 50 composite recipes use Russian results and both ingredient columns; contextual occurrences are not additional spells.

Close the game, move the entire old `mods/ru` outside `mods`, then extract the base ZIP beside the FreeFrank EXE. Select **Settings → System → Game language → Russian**, save and fully restart. Install optional Dreams over the same base version. To remove Dreams, replace the entire `mods/ru` with a clean base; keep saves/achievements.

**Limitations:** All-Stonus remains English. Long names/UI fields can overflow, especially IDs 102/121 and five longer composite names. Host UI and XMB coverage remain incomplete. Optional Dreams retain serious overlap and animation problems. Rejected geometry experiments, Reading Mode, engine patches, EXE/DLL and artwork mods are excluded. New magic is approved for Beta, not visually tested in every context; no full playthrough is claimed.

Original game data is not included. Written rightsholder authorization for derivative text or depicted game content is not claimed; LEGAL_REVIEW_REQUIRED remains. Noto additions retain SIL OFL 1.1. See LICENSE.md and THIRD_PARTY_NOTICES.md.

---

# v0.1.0-beta — Release Notes / Примечания к выпуску

## Русский

Первая публичная Beta существующего русского перевода.

Русификатор предназначен для официального LostOdysseyRecomp от FreeFrank (Windows x64). Проверена работа на версии v1.0.4. Более новые версии могут быть совместимы, но пока не проверены. Обновления FreeFrank могут потребовать адаптации русификатора.

Автор русификатора: **Sanya1988**. Спасибо FreeFrank и участникам его проекта за порт и поддержку language packs.

В Settings → System → Game language выбирайте **Russian**. Имя латиницей обходит отсутствие кириллицы в шрифте настроек v1.0.4; игровой перевод и `id=ru` прежние.
Data-only: штатные `language.ini`, JSON и LOFONT; замена EXE, DLL и игровых архивов не требуется.
Основной пакет: 27 951 ключ / 536 ресурсов / 11 LOFONT. Диалоги, субтитры, игровые меню,
предметы, бесконфликтная магия, навыки с исправленным `%`, действия, часть локаций и обучение.
Опционально: 34 русских сна, 7 802 ключа; вместе 35 753 ключа / 570 ресурсов.
Из-за серьёзных проблем layout экспериментальные сны отключены в основном ZIP.
Есть английские названия/host UI, ограничения XMB и переполнения; см. KNOWN_ISSUES.
Графические производные, диски, исполняемые файлы, сохранения и приватная Git-история исключены.
Прежняя игровая проверка выборочная. Новый ZIP проверен автоматически/offline; 100% перевод и полное прохождение не заявляются.
Правовой риск производного перевода сохраняется: письменное разрешение правообладателей оригинала не подтверждено.

## English

First public Beta of the existing Russian translation.

This language pack is intended for the official LostOdysseyRecomp from FreeFrank (Windows x64). It has been tested on v1.0.4. Newer versions may be compatible but have not yet been tested. FreeFrank updates may require the language pack to be adapted.

Russian language pack author: **Sanya1988**. Thanks to FreeFrank and its project contributors for the port and language-pack support.

Choose **Russian** in Settings → System → Game language. The ASCII label avoids missing Cyrillic glyphs in the v1.0.4 settings font; translated game text and `id=ru` are unchanged.
Data only: stock `language.ini`, JSON and LOFONT. No EXE, DLL or game archive replacement.
Default: 27,951 keys / 536 resources / 11 LOFONT; dialogue, subtitles, in-game menus,
items, supported magic, corrected `%` skill names, actions, selected locations and tutorials.
Optional: 34 Russian Dreams / 7,802 keys; combined 35,753 keys / 570 resources.
Serious Dream layout issues keep these overrides out of the default ZIP.
English names/host UI, XMB limits and UI overflow remain; see KNOWN_ISSUES.
Native-derived artwork, discs, executables, saves and private Git history are excluded.
Prior gameplay checks were selective. The new ZIP is validated automatically/offline; no complete localization or playthrough is claimed.
The derivative translation has unresolved rights: written authorization from the original rightsholders has not been established.

## Repository gallery / Галерея репозитория

The GitHub README now includes four owner-supplied gameplay screenshots: three from FreeFrank v1.0.4
and one earlier v1.0.0 dialogue capture. They are documentation only, excluded from the unchanged
installation ZIPs. Rights to distribute the depicted game content have not been established.
Галерея не означает полного игрового PASS или подтверждённых прав на публичное размещение кадров.
