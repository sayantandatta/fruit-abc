# Fruit ABC

A tap-a-letter fruit alphabet for toddlers. Tap a letter in the ribbon (or All for any fruit) and a random fruit starting with that letter pops up, with its name spoken slowly in a British English voice (a menu at the bottom lets you pick the clearest voice on your device) and a one-line description of how it tastes. Arrows on the picture (or a swipe) move between fruits for that letter.

The fruit list comes from the [Wikijunior Fruit Alphabet](https://en.wikibooks.org/wiki/Wikijunior:Fruit_Alphabet) chart. All 99 fruits and their toddler-friendly taste sentences are in `index.html`.

## Files

- `index.html` is the whole site, with no build step. Open it in a browser or serve it from GitHub Pages.
- `images/` holds the fruit photos, named by fruit (`apple.jpg`, `dragon-fruit.jpg`). Fruits without a photo are shown as emoji or drawings.

## Adding or replacing a photo

Put a square-ish photo on a white background in `images/` and add a line to the `PHOTOS` object near the top of the script in `index.html`, for example `"Durian":"images/durian.jpg"`. The name must match the fruit name exactly.

## Photo credits

Most photos are the lead images of each fruit's Wikipedia article, taken from Wikimedia Commons and resized to about 730 px. Four fruits (Nectarine, Raspberry, Tart Cherry, Queen Anne Cherry) use photos from the [Fruits-360](https://github.com/fruits-360) dataset by Mihai Oltean, CC BY-SA 4.0. Each photo is also credited on the page itself. Four photos (Apple, Apricot, Boysenberry, Rambutan) are under the GNU Free Documentation License 1.2.

| Fruit | Photo | Author | Licence |
|---|---|---|---|
| Apple | [Pink_lady_and_cross_section.jpg](https://commons.wikimedia.org/wiki/File:Pink_lady_and_cross_section.jpg) | fir0002 / Flagstaffotos | GFDL 1.2 |
| Apricot | [Apricot_and_cross_section.jpg](https://commons.wikimedia.org/wiki/File:Apricot_and_cross_section.jpg) | Fir0002 | GFDL 1.2 |
| Avocado | [Persea_americana_fruit_2.JPG](https://commons.wikimedia.org/wiki/File:Persea_americana_fruit_2.JPG) | B.navez | CC BY-SA 3.0 |
| Banana | [Bananavarieties.jpg](https://commons.wikimedia.org/wiki/File:Bananavarieties.jpg) | TimothyPilgrim | CC BY-SA 3.0 |
| Bing Cherry | [Bing_Cherries_(USDA_ARS).jpg](https://commons.wikimedia.org/wiki/File:Bing_Cherries_(USDA_ARS).jpg) | Peggy Greb, USDA ARS | Public domain |
| Blackberry | [Ripe,_ripening,_and_green_blackberries.jpg](https://commons.wikimedia.org/wiki/File:Ripe,_ripening,_and_green_blackberries.jpg) | Ragesoss | CC BY-SA 3.0 |
| Blueberry | [Blueberries.jpg](https://commons.wikimedia.org/wiki/File:Blueberries.jpg) | Oven Fresh | Public domain |
| Boysenberry | [Boysenberries.jpg](https://commons.wikimedia.org/wiki/File:Boysenberries.jpg) | — | GFDL 1.2 |
| Cantaloupe | [Meloen_vrucht_met_bloem.jpg](https://commons.wikimedia.org/wiki/File:Meloen_vrucht_met_bloem.jpg) | Rasbak | CC BY-SA 3.0 |
| Cherry | [Cherry_season_(48216568227).jpg](https://commons.wikimedia.org/wiki/File:Cherry_season_(48216568227).jpg) | spurekar | CC BY 2.0 |
| Clementine | [Clementines_whole,_peeled,_half_and_sectioned.jpg](https://commons.wikimedia.org/wiki/File:Clementines_whole,_peeled,_half_and_sectioned.jpg) | carol | CC BY-SA 3.0 |
| Crab Apple | [Malus_evereste.JPG](https://commons.wikimedia.org/wiki/File:Malus_evereste.JPG) | JMiall | CC BY 3.0 |
| Cucumber | [ARS_cucumber.jpg](https://commons.wikimedia.org/wiki/File:ARS_cucumber.jpg) | Stephen Ausmus, USDA ARS | Public domain |
| Damson Plum | [Damson_plum_fruit.jpg](https://commons.wikimedia.org/wiki/File:Damson_plum_fruit.jpg) | Jonathan Billinger | CC BY-SA 2.0 |
| Date | [Dates005.jpg](https://commons.wikimedia.org/wiki/File:Dates005.jpg) | Nepenthes | CC BY-SA 3.0 |
| Dewberry | [Rubus_caesius_fruit_-_Keila.jpg](https://commons.wikimedia.org/wiki/File:Rubus_caesius_fruit_-_Keila.jpg) | Ivar Leidus | CC BY-SA 4.0 |
| Dinosaur Egg | [Raspberry_jewel_pluot.jpg](https://commons.wikimedia.org/wiki/File:Raspberry_jewel_pluot.jpg) | BMRR | CC BY-SA 3.0 |
| Dragon Fruit | [Pitaya_cross_section_ed2.jpg](https://commons.wikimedia.org/wiki/File:Pitaya_cross_section_ed2.jpg) | SMasters | CC BY-SA 3.0 |
| Durian | [Durian_in_black.jpg](https://commons.wikimedia.org/wiki/File:Durian_in_black.jpg) | مانفی | CC BY-SA 4.0 |
| Eggfruit | [Egg_fruit_DS.jpg](https://commons.wikimedia.org/wiki/File:Egg_fruit_DS.jpg) | Augustus Binu | CC BY-SA 3.0 |
| Elderberry | [Sambucus-berries.jpg](https://commons.wikimedia.org/wiki/File:Sambucus-berries.jpg) | Edal Anton Lefterov | CC BY-SA 3.0 |
| Entawak | [Artocarpus_anisophyllus_fruit,_Desa_Kebadu,_Kecamatan_Balai,_Kabupaten_Sanggau_-_West_Kalimantan.jpg](https://commons.wikimedia.org/wiki/File:Artocarpus_anisophyllus_fruit,_Desa_Kebadu,_Kecamatan_Balai,_Kabupaten_Sanggau_-_West_Kalimantan.jpg) | Hadi Arifianto | CC BY-SA 4.0 |
| Evergreen Huckleberry | [Vacciniumovatum.jpg](https://commons.wikimedia.org/wiki/File:Vacciniumovatum.jpg) | Gordon Leppig & Andrea J. Pickart | Public domain |
| Fig | [Fig_cut_open.jpg](https://commons.wikimedia.org/wiki/File:Fig_cut_open.jpg) | FrogsLegs71 | CC BY-SA 3.0 |
| Finger Lime | [Finger_lime_with_juice_vesicles_and_seeds_partially_extracted.jpg](https://commons.wikimedia.org/wiki/File:Finger_lime_with_juice_vesicles_and_seeds_partially_extracted.jpg) | Ivar Leidus | CC BY-SA 4.0 |
| Gooseberry | [Stachelbeeren.jpg](https://commons.wikimedia.org/wiki/File:Stachelbeeren.jpg) | — | CC BY-SA 3.0 |
| Grape | [Grapes,_Rostov-on-Don,_Russia.jpg](https://commons.wikimedia.org/wiki/File:Grapes,_Rostov-on-Don,_Russia.jpg) | Vyacheslav Argenberg | CC BY 4.0 |
| Grapefruit | [Grapefruits_-_whole-halved-segments.jpg](https://commons.wikimedia.org/wiki/File:Grapefruits_-_whole-halved-segments.jpg) | Ivar Leidus | CC BY-SA 4.0 |
| Guava | [Guava_pink_fruit.jpg](https://commons.wikimedia.org/wiki/File:Guava_pink_fruit.jpg) | Ivar Leidus | CC BY-SA 4.0 |
| Hackberry | [Celtis_aetnensis.jpg](https://commons.wikimedia.org/wiki/File:Celtis_aetnensis.jpg) | Girolamo Giardina | CC BY-SA 3.0 |
| Honeycrisp Apple | [Honeycrisp-Apple.jpg](https://commons.wikimedia.org/wiki/File:Honeycrisp-Apple.jpg) | Evan-Amos | CC0 |
| Honeydew | [Honeydew.jpg](https://commons.wikimedia.org/wiki/File:Honeydew.jpg) | Yotoen | Public domain |
| Huckleberry | [Bog_huckleberry.jpg](https://commons.wikimedia.org/wiki/File:Bog_huckleberry.jpg) | VersicolorA | CC BY-SA 3.0 |
| Imbe | [Garcinialivingstonei.jpg](https://commons.wikimedia.org/wiki/File:Garcinialivingstonei.jpg) | Christopher Hind | Attribution |
| Indian Fig | [Cactus_fruit.jpg](https://commons.wikimedia.org/wiki/File:Cactus_fruit.jpg) | Snapdragon66 | CC BY-SA 3.0 |
| Indian Prune | [Flacourtia_jangomas_(Lubika).jpg](https://commons.wikimedia.org/wiki/File:Flacourtia_jangomas_(Lubika).jpg) | Augustus Binu | CC BY-SA 3.0 |
| Jackfruit | [The_jackfruit_is_holding_on_to_the_tree.jpg](https://commons.wikimedia.org/wiki/File:The_jackfruit_is_holding_on_to_the_tree.jpg) | Tushar Hossain | CC BY-SA 4.0 |
| Jambolan | [Kalo_jaam.JPG](https://commons.wikimedia.org/wiki/File:Kalo_jaam.JPG) | A junaid alam khan | Public domain |
| Java Apple | [2014-04-26_Syzygium_samarangense_04_anagoria.JPG](https://commons.wikimedia.org/wiki/File:2014-04-26_Syzygium_samarangense_04_anagoria.JPG) | Anagoria | CC BY 3.0 |
| Key Lime | [Citrus_×_aurantiifolia_(Christm.)_Swingle_(51906868474).jpg](https://commons.wikimedia.org/wiki/File:Citrus_×_aurantiifolia_(Christm.)_Swingle_(51906868474).jpg) | Dinesh Valke | CC BY-SA 2.0 |
| Kiwi | [Hardy-Kiwi-Comparison-3.jpg](https://commons.wikimedia.org/wiki/File:Hardy-Kiwi-Comparison-3.jpg) | Hiperpinguino | CC BY-SA 3.0 |
| Kumquat | [Kumquat_from_Spain.jpg](https://commons.wikimedia.org/wiki/File:Kumquat_from_Spain.jpg) | Ivar Leidus | CC BY-SA 4.0 |
| Lemon | [P1030323.JPG](https://commons.wikimedia.org/wiki/File:P1030323.JPG) | Elena Chochkova | CC BY-SA 4.0 |
| Lime | [Citrus_hystrix_dsc07772.jpg](https://commons.wikimedia.org/wiki/File:Citrus_hystrix_dsc07772.jpg) | David Monniaux | CC BY-SA 3.0 |
| Longan | [Frutos_Exóticos-LonganFruit-002.JPG](https://commons.wikimedia.org/wiki/File:Frutos_Exóticos-LonganFruit-002.JPG) | Nelson Ramos-Lopes | Public domain |
| Loquat | [Loquat-0.jpg](https://commons.wikimedia.org/wiki/File:Loquat-0.jpg) | Aftabbanoori | CC BY-SA 3.0 |
| Lychee | [Litchi_chinensis_fruits.JPG](https://commons.wikimedia.org/wiki/File:Litchi_chinensis_fruits.JPG) | B.navez | CC BY-SA 3.0 |
| Mandarin Orange | [Citrus_reticulata_April_2013_Nordbaden.JPG](https://commons.wikimedia.org/wiki/File:Citrus_reticulata_April_2013_Nordbaden.JPG) | 4028mdk09 | CC BY-SA 3.0 |
| Mango | [Mangos_-_single_and_halved.jpg](https://commons.wikimedia.org/wiki/File:Mangos_-_single_and_halved.jpg) | Ivar Leidus | CC BY-SA 4.0 |
| Melon | [Cantaloupe_and_canary_melon.jpg](https://commons.wikimedia.org/wiki/File:Cantaloupe_and_canary_melon.jpg) | Atomicbre | CC BY 3.0 |
| Mulberry | [Mulberry_in_Southern_Brazil.jpg](https://commons.wikimedia.org/wiki/File:Mulberry_in_Southern_Brazil.jpg) | Cwambier | CC BY-SA 4.0 |
| Nashi Pear | [Nashi_pear.jpg](https://commons.wikimedia.org/wiki/File:Nashi_pear.jpg) | — | CC BY-SA 3.0 |
| Navel Orange | [Navel_orange.jpg](https://commons.wikimedia.org/wiki/File:Navel_orange.jpg) | Enoryt nwased lamaj | CC BY-SA 4.0 |
| Nectarine | Fruits-360 dataset | Mihai Oltean (Fruits-360) | CC BY-SA 4.0 |
| Ogeechee Lime | [Ogeechee_Lime.jpg](https://commons.wikimedia.org/wiki/File:Ogeechee_Lime.jpg) | FloridaSwampFlower | CC BY-SA 3.0 |
| Olive | [Olivesfromjordan.jpg](https://commons.wikimedia.org/wiki/File:Olivesfromjordan.jpg) | Nickfraser | CC BY-SA 3.0 |
| Orange | [Oranges_-_whole-halved-segment.jpg](https://commons.wikimedia.org/wiki/File:Oranges_-_whole-halved-segment.jpg) | Ivar Leidus | CC BY-SA 4.0 |
| Oval Kumquat | [4-3-fortunella_margarita_21.jpg](https://commons.wikimedia.org/wiki/File:4-3-fortunella_margarita_21.jpg) | Archive | CC BY-SA 3.0 |
| Papaya | [Carica_papaya_005.JPG](https://commons.wikimedia.org/wiki/File:Carica_papaya_005.JPG) | H. Zell | CC BY-SA 3.0 |
| Passion Fruit | [Passion_fruits_-_whole_and_halved.jpg](https://commons.wikimedia.org/wiki/File:Passion_fruits_-_whole_and_halved.jpg) | Ivar Leidus | CC BY-SA 4.0 |
| Paw Paw | [Asimina_triloba3.jpg](https://commons.wikimedia.org/wiki/File:Asimina_triloba3.jpg) | Scott Bauer, USDA | Public domain |
| Peach | [Autumn_Red_peaches.jpg](https://commons.wikimedia.org/wiki/File:Autumn_Red_peaches.jpg) | Jack Dykinga, USDA | Public domain |
| Persimmon | [Fuyu_persimmon_fruits,_one_cut_open.jpg](https://commons.wikimedia.org/wiki/File:Fuyu_persimmon_fruits,_one_cut_open.jpg) | Frank Schulenburg | CC BY-SA 4.0 |
| Pineapple | [കൈതച്ചക്ക.jpg](https://commons.wikimedia.org/wiki/File:കൈതച്ചക്ക.jpg) | Suniltg | CC BY 3.0 |
| Pomegranate | [Pomegranate_Juice_(2019).jpg](https://commons.wikimedia.org/wiki/File:Pomegranate_Juice_(2019).jpg) | Augustus Binu | CC BY-SA 3.0 |
| Prickly Pear | [Cactus_fruit.jpg](https://commons.wikimedia.org/wiki/File:Cactus_fruit.jpg) | Snapdragon66 | CC BY-SA 3.0 |
| Quararibea | [Matisia_cordata_210159670.jpg](https://commons.wikimedia.org/wiki/File:Matisia_cordata_210159670.jpg) | Whaldener Endo | CC0 |
| Queen Anne Cherry | Fruits-360 dataset | Mihai Oltean (Fruits-360) | CC BY-SA 4.0 |
| Quince | [Bourgeat_Quince_(5207851992)_(cropped).jpg](https://commons.wikimedia.org/wiki/File:Bourgeat_Quince_(5207851992)_(cropped).jpg) | Leslie Seaton | CC BY 2.0 |
| Rambutan | [Rambutan_white_background_alt.jpg](https://commons.wikimedia.org/wiki/File:Rambutan_white_background_alt.jpg) | Muhammad Mahdi Karim | GFDL 1.2 |
| Raspberry | Fruits-360 dataset | Mihai Oltean (Fruits-360) | CC BY-SA 4.0 |
| Rose Hip | [Rose_hips.jpg](https://commons.wikimedia.org/wiki/File:Rose_hips.jpg) | Morn the Gorn | CC BY-SA 3.0 |
| Star Fruit | [Averrhoa_carambola_ARS_k5735-7.jpg](https://commons.wikimedia.org/wiki/File:Averrhoa_carambola_ARS_k5735-7.jpg) | USDA ARS | Public domain |
| Strawberry | [Garden_strawberry_(Fragaria_×_ananassa)_single2.jpg](https://commons.wikimedia.org/wiki/File:Garden_strawberry_(Fragaria_×_ananassa)_single2.jpg) | Ivar Leidus | CC BY-SA 4.0 |
| Sugar Baby Watermelon | [Taiwan_2009_Tainan_City_Organic_Farm_Watermelon_FRD_7962.jpg](https://commons.wikimedia.org/wiki/File:Taiwan_2009_Tainan_City_Organic_Farm_Watermelon_FRD_7962.jpg) | Fred Hsu | CC BY-SA 3.0 |
| Tamarind | [Tamarindus_indica_pods.JPG](https://commons.wikimedia.org/wiki/File:Tamarindus_indica_pods.JPG) | B.navez | CC BY 2.5 |
| Tangerine | [TangerineFruit.jpg](https://commons.wikimedia.org/wiki/File:TangerineFruit.jpg) | Brent Ramerth | CC BY-SA 3.0 |
| Tart Cherry | Fruits-360 dataset | Mihai Oltean (Fruits-360) | CC BY-SA 4.0 |
| Tomato | [Tomato_je.jpg](https://commons.wikimedia.org/wiki/File:Tomato_je.jpg) | Softeis | CC BY-SA 3.0 |
| Ugli Fruit | [Uniq_Fruit_from_Jamaica.jpg](https://commons.wikimedia.org/wiki/File:Uniq_Fruit_from_Jamaica.jpg) | Mostlund | CC BY-SA 3.0 |
| Ugni | [Ugni_molinae.jpg](https://commons.wikimedia.org/wiki/File:Ugni_molinae.jpg) | MPF | CC BY 2.5 |
| Uniq Fruit | [Uniq_Fruit_from_Jamaica.jpg](https://commons.wikimedia.org/wiki/File:Uniq_Fruit_from_Jamaica.jpg) | Mostlund | CC BY-SA 3.0 |
| Vanilla Bean | [Vanilla_6beans.JPG](https://commons.wikimedia.org/wiki/File:Vanilla_6beans.JPG) | B.navez | CC BY-SA 3.0 |
| Velvet Pink Banana | [Starr_080716-9301_Musa_velutina.jpg](https://commons.wikimedia.org/wiki/File:Starr_080716-9301_Musa_velutina.jpg) | Forest & Kim Starr | CC BY 3.0 |
| Watermelon | [Taiwan_2009_Tainan_City_Organic_Farm_Watermelon_FRD_7962.jpg](https://commons.wikimedia.org/wiki/File:Taiwan_2009_Tainan_City_Organic_Farm_Watermelon_FRD_7962.jpg) | Fred Hsu | CC BY-SA 3.0 |
| White Mulberry | [Morus-alba.jpg](https://commons.wikimedia.org/wiki/File:Morus-alba.jpg) | GerardM | CC BY-SA 2.1 es |
| Wolfberry | [Lycium_barbarum_-_Wolfberries_China_7-05.jpg](https://commons.wikimedia.org/wiki/File:Lycium_barbarum_-_Wolfberries_China_7-05.jpg) | Paul Gross and Richard Zhang | Public domain |
| Xango Mangosteen | [Mangosteens_-_whole_and_opened.jpg](https://commons.wikimedia.org/wiki/File:Mangosteens_-_whole_and_opened.jpg) | Ivar Leidus | CC BY-SA 4.0 |
| Xigua | [Taiwan_2009_Tainan_City_Organic_Farm_Watermelon_FRD_7962.jpg](https://commons.wikimedia.org/wiki/File:Taiwan_2009_Tainan_City_Organic_Farm_Watermelon_FRD_7962.jpg) | Fred Hsu | CC BY-SA 3.0 |
| Ximenia | [Ximenia_caffra01.jpg](https://commons.wikimedia.org/wiki/File:Ximenia_caffra01.jpg) | Paul venter | CC BY-SA 3.0 |
| Yangmei | [Yangmei_grown_in_Fremont,_California.jpg](https://commons.wikimedia.org/wiki/File:Yangmei_grown_in_Fremont,_California.jpg) | Lucuscal | CC BY-SA 4.0 |
| Zinfandel Grape | [Ripe_Zinfandel_grapes_in_Dry_Creek_Valley-8958.jpg](https://commons.wikimedia.org/wiki/File:Ripe_Zinfandel_grapes_in_Dry_Creek_Valley-8958.jpg) | Frank Schulenburg | CC BY-SA 4.0 |
| Zucchini | [CSA-Striped-Zucchini.jpg](https://commons.wikimedia.org/wiki/File:CSA-Striped-Zucchini.jpg) | Evan-Amos | Public domain |
