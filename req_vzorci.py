import re
import test


with open('html_koda.html', 'r') as datoteka:
    vsebina = datoteka.read()


vzorec_bloka = re.compile(
    r"<td class='collection_rank' align='center' >.*?"
    r"<td class='collection_shop'>",
    flags=re.DOTALL
)

vzorec_igre = re.compile(
    r'<a   href="/boardgame/\d/\D" >',
    flags=re.DOTALL
)

vzorec_ocene = re.compile(
    r"<td class='collection_bggrating' align='center'>\s",
    flags=re.DOTALL
)

count = 0
for ujemanje in re.finditer(vzorec_ocene, vsebina):
    print(ujemanje)
    count += 1
print(count)