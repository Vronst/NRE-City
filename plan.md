# Miasto

- startuje z jednym kontraktem do innego miasta, stolica ma 2
- kontrakt moze byc zmieniony na inne miasta przy zakonczonej transakcji produkowanego surowca z szansa 1%
- 0.1% szansy na spwan misji wyslij list kontraktowy (misja ta bd tworzyla nowy kontrakt miedzy miastami) i szansa bd sie zwiekszala
  az do 5% przy kazdej sprzedazy surowca z innego miasta
- szansa na fabryke to 40% przy miescie (o ile lokacja pozwala), 'big' miasto bd mialo gwarantowana fabryke i 20% szansy na 2

## Struktura miasta

`python 
json = {
  cities: [
    "Eldorado": {
        "size": "big",  
        "factory": ["mine", "20%for other if big"],
        "fee": 100
        "number of connections": "6",
        "commodieties": {
          "metal": {"quantity": 100, "price": 200, "regular price": 150},
          "gems": {"quantity": 75, "price": 250, "regular price": 300},
          "food": {"quantity": 50, "price": 50, "regular price": 45},
          "fuel": {"quantity": 50, "price": 100, "regular price": 80},
          "relics": {"quantity": 1, "price": 1250, "regular price": 1300},
          "special": null,
         },
        "missions": 2,
        "mission_title": ["Agata mysli nad tym prawda?", "Oby Adam sie nie mylil"],
        "connecitons": [
          "Romania", "Kraina Czapl", ...,
          ]
         },
         ]
}
`


# Surowce -> Fabryki 
- metal -> Wysypisko
- krysztaly -> Kopalnia
- jedzenie -> Farma
- benzyna -> Cmentarz
- itemy z kampani -> Null
- relikty przeszlosci -> Pole bitwy

# Surowce -> zmiany
- miasto kupuje -> zasob przy nastepnym refreshu zwieksza sie pomiedzy 25%-50% losowo
- miasto sprzedaje -> zasob przy nastepnym refreshu zmniejsza sie o 10%-50%
- kontrakt -> zasob przy nastepnym refreshu nie moze spasc ponizej standardu + 10%
- cena zmienia sie 5%-10% przy refreshu (plus dodatkowa zmiana od ilosci zasobu)```md

# Mechanika handlu

Ilosc zasobu (tj maksymalna ilosc stuk) zalezec bedzie od wielkosci miasta. Duze miasta beda mialy 5x wiecej surowcow w porownaniu do malych miast.
Kazde miasto zelznie od polozenia bd moglo miec fabryke surowca (moze nie miec zadnej)

Ilosci zasobu bd zalezaly takze od graczy i botow oraz tranzakcji miedzy miejskich. 
Tranzakcje te bd okreslaly jakie miasto handluje z jakim i ktore surowce sa wymieniane.
Na podstawie tych tranzakcji oraz misji pocztowych gracz bd mogl wykonywac malo platne zlecenia z miasta do miasta.
Tranzakcje nie musza byc jawne dla graczy nie wypelniajacych ich (tj. gracz weznie zadanie, to dopiero wtedy wie jaki surowiec bd
transportowany, co daje mu mozliwosc ustalenia iz miasto docelowe napenwno bd mialo przynajmniej standardowa ilosc tego surowca)

## Sprzedaz:
*Niemalze wyczerpane zasoby* - 200\*-300%
*Mala ilosc zasobu* - 150\*-200%
*Standardowa ilosc zasobu* - 90\*-100%
*Duza ilosc zasobow* -  75\*-80%

## Skup:
*Niemalze wyczerpane zasoby* - 80\*-90% (80 jesli miasto posiada fabryke surowca)
*Mala ilosc zasobu* - 60\*-75% ceny 
*Standardowa ilosc zasobow* - 30\*-50% ceny zasobu
*Duza ilosc Zasobu* - 0\*-25% ceny

\* ( jesli miasto posiada fabryke surowca)
```