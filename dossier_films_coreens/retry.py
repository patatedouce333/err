import urllib.request, urllib.parse, json, os, time

BASE = "/workspace/eea07906-06e7-485f-a7ac-2203b0d8c68c/sessions/agent_b964b787-f000-47c3-8473-1ced46687ed5/dossier_films_coreens"
AFF = os.path.join(BASE, "affiches")
ACT = os.path.join(BASE, "acteurs")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}

ACTORS = {
 "song_kang_ho": ("Song Kang-ho", "File:Song Kang-Ho (cropped).jpg", None),
 "choi_min_sik": ("Choi Min-sik", "File:Choi Min-sik.jpg", None),
 "choi_woo_shik": ("Choi Woo-shik", "File:Choi Woo-shik for the premiere of Wonderland June 2024.png", None),
 "lee_sun_kyun": ("Lee Sun-kyun", "File:이선균 (LEE SUN KYUN) - 2023.10.28.jpg", None),
 "yoo_ji_tae": ("Yoo Ji-tae", "File:Yoo Ji-tae, Keum Sae-rok, Lee Jin-wook, Lim Sun-ae at the Busan International Film Festival 2025 01.jpg", None),
 "kim_sang_kyung": ("Kim Sang-kyung", "File:Kim Sang-kyung (김상경) Poong, The Joseon Psychiatrist Script Reading (1).jpg", None),
 "ryu_seung_ryong": ("Ryu Seung-ryong", None, "Ryu Seung-ryong actor"),
 "won_bin": ("Won Bin", "File:Won Bin from acrofan.jpg", None),
 "lee_byung_hun": ("Lee Byung-hun", "File:Lee Byung-hun.2019.jpg", None),
 "ha_jung_woo": ("Ha Jung-woo", "File:Ha Jung-woo.2019.jpg", None),
 "kim_yoon_seok": ("Kim Yoon-seok", "File:Kim Yoon-Seok.jpg", None),
 "gong_yoo": ("Gong Yoo", "File:Gong Yoo in 2021 - 1.png", None),
 "ma_dong_seok": ("Ma Dong-seok", "File:Ma Dong-seok.png", None),
 "bae_dona": ("Bae Doona", "File:Bae Doona-181119(cut).jpg", None),
 "tilda_swinton": ("Tilda Swinton", "File:Tilda Swinton by Gage Skidmore (cropped).jpg", None),
 "byun_hee_bong": ("Byun Hee-bong", "File:Byun hee bong 2017okja.png", None),
 "lee_jung_jae": ("Lee Jung-jae", None, "Lee Jung-jae actor"),
 "yoo_ah_in": ("Yoo Ah-in", None, "Yoo Ah-in actor"),
 "hwang_jung_min": ("Hwang Jung-min", None, "Hwang Jung-min actor"),
 "song_joong_ki": ("Song Joong-ki", "File:Song Joong-ki crop.JPG", None),
 "kim_tae_ri": ("Kim Tae-ri", "File:Kim Tae-ri 김태리 in 2022.png", None),
 "gang_dong_won": ("Gang Dong-won", "File:Gang Dong-won in 2018.jpg", None),
 "lee_young_ae": ("Lee Young-ae", None, "Lee Young-ae actress"),
 "kwak_do_won": ("Kwak Do-won", None, "Kwak Do-won actor"),
 "im_soo_jung": ("Im Soo-jung", None, "Im Soo-jung actress"),
 "lee_sung_min": ("Lee Sung-min", None, "Lee Sung-min actor"),
 "yoon_jeong_hee": ("Yoon Jeong-hee", None, "Yoon Jeong-hee actress"),
 "kim_da_mi": ("Kim Da-mi", None, "Kim Da-mi actress"),
 "jung_woo_sung": ("Jung Woo-sung", None, "Jung Woo-sung actor"),
 "sul_kyung_gu": ("Sol Kyung-gu", None, "Sol Kyung-gu actor"),
 "byun_yo_han": ("Byun Yo-han", None, "Byun Yo-han actor"),
 "so_ji_sub": ("So Ji-sub", None, "So Ji-sub actor"),
 "kim_ok_vin": ("Kim Ok-vin", None, "Kim Ok-vin actress"),
 "uhm_tae_goo": ("Uhm Tae-goo", None, "Uhm Tae-goo actor"),
 "ryu_jun_yeol": ("Ryu Jun-yeol", None, "Ryu Jun-yeol actor"),
 "kim_hye_soo": ("Kim Hye-soo", None, "Kim Hye-soo actress"),
 "yum_jung_ah": ("Yum Jung-ah", None, "Yum Jung-ah actress"),
 "jeon_do_yeon": ("Jeon Do-yeon", None, "Jeon Do-yeon actress"),
 "park_seo_joon": ("Park Seo-joon", None, "Park Seo-joon actor"),
 "jo_in_sung": ("Jo In-sung", None, "Jo In-sung actor"),
 "kim_go_eun": ("Kim Go-eun", None, "Kim Go-eun actress"),
 "lee_je_hoon": ("Lee Je-hoon", None, "Lee Je-hoon actor"),
 "jung_yu_mi": ("Jung Yu-mi", None, "Jung Yu-mi actress"),
 "kim_hye_yoon": ("Kim Hye-yoon", None, "Kim Hye-yoon actress"),
 "cho_jin_woong": ("Cho Jin-woong", None, "Cho Jin-woong actor"),
 "jo_jong_suk": ("Jo Jong-suk", None, "Jo Jong-suk actor"),
 "im_yoon_ah": ("Im Yoon-ah", None, "Yoona Girls' Generation actress"),
 "jung_jae_young": ("Jung Jae-young", None, "Jung Jae-young actor"),
 "kim_nam_gil": ("Kim Nam-gil", None, "Kim Nam-gil actor"),
 "son_ye_jin": ("Son Ye-jin", None, "Son Ye-jin actress"),
 "kim_woo_bin": ("Kim Woo-bin", None, "Kim Woo-bin actor"),
}

def fetch(url, timeout=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()

def poster_rest(wiki):
    for _ in range(3):
        try:
            u = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(wiki)
            d = json.loads(fetch(u))
            s = d.get("originalimage", {}).get("source")
            if s: return s
        except Exception:
            time.sleep(3)
    return None

def poster_pageimages(wiki):
    try:
        p = {"action":"query","format":"json","prop":"pageimages","piprop":"original","titles":wiki}
        d = json.loads(fetch("https://en.wikipedia.org/w/api.php?"+urllib.parse.urlencode(p)))
        for pg in d.get("query",{}).get("pages",{}).values():
            if "original" in pg: return pg["original"]["source"]
    except Exception:
        pass
    return None

def tmdb_poster(title):
    try:
        q = urllib.parse.quote(title)
        p = {"api_key":"", "query":title, "language":"en-US"}
        # search TMDB (public, may need key) -> fallback use known pattern not possible; skip
    except Exception:
        pass
    return None

def actor_search(query):
    for _ in range(2):
        try:
            p = {"action":"query","format":"json","list":"search","srsearch":query,"srnamespace":6,"srlimit":6}
            d = json.loads(fetch("https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode(p)))
            for it in d.get("query",{}).get("search",[]):
                t = it["title"]
                if t.lower().endswith((".jpg",".png",".jpeg",".webp")):
                    return t
        except Exception:
            time.sleep(2)
    return None

def thumb_url(title, width=640):
    p = {"action":"query","format":"json","prop":"imageinfo","iiprop":"url","iiurlwidth":width,"titles":title}
    d = json.loads(fetch("https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode(p)))
    for pg in d.get("query",{}).get("pages",{}).values():
        if "imageinfo" in pg:
            return pg["imageinfo"][0].get("thumburl")
    return None

def download_actor(key):
    name, file, query = ACTORS[key]
    if any(os.path.exists(os.path.join(ACT,f"{key}.{e}")) for e in ("jpg","png")):
        return True
    out = None
    try:
        if file:
            tu = thumb_url(file)
            if tu:
                data = fetch(tu); ext=tu.rsplit(".",1)[1].split("?")[0]
                open(os.path.join(ACT,f"{key}.{ext}"),"wb").write(data); out=True
        if not out and query:
            t = actor_search(query)
            if t:
                tu = thumb_url(t)
                if tu:
                    data = fetch(tu); ext=tu.rsplit(".",1)[1].split("?")[0]
                    open(os.path.join(ACT,f"{key}.{ext}"),"wb").write(data); out=True
    except Exception as e:
        print("  actor ERR", key, repr(e))
    return out

films = json.load(open(os.path.join(BASE,"films.json"), encoding="utf-8"))
print("=== RETRY POSTERS ===")
fixed=0
for f in films:
    pf = f.get("poster_file","")
    if pf.endswith(".svg"):
        url = poster_rest(f["wiki"]) or poster_pageimages(f["wiki"])
        if url:
            try:
                data = fetch(url, timeout=90)
                ext = url.rsplit(".",1)[1].split("?")[0]
                if ext.lower() not in ("jpg","jpeg","png","webp"): ext="jpg"
                fn=f"{f['id']}.{ext}"
                # remove old placeholder svg
                old=os.path.join(AFF,pf)
                if os.path.exists(old): os.remove(old)
                open(os.path.join(AFF,fn),"wb").write(data)
                f["poster_file"]=fn; f["poster_source"]="Wikipedia"
                fixed+=1; print("FIX poster", fn)
            except Exception as e:
                print("  poster ERR", f["id"], repr(e))
        else:
            print("  still missing", f["id"])
        time.sleep(2.5)

print("=== RETRY ACTORS ===")
afixed=0
for key in ACTORS:
    if download_actor(key):
        afixed+=1
    time.sleep(1.5)

json.dump(films, open(os.path.join(BASE,"films.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"DONE fixed posters={fixed} actors_present={afixed}/{len(ACTORS)}")
