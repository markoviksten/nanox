# RAGAS Evaluointiraportti

**Aikaleima:** 20260130_062000

**Query Mode:** `mix`

**Testitapausten määrä:** 18

**Testin kesto:** 0:05:21 (321.5s)

**Token-käyttö (arvio):**
- Input tokens: 221,544
- Output tokens: 10,800
- Embedding tokens: 2,592
- **Yhteensä: 234,936 tokenia**

**Kustannusarvio:**
- LLM Input: $0.0332
- LLM Output: $0.0065
- Embeddings: $0.0003
- **Yhteensä: $0.0400**

---

## 📊 Kokonaistulokset

| Metriikka | Tulos | Status |
|-----------|-------|--------|
| Totuudenmukaisuus | 0.8711 | ✅ Erinomainen |
| Vastauksen relevanssi | 0.6888 | ⚠️ Hyvä |
| Kontekstin kattavuus | 0.9259 | ✅ Erinomainen |
| Kontekstin tarkkuus | 0.8318 | ✅ Erinomainen |
| **RAGAS Score (Keskiarvo)** | **0.8294** | **✅ Erinomainen** |

### Tulkinnat

- ✅ **0.80-1.00:** Erinomainen (Tuotantovalmis)
- ⚠️ **0.60-0.80:** Hyvä (Parannettavaa)
- ❌ **0.00-0.60:** Heikko (Vaatii optimointia)

---

## 🔍 Yksittäiset Testitapaukset

### Test Case #1

**Kysymys:**

Miten työaika kirjataan Netvisor-mobiiliapissa?

**Ground Truth (Odotettu vastaus):**

Työaika kirjataan Netvisor-mobiiliapissa valitsemalla vasemman yläkulman kolme viivaa, valitsemalla 'Työaika', kuittamalla työaika klikkaamalla harmaa päivä vihreäksi, ja tarvittaessa tekemällä muutokset päivän kohdalla '+'-painikkeella ja tallentamalla.

**Saatu vastaus (RAG):**

Työaika kirjataan Netvisor-mobiiliapissa seuraavasti: 

1. Avaa Netvisor mobiili-appi ja valitse vasemman yläkulman kolmesta viivasta "Työaika"-valikko.
2. Kuittaa työaika klikkaamalla harmaa päivävihreäksi. Tämä merkitsee kyseisen päivän työtuntien kirjaamista.
3. Jos työtunteihin on tehtävä muutoksia, klikkaa päivän kohdalla "+"-symbolia ja tee tarvittavat muutokset tunteihin. Tämän jälkeen muista klikata "Tallenna työtunnit".

Ohje sisältää vaiheittaiset vaiheet työaikakirjauksen tekemiseksi helpommin mobiililaitteella, mikä suositellaan työajan kirjaamiseen helpomman käytön vuoksi[^2][^3].

---

### References

- [2] HR DOC Työajanseuranta.pdf
- [3] DOC HR Loma- ja poissaolokirjaukset Netvisoriin.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

Extra-luokan 
mukaan. 
 
Lentoliput korvataan economy-luokan hintatason mukaan.  
 
Viisuminhankinta-, passi – ja passivalokuvamaksut korvataan verohallinnon voimassa 
olevien ohjeiden mukaisesti. Jos työnantaja kustantaa palkansaajalle passin, kysymyksessä 
on veronalainen etu (paitsi työtehtävistä johtuva kaksoispassin hankinta). Viisumin 
hankkiminen työskentelyvaltioon on työn suorittamisesta aiheutunut kustannus, jonka 
työnantaja voi korvata ilman, että syntyy veronalaista etua. Valuutanva...

**Konteksti 2:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

**Konteksti 3:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 4:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

</details>

---

### Test Case #2

**Kysymys:**

Kuinka kauan työaikatiedot on säilytettävä viranomaisille ja työntekijöille nähtäväksi?

**Ground Truth (Odotettu vastaus):**

Työaikatiedot on säilytettävä vähintään kahden vuoden ajan ja ne on näytettävä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle pyynnöstä.

**Saatu vastaus (RAG):**

Työaikatiedot on säilytettävä vähintään kahden vuoden ajan, ja niistä on tehtävä nähtäville pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle. Tämä velvollisuus perustuu työaikalakiin (872/2019), joka säätää, että työnantajan on pidettävä kirjaa tehdyistä työtunneista ja säilytettävä aineisto tämän ajan. Työaikatiedot liittyvät siis työajanseurantaan ja niiden säilyttäminen on tärkeää sekä työnantajan että viranomaisten valvontaa varten (ref. 2, 3).

### References

- [2] HR DOC Työajanseuranta.pdf
- [3] DOC HR Loma- and poissaolokirjaukset Netvisoriin.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

ipaikkaan ja matka 
tapahtuu pääosin normaalina työaikana ja ei täytä kokopäivärahan ehtoja, maksetaan 
vain matkasta aiheutuneet ylimääräiset kulut ilman päivärahaa.  
 
2. Koti- ja ulkomaanmatkat: Jos työnantaja järjestää toimihenkilölle ilmaisen ruoan, 
vähennetään päivärahakorvauksesta puolet. Ilmaisella ruoalla tarkoitetaan 
kokopäivärahan kyseessä ollen kahta ja osapäivärahan kyseessä ollen yhtä ilmaista 
ateriaa. Hotellihuoneen hintaan sisältyvää aamiaista ei lasketa työnantajan 
maksamak...

**Konteksti 2:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

**Konteksti 3:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 4:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

</details>

---

### Test Case #3

**Kysymys:**

Mistä linkistä voi tehdä matkalaskun netvisorissa selaimella?

**Ground Truth (Odotettu vastaus):**

Matkalaskun tekeminen Netvisoriin tapahtuu kirjautumalla osoitteeseen https://suomi.netvisor.fi.

**Saatu vastaus (RAG):**

Matkalaskun tekeminen Net visorissa selaimella onnistuu kirjautumalla seuraavan linkin kautta: [https://login.netvisor.fi](https://login.netvisor.fi). Tämä on Netvisorin kirjautumissivu, josta voit pääsee sisään ja tehdä matkalaskut selainversiolla.  

Lisäksi, ohjeen mukaan matkalaskun tekemisestä on saatavilla myös videomateriaalia, kuten esimerkiksi: [https://youtu.be/DPSDUv1Shb8](https://youtu.be/DPSDUv1Shb8).  

**Lähteet:**  
### References
- [1] HR DOC Matkustussääntö.pdf
- [2] HR DOC Matkalaskun tekeminen.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

. Matkaraportti 
Tarvittaessa matkalaskun yhteydessä tulee toimittaa matkaraportti esimiehelle. Matkaraportissa tulee 
kuvata keskeiset matkan tarkoitukseen liittyvät asiat. 
 
7. Luottokorttitilitykset 
 
Yrityksen luottokortilla maksettuja matka- ja edustuskuluja ei merkitä matkalaskuun. Alkuperäiset 
luottokorttiostotositteet liitetään luottokorttilaskuun. 
 
8. Bonuspisteet 
 
Eri lentoyhtiöillä on käytössään ohjelmia, joissa asiakas saa ohjelmassa sovittujen maksullisten lentojen 
ja muiden...

**Konteksti 2:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 3:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 4:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

</details>

---

### Test Case #4

**Kysymys:**

Mitä tulisi muistaa lisätä matkalaskuun, kun siihen merkitään osallistujat?

**Ground Truth (Odotettu vastaus):**

Selite-kohdassa tulee lisätä osallistuneiden nimet ja yrityksen nimi, jos asiakas tai muita henkilöitä osallistuu kulutukseen tai tarjoiluun.

**Saatu vastaus (RAG):**

Kun merkitään osallistujat matkalaskuun, on tärkeää muistaa lisätä heidän nimensä sekä mahdollisesti kuljetetun tavaran määrä ja sisältö. Tämä varmistaa, että matkalasku on täydellinen ja oikeudenmukainen, ja se auttaa dokumentoimaan osallistuneet henkilöt sekä kuljetetut esineet kulujen oikean kohdentamisen ja todentamisen puolesta.[1] Nämä tiedot tulisiLisätä selitteeseen, jotta matkakustannusten korvaus voidaan kattaa asianmukaisesti ja kuitattavien menojen yhteydessä.

### References

- [1] HR DOC Matkustussääntö.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

. Matkaraportti 
Tarvittaessa matkalaskun yhteydessä tulee toimittaa matkaraportti esimiehelle. Matkaraportissa tulee 
kuvata keskeiset matkan tarkoitukseen liittyvät asiat. 
 
7. Luottokorttitilitykset 
 
Yrityksen luottokortilla maksettuja matka- ja edustuskuluja ei merkitä matkalaskuun. Alkuperäiset 
luottokorttiostotositteet liitetään luottokorttilaskuun. 
 
8. Bonuspisteet 
 
Eri lentoyhtiöillä on käytössään ohjelmia, joissa asiakas saa ohjelmassa sovittujen maksullisten lentojen 
ja muiden...

**Konteksti 2:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 3:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 4:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

</details>

---

### Test Case #5

**Kysymys:**

Miten vuosiloma merkitään Netvisoriin mobiiliapissa?

**Ground Truth (Odotettu vastaus):**

Vuosiloma merkitään mobiiliapissa valitsemalla poissaolon Kirjauslaji ja lisäämällä alkamis- ja päättymispäivämäärä, jonka jälkeen tallennetaan. Vuosiloma käyttää kirjauslajia koodilla 02.

**Saatu vastaus (RAG):**

Vuosiloma merkitään Netvisorin mobiiliapissa seuraavasti:

1. Lataa Netvisorin mobiiliappi puhelimelle tai laitteelle.
2. Avaa sovellus ja siirry kohtaan **"Työaika"**.
3. Valitse kohta **"Lisää loma tai poissaolo"**.
4. Valitse poissaolon kirjauslaji ja lisää alku- ja lopppupäivämäärät. Vuosiloma merkitään kirjauslajilla **"02"**, joka vastaa vuosiloman kirjauslajia.
5. Tallenna tiedot.

Näin vuosiloma kirjataan järjestelmään mobiiliapilla oikealla kirjauslajilla, ja se näkyy jatkossa järjestelmässä vuosilomana, jonka työntekijä on pitänyt vuosilomana.

---

### References

- [2] DOC HR Loma- ja poissaolokirjaukset Netvisoriin.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

. Matkaraportti 
Tarvittaessa matkalaskun yhteydessä tulee toimittaa matkaraportti esimiehelle. Matkaraportissa tulee 
kuvata keskeiset matkan tarkoitukseen liittyvät asiat. 
 
7. Luottokorttitilitykset 
 
Yrityksen luottokortilla maksettuja matka- ja edustuskuluja ei merkitä matkalaskuun. Alkuperäiset 
luottokorttiostotositteet liitetään luottokorttilaskuun. 
 
8. Bonuspisteet 
 
Eri lentoyhtiöillä on käytössään ohjelmia, joissa asiakas saa ohjelmassa sovittujen maksullisten lentojen 
ja muiden...

**Konteksti 2:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 3:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 4:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

</details>

---

### Test Case #6

**Kysymys:**

Mitä poissaolon kirjauslajiä käytetään vuosiloman merkitsemiseen Netvisorissa?

**Ground Truth (Odotettu vastaus):**

Vuosiloma merkitään Kirjauslaji-valikon koodilla 02.

**Saatu vastaus (RAG):**

Vuosiloman merkitsemiseen Netvisorissa käytetään kirjauslajia, jonka koodi on **02**. Tämä kirjauslaji sisältää erilaisten poissaolotyyppien kirjauslajit, mutta vuosilomaa varten valitaan juuri tämä koodi.

**Lisäksi** ohjeiden mukaan vuosiloma merkitään joko mobiiliapissa tai selainversiossa valitsemalla oikea kirjauslaji ja lisäämällä alkupäivämäärä sekä loppupäivämäärä, ja lopuksi tallentamalla kirjaus. Tämä menettely mahdollistaa vuosiloman oikean kirjaamisen järjestelmään.

**Yhteenvetona:**  
- Vuosiloman kirjauslaji Netvisorissa on **koodi 02**.

### References
- [2] DOC HR Loma- ja poissaolokirjaukset Netvisoriin.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

Extra-luokan 
mukaan. 
 
Lentoliput korvataan economy-luokan hintatason mukaan.  
 
Viisuminhankinta-, passi – ja passivalokuvamaksut korvataan verohallinnon voimassa 
olevien ohjeiden mukaisesti. Jos työnantaja kustantaa palkansaajalle passin, kysymyksessä 
on veronalainen etu (paitsi työtehtävistä johtuva kaksoispassin hankinta). Viisumin 
hankkiminen työskentelyvaltioon on työn suorittamisesta aiheutunut kustannus, jonka 
työnantaja voi korvata ilman, että syntyy veronalaista etua. Valuutanva...

**Konteksti 2:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 3:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

**Konteksti 4:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

</details>

---

### Test Case #7

**Kysymys:**

Kuka hyväksyy matkasuunnitelman ulkomaan matkoille DOC-konsernissa?

**Ground Truth (Odotettu vastaus):**

Ulkomaan matkojen matkasuunnitelman hyväksyy toimitusjohtaja tai hänen erikseen valtuuttamansa esimies.

**Saatu vastaus (RAG):**

Ulkomaan matkoille DOC-konsernissa matkasuunnitelman hyväksyy toimitusjohtaja tai hänen erikseen valtuuttamansa esimies. Poikkeuksen muodostavat asiakkaalta laskutettavat huolto- ja asennusmatkat, jotka voivat päättää osaston päällikkö (Reference [1], s. 2/5). Näin ollen, ennen matkaa tapahtuva matkasuunnitelman hyväksyntä on tärkeä osa matkavalmisteluja ja varmistaa, että matkasuunnitelma on virallisesti vahvistettu oikean henkilön toimesta.

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

19.1.2023        1 / 5 
 
 
MATKUSTUSSÄÄNTÖ 
 
Matkustussääntöä noudatetaan kaikissa DOC-konsernin kotimaisissa yhtiöissä. 
 
1. Matkustaminen 
 
Yhtiön henkilöstö matkustaa tarvittaessa ylläpitääkseen, tukeakseen ja kehittääkseen liikesuhteita 
sidosryhmiin tai osallistuakseen yhtiön osoittamaan koulutukseen. 
 
Matkustamisessa käytetään pääsääntöisesti omia tai työsuhdeautoja tai edullisinta julkista 
liikennevälinettä riippuen tarkoituksen mukaisuudesta. 
 
Matkustamisesta aiheutuvat kustannu...

**Konteksti 2:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 3:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 4:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

</details>

---

### Test Case #8

**Kysymys:**

Miten matkakustannukset korvataan junamatkoissa DOC-konsernissa?

**Ground Truth (Odotettu vastaus):**

Junaliput korvataan Eko-luokan mukaan, ja perustellusta syystä voidaan korvata myös Extra-luokan mukaisesti.

**Saatu vastaus (RAG):**

Dokumenttien ja tietojen perusteella junamatkojen matkakustannusten korvaaminen DOC-konsernissa tapahtuu seuraavasti:

Junamatkojen matkakustannukset korvataan Eko-luokan mukaan. Junalippu, joka oikeuttaa junamatkan, on asiakirja, ja se korvataan Eko-luokan hintojen mukaan (reference_id: 1 ja 2). Tämä tarkoittaa, että korvaus perustuu junalipun tai matkalipun todelliseen hintaan, mutta käytössä on rajoituksena Eko-luokka.

Lisäksi junaliput ovat osa matkakustannusten korvaamista, ja niiden hankinta tulee dokumentoida kuitteja vastaan. Junaliput, kuten muut matkaliput, korvataan siis Eko-luokan hintatason mukaan ja korvaus perustuu asianmukaisesti hankittuun ja kuitattu asiakirjaan.

Yhtiössä matkakustannusten korvaaminen junamatkoissa sisältää siis seuraavat vaiheet:
- Lähteä matkasta junalipulla, joka oikeuttaa junamatkan.
- Junalipun tulee olla asiakirja, joka oikeuttaa matkustamiseen.
- Junalipun tai matkalipun hinta korvataan Eko-luokan mukaan.
- Matkan ja lipun dokumentointi kuitteja vastaan.

Näin ollen junamatkojen matkakustannukset korvataan yhtiössä junalipun tai vastaavan matkustusasiakirjan mukaisesti, käyttäen Eko-luokan hintatason mukaista korvausta.

---

### References

- [1] HR DOC Matkustussääntö.pdf
- [2] HR DOC Matkalaskun tekeminen.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

19.1.2023        1 / 5 
 
 
MATKUSTUSSÄÄNTÖ 
 
Matkustussääntöä noudatetaan kaikissa DOC-konsernin kotimaisissa yhtiöissä. 
 
1. Matkustaminen 
 
Yhtiön henkilöstö matkustaa tarvittaessa ylläpitääkseen, tukeakseen ja kehittääkseen liikesuhteita 
sidosryhmiin tai osallistuakseen yhtiön osoittamaan koulutukseen. 
 
Matkustamisessa käytetään pääsääntöisesti omia tai työsuhdeautoja tai edullisinta julkista 
liikennevälinettä riippuen tarkoituksen mukaisuudesta. 
 
Matkustamisesta aiheutuvat kustannu...

**Konteksti 2:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 3:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 4:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

</details>

---

### Test Case #9

**Kysymys:**

Miten työnantaja korvaa viisumin hankkimiskustannukset?

**Ground Truth (Odotettu vastaus):**

Työnantaja voi korvata viisumin hankkimisen työskentelyvaltioon liittyvät kustannukset veronalaista etua syntymättä, mikäli kyseessä ei ole työtehtävistä johtuva kaksoispassin hankinta.

**Saatu vastaus (RAG):**

Työnantaja voi korvata viisumin hankkimiskustannukset verohallinnon voimassa olevien ohjeiden mukaisesti. Tämä tarkoittaa, että viisumin ja passivalokuvien maksut korvataan työnantajalta, ja tämä korvaus noudattaa verohallinnon ohjeita, jotka on selkeästi määritelty matkakustannusten korvauskäytännöissä. 

Lisäksi on tärkeää huomata, että passin hankinnasta aiheutuvat kulut voidaan myös korvata samalla tavalla verohallinnon ohjeiden mukaisesti. Jos työnantaja kustantaa palkansaajalle passin, kyseessä on veronalainen etu, ellei se liity työtehtävistä johtuvaan kaksoispassin hankintaan. Viisumin hankkiminen liittyy työn suorittamisesta aiheutuvaan kustannukseen, jonka työnantaja voi korvata ilman, että siitä muodostuu veronalaista etua, mikäli tämä tapahtuu työn ohjeiden ja verohallinnon ohjeiden mukaisesti.

### References
- [1] HR DOC Matkustussääntö.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

Extra-luokan 
mukaan. 
 
Lentoliput korvataan economy-luokan hintatason mukaan.  
 
Viisuminhankinta-, passi – ja passivalokuvamaksut korvataan verohallinnon voimassa 
olevien ohjeiden mukaisesti. Jos työnantaja kustantaa palkansaajalle passin, kysymyksessä 
on veronalainen etu (paitsi työtehtävistä johtuva kaksoispassin hankinta). Viisumin 
hankkiminen työskentelyvaltioon on työn suorittamisesta aiheutunut kustannus, jonka 
työnantaja voi korvata ilman, että syntyy veronalaista etua. Valuutanva...

**Konteksti 2:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 3:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

**Konteksti 4:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

</details>

---

### Test Case #10

**Kysymys:**

Milloin maksetaan osapäivärahaa kotimaan matkalla?

**Ground Truth (Odotettu vastaus):**

Osapäiväraha maksetaan vajaalta matkavuorokaudelta, joka kestää vähintään 6 mutta enintään 10 tuntia, ja sitä maksetaan myös, jos työmatkaan käytetty aika ylittää viimeisen täyden matkavuorokauden vähintään 2 tunnilla.

**Saatu vastaus (RAG):**

Osapäivärahaa kotimaan matkalla maksetaan vajaalta matkavuorokaudelta, joka kestää vähintään 6 tuntia mutta enintään 10 tuntia. Jos kuitenkin matkalla käytetty aika ylittää viimeisen täyden (24 tunnin) matkavuorokauden vähintään 2 tunnilla, maksetaan osapäiväraha myös tästä ylityksestä. Lisäksi, jos matkustusaika on vähintään 6 tuntia ja alle 10 tuntia, maksetaan osapäiväraha tästä ajasta.

**Yhteenvetona:**  
- Vajaalta matkavuorokaudelta, joka kestää vähintään 6 ja enintään 10 tuntia, maksetaan osapäivärahaa.  
- Jos ylitetään 24 tunnin matkavuorokausi vähintään 2 tunnilla, maksetaan osapäiväraha myös tästä ylityksestä.

### References

- [1] HR DOC Matkustussääntö.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

Extra-luokan 
mukaan. 
 
Lentoliput korvataan economy-luokan hintatason mukaan.  
 
Viisuminhankinta-, passi – ja passivalokuvamaksut korvataan verohallinnon voimassa 
olevien ohjeiden mukaisesti. Jos työnantaja kustantaa palkansaajalle passin, kysymyksessä 
on veronalainen etu (paitsi työtehtävistä johtuva kaksoispassin hankinta). Viisumin 
hankkiminen työskentelyvaltioon on työn suorittamisesta aiheutunut kustannus, jonka 
työnantaja voi korvata ilman, että syntyy veronalaista etua. Valuutanva...

**Konteksti 2:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 3:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

**Konteksti 4:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

</details>

---

### Test Case #11

**Kysymys:**

Miten matkasta aiheutuneet ylimääräiset kulut korvataan, jos ne tapahtuvat normaalin työajan ulkopuolella eikä päivärahaa täytetä?

**Ground Truth (Odotettu vastaus):**

Matkasta aiheutuneet ylimääräiset kulut maksetaan vain matkasta ilman päivärahaa, koska tapahtuvat pääosin normaalina työaikana eivätkä täytä kokopäivärahan ehtoja.

**Saatu vastaus (RAG):**

Mikäli matkasta aiheutuneet ylimääräiset kulut liittyvät poikkeustilanteisiin, kuten tapahtuvat normaalin työajan ulkopuolella ja eivät täytä päivärahan maksamisen ehtoja, näitä kuluja korvataan kuitteja tai muiden tarkkojen selvitysten perusteella. Välttämättömistä menoista, kuten pesulasta ja internetistä, korvaus maksetaan vastaanotettujen kuittien tai selvitysten perusteella (Reference ID: 1, kohta 4.7).

Jos kulut liittyvät matkakuluihin, kuten esimerkiksi pesula- tai internet-kuluihin, korvaus maksetaan kuitteja vastaan. Tärkeää on, että kulut on dokumentoitu tarkasti ja liitetty matkalaskuun (Reference ID: 1, kohta 4.7).

**Tiivistettynä:**  
- Ylimääräiset kulut korvataan kuitteja tai muita selvityksiä vastaan.  
- Kulujen tulee olla välttämättömiä ja liittyä matkalla olevaan tarpeeseen.  
- Dokumentoidut menot liitetään matkalaskuun, ja korvaus maksetaan näiden perusteella.

### References

- [1] HR DOC Matkustussääntö.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

Extra-luokan 
mukaan. 
 
Lentoliput korvataan economy-luokan hintatason mukaan.  
 
Viisuminhankinta-, passi – ja passivalokuvamaksut korvataan verohallinnon voimassa 
olevien ohjeiden mukaisesti. Jos työnantaja kustantaa palkansaajalle passin, kysymyksessä 
on veronalainen etu (paitsi työtehtävistä johtuva kaksoispassin hankinta). Viisumin 
hankkiminen työskentelyvaltioon on työn suorittamisesta aiheutunut kustannus, jonka 
työnantaja voi korvata ilman, että syntyy veronalaista etua. Valuutanva...

**Konteksti 2:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 3:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

**Konteksti 4:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

</details>

---

### Test Case #12

**Kysymys:**

Miten työntekijä kirjaa työaikansa Netvisorissa ja mitä hänen tulee tehdä, jos työtuntien aikana tapahtuu muutoksia?

**Ground Truth (Odotettu vastaus):**

Työntekijä kirjaa työaikansa Netvisor-appissa valitsemalla 'Työaika' ja kuittaamalla päivän vihreäksi. Jos työtunteihin tulee muutoksia, hän klikkaa päivän kohdalta '+' ja tekee muutokset tunteihin sekä tallentaa ne. Työaikalaki velvoittaa kirjaamaan tehdyt työtunnit, jotka tulee säilyttää vähintään kaksi vuotta, ja näitä kirjaamisia tehdään viikoittain.

**Saatu vastaus (RAG):**

Työntekijä kirjaa työaikansa Netvisorissa käyttämällä Netvisor-mobiiliappia, joka on mobiilisovellus helpottamaan työajan kirjaamista. Työaikakirjausprosessiin liittyvät päävaiheet ovat seuraavat:

- **Työaika**n kirjaaminen aloitetaan avaamalla Netvisor-appi ja valitsemalla vasemmasta yläkulmasta kolme viivaa, josta valitaan "Työaika". 
- Tämän jälkeen työntekijä kuittaa työaikansa päivittäisinä valitsemalla päivän kohdalta harmaata päivää ja klikkaamalla sitä vihreäksi. 
- Jos työtuntien aikana tapahtuu muutoksia, työntekijä voi klikata päivän kohdalta "+"-ikonia ja tehdä tarvittavat muutokset tunteihin. 
- Muutosten jälkeen hänen tulee tallentaa päivitetyt työtunnit klikkaamalla "Tallenna työtunnit".

Työntekijän tulee suorittaa työaikakirjaus yleensä viikoittain, ja kaikissa vaiheissa ohjeet on esitetty Netvisorin ohjeissa (referenssi [2], DOC Työajanseuranta.pdf). Jos muutoksia on tehtävä jälkikäteen tai päivämäärissä, työntekijän on hyvä käyttää Netvisor-mobiiliappia mahdollisimman helpomman käytön vuoksi.

**Jos työtuntien aikana tapahtuu muutoksia**, hänen tulee klikata päivän kohdalta "+"-ikonia, tehdä tarvittavat muokkaukset tunteihin ja muuttaa tunnit halutessaan, minkä jälkeen ne on tallennettava. Näin varmistetaan, että työaikakirjaus pysyy ajan tasalla ja se on työnantajan nähtävissä työaikalain velvoitteiden mukaisesti.

---

### References

- [2] HR DOC Työajanseuranta.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

Extra-luokan 
mukaan. 
 
Lentoliput korvataan economy-luokan hintatason mukaan.  
 
Viisuminhankinta-, passi – ja passivalokuvamaksut korvataan verohallinnon voimassa 
olevien ohjeiden mukaisesti. Jos työnantaja kustantaa palkansaajalle passin, kysymyksessä 
on veronalainen etu (paitsi työtehtävistä johtuva kaksoispassin hankinta). Viisumin 
hankkiminen työskentelyvaltioon on työn suorittamisesta aiheutunut kustannus, jonka 
työnantaja voi korvata ilman, että syntyy veronalaista etua. Valuutanva...

**Konteksti 2:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

**Konteksti 3:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 4:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

</details>

---

### Test Case #13

**Kysymys:**

Miten työntekijä kirjaa vuosilomansa Netvisorin mobiili- ja selainversiossa?

**Ground Truth (Odotettu vastaus):**

Työntekijä lisää lomansa Netvisorin mobiiliapissa valitsemalla työaikaseurannan kautta 'Lisää loma tai poissaolo', valitsemalla poissaolon kirjauslajin, kuten koodilla 02 vuosiloma, ja lisäämällä alkamis- ja päättymispäivämäärän. Sama käytäntö pätee myös selainversiossa, missä kirjaus tehdään valitsemalla 'Uusi loma tai poissaolo' ja syöttämällä päivämäärät.

**Saatu vastaus (RAG):**

Työntekijä voi kirjata vuosilomansa Netvisorin mobiili- ja selainversiossa seuraavasti:

**Mobiiliappi:**  
- Lataa Netvisorin mobiiliappi puhelimelle tai laitteelle.  
- Navigoi kohtaan **Työaika**.  
- Valitse **Lisää loma tai poissaolo**.  
- Valitse poissaolon kirjauslaji, eli **Vuosiloma**, joka on kirjauslajikoodilla 02.  
- Lisää alkupäivämäärä ja loppupäivämäärä.  
- Tallenna kirjaus.  

**Selainversio:**  
- Kirjaudu Netvisoriin osoitteessa [https://login.netvisor.fi](https://login.netvisor.fi).  
- Mene kohtaan **Työaika**.  
- Valitse **Uusi loma tai poissaolo**.  
- Klikkaa **Lisää loma/poissaolo**.  
- Valitse poissaolon kirjauslaji **Vuosiloma**, joka on kirjauslajikoodilla 02.  
- Lisää alkupäivämäärä ja loppupäivämäärä.  
- Klikkaa **Tallenna**.  

Näin työntekijä merkitsee vuosilomansa järjestelmään kohdistamalla poissaolon kirjauslajin oikeaksi ja valitsemalla sopivan ajanjakson.

**Huom:** Vuosiloma merkitään kirjauslajilla 02, ja kirjaus näkyy järjestelmässä lomana, jonka työntekijä on pitänyt vuosilomana.

---

### References

- [2] DOC HR Loma- ja poissaolokirjaukset Netvisoriin.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

. Matkaraportti 
Tarvittaessa matkalaskun yhteydessä tulee toimittaa matkaraportti esimiehelle. Matkaraportissa tulee 
kuvata keskeiset matkan tarkoitukseen liittyvät asiat. 
 
7. Luottokorttitilitykset 
 
Yrityksen luottokortilla maksettuja matka- ja edustuskuluja ei merkitä matkalaskuun. Alkuperäiset 
luottokorttiostotositteet liitetään luottokorttilaskuun. 
 
8. Bonuspisteet 
 
Eri lentoyhtiöillä on käytössään ohjelmia, joissa asiakas saa ohjelmassa sovittujen maksullisten lentojen 
ja muiden...

**Konteksti 2:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 3:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

**Konteksti 4:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

</details>

---

### Test Case #14

**Kysymys:**

Miten vuosilomat ja poissaolot kirjaetaan sekä Netvisorin mobiili- että selainversiossa?

**Ground Truth (Odotettu vastaus):**

Vuosilomat ja poissaolot, kuten palkaton vapaa, sairausloma ja vanhempainvapaa, kirjataan Netvisorin työaikaseurantaan joko mobiiliapissa tai selainversiossa. Vuosiloma merkitään Kirjauslaji-valikon koodilla 02, ja kirjaus tehdään valitsemalla poissaolon kirjauslaji, lisäämällä alkamis- ja päättymispäivämäärä sekä tallentamalla.

**Saatu vastaus (RAG):**

Vuosilomat ja poissaolot kirjaavat itse työntekijät itse Netvisorin työaikaseurantaan, kuten on kuvattu DOCin työntekijöiden ohjeistuksessa. Kirjaaminen onnistuu sekä mobiili- että selainversiossa seuraavasti:

**Mobiiliappi:**
1. Lataa Netvisorin mobiiliappi puhelimeen tai laitteeseen.
2. Valitse työaikaseuranta ja sitten kohta "Lisää loma tai poissaolo".
3. Valitse poissaolon kirjauslaji (esim. vuosiloma) ja lisää alku- sekä loppiapäivämäärät.
4. Tallenna tiedot. 
   - Vuosiloma merkitään kirjauslajilla 02, joka tarkoittaa vuosilomaa.
   - Myös muut poissaolot, kuten palkaton vapaa, sairausloma ja vanhempainvapaa, löytyvät valikosta.

**Selainversio:**
1. Kirjaudu Netvisoriin osoitteessa https://login.netvisor.fi.
2. Siirry työaikaan -> Uusi loma tai poissaolo.
3. Valitse poissaolon kirjauslaji ja lisää alkupäivämäärä sekä lopppupäivämäärä.
4. Tallenna tiedot.
   - Vuosiloma merkitään kirjauslajilla 02 (Vuosiloma).
   - Muut poissaolot löytyvät myös valikosta ja kirjaantuvat samalla tavalla.

Näin työntekijät voivat itse tehdä vuosilomien ja poissaolojen kirjaamisen sujuvasti molemmissa versioissa joko mobiilisti tai tietokoneella.

---

### References

- [2] DOC HR Loma- ja poissaolokirjaukset Netvisoriin.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

ipaikkaan ja matka 
tapahtuu pääosin normaalina työaikana ja ei täytä kokopäivärahan ehtoja, maksetaan 
vain matkasta aiheutuneet ylimääräiset kulut ilman päivärahaa.  
 
2. Koti- ja ulkomaanmatkat: Jos työnantaja järjestää toimihenkilölle ilmaisen ruoan, 
vähennetään päivärahakorvauksesta puolet. Ilmaisella ruoalla tarkoitetaan 
kokopäivärahan kyseessä ollen kahta ja osapäivärahan kyseessä ollen yhtä ilmaista 
ateriaa. Hotellihuoneen hintaan sisältyvää aamiaista ei lasketa työnantajan 
maksamak...

**Konteksti 2:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 3:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 4:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

</details>

---

### Test Case #15

**Kysymys:**

Mistä löytyy ohjeet matkalaskun tekemiseen Netvisorissa?

**Ground Truth (Odotettu vastaus):**

Ohjeet matkalaskun tekemiseen Netvisorissa löytyvät YouTube-videoista, joita ovat https://youtu.be/DPSDUv1Shb8 ja https://youtu.be/Slvpf-iJ83s.

**Saatu vastaus (RAG):**

Ohjeet matkalaskun tekemiseen Netvisorissa löytyvät dokumentista **"Matkalaskun tekeminen"**, joka sisältää yksityiskohtaiset vaiheet ja vinkit matkalaskun laatimiseen Netvisor-järjestelmään. Tässä ohjeessa kerrotaan, kuinka voit tehdä matkalaskun joko selaimella tai mobiilisovelluksella, ja siihen liittyy myös videolinkkejä, jotka opastavat prosessin läpi.

Lisäksi ohje sisältää tärkeät vinkit matkalaskun täyttämiseen, kuten matkan otsikon määrittelyn, kululajien lisäämisen, ALV:n lisäämisen sekä tarvittavien liitteiden liittämisen. Ohje myös neuvoo, miten kuitit ja muut dokumentit liitetään matkalaskuun ja miten hallinnoida erilaisia kuluja ja kuluarvioita.

Kyseinen dokumentti löytyy nimellä **HR DOC Matkalaskun tekeminen.pdf**, ja se tarjoaa kattavat ohjeet matkalaskujen tekemiseen Netvisoriin.

### Referenssit
- [2] HR DOC Matkalaskun tekeminen.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

. Matkaraportti 
Tarvittaessa matkalaskun yhteydessä tulee toimittaa matkaraportti esimiehelle. Matkaraportissa tulee 
kuvata keskeiset matkan tarkoitukseen liittyvät asiat. 
 
7. Luottokorttitilitykset 
 
Yrityksen luottokortilla maksettuja matka- ja edustuskuluja ei merkitä matkalaskuun. Alkuperäiset 
luottokorttiostotositteet liitetään luottokorttilaskuun. 
 
8. Bonuspisteet 
 
Eri lentoyhtiöillä on käytössään ohjelmia, joissa asiakas saa ohjelmassa sovittujen maksullisten lentojen 
ja muiden...

**Konteksti 2:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 3:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 4:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

</details>

---

### Test Case #16

**Kysymys:**

Mikä on Netvisorin verkkosivun URL-osoite, johon kirjaudutaan matkalaskujen tekemiseksi?

**Ground Truth (Odotettu vastaus):**

Netvisorin verkkosivun URL-osoite on https://suomi.netvisor.fi.

**Saatu vastaus (RAG):**

Netvisorin verkkosivun URL-osoite, johon kirjaudutaan matkalaskujen tekemiseksi, on https://suomi.netvisor.fi [2]. Tämä sivusto mahdollistaa kirjautumisen pankkitunnuksilla ja matkalaskujen teon joko selaimen tai mobiilisovelluksen kautta.

### References

- [1] HR DOC Matkustussääntö.pdf
- [2] HR DOC Matkalaskun tekeminen.pdf
- [3] DOC HR Loma- ja poissaolokirjaukset Netvisoriin.pdf
- [4] HR DOC Työajanseuranta.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

. Matkaraportti 
Tarvittaessa matkalaskun yhteydessä tulee toimittaa matkaraportti esimiehelle. Matkaraportissa tulee 
kuvata keskeiset matkan tarkoitukseen liittyvät asiat. 
 
7. Luottokorttitilitykset 
 
Yrityksen luottokortilla maksettuja matka- ja edustuskuluja ei merkitä matkalaskuun. Alkuperäiset 
luottokorttiostotositteet liitetään luottokorttilaskuun. 
 
8. Bonuspisteet 
 
Eri lentoyhtiöillä on käytössään ohjelmia, joissa asiakas saa ohjelmassa sovittujen maksullisten lentojen 
ja muiden...

**Konteksti 2:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 3:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 4:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

</details>

---

### Test Case #17

**Kysymys:**

Kuka hyväksyy matkasuunnitelman ulkomaan matkoille yhtiössä?

**Ground Truth (Odotettu vastaus):**

Ulkomaan matkojen matkasuunnitelman hyväksyy toimitusjohtaja tai hänen erikseen valtuuttamansa esimies.

**Saatu vastaus (RAG):**

Ulkomaan matkojen matkasuunnitelman hyväksyy toimitusjohtaja tai hänen erikseen valtuuttamansa esimies. Poikkeuksena ovat asiakkaalta laskutettavat huolto- ja asennusmatkat, jotka voi päättää osaston päällikkö (Reference: [1], kohta 2.2 Ulkomaan matkat). Tämä menettely varmistaa, että matkasuunnitelma on asianmukaisesti hyväksytty ennen matkaan lähtöä.

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

19.1.2023        1 / 5 
 
 
MATKUSTUSSÄÄNTÖ 
 
Matkustussääntöä noudatetaan kaikissa DOC-konsernin kotimaisissa yhtiöissä. 
 
1. Matkustaminen 
 
Yhtiön henkilöstö matkustaa tarvittaessa ylläpitääkseen, tukeakseen ja kehittääkseen liikesuhteita 
sidosryhmiin tai osallistuakseen yhtiön osoittamaan koulutukseen. 
 
Matkustamisessa käytetään pääsääntöisesti omia tai työsuhdeautoja tai edullisinta julkista 
liikennevälinettä riippuen tarkoituksen mukaisuudesta. 
 
Matkustamisesta aiheutuvat kustannu...

**Konteksti 2:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 3:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 4:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

</details>

---

### Test Case #18

**Kysymys:**

Keneen tai mihin organisaatioon tai palveluun tulisi ottaa yhteyttä matkakuluihin liittyvissä kysymyksissä ja mistä löytyy tarvittavat yhteystiedot?

**Ground Truth (Odotettu vastaus):**

Matkalaskujen ja matkakorvausten asioissa yhteystiedot löytyvät taloushallinnon järjestelmästä, ja matkasuunnitelman hyväksymisestä vastaa esimies. Yhtiön luottokortti- ja matka- ja edustuskulujen määräykset liittyvät talousjohtajaan, jonka yhteystietoja ei ole annettu, mutta joita käytetään matkakorvausten yhteydessä. Näiden yhteystietojen tarkka sijainti ei käy ilmi dokumentista, mutta järjestelmät ja vastuuhenkilöt ovat taloushallinnon ja esimiehen roolien kautta yhteydessä.

**Saatu vastaus (RAG):**

Matkakuluihin liittyvissä kysymyksissä tulisi olla yhteydessä yrityksen taloushallintoon, joka vastaa matkalaskujen käsittelystä ja maksamisesta. Taloushallinto on organisaatio, johon kaikki kuitatut matkalaskut siirtyvät käsittelyä ja maksua varten. 

Tarvittavat yhteystiedot ja lisätietoja löytyy taloushallinnon järjestelmistä ja ohjeista, kuten Netvisorin työaikaseurannasta ja matkalaskujen tekemislinkeistä. Näihin ohjeisiin ja yhteystietoihin viitataan esimerkiksi matkalaskun tekemisohjeissa ja yrityksen sisäisissä materiaalipohjissa. 

Lisäksi matkan yhteydessä ja mahdollisissa vaatimuksissa voidaan olla yhteydessä esimiehiin tai liiketoimintajohtajiin, jotka tarkastavat kuitatut matkalaskut, mutta varsinaiset maksuliikenne- ja kysymykset liittyvät taloushallintoon.

### References
- [1] HR DOC Matkustussääntö.pdf
- [2] HR DOC Matkalaskun tekeminen.pdf

**Metriikat:**

| Metriikka | Tulos | Status |
|-----------|-------|--------|

<details>
<summary>📚 Haetut kontekstit (klikkaa nähdäksesi)</summary>

**Konteksti 1:**

19.1.2023        1 / 5 
 
 
MATKUSTUSSÄÄNTÖ 
 
Matkustussääntöä noudatetaan kaikissa DOC-konsernin kotimaisissa yhtiöissä. 
 
1. Matkustaminen 
 
Yhtiön henkilöstö matkustaa tarvittaessa ylläpitääkseen, tukeakseen ja kehittääkseen liikesuhteita 
sidosryhmiin tai osallistuakseen yhtiön osoittamaan koulutukseen. 
 
Matkustamisessa käytetään pääsääntöisesti omia tai työsuhdeautoja tai edullisinta julkista 
liikennevälinettä riippuen tarkoituksen mukaisuudesta. 
 
Matkustamisesta aiheutuvat kustannu...

**Konteksti 2:**

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

**Konteksti 3:**

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

**Konteksti 4:**

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

</details>

---

