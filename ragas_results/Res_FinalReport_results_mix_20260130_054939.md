# RAGAS Evaluointiraportti

**Aikaleima:** 20260130_054939

**Query Mode:** `mix`

**Testitapausten määrä:** 18

**Testin kesto:** 0:07:37 (457.7s)

**Token-käyttö (arvio):**
- Input tokens: 224,976
- Output tokens: 10,800
- Embedding tokens: 3,450
- **Yhteensä: 239,226 tokenia**

**Kustannusarvio:**
- LLM Input: $0.0000
- LLM Output: $0.0000
- Embeddings: $0.0004
- **Yhteensä: $0.0004**

---

## 📊 Kokonaistulokset

| Metriikka | Tulos | Status |
|-----------|-------|--------|
| Totuudenmukaisuus | 0.9838 | ✅ Erinomainen |
| Vastauksen relevanssi | 0.3785 | ❌ Heikko |
| Kontekstin kattavuus | 0.8889 | ✅ Erinomainen |
| Kontekstin tarkkuus | 0.8164 | ✅ Erinomainen |
| **RAGAS Score (Keskiarvo)** | **0.7669** | **⚠️ Hyvä** |

### Tulkinnat

- ✅ **0.80-1.00:** Erinomainen (Tuotantovalmis)
- ⚠️ **0.60-0.80:** Hyvä (Parannettavaa)
- ❌ **0.00-0.60:** Heikko (Vaatii optimointia)

---

## 🔍 Yksittäiset Testitapaukset

### Test Case #1

**Kysymys:**

Miten työaika kirjataan Netvisorissa?

**Ground Truth (Odotettu vastaus):**

Työaika kirjataan Netvisorissa mobiili-appin kautta valitsemalla vasemman yläkulman kolme viivaa ja sitten 'Työaika'. Työaika kuittataan klikkaamalla harmaa päivä vihreäksi.

**Saatu vastaus (RAG):**

Työaika kirjataan Netvisorissa työajanseurannan kautta, joka liittyy työaikalakiin (872/2019). Työaikakirjaaminen tapahtuu joko Netvisorin mobiili-appilla tai selainversiolla.  

Mobiili-appi mahdollistaa työajan kirjaamisen helposti puhelimella tai laitteella. Ohjeiden mukaan työajan kirjaaminen sujuu seuraavasti:  
1. Avaa Netvisor mobiili-appi ja valitse vasemman yläkulman kolme viivaa.  
2. Valitse kohta "Työaika".  
3. Kuittaa työaika klikkaamalla harmaa päivä vihreäksi.  
4. Jos työtunneissa on muutoksia, klikkaa päivän kohdalta "+" ja tee tarvittavat muutokset tunteihin, sitten klikkaa "Tallenna työtunnit".  

Selainversiossa työaika kirjataan valitsemalla "Uusi loma tai poissaolo" ja valitsemalla poissaolon lajiksi oikea vaihtoehto, lisäämällä alkamis- ja lopetuspäivämäärät, ja tallentamalla tiedot.  

Työajan kirjaaminen voidaan siis tehdä molemmilla tavoilla, ja sitä suositellaan tehtäväksi viikoittain. Tätä toimintoa ohjaa työaikalaki, joka velvoittaa työnantajaa ja työntekijää huolehtimaan työaikasäännösten noudattamisesta.  

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

Kuinka kauan työnantaja on velvoitettu säilyttämään työaikakirjanpito?

**Ground Truth (Odotettu vastaus):**

Työnantaja on velvoitettu säilyttämään työaikakirjanpito vähintään kahden vuoden ajan.

**Saatu vastaus (RAG):**

Työnantaja on velvoitettu säilyttämään työaikakirjanpitoa vähintään kaksi vuotta. Tämä velvoite perustuu Työaikalakiin (872/2019), joka säätelee työajan kirjaamisen ja velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista ja säilyttämään sen aineiston pyydettäessä. Työaikalaki ohjaa käytäntöjä työajan kirjaamisessa ja edellyttää, että kirjaus säilytetään vähintään kahden vuoden ajan [2], [3].  

### References

- [2] HR DOC Työajanseuranta.pdf
- [3] DOC HR Loma- ja poissaolokirjaukset Netvisoriin.pdf

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

Mitä tietoja tarvitset matkalaskun täyttämiseen Netvisorissa?

**Ground Truth (Odotettu vastaus):**

Matkalaskun täyttämiseen Netvisorissa tarvitaan pakolliset kohdat, kuten matkan otsikko, muu kulu, kilometrikorvaus ja päiväraha. Lisäksi on tärkeää lisätä selite ja liite eli kuitti.

**Saatu vastaus (RAG):**

Matkalaskun täyttämiseen Netvisorissa tarvitsee seuraavat tiedot:

- Matkan otsikko, esimerkiksi "Tammikuu 2022" tai asiakkaan nimi, jonka voi lisätä matkalaskuun.
- Matkan kulut, kuten matkakulut, kilometrit ja mahdolliset päivärahat, jotka on merkitty oikeaan kohtaan.
- Kulutyyppi, esimerkiksi lounaskokous, edustuskulut tai lahjat, ja ALV-koodit, paitsi edustuskulut 0 %.
- Selite-kohdassa osallistuneiden henkilöiden nimet ja asiakkaiden/tavaroiden nimet, jos on kyse esimerkiksi osallistumisesta tapahtumaan.
- Liitteet, kuten kuitit tai muut selvitykset menoista.
- Mahdolliset kilometrikorvaukset ja päivärahat, sekä niiden tarkat tiedot.
- Matkan tarkoitus ja reitti, erityisesti jos menot liittyvät esim. työmatkaan tai asiakaskäynnille.
- Jos matkalle liittyviä muita kuluja tai erityistilanteita, kuten autolla tehty matka tai matkustustapa, nämä on myös syytä dokumentoida tarkasti.

Lisäksi on hyvä muistaa lisätä kaikki tositteet ja merkinnät, ja varmista, että kaikki vaaditut pakolliset kohdat on täytetty, kuten punaisella tähdellä merkatut kohdat ja selitteet. Tämä auttaa varmistamaan, että matkalasku voidaan käsitellä tehokkaasti ja oikein.

---

Jos haluat nähdä tarkemmat ohjeistukset, niihin voi tutustua esimerkiksi Netvisorin ohjevideoihin tai dokumentteihin, kuten Matkalaskun tekemisen ohjeeseen[2].

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

Miten matkalasku tallennetaan Netvisorissa?

**Ground Truth (Odotettu vastaus):**

Matkalasku tallennetaan Netvisorissa, kun kaikki valmiit rivit on täytetty ja lopuksi klikataan tallennuspainiketta.

**Saatu vastaus (RAG):**

Matkalaskun tallentaminen Netvisorissa tapahtuu heti matkan päätyttyä, ja siihen on liitettävä kaikki matkakulut todentavat tositteet tai muut selkeät menojen selvitykset [2, reference_id: "1"]. Matkalasku voidaan tehdä joko selaimella tai mobiilisovelluksella, ja ohjeet löytyvät esim. YouTube-videoista, kuten "Matkalaskun teko Netvisorissa" [2].

Matkalaskun tekeminen alkaa kirjautumalla Netvisoriin pankkitunnuksillasi osoitteessa https://suomi.netvisor.fi. Voit käyttää joko Netvisorin selainversiota tai mobiiliappia. Mobiiliappia käytettäessä kirjaaminen onnistuu helposti puhelimen tai laitteen kautta valitsemalla työaikaan liittyvät kohdat ja lisäämällä matka- tai muita kuluja [2].

Malliesimerkin mukaan matkalaskulle voidaan antaa otsikko, esimerkiksi matkan kuukausi tai asiakasfirman nimi. Kulutyyppien lisääminen, ALV:n lisääminen ja selitteet ovat myös mahdollisia, ja on tärkeää muistaa liittää kuitit tai tositteet hyvin tarkasti [2]. Kun kaikki tiedot on syötetty, tallennetaan ja lopuksi rivit sekä mahdolliset liitteet varmennetaan, että matkalasku on valmis hyväksyttäväksi [2].

Mikäli matkan aikana on ehtinyt kerätä useampia erillisiä matkalaskuja, niitä voi tehdä myös pidemmältä ajanjaksolta, kuten kuukaudesta, jonka jälkeen ne voidaan käydä läpi ja hyväksyä [2].

Lyhyesti: Matkalasku tallennetaan Netvisorissa kirjaamalla kaikki matkakulut järjestelmään, liittämällä kuitit ja tarkistamalla tiedot, ja lopuksi tallentamalla ja lähettämällä se hyväksyttäväksi [2].

### References

- [1] HR DOC Matkustussääntö.pdf
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

### Test Case #5

**Kysymys:**

Mikä on lomien ja poissaolojen kirjaamisen kirjauslaji vuosilomalle?

**Ground Truth (Odotettu vastaus):**

Vuosiloma merkitään Kirjauslaji-valikon koodilla 02. Vuosiloma.

**Saatu vastaus (RAG):**

Vuosiloman kirjauslaji on kirjauslajilla 02. Tämä laji sisältää vuosiloman kirjaamisen ja näkyy järjestelmässä lomana, jonka työntekijä on pitänyt vuosilomana. (Reference: [2])

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

### Test Case #6

**Kysymys:**

Mikä sovellus on käytössä poissaolojen kirjaamiseen DOCin työntekijöillä?

**Ground Truth (Odotettu vastaus):**

DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan.

**Saatu vastaus (RAG):**

DOCin työntekijöillä poissaolojen, kuten vuosilomien ja muiden poissaolojen, kirjaamiseen käytetään Netvisorin työaikaseurantajärjestelmää. Suomessa työaikalain (872/2019) velvoitteen mukaisesti työnantaja kirjaa ja säilyttää työaikatiedot, ja tämä kirjaaminen tapahtuu joko Netvisorin mobiiliapilla tai selainversiolla, jossa voi valita poissaolon kirjauslajin ja tarkentaa päivämäärät.[2] 

Lisäksi lomat ja poissaolot kirjataan myös M-Filesiin HR DOC Lomakalenteriin, mutta varsinaisen poissaolojen kirjaamisen järjestelmä on Netvisor.[2]

**Yhteenvetona:**  
- **Käytössä oleva sovellus poissaolojen kirjaamiseen DOCin työntekijöillä on Netvisor, erityisesti Netvisorin mobiili- ja selainversiot.**

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

Mitä matkasuunnitelmassa tulee määritellä?

**Ground Truth (Odotettu vastaus):**

Matkasuunnitelmassa tulee määritellä matkan tarkoitus, aikataulu (lähtö, paluu) ja reitti, matkakohde ja tavattavat henkilöt, matkustustapa, hotellien käyttö ja taso, mahdollinen auton vuokraus kohdepaikkakunnalla sekä arvio matkan kokonaiskustannuksista.

**Saatu vastaus (RAG):**

Matkasuunnitelmassa tulee määritellä seuraavat keskeiset asiat:

- Matkan tarkoitus
- Aikataulu, eli lähtö- ja paluuajat
- Reitti, joka kuvaa kulkureitin lähtöpaikasta kohteeseen
- Matkakohde
- Tavattavat henkilöt
- Matkustustapa (esim. juna, lento, linja-auto, laiva, yhtiön auto jne.)
- Hotellien käyttö ja taso
- Mahdollinen auton vuokraus kohdepaikkakunnalla
- Arvio matkan kokonaiskustannuksista

Tavoitteena on, että matkasuunnitelma on mahdollisimman kattava, jotta matkan suorittaminen on suunnitellusti ja kustannustehokkaasti mahdollista (Kohdat: [1], Reference).

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

### Test Case #8

**Kysymys:**

Kuka hyväksyy ulkomaan matkasuunnitelman?

**Ground Truth (Odotettu vastaus):**

Ulkomaan matkasuunnitelman hyväksyy toimitusjohtaja tai hänen erikseen valtuuttamansa esimies.

**Saatu vastaus (RAG):**

Ulkomaan matkasuunnitelman hyväksyy toimitusjohtaja tai hänen erikseen valtuuttamansa esimies. Tämä varmistaa, että matkasuunnitelma on asianmukaisesti tarkistettu ja hyväksytty ennen matkan aloittamista. 

Lisäksi poikkeuksena ovat asiakkaalta laskutettavat huolto- ja asennusmatkat, jotka voivat olla päättänyt osaston päällikkö. Näissä tapauksissa ei välttämättä tarvita toimitusjohtajan tai erikseen valtuutetun esimiehen hyväksyntää.

**Refence:** [1] HR DOC Matkustussääntö.pdf

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

Mikä on päivärahan edellytys?

**Ground Truth (Odotettu vastaus):**

Päivärahan edellytys on, että matkan pituus on vähintään 15 km työpaikasta tai asunnosta.

**Saatu vastaus (RAG):**

Päivärahan edellytys on, että matkalla on vähintään 15 km matka työpaikalta tai asuinpaikalta (ks. "Päiväraha lasketaan matkavuorokausittain" ja "Päivärahan edellytys on, että matkan pituus on vähintään 15 km työpaikasta tai asunnosta"). Lisäksi matkasta tulee olla kyseessä matka, joka tarkoittaa liikennettä paikasta toiseen ja sisältää matkakuluja (ks. "Matka tarkoittaa liikennettä paikasta toiseen, sisältäen matkakuluja ja liittyviä ehtoja"). 

Päiväraha lasketaan matkavuorokauden perusteella, ja matkavuorokausi tarkoittaa 24 tunnin jaksoa, jonka alusta tai päättymisestä päiväraha määräytyy. Kotimaan päiväraha maksetaan vähintään 15 km matkasta, ja osapäiväraha perustuu matkustusajasta ja matkavuorokauden kestosta (ks. "Kotimaan päiväraha maksetaan vähintään 15 km matkasta, ja osapäiväraha määräytyy matkustusajasta"). Ulkomaan päiväraha taas määräytyy matkavuorokauden päättymispaikan mukaan ja laskettuna matkasta ulkomailla (ks. "Ulkomaan päiväraha määräytyy matkavuorokauden päättymispaikan mukaan ja laskettuna matkasta ulkomailla").

Lisäksi poikkeustilanteet voivat vaikuttaa päivärahojen maksamiseen poikkeuksellisten säädösten vuoksi (ks. "Poikkeustilanteisiin liittyvät säädökset voivat vaikuttaa päivärahojen maksamiseen").

### References

- [1] HR DOC Matkustussääntö.pdf
- [2] HR DOC Työajanseuranta.pdf
- [3] HR DOC Matkalaskun tekeminen.pdf

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

DOC MATKALASKUN TEKEMINEN
Docilla jokainen tekee itse matkalaskunsa Netvisoriin, eli korƫmaksut/kuiƟt, kilometrikorvaukset ja 
mahdolliset pvärahat hoituvat sitä kauƩa. 
Jokaiselle on avaƩu palkansaajatunnukset Netvisoriin matkalaskujen tekoa varten.
1. Kirjaudu Ɵetokoneella Netvisoriin pankkitunnuksillasi hƩps://suomi.netvisor.ﬁ
2. Lataa ”Netvisor”-mobiiliappi puhelimeen ja kirjaudu sinnekin (appissa näet myös mm. palkka- ja
verokorƫƟetosi, myös lomaƟedot ja tarviƩaessa työaikaseuranta)
3. Tee ...

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

Miten työntekijät voivat tehdä matkalaskuja Netvisorissa?

**Ground Truth (Odotettu vastaus):**

Työntekijät voivat tehdä matkalaskuja Netvisorissa joko tietokoneella tai mobiiliappilla kirjautumalla pankkitunnuksillaan Netvisoriin. Matkalaskun täyttämisessä on huomioitava pakolliset kohdat, kuten matkan otsikko ja selite, ja kuitit tulee liittää mukaan.

**Saatu vastaus (RAG):**

Työntekijät voivat tehdä matkalaskuja Netvisorissa seuraamalla ohjeita ja käyttämällä järjestelmän tarjoamia toimintoja. Matkalaskun tekeminen edellyttää, että työntekijällä on palkansaajatunnukset, jotka mahdollistavat pääsyn Netvisor-järjestelmään.  

Ensimmäinen vaihe on kirjautua Netvisoriin joko tietokoneelta tai mobiililaitteelta. Kirjautumisen jälkeen hän voi valita joko selaimen kautta tai Netvisor mobiiliappi-sovelluksen avulla matkalaskun tekemisen.  

Matkalaskun tekoon on ohjeistettu kaksi päämenetelmää: tietokoneen selaimella tai mobiilisovelluksella. Klikkaamalla esimerkiksi "Matkan otsikko" -kenttään, hän voi otsikoida matkansa, kuten "Tammikuu 2022". Tämän jälkeen hän lisää kuluja valitsemalla "Lisää muu kulu" ja valitsemalla oikean kulutyypin, kuten "Kokous ja neuvottelukulut" tai "Edustuskulut". Kulutyyppiin voi liittyä myös ALV:n lisääminen.  

Lisäksi on tärkeää liittää kuitit menolaskuun, kuten matkaliput, hotellien kuitit, ruokailukulut ja muut tositteet, jotka todentavat kulut. Matkan ajankohta, osallistuneet henkilöt ja mahdollinen kuljetettujen tavaroiden määrä tulee myös dokumentoida matkaan liittyvässä selitteessä.  

Matkalaskun lopuksi tallennetaan ja varmennetaan kaikki rivit, ja mahdollisesti tehdään pidempi matkalasku esimerkiksi kuukauden ajalta. Kun matkalasku on valmis, sen kuitatut menoerät arvioidaan ja hyväksytään liiketoimintajohtajan sekä talousjohtajan toimesta.  

Mitä tulee ohjeisiin, työntekijöitä kehotetaan myös liittämään matkaraportti, mikäli sitä vaaditaan, ja varmistamaan, että kaikki matkakuluja koskevat kuitit ja selvitykset ovat liitettynä ja asianmukaisesti dokumentoitu.  

Näin varmistetaan, että matkalasku on valmis hyväksyttäväksi ja maksaa ajallaan, kuten ohjeistuksessa mainitaan, että matkalaskut pyritään käsittelemään ja maksamaan viikottain.  

> Referenssit:  

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

Miten työaikojen kirjaaminen tapahtuu Netvisorin mobiili-appissa?

**Ground Truth (Odotettu vastaus):**

Työaikojen kirjaaminen Netvisorin mobiili-appissa tapahtuu klikkaamalla vasemmassa yläkulmassa kolmea viivaa, valitsemalla 'Työaika' ja kuittaamalla työaika klikkaamalla harmaata päivää vihreäksi. Mikäli työtunneissa on muutoksia, ne voidaan muuttaa päivän kohdalla lisäämällä tunteja ja tallentamalla ne.

**Saatu vastaus (RAG):**

Työaikojen kirjaaminen Netvisorin mobiili-appissa tapahtuu seuraavasti:  

1. Avaa Netvisor mobiili-appi ja valitse vasemman yläkulman kolme viivaa.  
2. Valitse valikosta vaihtoehto ”Työaika”.  
3. Kuittaa työaika klikkaamalla harmaa päivä vihreäksi.  
4. Jos työtunneissa on muutoksia, klikkaa päivän kohdalta ”+” ja tee tarvittavat muutokset tunteihin.  
5. Tallenna työaikasi klikkaamalla ”Tallenna työtunnit”.  

Ohjeiden mukaan työajan kirjaaminen suositellaan tehtävän viikoittain, mikä helpottaa työpäivien ja tuntien hallintaa.  

### References

- [2] HR DOC Työajanseuranta.pdf

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

### Test Case #12

**Kysymys:**

Mitä ohjelmaa käytetään lomien ja poissaolojen kirjaamiseen?

**Ground Truth (Odotettu vastaus):**

Lomien ja poissaolojen kirjaamiseen käytetään Netvisoria, johon työntekijät kirjaavat omat vuosilomat ja muut poissaolot. Myös matkalaskut voidaan tehdä Netvisorin mobiiliappissa ja selainversiossa.

**Saatu vastaus (RAG):**

Lomien ja poissaolojen kirjaamiseen käytetään Netvisoria, joka sisältää sekä mobiiliapplikaation että selainversion. Näissä järjestelmissä työntekijät voivat itse kirjaata vuosilomansa ja muut poissaolonsa, kuten palkattoman vapaan, sairausloman ja vanhempainvapaan. Lomien ja poissaolojen kirjaaminen on ohjeistettu Netvisorin mobiiliapilla ja selainversiolla, joissa valitaan poissaolon laji ja määritellään päivämäärät (reference_id: 2).

Lisäksi lomien kirjaaminen tapahtuu myös M-Filesin HR DOC Lomakalenteriin, mikäli tarvitaan. Netvisor sisältää monipuolisia toimintoja lomien ja poissaolojen kirjaamiseen ja tarjoaa helpon tavan päivittää tiedot sekä puhelimella että selaimella (reference_id: 2).

### References

- [1] HR DOC Matkustussääntö.pdf
- [2] DOC HR Loma- ja poissaolokirjaukset Netvisoriin.pdf
- [3] HR DOC Työajanseuranta.pdf
- [4] HR DOC Matkalaskun tekeminen.pdf

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

### Test Case #13

**Kysymys:**

Miksi työajanseuranta on tärkeää työnantajalle, ja mitä velvoitteita se tuo mukanaan?

**Ground Truth (Odotettu vastaus):**

Työajanseuranta on tärkeää työnantajalle, koska Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista. Tämä tarkoittaa, että työnantajan on näytettävä kirjanpito pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle. Lisäksi työnantajan on säilytettävä aineisto vähintään kahden vuoden ajan, mikä auttaa varmistamaan lain noudattamisen ja työntekijöiden oikeuksien toteutumisen.

**Saatu vastaus (RAG):**

Työajanseuranta on tärkeää työnantajalle, koska se liittyy työajan kirjaamiseen ja työnantajan velvollisuuksiin työntekijöitä koskevassa työaikalain (872/2019) alaisuudessa. Työajanseuranta varmistaa, että työnantaja pitää kirjaa tehdyistä työtunneista, mikä on lakisääteinen velvoite työaikalain puitteissa [[2](HR DOC Työajanseuranta.pdf)].

Velvoitteet, jotka tämä velvollisuus tuo mukanaan, sisältävät seuraavat keskeiset kohdat:
- Työnantajan on pidettävä kirjaa tehdyistä työtunneista ja säilytettävä tämä aineisto vähintään kahden vuoden ajan [[2](HR DOC Työajanseuranta.pdf)].
- Kirjanpidon tulee olla nähtävissä pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle [[2](HR DOC Työajanseuranta.pdf)].
- Työajan kirjaaminen tehdään joko Netvisorissa tai Severassa, mutta Netvisorin tapauksessa suositellaan Netvisor-appin käyttöä, koska se on helpompi ja mahdollistaa kirjaamisen helposti parilla näppäilyllä [[2](HR DOC Työajanseuranta.pdf)].
- Työntekijä on oikeutettu näkemään kirjanpidon ja voi pyytää sitä työnantajalta [[2](HR DOC Työajanseuranta.pdf)].

Näin ollen työajanseuranta auttaa työnantajaa noudattamaan työaikalain vaatimuksia sekä mahdollistaa oikean työaikakirjanpidon ylläpitämisen ja valvonnan.

### References

- [1] HR DOC Matkustussääntö.pdf
- [2] HR DOC Työajanseuranta.pdf
- [3] HR DOC Matkalaskun tekeminen.pdf
- [4] DOC HR Loma- ja poissaolokirjaukset Netvisoriin.pdf

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

DOC Työajanseuranta
Työaikalaki (872/2019) velvoittaa työnantajaa pitämään kirjaa tehdyistä työtunneista, näyttämään
kirjanpidon pyydettäessä työntekijälle, työsuojeluviranomaiselle tai työntekijöiden edustajalle sekä
säilyttämään aineiston vähintään kahden vuoden ajan.
Työajan kirjaaminen tehdään omassa Netvisorissa tai Severassa. Netvisorin tapauksessa Netvisor-appin
käyttö suositeltavaa (helpompaa kuin koneella), siellä kirjaaminen tapahtuu helposti parilla näppäilyllä, siitä
ohjeet alla. Työ...

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

24.5.2024 
 
 
 
 
 
 
 
 
 
 
LOMIEN JA POISSAOLOJEN KIRJAAMINEN  
 
1.  Lomien ja p oissaolojen kirjaaminen  
 
DOCin työntekijät kirjaavat itse vuosilomat ja muut poissaolonsa Netvisorin työaikaseurantaan. Vuosiloman lisäksi muita poissaoloja ovat 
mm. palkaton vapaa, sairausloma ja vanhempainvapaa. Lomat sovitaan aina esimiehen/tiimin kanssa ja kirjataan myös M-Filesiin HR 
DOC Lomakalenteriin. 
 
Netvisorin mobiiliappissa ja selainversiossa löytyy työaikaseurannan lisäksi mm. omat palkkakui...

</details>

---

### Test Case #14

**Kysymys:**

Miten työajan kirjaaminen tapahtuu Netvisorissa ja miksi se suositellaan tehtäväksi viikoittain?

**Ground Truth (Odotettu vastaus):**

Työajan kirjaaminen Netvisorissa tapahtuu mobiili-appin kautta, jossa käyttäjä valitsee 'Työaika' ja kuittaa työajan klikkaamalla harmaa päivä vihreäksi. Jos työtunneissa on muutoksia, käyttäjä voi tehdä ne helposti ja tallentaa muutokset. Työajan kirjaamista suositellaan tehtäväksi viikoittain, koska se helpottaa tuntien hallintaa ja varmistaa ajantasaisen ja tarkan kirjanpidon.

**Saatu vastaus (RAG):**

Työajan kirjaaminen Netvisorissa tapahtuu työaikatietojen syöttämisen kautta, jossa kirjaudaan tehtyjä työtunteja, ja siihen on mahdollisuus tehdä muokkauksia sekä tallentaa kirjaus. Ohjeiden mukaan työaikaa kirjaamalla varmistetaan, että työtuntien kirjaaminen tehdään vaiheittain Netvisor mobiili-appilla, aloittamalla valitsemalla ”Työaika” ja varmentamalla päivän tunnit klikkaamalla harmaata päivää vihreäksi. Jos työtunteihin tehdään muutoksia, päivämäärän kohdalta klikataan ”+” ja päivitetään tunnit, jonka jälkeen ne tallennetaan.

Työajan kirjaamisen suositellaan tehtäväksi viikoittain, koska tämä auttaa ylläpitämään ajantasaista ja järjestelmällistä kirjanpitoa. Vähentää unohduksia ja virheitä sekä varmistaa, että työaikatiedot ovat oikeassa muodossa arvioidun raportoinnin ja lain vaatimusten täyttämisen kannalta. Työaikakirjaus ohjeistuksineen auttaa myös työnantajaa täyttämään työaikalain (872/2019) velvoitteet, jotka edellyttävät, että työaikaa kirjaudaan säännöllisesti ja asianmukaisesti.

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

### Test Case #15

**Kysymys:**

Miksi on suositeltavaa tehdä matkalasku pidemmältä ajalta, kuten kuukaudelta?

**Ground Truth (Odotettu vastaus):**

Pidemmältä ajalta, kuten kuukaudelta, matkalaskun tekeminen helpottaa hallinnon työtä. Tämä johtuu siitä, että matkalaskun voi otsikoida, esimerkiksi 'Helmikuu 2023', ja täytellä ja tallennella sitä vähitellen. Tällöin on myös mahdollista koota useita kuluja yhteen laskuun, mikä voi säästää aikaa ja vaivannäköä laskujen käsittelyssä.

**Saatu vastaus (RAG):**

On suositeltavaa tehdä matkalasku pidemmältä ajalta, kuten esimerkiksi kuukaudelta, koska se helpottaa hallinnon työtä ja tehostaa maksuprosessia. Tämä lähestymistapa mahdollistaa sen, että kaikki menoerät voidaan kirjata yhdellä kertaa ja lopuksi käsitellä kokonaisuudessaan, mikä vähentää työtaakkaa ja virheiden mahdollisuutta. Lisäksi tällaiseen järjestelyyn voi otsikoida matkalaskun esimerkiksi kuukauden tai ajanjakson mukaan (esim. "Helmikuu 2023"), mikä helpottaa seurattavuutta ja järjestelmällisyyttä taloushallinnossa.

Näin ollen, pidennetyllä aikavälillä tehty matkalasku sujuvoittaa prosesseja ja vähentää tarvetta tehdä useita pienempiä laskuja, mikä puolestaan tehostaa maksujen käsittelyä ja varmistaa, että kaikki kulut tulevat asianmukaisesti huomioiduiksi yhdessä maksuerässä.

> Muutama lisävinkki asiaan liittyen: "Tee matkalasku pidemmältä ajalta, esim. 1kk, helpottaa hallinnon työtä ja lopuksi kuihtaa valmis matkalasku." (Ref [2])

### References

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

Miten matkalaskun täyttämisessä otetaan huomioon mahdolliset lisäkulut?

**Ground Truth (Odotettu vastaus):**

Matkalaskun täyttämisessä otetaan huomioon mahdolliset lisäkulut käyttämällä 'Lisää muu kulu' -vaihtoehtoa, johon voidaan lisätä omalla kustannuksella maksetut kulut. Esimerkiksi lounaskokous asiakkaan kanssa merkitään pääsääntöisesti 'Kokous ja neuvottelukulut', ja edustuskulut, kuten lahjat ja iltatarjoilut, merkitään 'Edustuskulut'. Tämän lisäksi on tärkeää lisätä ALV kaikilta kuluista, lukuun ottamatta edustuskuluja, joihin ALV ei kuulu.

**Saatu vastaus (RAG):**

Matkalaskun täyttämisprosessissa mahdolliset lisäkulut otetaan huomioon lisäämällä ne omalla korolla merkityllä tavalla matkalaskuun. Tämä tapahtuu käyttämällä "Lisää muu kulu" -toimintoa, jonka avulla voidaan lisätä erillisiä kuluja matkalaskuun. Esimerkiksi erilaiset menoerät, jotka eivät kuulu suoraan matkakuluihin, voidaan dokumentoida tällä toiminnolla.  

Lisäksi matkalaskuun on tärkeää liittää kaikki kulut todentavat kuitit tai muut selvitykset/liitteet, ja ne tulee merkitä kohtaan, jolle on varattu tähän tarkoitukseen. Näin varmistetaan, että lisäkulut dokumentoidaan asianmukaisesti ja ne ovat valmis taloushallintoon käsittelyä varten.  

Mikäli lisäkulut liittyvät esimerkiksi korvausryhmiin kuten edustuskulut tai muut kulutyypit, ne valitaan oikean kulutyyppinumeron avulla, esimerkiksi "Kokous ja neuvottelukulut" tai "Edustuskulut", ja ALV-käytännöt huomioidaan kulutyyppien mukaan.  

Tämä menettely varmistaa, että kaikki matkakuluihin liittyvät lisäkulut tulevat asianmukaisesti kirjatuiksi ja voidaan hyväksyä maksuun taloushallinnon kautta.

---

### References

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

### Test Case #17

**Kysymys:**

Miksi työntekijöiden on tärkeää kirjata lomat ja poissaolot Netvisoriin, ja miten tämä liittyy matkalaskujen tekemiseen?

**Ground Truth (Odotettu vastaus):**

Työntekijöiden on tärkeää kirjata lomat ja poissaolot Netvisoriin, koska se mahdollistaa riittävän seurannan ja hallinnan henkilöstön poissaolojen osalta. Kun lomat ja poissaolot on merkitty, se helpottaa myös matkalaskujen tekemistä, sillä työntekijät voivat varmistaa, että heidän käytettävissään on riittävästi työaikaa matkoihin. Tämä prosessi varmistaa, että kaikki kulut ja poissaolot on dokumentoitu selkeästi ja että johtajat voivat hyväksyä matkalaskut tehokkaasti.

**Saatu vastaus (RAG):**

Työntekijöiden on tärkeää kirjata lomat ja poissaolot Netvisoriin, koska työaikalain (872/2019) velvoittama työajanseuranta edellyttää, että työnantaja pitää kirjaa tehdyistä työtunneista. Tämä kirjaaminen mahdollistaa työntekijöiden poissaolojen ja lomien asianmukaisen rekisteröinnin sekä varmistaa, että työaikalain vaatimukset täyttyvät. Lisäksi työaikatiedot ovat työnantajan käytettävissä pyydettäessä, esimerkiksi työsuojeluviranomaisille tai työntekijöiden edustajille, ja aineiston säilytysvaatimus on vähintään kaksi vuotta.

Lomien ja poissaolojen kirjaaminen Netvisorissa liittyy myös matkalaskujen tekoon merkittävästi. Kun työntekijä on kirjannut lomansa tai poissaolonsa, hänellä on ajantasainen ja luotettava tieto siitä, milloin hän on ollut matkalla tai poissa työstä, mikä vaikuttaa matkakorvausten ja päivärahojen oikeudenmukaisuuteen. Lisäksi Netvisorin mobiili- ja selainversioissa voi tehdä ja hallinnoida matkalaskuja, ja oikeat poissaolotiedot varmistavat, että matkakorvaukset perustuvat oikeisiin päiviin ja työaikaan. Näin ollen poissaolojen ja lomien asianmukainen kirjaaminen auttaa varmistamaan matkakorvausten oikeellisuuden ja valmistelun sujuvuuden.

**Supportaat:**  
- Työajanseuranta on velvoite työaikalain mukaan ja tehdään Netvisorissa (Reference [4]).  
- Lomien ja poissaolojen kirjaaminen on mahdollista Netvisorin mobiili- ja selainversioissa ja kattaa vuosilomat sekä muut poissaolot (Reference [3]).  
- Matkalaskujen tekeminen edellyttää ajan tasalla olevia poissaolotietoja, jotta matkakorvaukset voidaan suorittaa oikein ja hyväksyä hyväksyttyinä (Reference [2], [3]).

### References

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

### Test Case #18

**Kysymys:**

Miten matkaraportti ja luottokorttitilitykset liittyvät toisiinsa matkakulujen hallinnassa?

**Ground Truth (Odotettu vastaus):**

Matkaraportti on tärkeä asiakirja, joka tulee toimittaa esimiehelle matkalaskun yhteydessä, ja siinä kuvataan matkan keskeiset asiat. Luottokorttitilitykset puolestaan käsittelevät yrityksen luottokortilla maksettuja matka- ja edustuskuluja, jotka eivät kuulu matkalaskun piiriin. Alkuperäiset luottokorttiostotositteet liitetään luottokorttilaskuun, mikä tekee selväksi, että nämä kaksi asiakirjaa palvelevat eri tarkoituksia matkakulujen raportoinnissa mutta ovat silti keskeisiä yrityksen taloushallinnan kannalta. Matkaraportti keskittyy matkan tarkoitukseen ja kulujen selvittämiseen, kun taas luottokorttitilitykset varmistavat, että kaikki luottokortilla tehdyt ostokset kirjataan asianmukaisesti.

**Saatu vastaus (RAG):**

Matkaraportti ja luottokorttitilitykset ovat keskeisiä dokumentteja matkakulujen hallinnassa, sillä ne täydentävät toisiaan ja varmistavat kulujen oikean käsittelyn.

Matkaraportti on asiakirja, joka sisältää tiedot matkan tarkoituksesta ja siihen liittyvistä keskeisistä asioista. Se kuvastaa matkan tarkoituksen ja tärkeimmät tapahtumat, ja tarvittaessa se tulee toimittaa esimiehelle matkalaskun yhteydessä. Matkaraporttiin kirjataan myös matkan mahdolliset erityiset kulut ja menot, joten se auttaa tilinpidossa ja kulujen oikeellisuuden varmistamisessa [1].

Luottokorttitilitykset puolestaan sisältävät yrityksen luottokortilla maksetut matka- ja edustuskulut, jotka eivät merkitä suoraan matkalaskuun. Alkuperäiset luottokorttiostotositteet ja tilitykset liitetään luottokorttilaskuun erikseen, eikä niitä merkitä matkalaskuun [1]. Näin ollen luottokorttitilitykset edustavat maksutapahtumia, jotka on tehty yrityksen luottokortilla, ja niiden erillinen dokumentointi auttaa kulujen oikean kohdentamisen ja maksunhallinnan.

Yhdessä matkaraportti ja luottokorttitilitykset varmistavat matkakulujen kokonaisvaltaisen hallinnan: Matkaraportti tarjoaa selkeän kuvauksen matkan tarkoituksesta ja kustannuksista, kun taas luottokorttitilitykset dokumentoivat maksutapahtumat ja toimivat todisteina mahdollisista kuluista. Näin varmistetaan, että kaikki matkakuluista aiheutuneet menot käsitellään oikeudenmukaisesti ja läpinäkyvästi taloushallinnossa.

---
[1] HR DOC Matkustussääntö.pdf

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

