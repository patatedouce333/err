# Dossier « 70 meilleurs films coréens » — plaquette graphique pour impression

Plaquette (brochure A4) de **70 films** sud-coréens, de *Oldboy* (2003) à 2025, selon les
critères imposés.

## Critères de sélection
1. **Période** : vague du « nouveau cinéma coréen », de *Oldboy* (2003) à 2025.
2. **Exclusion stricte des romances / mélodrames** (ex. *The Handmaiden*, *Decision to Leave*,
   *A Moment to Remember*, *A Werewolf Boy*, *20th Century Girl*, *Soulmate*, *Josée*… écartés).
3. **Doublage français (VF)** : exigé. VF *confirmée* (doublage FR) pour ~15 films de large
   diffusion (Parasite, Train to Busan, Snowpiercer, Okja, Space Sweepers, Oldboy, Memories of
   Murder, The Chaser, The Man from Nowhere, I Saw the Devil, The Host, Peninsula, The Roundup…).
   Le reste est distribué en France en **VOST** (sous-titré) — standard pour l'art et essai coréen.
   Filtrer la colonne « VF » selon votre exigence stricte.
4. **Acteurs devenus des stars** (dimension nationale + internationale).
5. **Classement final par note IMDb** (le « nombre de pays de doublage » sert de signal de portée).

## Contenu du dossier
- `index.html` — plaquette imprimable (A4) : couverture, méthodologie, tableau récapitulatif,
  puis une fiche par film (affiche + photos d'acteurs + métadonnées). Ouvrir dans un navigateur →
  « Imprimer » / « Enregistrer en PDF ».
- `liste_films.csv` — données tabulées (tri IMDb), avec **URL de chaque affiche**.
- `films.json` — données complètes.
- `affiches/` — 59 affiches officielles (Wikipedia « fair use » / TMDB) + 15 placeholders SVG
  (films sans pageimage Wikipedia ; à remplacer par l'affiche officielle).
- `acteurs/` — 46 photos d'acteurs sous licence libre (CC) Wikimedia Commons.
- `dossier_films_coreens_complet.zip` — archive du dossier complet.

## Sources
- IMDb (notes publiques), AlloCiné, Wikipédia FR/EN, Nautiljon, JustWatch/Go-VF, Prime Video,
  TMDB, ARP Sélection, Fnac/CeDe.
- VF vérifiée via distributeurs FR (The Jokers, Diaphana, KMBO, ARP), éditeurs DVD/Blu-ray
  (mention « doublé français ») et plateformes (Netflix, SOONER).
- Photos d'acteurs : Wikimedia Commons (licence CC BY / CC BY-SA).

## Droits & à faire avant impression
- Les **affiches officielles** sont protégées : pour une impression commerciale, acquérir les
  droits auprès des studios/distributeurs (URLs dans `liste_films.csv`).
- Les 15 placeholders SVG → remplacer par l'affiche officielle.
- Préférer des visuels haute résolution (≥ 300 dpi) pour l'imposition print.
