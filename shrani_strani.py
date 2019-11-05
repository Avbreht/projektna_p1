import re
import test
import req_vzorci

stevilo_strani = 10

for i in range(1, stevilo_strani):
    url = (
        f'https://boardgamegeek.com/browse/boardgame/page/{i}'
    )
    ime_datoteke = (
        f'html_koda{i}.html'
    )
    test.pripravi_imenik(ime_datoteke)
    test.shrani_spletno_stran(url, ime_datoteke)

    with open('html_koda1.html', 'r') as datoteka:
        vsebina = datoteka.read()
    count = 0
    for ujemanje in re.finditer(req_vzorci.vzorec_igre, vsebina):
        print(ujemanje)
        count += 1