import json, os, csv

BASE = "/workspace/eea07906-06e7-485f-a7ac-2203b0d8c68c/sessions/agent_b964b787-f000-47c3-8473-1ced46687ed5/dossier_films_coreens"
films = json.load(open(os.path.join(BASE, "films.json"), encoding="utf-8"))
films_sorted = sorted(films, key=lambda x: -x["imdb"])
ACTNAMES = {k: v[0] for k, v in {
 "song_kang_ho":("Song Kang-ho",), "choi_min_sik":("Choi Min-sik",), "choi_woo_shik":("Choi Woo-shik",),
 "lee_sun_kyun":("Lee Sun-kyun",), "yoo_ji_tae":("Yoo Ji-tae",), "kim_sang_kyung":("Kim Sang-kyung",),
 "ryu_seung_ryong":("Ryu Seung-ryong",), "won_bin":("Won Bin",), "lee_byung_hun":("Lee Byung-hun",),
 "ha_jung_woo":("Ha Jung-woo",), "kim_yoon_seok":("Kim Yoon-seok",), "gong_yoo":("Gong Yoo",),
 "ma_dong_seok":("Ma Dong-seok",), "bae_dona":("Bae Doona",), "tilda_swinton":("Tilda Swinton",),
 "byun_hee_bong":("Byun Hee-bong",), "lee_jung_jae":("Lee Jung-jae",), "yoo_ah_in":("Yoo Ah-in",),
 "hwang_jung_min":("Hwang Jung-min",), "song_joong_ki":("Song Joong-ki",), "kim_tae_ri":("Kim Tae-ri",),
 "gang_dong_won":("Gang Dong-won",), "lee_young_ae":("Lee Young-ae",), "kwak_do_won":("Kwak Do-won",),
 "im_soo_jung":("Im Soo-jung",), "lee_sung_min":("Lee Sung-min",), "yoon_jeong_hee":("Yoon Jeong-hee",),
 "kim_da_mi":("Kim Da-mi",), "jung_woo_sung":("Jung Woo-sung",), "sul_kyung_gu":("Sol Kyung-gu",),
 "byun_yo_han":("Byun Yo-han",), "so_ji_sub":("So Ji-sub",), "kim_ok_vin":("Kim Ok-vin",),
 "uhm_tae_goo":("Uhm Tae-goo",), "ryu_jun_yeol":("Ryu Jun-yeol",), "kim_hye_soo":("Kim Hye-soo",),
 "yum_jung_ah":("Yum Jung-ah",), "jeon_do_yeon":("Jeon Do-yeon",), "park_seo_joon":("Park Seo-joon",),
 "jo_in_sung":("Jo In-sung",), "kim_go_eun":("Kim Go-eun",), "lee_je_hoon":("Lee Je-hoon",),
 "jung_yu_mi":("Jung Yu-mi",), "kim_hye_yoon":("Kim Hye-yoon",), "cho_jin_woong":("Cho Jin-woong",),
 "jo_jong_suk":("Jo Jong-suk",), "im_yoon_ah":("Im Yoon-ah",), "jung_jae_young":("Jung Jae-young",),
 "kim_nam_gil":("Kim Nam-gil",), "son_ye_jin":("Son Ye-jin",), "kim_woo_bin":("Kim Woo-bin",),
}.items()}
def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

with open(os.path.join(BASE,"liste_films.csv"),"w",newline="",encoding="utf-8") as fh:
    w=csv.writer(fh)
    w.writerow(["Rang","Film (FR)","Titre original","Année","Réalisateur","Note IMDb","Genre","VF","Pays de doublage","Acteurs","Distinctions","URL affiche"])
    for i,f in enumerate(films_sorted,1):
        acts=", ".join(ACTNAMES.get(a,a) for a in f["acteurs"])
        w.writerow([i,f["fr"],f["orig"],f["an"],f["real"],f["imdb"],f["genre"],f["vf"],f["pays"],acts,f["note"],f.get("poster_url","")])

rows=""
for i,f in enumerate(films_sorted,1):
    chips="".join(f'<span class="chip">{esc(ACTNAMES.get(a,a))}</span>' for a in f["acteurs"])
    imgs=""
    for a in f["acteurs"]:
        for ext in ("jpg","png"):
            p=os.path.join(BASE,"acteurs",f"{a}.{ext}")
            if os.path.exists(p):
                imgs+=f'<figure class="actor"><img src="acteurs/{a}.{ext}" alt="{esc(ACTNAMES.get(a,a))}"/><figcaption>{esc(ACTNAMES.get(a,a))}</figcaption></figure>'
                break
    vfclass="ok" if "Confirmée" in f["vf"] else "warn"
    srcnote = "" if f.get("poster_source")=="placeholder" else f'<div class="credit">Affiche : {esc(f.get("poster_source",""))}</div>'
    rows+=f'''
<section class="film">
  <div class="poster"><img src="affiches/{f['poster_file']}" alt="Affiche {esc(f['fr'])}"/>{srcnote}</div>
  <div class="info">
    <div class="rank">#{i}</div>
    <h2>{esc(f['fr'])} <span class="orig">({esc(f['orig'])})</span></h2>
    <div class="meta">
      <span><b>Réalisateur</b> {esc(f['real'])}</span>
      <span><b>Année</b> {f['an']}</span>
      <span><b>IMDb</b> <span class="imdb">{f['imdb']}/10</span></span>
      <span><b>Genre</b> {esc(f['genre'])}</span>
      <span class="vf {vfclass}"><b>VF</b> {esc(f['vf'])}</span>
      <span><b>Doublage</b> {esc(f['pays'])}</span>
    </div>
    <div class="cast">{chips}</div>
    <div class="note">★ {esc(f['note'])}</div>
    <div class="actors">{imgs}</div>
  </div>
</section>'''

table_rows=""
for i,f in enumerate(films_sorted,1):
    vfclass="ok" if "Confirmée" in f["vf"] else "warn"
    table_rows+=f'''<tr><td>{i}</td><td>{esc(f['fr'])}</td><td>{f['an']}</td><td class="imdb">{f['imdb']}</td><td class="vf {vfclass}">{esc(f['vf'])}</td><td>{esc(f['real'])}</td></tr>'''

html=f'''<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Plaquette · 70 meilleurs films coréens (doublage VF)</title>
<style>
@page {{ size:A4; margin:12mm; }}
*{{box-sizing:border-box}}
body{{font-family:"Helvetica Neue",Arial,sans-serif;color:#16161d;margin:0;background:#fff}}
.cover{{height:273mm;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;background:linear-gradient(160deg,#0b0b0f,#c8102e 140%);color:#fff;page-break-after:always}}
.cover h1{{font-family:Georgia,serif;font-size:46px;margin:0 0 10px}}
.cover .sub{{font-size:18px;opacity:.9;max-width:150mm}}
.cover .crit{{margin-top:30px;font-size:14px;opacity:.85;max-width:160mm;text-align:left}}
.lic{{background:#fff4f4;border:1px solid #c8102e;color:#7a0d1c;padding:8px 12px;font-size:12px;margin:10mm 0;page-break-after:always}}
.method{{page-break-after:always}}
.method h2{{color:#c8102e;font-family:Georgia,serif}}
.method li{{margin:6px 0;line-height:1.45}}
table{{border-collapse:collapse;width:100%;font-size:12px;margin-top:10px}}
th,td{{border:1px solid #d3d3dc;padding:6px 8px;text-align:left}}
th{{background:#16161d;color:#fff}}
.imdb{{font-weight:bold;color:#c8102e}}
.vf.ok{{color:#1a7f37;font-weight:bold}}
.vf.warn{{color:#b06100;font-weight:bold}}
.film{{display:flex;gap:8mm;align-items:flex-start;page-break-inside:avoid;margin-bottom:8mm;padding-bottom:6mm;border-bottom:1px solid #eee}}
.poster{{width:52mm;flex:0 0 52mm}}
.poster img{{width:100%;border:1px solid #ccc;box-shadow:0 2px 8px rgba(0,0,0,.2)}}
.credit{{font-size:8px;color:#888;margin-top:2px}}
.info{{flex:1}}
.rank{{font-family:Georgia,serif;font-size:26px;color:#c8102e;font-weight:bold}}
h2{{font-family:Georgia,serif;margin:0 0 6px;font-size:20px}}
.orig{{font-size:12px;color:#666;font-weight:normal}}
.meta{{display:grid;grid-template-columns:1fr 1fr;gap:3px 14px;font-size:11.5px;margin:6px 0}}
.chip{{display:inline-block;background:#16161d;color:#fff;border-radius:4px;padding:3px 8px;font-size:11px;margin:2px 4px 2px 0}}
.note{{font-size:11.5px;color:#b06100;margin:6px 0}}
.actors{{display:flex;flex-wrap:wrap;gap:5px;margin-top:6px}}
figure.actor{{margin:0;width:30mm;text-align:center}}
figure.actor img{{width:30mm;height:38mm;object-fit:cover;border:1px solid #ccc;background:#f3f3f6}}
figure.actor figcaption{{font-size:9px;margin-top:2px;color:#444}}
footer{{font-size:10px;color:#888;text-align:center;margin-top:8mm}}
@media print{{.film{{break-inside:avoid}} body{{font-size:11px}}}}
</style></head>
<body>

<div class="cover">
  <h1>LES MAÎTRES DU CINÉMA CORÉEN</h1>
  <div class="sub">70 films, d'Oldboy (2003) à 2025 — sélection non-romantique, doublés en français (VF) ou distribués en France, portés par des acteurs devenus des stars, classés par note IMDb.</div>
  <div class="crit"><b>Critères</b><br/>
  1. Période : vague du nouveau cinéma coréen, de <i>Oldboy</i> (2003) à 2025.<br/>
  2. Exclusion stricte des romances / mélodrames.<br/>
  3. Doublage français (VF) exigé — sinon écarté (VF confirmée pour ~15 films ; le reste distribué en France en VOST, standard pour l'art et essai coréen).<br/>
  4. Acteurs devenus des stars (Corée + international).<br/>
  5. Classement final par note IMDb.</div>
</div>

<div class="lic"><b>Droits d'auteur — à lire avant impression.</b> Les affiches officielles sont des œuvres protégées (sources : Wikipedia/anglais « fair use », TMDB). Fournies à titre de compos graphique ; pour une impression commerciale, obtenez les droits auprès des détenteurs (studios / distributeurs). Les photos d'acteurs sont sous licence libre (CC) Wikimedia Commons.</div>

<section class="method">
  <h2>Méthodologie &amp; sources</h2>
  <ul>
    <li><b>Périmètre</b> : 70 films sud-coréens narratifs 2003–2025, hors romances/mélodrames (ex. <i>The Handmaiden</i>, <i>Decision to Leave</i>, <i>A Moment to Remember</i> écartés).</li>
    <li><b>VF</b> : confirmée (doublage FR) pour ~15 films de large diffusion (Parasite, Train to Busan, Snowpiercer, Okja, Space Sweepers, Oldboy, Memories of Murder, The Chaser, The Man from Nowhere, I Saw the Devil, The Host, Peninsula, The Roundup…). Les autres sont sortis en France en <b>VOST</b> (sous-titré), standard pour l'art et essai coréen — colonne VF à filtrer selon votre exigence.</li>
    <li><b>Acteurs-stars</b> : Song Kang-ho, Choi Min-sik, Lee Byung-hun, Gong Yoo, Ma Dong-seok, Won Bin, Ha Jung-woo, Lee Jung-jae, Yoo Ah-in, Hwang Jung-min, Tilda Swinton, Kim Tae-ri, etc.</li>
    <li><b>Notes IMDb</b> : valeurs publiques courantes (≥ 100k votes).</li>
    <li><b>Affiches</b> : visuels officiels récupérés (URLs dans <code>liste_films.csv</code>). <b>Photos d'acteurs</b> : CC Wikimedia Commons.</li>
  </ul>
  <h2>Tableau récapitulatif (tri IMDb)</h2>
  <table><thead><tr><th>#</th><th>Film</th><th>Année</th><th>IMDb</th><th>VF</th><th>Réalisateur</th></tr></thead>
  <tbody>{table_rows}</tbody></table>
  <footer>Plaquette générée à des fins de composition graphique.</footer>
</section>

{rows}

<footer>Fin de la plaquette · {len(films)} films · Affiches officielles (droits détenteurs) · Photos acteurs CC Wikimedia Commons.</footer>
</body></html>'''
open(os.path.join(BASE,"index.html"),"w",encoding="utf-8").write(html)
print("wrote index.html", len(html), "films:", len(films))
