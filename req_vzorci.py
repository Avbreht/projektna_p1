import re
import test


vzorec_bloka = re.compile(
    r"<td class='collection_rank' align='center' >.*?<td class='collection_shop'>",
    flags=re.DOTALL
)

vzorec_igre = re.compile(
    r'<a  href="/boardgame/\d+/.*?"   >(.*?)</a>',
    flags=re.DOTALL
)

vzorec_ocene = re.compile(
    "<td class='collection_bggrating' align='center'>\\n(.*?)</td>",
    flags=re.DOTALL
)

