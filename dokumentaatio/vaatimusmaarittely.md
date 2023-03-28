# Nurikabe-pelin vaatimusmäärittely

### Sovelluksen tarkoitus
Nurikabe on suorakulmion muotoisella ruudukolla pelattava pulmapeli, jossa pyritään luomaan numeroiden antaman kokoiset "saaret". Saaria on erotettava mustilla ruuduilla, jotka luovat yhdistetyn "vesistön". Pelin alkuperäinen julkaisija ja sääntöjen luoja on japanilainen pulmapelilehti Nikoli, [viralliset säännöt löytyvät Nikolin verkkosivuilta](https://www.nikoli.co.jp/en/puzzles/nurikabe/). Linkin takana myös kuvia pulman etenemisestä.

### Käyttäjät
Pelillä on oltava vain normaali käyttäjä/pelaaja. Pulmien luonti ei tapahdu käyttöliittymässä eikä vaadi erillistä ylläpitäjän tai pääkäyttäjän roolia.

### Toiminnallisuus
- Aloitusnäyttö valinnoilla "Uusi pulma", jonka jälkeen valitaan vaikeusaste, tai "Jatka", jos edellinen pulma on jäänyt kesken
- Pelin ruudukkoon piirtäminen: LMB = väritetty ruutu / "vesi", RMB = piste / "maa"
- Automaattinen laittomien "vesistöjen" ja "saarien" havainnointi (eli mustan ruudun on aina oltava yhdistettynä toiseen ja ei saa koskaan luoda 2x2 vesialuetta, saarien pinta-ala ei saa olla numeroa suurempi pulman ratkaisun aikana)

Lisätoiminnallisuutta
- Automaattinen pulmien generointi kolmella vaikeusasteella, helppo/normaali/vaikea (jos mahdollista, muuten lisätään vaan tietty määrä valmiiksi tehtyjä pulmia muutamaan vaikeusasteeseen)
- "Checkpoint-järjestelmä", eli juuri tehdyn muutoksen voi merkata, joka antaa ruudulle uniikin värin ja luo palautuspisteen. Tämä mahdollistaa yksittäisen ruudun arvaamisen ja tähän kohtaan palaamisen myöhemmin.
- Pelin tilan automaattinen tallennus; kun pelaaja jättää pulman kesken, voidaan palata samaan ruudukkoon myöhemmin, kun peli uudelleenkäynnistetään
- Pelin ikkunan koon säätö, säädettävissä oleva ikkuna tai koko näytön tila
