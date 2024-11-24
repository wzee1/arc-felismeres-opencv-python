# Képfeldolgozás a gyakorlatban projektmunka #

**Készítette:** Farkas Zoltán

---

## Projekt leírás

**Téma:** Arcdetektálás és felismerés (OpenCV, Python) \
Ez a Python *(3.11.4)* program lehetőség biztosít adott képen megtalálható, \
valamint webkamerán megjelenő arcok valós idejű felismerésére és megjelölésére. \
Továbbá előre megadott személyek arcainak felismerésére, megjelölésére és az adott \
személy nevének visszaadására. \
A program az OpenCV Python könyvtárat használja az arcok detektálására, \
a hasonlóságokat az ismert arcokkal **Mean Squared Error** *(MSE)* \
alapú metrika segítségével határozza meg.

---

## Program funkcionalitásai

- **Képfájl alapú arcfelismerés**: \
Felismeri az arcokat egy adott képen, valamint egy kék színű négyzetbe helyezi azokat.
- **Webkamera alapú arcfelismerés**: \
Élő webkameraképen ismer fel arcokat, valamint egy kék színű négyzetbe helyezi azokat.
- **Ismert arcok betöltése**: \
Egy adott mappából betöltött ismert arcok alapján felismeri az embereket, kék színű négyzetbe helyezi az arcukat, és a fölé írja a nevüket.
- **Interaktív menürendszer**: \
Egyszerű, szöveges, konzolban futó felhasználói felület a funkciók használatához.

---

## Használati Utasítás

1. **Projektstruktúra**:
   ```
   root/
   ├── detect_faces.py
   ├── recognize_faces.py
   ├── main.py
   ├── sample_pictures/
   ├── output/
   ├── data/
   │   ├── keresztnev_vezeteknev/
   │   │   ├── 1.jpg
   │   │   ├── 1.jpg
   │   │   ├── ...
   │   │   ├── n.jpg
   │   ├── keresztnev_vezeteknev/
   │       ├── ... 
   ```
   Ahol a `sample_pictures/` mappa alapképeket tartalmaz, amelyeket fel lehet használni a program kipróbálásához. \
   Az `output/` mappa a kimeneti fájlokat fogja tartalmazni futás után.
1. A `data/` mappába helyezze az ismert személyek képeit a következő struktúrával:  
   ```
   data/
   ├── keresztnev_vezeteknev/
   │   ├── 1.jpg
   │   ├── 2.jpg
   │   ├── ...
   │   ├── n.jpg
   ├── ...
   ```
   **Alapvetően támogatott emberek:**
    - Andrew Garfield
    - Dwayne Johnson
    - Johnny Depp
    - Kanye West
    - Will Smith
2. Telepítse az `opencv-python` könyvtárat:
   ```bash
   pip install opencv-python
   ```
3. Futtassa a programot a `main.py` fájl indításával:
   ```bash
   python main.py
   ```
4. Válassza ki a kívánt funkciót a menüből:
   - Arcok detektálása (kép vagy webkamera)
   - Személyfelismerés képből

5. Kövesse a megjelenő utasításokat a megfelelő opció kiválasztásához.

---

## Modulok és Függvények

### `detect_faces.py`
#### 1. `detect_faces_image(image_path)`
- **Leírás**: Arcok detektálása egy adott képen.
- **Bemenet**:
  - `image_path` *(str)*: A kép fájl elérési útvonala.
- **Kimenet**: Megjeleníti a képet az arcok köré rajzolt keretekkel.

#### 2. `detect_faces_webcam()`
- **Leírás**: Arcok detektálása élő webkamera képén.
- **Kimenet**: Folyamatosan megjeleníti a webkamera képét, az arcok köré kereteket rajzolva.

---

### `recognize_faces.py`
#### 1. `load_known_faces(directory)`
- **Leírás**: Ismert arcok és nevek betöltése egy könyvtárból.
- **Bemenet**:
  - `directory` *(str)*: A könyvtár elérési útvonala, amely az ismert személyek képeit tartalmazza.
- **Kimenet**:
  - `known_faces` *(list)*: Az ismert arcok adatainak listája.
  - `known_names` *(list)*: Az ismert arcokhoz tartozó nevek listája.

#### 2. `recognize_faces(image_path, known_faces, known_names)`
- **Leírás**: Felismeri a képen lévő arcokat az ismert arcok adatbázisa alapján.
- **Bemenet**:
  - `image_path` *(str)*: A felismerni kívánt kép elérési útvonala.
  - `known_faces` *(list)*: Az ismert arcok adatainak listája.
  - `known_names` *(list)*: Az ismert arcokhoz tartozó nevek listája.
- **Kimenet**: Megjeleníti a felismerés eredményét, a felismeréshez tartozó névvel.

---

### `main.py`
#### Fő funkciók:
- **Menü**: A felhasználó választhat az arcok detektálása (kép vagy webkamera) és az ismert arcok felismerése között.
- **Interaktív működés**: Kérdés-válasz alapú adatbevitel a felhasználótól.

---

## Példa Futtatás

1. **Ismert arcok betöltése**:
   - A `data/` mappában lévő arcok automatikusan betöltődnek a program indulásakor.

2. **Arcok detektálása képen**:
   ```bash
   Válasszon egy opciót: 1
   Kép (1/a) vagy webkamera (2/b): 1
   Adja meg a kép elérési útvonalát: path/to/image.jpg
   ```

3. **Személyfelismerés**:
   ```bash
   Válasszon egy opciót: 2
   Adja meg a kép elérési útvonalát: path/to/image.jpg
   ```

4. **Kilépés**:
   ```bash
   Kilépéshez írja be: 'exit'
   ```

---

## Lábjegyzet

**Készítette:** Farkas Zoltán \
**Intézmény:** Debreceni Egyetem Informatika Kar \
**Kurzus:** Képfeldolgozás 2024 ősz \
**Verzió:** 1.0 *(2024.11.24)* \
**Licensz:** MIT-licenc