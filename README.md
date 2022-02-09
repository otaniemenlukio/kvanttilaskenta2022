# Kvanttilaskennan lukiokurssi 2022

## Asennusohjeet

Jos käytät *omaa kannettavaa*, etene [tämän](https://sooluthomas.github.io/testTranslation/install.html) ohjeen mukaan

Jos käytät *Espoon lukiolaiskannettavaa*...

### 1. Ohjelmistojen asennus
1. Asenna VSCode yritysportaalista
2. Asenna [git](https://github.com/git-for-windows/git/releases/download/v2.35.1.windows.2/Git-2.35.1.2-64-bit.exe)

### 2. Tietovaraston kloonaus
1. Avaa VSCode
2. Paina `ctrl + shift + P`
3. Kirjoita kenttään `git clone` ja paina `enter`
4. Liitä kenttään tämän git-tietovaraston URL (`https://github.com/otaniemenlukio/kvanttilaskenta2022`) ja paina `enter`
5. Avaa VSCodessa kansio johon tietovarasto kloonattiin

### 3. Tarvittavien pakettien asennus
1. Avaa uusi pääte VSCodessa (`ctrl + shift + Ö`)
2. Kirjoita päätteeseen `python -m pip install -r requirements.txt`
