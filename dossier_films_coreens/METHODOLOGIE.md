# Dossier « Les meilleurs films coréens » — plaquette graphique pour impression

Constitution d'une plaquette (brochure A4) présentant une sélection des meilleurs films
sud-coréens, de *Oldboy* (2003) à aujourd'hui, selon 3 critères imposés.

## Critères de sélection (imposés)
1. **Période** : vague du « nouveau cinéma coréen », de *Oldboy* (2003) à 2025.
2. **Exclusion stricte des romances / mélodrames.** Films écartés pour ce motif :
   *The Handmaiden*, *Decision to Leave*, *A Moment to Remember*, *A Werewolf Boy*,
   *20th Century Girl*, *Be with You*, etc.
3. **VF obligatoire (doublage français).** Si le film n'est disponible qu'en VOST, il est
   écarté (ou signalé « à confirmer »). Le **nombre de pays de doublage** sert de signal de
   portée internationale (plus un film est doublé dans le monde, plus il a de chances d'avoir
   une VF et d'être porté par des stars).
4. **Acteurs devenus des stars** (dimension nationale + internationale).
5. **Classement final par note IMDb.**

## Contenu du dossier
- `index.html` — plaquette imprimable (A4) : couverture, méthodologie, tableau récapitulatif,
  puis une double-page par film (affiche + photos d'acteurs + fiche). Ouvrir dans un
  navigateur → « Imprimer » / « Enregistrer en PDF ».
- `liste_films.csv` — données tabulaires (tri IMDb).
- `films.json` — même données en JSON (pour automatisation).
- `affiches/` — **placeholders SVG** par film (les affiches officielles sont protégées par
  le droit d'auteur et ne peuvent être redistribuées ; les remplacer avant impression).
- `acteurs/` — **photos d'acteurs sous licence libre (CC)** issues de Wikimedia Commons.

## Sélection finale (tri par note IMDb)
| # | Film | Année | IMDb | VF | Réalisateur |
|---|------|-------|------|----|-------------|
| 1 | Parasite | 2019 | 8.5 | Confirmée | Bong Joon-ho |
| 2 | Oldboy | 2003 | 8.3 | DVD/Blu-ray VF | Park Chan-wook |
| 3 | Memories of Murder | 2003 | 8.1 | Confirmée | Bong Joon-ho |
| 4 | The Chaser | 2008 | 8.0 | Confirmée | Na Hong-jin |
| 5 | The Man from Nowhere | 2010 | 7.7 | Confirmée | Lee Jeong-beom |
| 6 | I Saw the Devil | 2010 | 7.7 | À confirmer | Kim Jee-woon |
| 7 | Train to Busan | 2016 | 7.6 | Confirmée | Yeon Sang-ho |
| 8 | Okja | 2017 | 7.3 | Confirmée (Netflix) | Bong Joon-ho |
| 9 | Snowpiercer | 2013 | 7.1 | Confirmée | Bong Joon-ho |
| 10 | The Host | 2006 | 7.1 | À confirmer | Bong Joon-ho |
| 11 | Space Sweepers | 2021 | 6.6 | Confirmée (Netflix) | Jo Sung-hee |
| 12 | Peninsula | 2020 | 5.6 | Confirmée | Yeon Sang-ho |

## Sources
- IMDb (notes publiques), AlloCiné, Wikipédia FR, SOONER, Nautiljon, Prime Video,
  Paris Match (« Parasite débarque en VF »).
- VF vérifiée via distributeurs FR (The Jokers, Diaphana, KMBO), éditeurs
  DVD/Blu-ray (mention « doublé français ») et plateformes (Netflix, SOONER).
- Photos d'acteurs : Wikimedia Commons (licence CC BY / CC BY-SA).

## À faire avant impression
- Remplacer chaque `affiches/<film>.svg` par l'affiche officielle (avec droits d'exploitation
  pour l'impression).
- Vérifier les 2 VF « à confirmer » (*I Saw the Devil*, *The Host*) si le doublage FR est
  exigé sans exception.
- Préférer des photos d'acteurs haute résolution (≥ 300 dpi) pour l'imposition print.
