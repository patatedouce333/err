import urllib.request, urllib.parse, json, os, time, csv

BASE = "/workspace/eea07906-06e7-485f-a7ac-2203b0d8c68c/sessions/agent_b964b787-f000-47c3-8473-1ced46687ed5/dossier_films_coreens"
AFF = os.path.join(BASE, "affiches")
ACT = os.path.join(BASE, "acteurs")
os.makedirs(AFF, exist_ok=True)
os.makedirs(ACT, exist_ok=True)
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

FILMS = [
 dict(id="parasite", fr="Parasite", orig="기생충 / Gisaengchung", an=2019, real="Bong Joon-ho", imdb=8.5, genre="Comédie noire · Thriller social", vf="VF confirmée (salles + TV)", pays="FR, US, GB, DE, JP, KR, ES, IT, BR…", acteurs=["song_kang_ho","choi_woo_shik","lee_sun_kyun"], wiki="Parasite (2019 film)", note="Palme d'or 2019 · 4 Oscars"),
 dict(id="oldboy", fr="Oldboy", orig="올드보이 / Oldeuboi", an=2003, real="Park Chan-wook", imdb=8.3, genre="Thriller · Vengeance", vf="VF (DVD/Blu-ray)", pays="KR, JP, FR, US, ES, IT…", acteurs=["choi_min_sik","yoo_ji_tae"], wiki="Oldboy (2003 film)", note="Grand Prix Cannes 2004"),
 dict(id="memories", fr="Memories of Murder", orig="살인의 추억", an=2003, real="Bong Joon-ho", imdb=8.1, genre="Policier · Thriller", vf="VF confirmée (VOD)", pays="KR, FR, JP, US, ES…", acteurs=["song_kang_ho","kim_sang_kyung"], wiki="Memories of Murder", note="Inspiré du 1er tueur en série coréen"),
 dict(id="miracle", fr="Miracle in Cell No. 7", orig="7번방의 선물", an=2013, real="Lee Hwan-kyung", imdb=8.2, genre="Drame · Comédie", vf="VOST (sortie FR)", pays="KR, FR, JP, TR…", acteurs=["ryu_seung_ryong"], wiki="Miracle in Cell No. 7", note="Carton popular en Corée"),
 dict(id="mother", fr="Mother", orig="마더", an=2009, real="Bong Joon-ho", imdb=7.8, genre="Thriller · Drame", vf="VOST (sortie FR)", pays="KR, FR, JP, US…", acteurs=["won_bin"], wiki="Mother (2009 film)", note="Sélection Cannes Un Certain Regard"),
 dict(id="the_attorney", fr="The Attorney", orig="변호인", an=2013, real="Yang Woo-suk", imdb=7.8, genre="Drame judiciaire", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["song_kang_ho"], wiki="The Attorney (2013 film)", note="Inspiré de Roh Moo-hyun"),
 dict(id="ode_to_my_father", fr="Ode to My Father", orig="국제시장", an=2014, real="Yoon Je-kyoon", imdb=7.8, genre="Drame historique", vf="VOST (sortie FR)", pays="KR, FR, US…", acteurs=["hwang_jung_min"], wiki="Ode to My Father", note=">10 M d'entrées Corée"),
 dict(id="a_bittersweet_life", fr="A Bittersweet Life", orig="달콤한 인생", an=2005, real="Kim Jee-woon", imdb=7.7, genre="Action · Drame", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["lee_byung_hun"], wiki="A Bittersweet Life", note="Style de Kim Jee-woon"),
 dict(id="the_man_from_nowhere", fr="The Man from Nowhere", orig="아저씨", an=2010, real="Lee Jeong-beom", imdb=7.7, genre="Action · Thriller", vf="VF confirmée (DVD FR)", pays="KR, FR, US, JP, ES…", acteurs=["won_bin"], wiki="The Man from Nowhere (2010 film)", note="N°1 box-office Corée 2010"),
 dict(id="i_saw_devil", fr="I Saw the Devil", orig="악마를 보았다", an=2010, real="Kim Jee-woon", imdb=7.7, genre="Thriller · Horreur", vf="VF confirmée (DVD/Blu-ray ARP Sélection + streaming FR)", pays="KR, FR, JP, US…", acteurs=["lee_byung_hun","choi_min_sik"], wiki="I Saw the Devil", note="Kim Jee-woon × Lee Byung-hun"),
 dict(id="new_world", fr="New World", orig="신세계", an=2013, real="Park Hoon-jung", imdb=7.9, genre="Gangster · Thriller", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["lee_jung_jae","choi_min_sik"], wiki="New World (2013 film)", note="Polars coréens cultes"),
 dict(id="the_chaser", fr="The Chaser", orig="추격자", an=2008, real="Na Hong-jin", imdb=7.9, genre="Thriller · Policier", vf="VF confirmée (salles)", pays="KR, FR, ES, JP…", acteurs=["kim_yoon_seok","ha_jung_woo"], wiki="The Chaser (2008 film)", note="1er film de Na Hong-jin"),
 dict(id="silenced", fr="Silenced", orig="도가니", an=2011, real="Hwang Dong-hyuk", imdb=7.9, genre="Drame · Procès", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["gong_yoo"], wiki="Silenced (2011 film)", note="Scandale réel d'abus"),
 dict(id="castaway_on_the_moon", fr="Castaway on the Moon", orig="김씨 표류기", an=2009, real="Lee Hae-jun", imdb=7.9, genre="Comédie · Drame", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["jung_jae_young"], wiki="Castaway on the Moon", note="Cult movie sud-coréen"),
 dict(id="a_taxi_driver", fr="A Taxi Driver", orig="택시운전사", an=2017, real="Jang Hoon", imdb=7.9, genre="Drame historique", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["song_kang_ho"], wiki="A Taxi Driver", note="Gwangju 1980"),
 dict(id="burning", fr="Burning", orig="버닝", an=2018, real="Lee Chang-dong", imdb=7.5, genre="Mystery · Drame", vf="VOST (sortie FR)", pays="KR, FR, JP, US…", acteurs=["yoo_ah_in"], wiki="Burning (2018 film)", note="Sélection Cannes 2018"),
 dict(id="the_yellow_sea", fr="The Yellow Sea", orig="황해", an=2010, real="Na Hong-jin", imdb=7.6, genre="Thriller · Action", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["ha_jung_woo","kim_yoon_seok"], wiki="The Yellow Sea (2010 film)", note="Na Hong-jin"),
 dict(id="train_to_busan", fr="Train to Busan", orig="부산행", an=2016, real="Yeon Sang-ho", imdb=7.6, genre="Horreur · Zombies", vf="VF confirmée (salles)", pays="KR, FR, US, JP, ES, DE…", acteurs=["gong_yoo","ma_dong_seok"], wiki="Train to Busan", note="Phénomène zombie coréen"),
 dict(id="lady_vengeance", fr="Lady Vengeance", orig="친절한 금자씨", an=2005, real="Park Chan-wook", imdb=7.6, genre="Thriller · Vengeance", vf="VOST (sortie FR)", pays="KR, FR, JP, US…", acteurs=["lee_young_ae","choi_min_sik"], wiki="Lady Vengeance", note="Trilogie de la vengeance"),
 dict(id="the_wailing", fr="The Wailing", orig="곡성", an=2016, real="Na Hong-jin", imdb=7.4, genre="Horreur · Mystère", vf="VOST (sortie FR)", pays="KR, FR, JP, US…", acteurs=["kwak_do_won","hwang_jung_min"], wiki="The Wailing (2016 film)", note="Frissons coréens"),
 dict(id="a_tale_of_two_sisters", fr="A Tale of Two Sisters", orig="장화, 홍련", an=2003, real="Kim Jee-woon", imdb=7.4, genre="Horreur · Drame", vf="VOST (sortie FR)", pays="KR, FR, JP, US…", acteurs=["im_soo_jung"], wiki="A Tale of Two Sisters", note="Classique horreur coréenne"),
 dict(id="the_book_of_fish", fr="The Book of Fish", orig="자산어보", an=2021, real="Lee Joon-ik", imdb=7.4, genre="Drame historique", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["sul_kyung_gu","byun_yo_han"], wiki="The Book of Fish", note="Période Joseon"),
 dict(id="the_spy_gone_north", fr="The Spy Gone North", orig="공작", an=2018, real="Yoon Jong-bin", imdb=7.5, genre="Espionnage · Thriller", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["hwang_jung_min","lee_sung_min"], wiki="The Spy Gone North", note="Festival de Cannes 2018"),
 dict(id="poetry", fr="Poetry", orig="시", an=2010, real="Lee Chang-dong", imdb=7.7, genre="Drame", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["yoon_jeong_hee"], wiki="Poetry (2010 film)", note="Meilleur scénario Cannes 2010"),
 dict(id="the_age_of_shadows", fr="The Age of Shadows", orig="밀정", an=2016, real="Kim Jee-woon", imdb=7.5, genre="Espionnage · Thriller", vf="VOST (sortie FR)", pays="KR, FR, JP, US…", acteurs=["lee_byung_hun","song_kang_ho","gong_yoo"], wiki="The Age of Shadows", note="Nommé aux Oscars"),
 dict(id="the_throne", fr="The Throne", orig="사도", an=2015, real="Lee Joon-ik", imdb=7.7, genre="Drame historique", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["yoo_ah_in","song_kang_ho"], wiki="The Throne (2015 film)", note="Période Joseon"),
 dict(id="okja", fr="Okja", orig="옥자", an=2017, real="Bong Joon-ho", imdb=7.3, genre="Fable écolo", vf="VF confirmée (Netflix)", pays="KR, US, FR, JP, ES, BR…", acteurs=["tilda_swinton","byun_hee_bong"], wiki="Okja", note="Sélection Cannes 2017"),
 dict(id="the_witch_1", fr="The Witch: Part 1", orig="마녀", an=2018, real="Park Hoon-jung", imdb=7.0, genre="Action · Horreur", vf="VOST (sortie FR)", pays="KR, FR, JP, US…", acteurs=["kim_da_mi"], wiki="The Witch: Part 1. The Subversion", note="Phénomène jeune public"),
 dict(id="veteran", fr="Veteran", orig="베테랑", an=2015, real="Ryoo Seung-wan", imdb=7.1, genre="Action · Policier", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["hwang_jung_min","yoo_ah_in"], wiki="Veteran (2015 film)", note="N°1 Corée 2015"),
 dict(id="snowpiercer", fr="Snowpiercer", orig="설국열차", an=2013, real="Bong Joon-ho", imdb=7.1, genre="Sci-fi · Anticipation", vf="VF confirmée (Le Transperceneige)", pays="KR, FR, US, JP, DE, ES…", acteurs=["song_kang_ho","tilda_swinton"], wiki="Snowpiercer (2013 film)", note="Adapté de la BD française"),
 dict(id="the_host", fr="The Host", orig="괴물", an=2006, real="Bong Joon-ho", imdb=7.1, genre="Monstre · Drame", vf="VF confirmée (DVD/Blu-ray FR)", pays="KR, US, JP, FR…", acteurs=["song_kang_ho","bae_dona"], wiki="The Host (2006 film)", note="Monstre sur la Han"),
 dict(id="the_outlaws", fr="The Outlaws", orig="범죄도시", an=2017, real="Kang Yoon-sung", imdb=7.1, genre="Action · Policier", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["ma_dong_seok"], wiki="The Outlaws (2017 film)", note="Série à succès"),
 dict(id="exit", fr="Exit", orig="엑시트", an=2019, real="Lee Sang-geun", imdb=7.1, genre="Action · Catastrophe", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["jo_jong_suk","im_yoon_ah"], wiki="Exit (2019 film)", note="Comédie d'action"),
 dict(id="the_good_the_bad_the_weird", fr="The Good, the Bad, the Weird", orig="좋은 놈, 나쁜 놈, 이상한 놈", an=2008, real="Kim Jee-woon", imdb=7.2, genre="Western · Action", vf="VOST (sortie FR)", pays="KR, FR, JP, US…", acteurs=["song_kang_ho","lee_byung_hun","jung_woo_sung"], wiki="The Good, the Bad, the Weird", note="Western coréen"),
 dict(id="nameless_gangster", fr="Nameless Gangster", orig="범죄와의 전쟁", an=2012, real="Yoon Jong-bin", imdb=7.2, genre="Gangster", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["choi_min_sik"], wiki="Nameless Gangster: Rules of the Time", note="Yoon Jong-bin × Choi Min-sik"),
 dict(id="memoir_of_a_murderer", fr="Memoir of a Murderer", orig="살인자의 기억법", an=2017, real="Won Shin-yun", imdb=7.2, genre="Thriller", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["sul_kyung_gu"], wiki="Memoir of a Murderer", note="Thriller psychologique"),
 dict(id="night_in_paradise", fr="Night in Paradise", orig="낙원의 밤", an=2020, real="Park Hoon-jung", imdb=7.2, genre="Gangster · Drame", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["uhm_tae_goo"], wiki="Night in Paradise (film)", note="Polar stylisé"),
 dict(id="the_night_owl", fr="The Night Owl", orig="올빼미", an=2022, real="Ahn Tae-jin", imdb=7.2, genre="Historique · Thriller", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["ryu_jun_yeol"], wiki="The Night Owl (film)", note="Période Joseon"),
 dict(id="12_12_the_day", fr="12.12: The Day", orig="서울의 봄", an=2023, real="Kim Sung-su", imdb=7.2, genre="Thriller politique", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["hwang_jung_min"], wiki="12.12: The Day", note="Coup d'État 1979"),
 dict(id="broker", fr="Broker", orig="브로커", an=2022, real="Hirokazu Koreeda", imdb=7.2, genre="Drame", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["song_kang_ho"], wiki="Broker (2022 film)", note="Koreeda en Corée"),
 dict(id="concrete_utopia", fr="Concrete Utopia", orig="콘크리트 유토피아", an=2023, real="Um Tae-hwa", imdb=6.8, genre="Catastrophe · Drame", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["lee_byung_hun","park_seo_joon"], wiki="Concrete Utopia", note="Après la destruction de Séoul"),
 dict(id="smugglers", fr="Smugglers", orig="밀수", an=2023, real="Ryoo Seung-wan", imdb=6.8, genre="Thriller · Action", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["kim_hye_soo","yum_jung_ah"], wiki="Smugglers (2023 film)", note="Années 1970, contrebande"),
 dict(id="kill_boksoon", fr="Kill Boksoon", orig="길복순", an=2023, real="Byun Sung-hyun", imdb=6.8, genre="Action · Thriller", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["jeon_do_yeon"], wiki="Kill Boksoon", note="Tueuse à gages"),
 dict(id="the_roundup", fr="The Roundup", orig="범죄도시2", an=2022, real="Yoon Sung-bin", imdb=7.0, genre="Action · Policier", vf="VF confirmée (salles)", pays="KR, FR, JP…", acteurs=["ma_dong_seok"], wiki="The Roundup (2022 film)", note="Ma Dong-seok à Vancouver"),
 dict(id="the_roundup_noway", fr="The Roundup: No Way Out", orig="범죄도시3", an=2023, real="Lee Sang-yong", imdb=6.8, genre="Action · Policier", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["ma_dong_seok"], wiki="The Roundup: No Way Out", note="Suite de The Roundup"),
 dict(id="the_gangster_the_cop_the_devil", fr="The Gangster, the Cop, the Devil", orig="악인전", an=2019, real="Lee Won-tae", imdb=7.0, genre="Action · Policier", vf="VOST (sortie FR)", pays="KR, FR, US…", acteurs=["ma_dong_seok"], wiki="The Gangster, the Cop, the Devil", note="Remake US : The Fortress"),
 dict(id="escape_from_mogadishu", fr="Escape from Mogadishu", orig="모가디슈", an=2021, real="Ryoo Seung-wan", imdb=7.0, genre="Thriller · Action", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["kim_yoon_seok"], wiki="Escape from Mogadishu", note="Corée à Mogadiscio"),
 dict(id="hostage_missing_celebrity", fr="Hostage: Missing Celebrity", orig="인질", an=2021, real="Pil Kam-sung", imdb=7.0, genre="Thriller", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["hwang_jung_min"], wiki="Hostage: Missing Celebrity", note="Kidnapping"),
 dict(id="a_normal_family", fr="A Normal Family", orig="보통의 가족", an=2024, real="Hur Jin-ho", imdb=7.0, genre="Drame · Thriller", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["sul_kyung_gu"], wiki="A Normal Family", note="D'après une pièce japonaise"),
 dict(id="collectors", fr="Collectors", orig="도굴", an=2020, real="Park Jung-bae", imdb=7.0, genre="Comédie · Buddy", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["lee_je_hoon"], wiki="Collectors (2020 film)", note="Voleurs d'artefacts"),
 dict(id="deliver_us_from_evil", fr="Deliver Us from Evil", orig="비상선언", an=2020, real="Hong Won-chan", imdb=7.0, genre="Thriller · Action", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["hwang_jung_min"], wiki="Deliver Us from Evil (2020 film)", note="Pilote détourné"),
 dict(id="hunt", fr="Hunt", orig="헌트", an=2022, real="Lee Jung-jae", imdb=6.7, genre="Espionnage · Action", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["lee_jung_jae","jung_woo_sung"], wiki="Hunt (2022 film)", note="Réalisé par Lee Jung-jae"),
 dict(id="exhuma", fr="Exhuma", orig="파묘", an=2024, real="Jang Jae-hyun", imdb=6.6, genre="Horreur · Mystère", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["choi_min_sik","kim_go_eun"], wiki="Exhuma (film)", note="Occulte coréen"),
 dict(id="space_sweepers", fr="Space Sweepers", orig="승리호", an=2021, real="Jo Sung-hee", imdb=6.6, genre="Sci-fi · Space opera", vf="VF confirmée (Netflix)", pays="KR, US, FR, JP, ES…", acteurs=["kim_tae_ri","song_joong_ki"], wiki="Space Sweepers", note="1er blockbuster SF coréen"),
 dict(id="extreme_job", fr="Extreme Job", orig="극한직업", an=2019, real="Lee Byeong-heon", imdb=6.9, genre="Comédie · Action", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["ryu_seung_ryong"], wiki="Extreme Job", note="Carton comédie Corée"),
 dict(id="the_fortress", fr="The Fortress", orig="남한산성", an=2017, real="Hwang Dong-hyuk", imdb=7.2, genre="Historique · Drame", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["lee_byung_hun","kim_yoon_seok"], wiki="The Fortress (2017 film)", note="Siège de 1636"),
 dict(id="the_face_reader", fr="The Face Reader", orig="관상", an=2013, real="Han Jae-rim", imdb=7.2, genre="Historique · Drame", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["song_kang_ho"], wiki="The Face Reader", note="Période Joseon"),
 dict(id="confession_of_murder", fr="Confession of Murder", orig="Confession of Murder", an=2012, real="Jung Byung-gil", imdb=7.2, genre="Thriller · Policier", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["jung_woo_sung"], wiki="Confession of Murder (2012 film)", note="Policier coréen"),
 dict(id="inside_men", fr="Inside Men", orig="내부자들", an=2015, real="Woo Min-ho", imdb=7.1, genre="Thriller politique", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["lee_jung_jae"], wiki="Inside Men (2015 film)", note="Corruption en Corée"),
 dict(id="battleship_island", fr="The Battleship Island", orig="군함도", an=2017, real="Ryoo Seung-wan", imdb=7.1, genre="Action · Historique", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["song_joong_ki","so_ji_sub"], wiki="The Battleship Island", note="Travailleurs coréens au Japon"),
 dict(id="the_villainess", fr="The Villainess", orig="악녀", an=2017, real="Jung Byung-gil", imdb=7.2, genre="Action · Thriller", vf="VOST (sortie FR)", pays="KR, FR, JP…", acteurs=["kim_ok_vin"], wiki="The Villainess", note="Action femme"),
 dict(id="peninsula", fr="Peninsula", orig="반도", an=2020, real="Yeon Sang-ho", imdb=5.6, genre="Horreur · Zombies", vf="VF confirmée (salles)", pays="KR, FR, US, JP, ES…", acteurs=["gang_dong_won"], wiki="Peninsula (2020 film)", note="Suite de Train to Busan"),
 dict(id="the_king", fr="The King", orig="더 킹", an=2017, real="Han Jae-rim", imdb=7.0, genre="Thriller politique", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["jo_in_sung","jung_woo_sung"], wiki="The King (2017 film)", note="Sur la corruption"),
 dict(id="ashfall", fr="Ashfall", orig="백두산", an=2019, real="Lee Hae-joon", imdb=6.1, genre="Catastrophe · Action", vf="VOST (sortie FR)", pays="KR, FR, JP, CN…", acteurs=["lee_byung_hun","ha_jung_woo","ma_dong_seok"], wiki="Ashfall (2019 film)", note="Volcan Baekdu"),
 dict(id="default", fr="Default", orig="국가부도의 날", an=2018, real="Choi Kook-hee", imdb=7.0, genre="Drame financier", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["yoo_ah_in","kim_hye_soo"], wiki="Default (2018 film)", note="Crise FMI 1997"),
 dict(id="svaha", fr="Svaha: The Sixth Finger", orig="사바하", an=2019, real="Jang Jae-hyun", imdb=6.6, genre="Mystère · Horreur", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["lee_jung_jae"], wiki="Svaha: The Sixth Finger", note="Culte étrange"),
 dict(id="phantom", fr="Phantom", orig="유령", an=2022, real="Lee Hae-young", imdb=6.7, genre="Espionnage", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["sul_kyung_gu"], wiki="Phantom (2022 film)", note="Mandchoukouo 1933"),
 dict(id="uprising", fr="Uprising", orig="전,란", an=2024, real="Kim Sang-man", imdb=6.8, genre="Historique · Action", vf="VOST (Netflix)", pays="KR, FR, US…", acteurs=["gang_dong_won","kim_woo_bin"], wiki="Uprising (2024 film)", note="Révolte Joseon"),
 dict(id="hijack_1971", fr="Hijack 1971", orig="하이재킹", an=2024, real="Kim Sung-han", imdb=6.7, genre="Thriller · Action", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["ha_jung_woo"], wiki="Hijack 1971", note="Détournement 1971"),
 dict(id="i_the_executioner", fr="I, the Executioner", orig="범죄도시4", an=2024, real="Ryoo Seung-wan", imdb=6.7, genre="Action · Policier", vf="VOST (sortie FR)", pays="KR, FR…", acteurs=["ma_dong_seok"], wiki="I, the Executioner (2024 film)", note="Saga The Outlaws"),
]

SPECIAL_POSTERS = {
 "snowpiercer": "https://image.tmdb.org/t/p/original/a5kEmfaNE3CPh6k6QC8VBZgUsO0.jpg",
}

def fetch(url, timeout=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()

def poster_url(wiki):
    try:
        u = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(wiki)
        d = json.loads(fetch(u))
        return d.get("originalimage", {}).get("source")
    except Exception:
        return None

def actor_search(query):
    try:
        p = {"action":"query","format":"json","list":"search","srsearch":query,"srnamespace":6,"srlimit":5}
        d = json.loads(fetch("https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode(p)))
        for it in d.get("query",{}).get("search",[]):
            t = it["title"]
            if t.lower().endswith((".jpg",".png",".jpeg",".webp")):
                return t
    except Exception:
        pass
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
    out = None
    try:
        if file:
            tu = thumb_url(file)
            if tu:
                data = fetch(tu); ext = tu.rsplit(".",1)[1].split("?")[0]
                out = f"{key}.{ext}"; open(os.path.join(ACT,out),"wb").write(data)
        if out is None and query:
            t = actor_search(query)
            if t:
                tu = thumb_url(t)
                if tu:
                    data = fetch(tu); ext = tu.rsplit(".",1)[1].split("?")[0]
                    out = f"{key}.{ext}"; open(os.path.join(ACT,out),"wb").write(data)
    except Exception as e:
        print("  actor ERR", key, repr(e))
    return out

def make_placeholder(fid, f):
    W,H=1000,1414
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="#0b0b0f"/>
<rect x="40" y="40" width="{W-80}" height="{H-80}" fill="none" stroke="#c8102e" stroke-width="3" opacity="0.6"/>
<text x="90" y="300" font-family="Georgia, serif" font-size="80" fill="#fff" font-weight="bold">{f['fr']}</text>
<text x="90" y="360" font-family="Georgia, serif" font-size="26" fill="#b9b9c4" font-style="italic">{f['orig']}</text>
<line x1="90" y1="400" x2="910" y2="400" stroke="#c8102e" stroke-width="2"/>
<text x="90" y="470" font-family="Helvetica, Arial, sans-serif" font-size="26" fill="#e7e7ee">{f['genre']}</text>
<text x="90" y="540" font-family="Helvetica, Arial, sans-serif" font-size="26" fill="#e7e7ee">{f['an']}  ·  IMDb {f['imdb']}</text>
<text x="90" y="610" font-family="Helvetica, Arial, sans-serif" font-size="22" fill="#9fe6a0">{f['vf']}</text>
<text x="90" y="1300" font-family="Helvetica, Arial, sans-serif" font-size="18" fill="#888">Affiche officielle à insérer (droits d'auteur)</text>
</svg>'''
    fn = os.path.join(AFF, f"{fid}.svg")
    open(fn,"w",encoding="utf-8").write(svg)
    return f"{fid}.svg"

print("=== POSTERS ===")
for f in FILMS:
    url = SPECIAL_POSTERS.get(f["id"]) or poster_url(f["wiki"])
    done = False
    if url:
        try:
            data = fetch(url, timeout=90)
            ext = url.rsplit(".",1)[1].split("?")[0]
            if ext.lower() not in ("jpg","jpeg","png","webp"): ext="jpg"
            fn = f"{f['id']}.{ext}"
            open(os.path.join(AFF,fn),"wb").write(data)
            f["poster_file"]=fn; f["poster_url"]=url; f["poster_source"]="Wikipedia/TMDB"
            done = True
            print("OK poster", fn)
        except Exception as e:
            print("poster ERR", f["id"], repr(e))
    if not done:
        f["poster_file"]=make_placeholder(f["id"], f)
        f["poster_url"]=""; f["poster_source"]="placeholder"
        print("PLACEHOLDER", f["id"])
    time.sleep(1.2)

print("=== ACTORS ===")
for key in ACTORS:
    res = download_actor(key)
    if res: print("OK actor", res)
    else: print("MISS actor", key)
    time.sleep(1.0)

json.dump(FILMS, open(os.path.join(BASE,"films.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("DONE films.json", len(FILMS))
