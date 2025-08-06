import json

import requests
from bs4 import BeautifulSoup

session = requests.session()
url = "https://sutochno.ru/api/json/search/searchObjectsOnMap"

payload = {}
headers = {
    'authority': 'sutochno.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'api-version': '2.1',
    'dnt': '1',
    'token': 'Hy6U3z61fflbgT2yJ/VdlQ2719',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
headers={
  'authority': 'sutochno.ru',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'ru-RU,ru;q=0.9',
  'api-version': '2.1',
  'baggage': 'sentry-environment=production,sentry-release=a9c0a0dc,sentry-public_key=555b213bdad1470d80b1e39d52f77597,sentry-trace_id=e7f9877a587342de996b66b7b292ade8,sentry-sample_rate=0.1,sentry-transaction=Search,sentry-sampled=false',
  'cookie': 'route=1751916169.996.40.8036|cb1faa23db9e30603aef3c84465716e1; spjs=1751916152501_1212b7dc_0134ff91_50a67e1c0017ecf85cffc8df479ba3ab_a8mINCx/b5pC96ZDgN0vEJAFCQ+Xuuu0S9LyC2c+fnWNTC2JEVO20t6a+j5J8PA4hWkKts5jY+9yfpcBqY7pKMHkpFKGpBRosQ1dofpJe7bKZhz91RW10crePm9Th/cMQT0Z1e0ioh7X+94XDYlJPJFWZVGIPO86TOA1CVXpKZPeJ2NKxyHU4CmN/RwS5nZjrloIsdlR5I3B269mL8YmeFA0ZeTpK74KA8cnM3GYHTVNISeOs17Lx8is+4sCtCIEyWyA6KC9g97grnyhqyen2taLdTCJPGsZUuYXVc4qi0BNdKFd48qK1970t1sFcTJknFqbTsPHt6M1GJg1DDbWmIGt6haK+XktEPLQBD8Ln4rEQqT5cey4ZV7yI74GW2rwyXoYzOQiwwO7r58q7IABPob6qNXPkAAcUq3gUNlPvhnJctbQixsvUdgV9dwCOupxPxNse2OWsbUbKIgIIONDTRJeftaKkxEdRdj8kp1YOJtiwsMmysj5bGjVtblHGu4jSlfWChNhNjOeiFisd3M3FP77DSFZZ8LexeipAKyQ4D3DcYehmS6+ulPn5xMk+HhF7VECntYry7dY7PhbBRS2sf7+r7mgEIDdRvgKVS3lp4ojL6Rz6GwNiRMWoXHbr2+VLHHBjbVqe3Y/5CBUI6fTZDyIWx/TMHJ2dRMrRCeScp1I18aq7K7smWJmBhIZvW0JzqQBfceySufN84FtFKhqswv/L9qDteeRSnyvWAyzYL6G+ijViTDkHEDSN/HKP18ZwPU20bq62JdNcqZeATlsFMnQeZ3R4qLESfstXgCz5SfHayJWnjjhjVX0aNYqD8/elSEDJo9uGE7ZFJXuJp1NRG0CAgrCoZEECHJhtf5Kmu83g9vEK6JDbs35WF6MMeubIX72UCsrK4+ms5JmEL05wclUtwuSH3m1K3Qvugn2F8HLc3ia0DPlSwRxKrUEYeC8dPmm0gru7pJCB6VTB5xIPb9iAuymKvgybHCBfTfBkeS8uH/dF9LWckV/PbBI5KCMYU08MPj7vZnGYEEUX3+vHBYjFc2DrA3QGzMkf5a87FHPCAjNhLNzpnr//wsMsWGa4j9b0fhzwg6B81BVXFoa28I3x7IaGy7hGNYUyUe8H0LoBO175kCwtv9q73sDNxeJ1OhMxc1Ckvty7v43SMxsWeFFs/LvCvrLzLA1PGQ72bVNYTDMlCf3g15YHtgQlGWY8QM7JoTOeN7EcaFdBHDhOsP8Dx8LbOcxG2QF2A+zY9ZP0rFSCyDAFHryf3kieOZfuTNcltB9s9EWuC9VLdHhLcRJp8eBjruVseAF8Yi9bBZPcSLcBj/JNZL6GChC5FwiPkikVHJh6s8aUIS0K2JmFHEw==; spcaphp=726s8fcp68ja7epg1kops5159o; spid=1751916152501_b59ce6b2cd8c5708e7f9e9888222db71_57jtmtp1qjk983p0; spsc=1751916152501_c11568b3a9da15d341edaf124cfa6312_sCzVb3yI-.KiW8DgFTNOrirQ1Jx07ABsvEXSJjfRue4Z; spca=1751916152501_32f44bba92b1eaee91c0d1b1e9c01003_sCzVb3yI-.KiW8DgFTNOrirQ1Jx07ABsvEXSJjfRue4Z; tmr_lvid=9ff6943ac5254151bada06fcc8e2d17e; tmr_lvidTS=1751916147367; calendar_dates=%7B%22date_begin%22%3A%222025-07-07%22%2C%22date_end%22%3A%222025-07-27%22%2C%22guests%22%3A1%2C%22term%22%3A%22%22%7D; select_guests=%7B%22guests%22%3A%7B%22adults%22%3A1%2C%22childrens%22%3A%5B%5D%2C%22pets%22%3A%7B%22value%22%3Afalse%2C%22description%22%3A%22%22%7D%7D%7D; viewport=tablet; _ymab_param=vIIeqiiCcngSIDQ_fp2EbmdsaX159CjRqxbGor7j83JmtF6tQqZrR8lx2qbKsk7EiRJQY6W2F0FAdq767WwoEVYlAeo; _pk_id.1.7564=decdec5724bba10d.1751916149.; _pk_ses.1.7564=1; _gcl_au=1.1.1975642539.1751916149; _ga=GA1.1.700375026.1751916149; _ga_B0K4L0V6J8=GS2.1.s1751916149$o1$g0$t1751916149$j60$l0$h0; _ym_uid=1751916150766264338; _ym_d=1751916150; domain_sid=zHn3IaxnxGep_is_j9fNM%3A1751916149821; language_id=ru; _me_=tQaCHB1dsbC6Xm1%2BAdvkSg; _ym_isad=2; PHPSESSID=355a8f5f289ae053525932dd322d1382; _ym_visorc=b; DontShowHintBlockUpdate=true',
  'dnt': '1',
  'platform': 'js',
  'referer': 'https://sutochno.ru/front/searchapp/search?occupied=2025-07-07;2025-07-27&guests_adults=1&price_per=1&SW.lat=55.32504259685306&SW.lng=55.356769112548726&NE.lat=55.495562031181755&NE.lng=55.67777588745107&id=1',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': 'e7f9877a587342de996b66b7b292ade8-871fd3418970cd35-0',
  'token': 'Hy6U3z61fflbgT2yJ/VdlQ2719',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

offset = 0
count = 50
objects = []
# while offset < 10_000 - count:
total = 100
while 1 < total - len(objects):
    response = session.get(url, headers=headers, data=payload, params={
        "max_guests": 1,
        "currency_id": 1,
        "count": count,
        "offset": offset,
        "NE[lat]": "54.960116",
        "NE[lng]": "56.297733",
        "SW[lat]": "54.500719",
        "SW[lng]": "55.778561",
        "location_type": "city",
        "location_id": "273530",
        "relevance": "pairs",

    }
                           )

    offset += count
    objects.extend(response.json().get("data", {}).get("objects", []))
    # total =response.json().get("data", {}).get("totalCount")
aparts = []
headers={
  'authority': 'sutochno.ru',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'cookie': 'spid=1744010121979_7042f8326f8de76e17182fac420193ce_dgp4obxpan2734hn; _ym_uid=1744010124688050393; _ym_d=1744010124; _ymab_param=O3mBH5v7wp-ea_PBiSzCMqOP9hXH2KBZsT9nalN0h9yu4sAbs4vR4kT-pGFcMnjV8kLuI27ovdy3z2RWgHzBj7xm2uI; PHPSESSID=bcbfef97ddcd52092affb236d200cafb; language_id=ru; _me_=tQaCHB1dsbC6Xm1%2BAdvkSg; _gcl_au=1.1.1249730423.1748242224; _pk_id.1.7564=ef7deb8a831af3b4.1748242224.; _ia_=0; _pk_id.13.7564=c8dbce20ca3e59e2.1748242474.; x-request-id=122756ac4fbad448ea051c8d88b52d6f; rid=122756ac4fbad448ea051c8d88b52d6f; _ga=GA1.1.1107723626.1748242224; select_guests=%7B%22guests%22%3A%7B%22adults%22%3A1%2C%22childrens%22%3A%5B%5D%2C%22pets%22%3A%7B%22value%22%3Afalse%2C%22description%22%3A%22%22%7D%7D%7D; _ym_isad=1; DontShowHintBlockUpdate=true; _pk_ref.1.7564=%5B%22%22%2C%22%22%2C1751915340%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.1.7564=1; spjs=1751915443530_1eb48ac9_0134ff91_8ace149082cc0ceed01c04724fd5e40d_a49TQ/9GOmsVzHExVRUl6jML1E5KgbRHFusvfbQJJITYdvr6xmrjI42lIUCUya7L2lPXxxNUOBgnQMJTfsW1eKVLbi/ZDCmZ7jaC0yd/w/E9QOyZcFuSMl9HW7Tl2A19icezllJrry+UXHBUnYAPz7Mf0ODcArdksMltu4/SZ6cWVK3owU2kUW6mCnuSn2z86CTQhTRf3msLRFYl7KRMrPXesuJrZ647gIhMrbn0FpOyy6+qCznVQE1FKX0FjTKkiUPmCnMqNl6YZyHyJy6tLVFcAfC9B7vsl99jnd9FoAHFy/ou2mVHB11Vfz3RiPe06xLcHsNJTDwpsJUWs4u4WB0LJ2GdAHz8o591VoqygRUBTsgpfPdjN+Pbf6k0jdHgfUf8n0Nqp0aJMCQVoGkOj7kAdCVQRRuLlt8vW+6GyTiYRKvtWwGWotdfmntah7Bg+rWZ6ffdETY7lq0CgqtpyciU0PRxL5s9N5klwAvTCMmzGhSgWKFH5xPqKutPZmNlMPMdXBT6p5Y642/OlSy72RxkAHDFX2zNzLaC1alBaO6gytdXi1GYKJPaf3t6orXDkU5d30sc4EAN1Tlq9s4js79g1OQAGZ1NCtIiJNcq60ugzXHDfibaKxTO0Cz71/BwdR5+DTpSV3dNJH8KBZ0yY35GG/tnWC2Madb2LfGZiJpuuYVlDQIsjCcl8TP1pCdnHuQQ0DqQtmcwWNxrx48y85AVuwsVgiAhm8FXFsKaP01ZwPWkUYe5axROcSHehTtI1Mv+r18CsuYS7O2OGAEC457G6KtkjIJhH0R8J9cLO+6f4aPjA9z4OhfJ8yXegbjRlVz4IEwKt3cDx75/+DGUIMcQ3VxRXEa0iyJPmfSrGL47MdRwFJ/L+lpMu8wgeMUVabIBsvmUGZiby44lWgO+ZXNBLC75GXV1+IFMH8KLYjebZWFxRC0vT3lK9cXbyEo7lUCm4A4Fv71WR/DM0lO3RiLIfKzY0LRsHDV7KNt+dcvtVdiadBiuyDpCVwTl/8oa7omhp8ngiIgXSefHmtL1djd+6kouxednlF6bbYFN8OZIEs+7UZpXJk0B8gRAjrmvnTfSs1aBLVwkzSFy3oc6bLAOjasuQZT0082KKo5kRyGcBBnIxC10F0rgzrCRjki4vjU3BTR+6kihWDEA3QVKf4bflrMfcMQBJNwoTpryN6ezdG2IMTikMZ6G70u2DTxPG1LmtkIZrX0MZrShzqY6Yn6CUABVqXX5IkN3JtJCtMSRxjEXGR68KRP2G6HdhTggHeNXLs4zB4apgHiE8qjwq3xeGFK09VOJ/iySqtijVmajScwtTQ2EgRA3bop2DiDhnMT6qFaLuU+6HHydpchlTQnrxSrS9e9jiCeKDz+h5+Wcrr; spcaphp=c1s6qg08tblktq6o903eor16i1; spca=1751915443530_14f0092396aa522985229c90aa90b3b1_sCzVb3yI-.KiW8DgFTNOrirQ1Jx07ABsvEXSJjfRue4Z; spsc=1751915488178_5d3212a3aa17e33d032de5313b7682ad_tKI0TXIU5asoy0xWlKxWW6EvkOoV6v-PjLWJ9N6Xnw7ckXqPBMoqZSI20mKFexp4Z; viewport=desktopWide; _ga_B0K4L0V6J8=GS2.1.s1751915336$o16$g1$t1751915474$j55$l0$h0; _ym_visorc=b; spsc=1751916677244_bda2371bab52ab0955b74fe7429beff1_X40kPXeOhLt5ZgXzEQoBqMLDiLdkvLqD63MiCKTqwHWlqT3VJgKMfWXzqFL2adyGZ',
  'dnt': '1',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
not_search = []
for o in objects:
    try:
        url = f"https://sutochno.ru/front/searchapp/detail/{o.get('id')}"
        response = session.get(url, data={}, headers=headers)
        soup = BeautifulSoup(response.text)
        o_json = json.loads(soup.find("script", id="__NUXT_DATA__").text)
        area = None
        try:
            for i, v in enumerate(o_json):
                if v == 'area':
                    area = o_json[i + 2]
        except Exception:
            pass
        imgs = []
        try:
            for v in soup.find_all("div", class_='navigation__preview'):
                imgs.append(f"""https:{v.find("img").get("src")}""")
        except Exception:
            pass
        title = ""
        try:
            title = soup.find("h1").text
        except Exception:
            pass
        review = ""
        try:
            review = soup.find("div", class_='review').text
        except Exception:
            pass
        title = ""
        try:
            title = soup.find("h1").text
        except Exception:
            pass
        address = ""
        try:
            address = soup.find("div", class_='address').text
        except Exception:
            pass
        description = ""
        try:
            description = soup.find("div", class_='object-data--desk').text
        except Exception:
            pass
        sleep_place = ""
        try:
            sleep_place = soup.find("div", class_='object-data--sleeping-places').text
        except Exception:
            pass
        bed = ""
        try:
            bed = soup.find("span", class_='object-data--bed').text
        except Exception:
            pass
        properties = []
        try:
            properties = [p.text for p in soup.find("div", class_='info-block').find_all("p")]
        except Exception:
            pass
        aparts.append(
            {
                "title": title,
                "review": review,
                "address": address,
                "type": soup.find("div", class_='object-data--type').text,
                "params": [p.text for p in soup.find("div", class_='object-data--params').find_all("span")],
                "description": description,
                "sleep_place": sleep_place,
                "bed": bed,
                "clock": [p.text for p in soup.find("div", class_='clock').find_all("div")],
                "rules_list": [p.text for p in soup.find("div", class_='rules--list').find_all("div") if
                               p.text.strip()],
                "properties": properties,
                # "all_properties": [p.text for p in soup.find("div", class_='info-block').find_all("p")],
                "url": url,
                "price": o.get('price'),
                "area": area,
                "imgs": imgs,
            }
        )
    except Exception as e:
        not_search.append(url)
with open("Белебей.json", mode="w") as json_file:
    json.dump(aparts, json_file, indent=4, ensure_ascii=False)

print(response.text)
