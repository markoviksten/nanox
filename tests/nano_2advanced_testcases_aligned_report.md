# Testikysymysten Generointiraportti

**Luotu:** 2026-01-29 09:59:03

**Input tiedosto:** `vdb_chunks.json`

**Output tiedosto:** `nano_2advanced_testcases_aligned.json`

---

## 📊 Yhteenveto

| Metriikka | Arvo |
|-----------|------|
| **Luotuja kysymyksiä** | 48 kpl |
| **Generointi kesti** | 0:04:39 (279.4s) |
| **Input tokens** | 100,940 |
| **Output tokens** | 11,567 |
| **Yhteensä tokens** | 112,507 |
| **Input kustannus** | $0.0151 |
| **Output kustannus** | $0.0069 |
| **Kokonaiskustannus** | **$0.0221** |
| **Käytetty malli** | gpt-4o-mini |

---

## ⚙️ Konfiguraatio

### Chunk-määrät

| Chunk-tyyppi | Käytössä | Tavoite % |
|--------------|----------|----------|
| Single (1) | ✓ | 20% |
| Dual (2) | ✓ | 20% |
| Triple (3) | ✓ | 25% |
| Quad (4) | ✓ | 20% |
| Quint (5) | ✓ | 15% |

### Kysymystyypit

| Kysymystyyppi | Käytössä | Tavoite % |
|---------------|----------|----------|
| Short Factual | ✓ | 30% |
| Reasoning | ✓ | 40% |
| Synthesis | ✓ | 30% |

---

## 📈 Toteutunut Jakauma

### Kysymystyypit

| Tyyppi | Määrä | Osuus |
|--------|-------|-------|
| short_factual | 14 | 29.2% |
| reasoning | 20 | 41.7% |
| synthesis | 14 | 29.2% |

### Chunk-määrät

| Chunk-määrä | Määrä | Osuus |
|-------------|-------|-------|
| 1-chunk | 10 | 20.8% |
| 2-chunk | 10 | 20.8% |
| 3-chunk | 11 | 22.9% |
| 4-chunk | 10 | 20.8% |
| 5-chunk | 7 | 14.6% |

---

## 📝 Generoidut Testikysymykset

| # | Tyyppi | Chunkit | Kysymys | Ground Truth |
|---|--------|---------|---------|-------------|
| 1 | short_factual | 1 | Miten lomat ja poissaolot kirjataan Netvisorissa? | Lomat ja poissaolot kirjataan Netvisorin työaikaseurantaan, ja ne sovitaan aina ... |
| 2 | short_factual | 1 | Mitä voi tehdä Netvisorin mobiiliapissa? | Netvisorin mobiiliapissa voi seurata työaikaseurantaa, omia palkkakuittia, lomas... |
| 3 | short_factual | 1 | Mikä on kilometrikorvauksen edellytys, jos matka tehdään omalla autolla? | Jos matka on sovittu tehtäväksi omalla autolla, henkilölle maksetaan kilometriko... |
| 4 | short_factual | 2 | Miten työntekijä voi tehdä matkalaskun Netvisorissa? | Työntekijä voi tehdä matkalaskun joko tietokoneella Netvisoriin pankkitunnuksill... |
| 5 | short_factual | 2 | Kuinka pitkään työnantaja on velvoitettu säilyttämään työaikakirjanpito? | Työnantaja on velvoitettu säilyttämään työaikakirjanpito vähintään kahden vuoden... |
| 6 | short_factual | 2 | Miten työntekijät kirjaavat lomat Netvisorissa? | Työntekijät kirjaavat lomansa Netvisorin työaikaseurantaan joko mobiiliappilla t... |
| 7 | short_factual | 3 | Miten työntekijät kirjaavat lomat ja poissaolot Netvisorissa? | Työntekijät kirjaavat lomat ja poissaolot Netvisorin työaikaseurantaan joko mobi... |
| 8 | short_factual | 3 | Mitä sovitaan lomista ja miten ne kirjataan? | Lomat sovitaan aina esimiehen ja tiimin kanssa, ja ne kirjataan myös M-Filesiin ... |
| 9 | short_factual | 3 | Mitä ohjeita tulee noudattaa matkustamisessa DOC-konsernissa, kun matkalasku teh... | DOC-konsernissa matkustamisessa noudatetaan matkustussääntöä, joka vaatii matkas... |
| 10 | short_factual | 4 | Miten työntekijä voi kirjata lomansa ja poissaolonsa Netvisorissa ja mitä muita ... | Työntekijät voivat kirjata lomansa ja poissaolonsa Netvisorin työaikaseurantaan ... |
| 11 | short_factual | 4 | Mitä vaatimuksia tai ohjeita on matkasuunnitelman tekemiselle DOC-konsernin matk... | Matkasuunnitelman tulee olla esimiehen hyväksymä ennen matkalle lähtöä ja siinä ... |
| 12 | short_factual | 4 | Miten työntekijät kirjaavat vuosilomat ja poissaolot Netvisorissa ja mitä matkus... | Työntekijät kirjaavat vuosilomat ja muut poissaolot Netvisorin työaikaseurantaan... |
| 13 | short_factual | 5 | Mitä vaatimuksia työajanseuranta sisältää työnantajalle? | Työnantajan on pidettävä kirjaa tehdyistä työtunneista, näytettävä kirjanpito py... |
| 14 | short_factual | 5 | Miten loma tai poissaolo kirjataan Netvisorissa? | Loma tai poissaolo kirjataan Netvisorissa valitsemalla työaikaseurannassa 'Uusi ... |
| 15 | reasoning | 1 | Miksi työnantajan on velvollisuus pitää kirjaa tehdyistä työtunneista? | Työnantajan velvollisuus pitää kirjaa tehdyistä työtunneista johtuu työaikalaist... |
| 16 | reasoning | 1 | Miten työajan kirjaaminen tapahtuu Netvisor-appissa? | Työajan kirjaaminen Netvisor-appissa tapahtuu seuraavasti: ensin avataan mobiili... |
| 17 | reasoning | 1 | Miksi on tärkeää, että matkalaskussa täytetään punaisella tähdellä merkatut pako... | Punaisella tähdellä merkatut kohdat ovat pakollisia, jotta matkalasku voidaan kä... |
| 18 | reasoning | 1 | Miten matkalaskun teko Netvisorissa voi helpottaa hallinnon työtä? | Matkalaskun tekeminen Netvisorissa voi helpottaa hallinnon työtä, koska se mahdo... |
| 19 | reasoning | 2 | Miksi työnantaja on velvoitettu pitämään kirjaa työntekijöiden työtunneista ja m... | Työajanseuranta on tärkeää, koska Työaikalaki (872/2019) velvoittaa työnantajaa ... |
| 20 | reasoning | 2 | Miten matkalaskujen täyttämiseen liittyvät vaatimukset voivat vaikuttaa työnteki... | Matkalaskujen täyttämiseen liittyvät vaatimukset, kuten pakollisten kohtien täyt... |
| 21 | reasoning | 2 | Miksi työntekijöiden on tärkeää kirjata lomat ja poissaolot Netvisorin työaikase... | Työntekijöiden on tärkeää kirjata lomat ja poissaolot Netvisorin työaikaseuranta... |
| 22 | reasoning | 2 | Miten Netvisorin mobiiliappi helpottaa sekä matkalaskujen tekemistä että lomien ... | Netvisorin mobiiliappi helpottaa matkalaskujen tekemistä ja lomien kirjaamista t... |
| 23 | reasoning | 3 | Miksi työntekijöiden on tärkeää kirjata lomat ja poissaolot Netvisoriin, ja mite... | Työntekijöiden on tärkeää kirjata lomat ja poissaolot Netvisoriin, koska Työaika... |
| 24 | reasoning | 3 | Miten Netvisorin mobiiliappi helpottaa työntekijöitä lomien ja poissaolojen sekä... | Netvisorin mobiiliappi helpottaa työntekijöitä lomien ja poissaolojen kirjaamise... |
| 25 | reasoning | 3 | Miksi on tärkeää, että matkasäännöissä määritellään matkasuunnitelman hyväksymis... | Matkasäännöissä matkasuunnitelman hyväksymisprosessi ennen matkustamista varmist... |
| 26 | reasoning | 3 | Miten työntekijät voivat kirjata lomiaan ja poissaolojaan Netvisorissa, ja miksi... | Työntekijät kirjaavat lomansa ja poissaolonsa Netvisorin työaikaseurantaan valit... |
| 27 | reasoning | 3 | Miksi on tärkeää hyväksyä matkasuunnitelma ennen matkalle lähtemistä ja miten tä... | Matkasuunnitelman hyväksyminen ennen matkalle lähtöä on tärkeää, koska se varmis... |
| 28 | reasoning | 4 | Miksi on tärkeää, että työntekijät kirjaavat omat työtunnit, lomat ja matkalasku... | Työntekijöiden on tärkeää kirjata omat työtunnit, lomat ja matkalaskut Netvisori... |
| 29 | reasoning | 4 | Miten Netvisorin käyttö matkalaskujen, työajan ja lomien kirjaamisessa vaikuttaa... | Netvisorin käyttö matkalaskujen, työajan ja lomien kirjaamisessa vaikuttaa DOCin... |
| 30 | reasoning | 4 | Miksi matkalaskun täyttäminen Netvisorissa vaatii tarkkuutta ja mitä seurauksia ... | Matkalaskun täyttäminen Netvisorissa vaatii tarkkuutta, koska pakollisten kentti... |
| 31 | reasoning | 4 | Miten lomien ja poissaolojen kirjaaminen Netvisorissa liittyy matkustussääntöjen... | Lomien ja poissaolojen kirjaaminen Netvisorissa on tärkeä osa henkilöstöhallinto... |
| 32 | reasoning | 5 | Miksi työntekijän tulee kirjata matkansa ja miten se liittyy työaikalakiin ja ma... | Työntekijän on tärkeää kirjata matkansa Netvisoriin, koska se mahdollistaa matka... |
| 33 | reasoning | 5 | Miten eri matkustussäännöt vaikuttavat matkakustannusten korvaamiseen ja miksi o... | Matkustussäännöt vaikuttavat matkakustannusten korvaamiseen määrittelemällä, mit... |
| 34 | reasoning | 5 | Miksi on tärkeää, että työntekijät kirjavat vuosilomat ja poissaolot Netvisorin ... | Työntekijöiden on tärkeää kirjata vuosilomat ja poissaolot Netvisorin työaikaseu... |
| 35 | synthesis | 1 | Miten lomien ja poissaolojen kirjaaminen tapahtuu Netvisorin mobiiliappissa ja s... | Lomien ja poissaolojen kirjaaminen Netvisorin mobiiliappissa ja selainversiossa ... |
| 36 | synthesis | 1 | Miten komennusmatkojen ja matka-ajan korvauksen säännöt eroavat toisistaan tässä... | Komennusmatkoista, jotka kestävät yli kuusi kuukautta, tehdään erillinen komennu... |
| 37 | synthesis | 1 | Miten matkalaskun teko Netvisorissa etenee ja mitä vaatimuksia siihen liittyy? | Matkalaskun teko Netvisorissa alkaa kirjautumisesta pankkitunnuksilla osoitteess... |
| 38 | synthesis | 2 | Miten työajanseuranta Netvisorissa ja matkalaskujen teko Netvisorissa liittyvät ... | Työajanseuranta ja matkalaskujen teko Netvisorissa ovat molemmat työntekijöiden ... |
| 39 | synthesis | 2 | Miten matkalaskujen teko ja lomien kirjaaminen Netvisorissa liittyvät toisiinsa ... | Matkalaskujen teko ja lomien kirjaaminen Netvisorissa ovat molemmat itsepalvelup... |
| 40 | synthesis | 2 | Miten lomien ja poissaolojen kirjaaminen Netvisorissa liittyy matkustussuunnitel... | Lomien ja poissaolojen kirjaaminen Netvisorin kautta tapahtuu työntekijöiden its... |
| 41 | synthesis | 3 | Miten työntekijöiden työaikaseuranta, lomien ja poissaolojen kirjaaminen sekä ma... | Työntekijät kirjaavat itse työtuntinsa Netvisorin työaikaseurantaan, mikä on lak... |
| 42 | synthesis | 3 | Miten matkalaskujen teko, lomien kirjaaminen ja matkustussäännöt liittyvät toisi... | DOC-konsernissa matkalaskujen teko, lomien kirjaaminen ja matkustussäännöt ovat ... |
| 43 | synthesis | 3 | Miten lomien ja poissaolojen kirjaaminen Netvisorissa liittyy matkustussääntöjen... | Lomien ja poissaolojen kirjaaminen Netvisorin kautta on olennainen osa työntekij... |
| 44 | synthesis | 4 | Miten työaikaseuranta, matkalaskujen teko, lomien kirjaaminen ja matkustussäännö... | DOCissa työaikaseuranta, matkalaskujen teko, lomien kirjaaminen ja matkustussään... |
| 45 | synthesis | 4 | Miten matkalaskujen tekeminen, lomien kirjaaminen, matkustussäännöt ja matkakust... | Matkalaskujen tekeminen, lomien kirjaaminen, matkustussäännöt ja matkakustannust... |
| 46 | synthesis | 4 | Miten vuosilomien ja poissaolojen kirjaaminen Netvisorissa liittyy matkustussään... | Vuosilomien ja poissaolojen kirjaaminen Netvisorissa tapahtuu työntekijöiden toi... |
| 47 | synthesis | 5 | Miten työntekijöiden työaikaseuranta, lomakirjaus, matkalaskujen teko ja matkust... | DOCin toimintakäytännöissä työntekijöiden työaikaseuranta, lomakirjaus, matkalas... |
| 48 | synthesis | 5 | Miten matkalaskujen teko, lomien kirjaaminen ja matkustussäännöt liittyvät toisi... | Matkalaskujen teko Netvisorin kautta on olennainen osa DOCin työntekijöiden matk... |

---

## 🔍 Esimerkkejä (Ensimmäiset 5)

### Esimerkki 1: short_factual (1-chunk)

**Kysymys:**

Miten lomat ja poissaolot kirjataan Netvisorissa?

**Ground Truth:**

Lomat ja poissaolot kirjataan Netvisorin työaikaseurantaan, ja ne sovitaan aina esimiehen tai tiimin kanssa. Vuosiloma merkitään Kirjauslaji-valikon koodilla 02. Vuosiloma.

---

### Esimerkki 2: short_factual (1-chunk)

**Kysymys:**

Mitä voi tehdä Netvisorin mobiiliapissa?

**Ground Truth:**

Netvisorin mobiiliapissa voi seurata työaikaseurantaa, omia palkkakuittia, lomasaldoja sekä tehdä matkalaskuja.

---

### Esimerkki 3: short_factual (1-chunk)

**Kysymys:**

Mikä on kilometrikorvauksen edellytys, jos matka tehdään omalla autolla?

**Ground Truth:**

Jos matka on sovittu tehtäväksi omalla autolla, henkilölle maksetaan kilometrikorvaus työehtosopimusten ja verohallituksen ohjeiden mukaisesti.

---

### Esimerkki 4: short_factual (2-chunk)

**Kysymys:**

Miten työntekijä voi tehdä matkalaskun Netvisorissa?

**Ground Truth:**

Työntekijä voi tehdä matkalaskun joko tietokoneella Netvisoriin pankkitunnuksilla tai mobiiliappissa. Matkalaskun tekeminen voi tapahtua myös puhelimella, ja kaikki pakolliset kohdat tulee täyttää ennen tallentamista.

---

### Esimerkki 5: short_factual (2-chunk)

**Kysymys:**

Kuinka pitkään työnantaja on velvoitettu säilyttämään työaikakirjanpito?

**Ground Truth:**

Työnantaja on velvoitettu säilyttämään työaikakirjanpito vähintään kahden vuoden ajan. Tämä koskee sekä työntekijöiden työtunteja että matkalaskuja.

---

