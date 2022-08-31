import time
import lxml.html as html
import urllib.request as request

OPENSAFELY_CODELISTS = "https://www.opencodelists.org/codelist/opensafely/"
SAFE_UA = "Mozilla/5.0 (X11; Linux x86_64) "\
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"


def get_page(url):
    rq = request.Request(url, data=None, headers={"User-Agent": SAFE_UA})
    return html.parse(request.urlopen(rq))


dm_d_codelists = []

codelist_page = get_page(OPENSAFELY_CODELISTS)

while True:
    codelists_dl = codelist_page.xpath('//*/dl[@class="home-codelists"]')[0]
    dm_d_codelists.extend(
        [
            e[0].get("href").replace("/codelist/", "")
            for e in codelists_dl.xpath("dt")
            if e[1].text == "dm+d"
        ]
    )
    pagination = codelist_page.xpath('//*/ul[@class="pagination"]')[0]
    this_page = [
        (i, e) for i, e in enumerate(pagination) if "active" in e.classes
    ][0]
    if this_page[0] == len(pagination) - 1:
        break
    else:
        next_page = pagination[this_page[0] + 1]
        time.sleep(0.1)
        codelist_page = get_page(
            OPENSAFELY_CODELISTS + next_page[0].get("href")
        )

with open("codelists/codelists.txt", "w") as f:
    f.writelines([c + "\n" for c in dm_d_codelists])
