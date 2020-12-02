import json
from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode

BASE_URL = "https://www.zillow.com/search/GetSearchPageState.htm?"
URL = BASE_URL + "searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Seattle%2C%20WA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.465159%2C%22east%22%3A-122.224432%2C%22south%22%3A47.491912%2C%22north%22%3A47.734145%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A16037%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%2C%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22]}&requestId=2"
COOKIE_STR = "zguid=23|%243d52c7d5-eb94-4793-99c3-432ffe1c61ab; loginmemento=1|2c9891888b3e3071583f6d660836216ab03902fc36fc65afc1006313f0295961; _ga=GA1.2.413621088.1605853473; zjs_anonymous_id=%223d52c7d5-eb94-4793-99c3-432ffe1c61ab%22; zjs_user_id=%22X1-ZUtpmlksxyujnt_1r7ky%22; _pxvid=1002298d-2af9-11eb-8ce8-0242ac120003; _gcl_au=1.1.58643568.1605853480; _pin_unauth=dWlkPU5tSTRObVkzTVdRdE9XTXhOQzAwWXpsaExUaGlaV1V0WkRJMlpXRm1ObU0wTVRKaQ; ki_r=; ki_s=; zgsession=1|3364c854-01bf-4cde-96ec-8bc641b77013; _gid=GA1.2.1825968386.1606867351; KruxPixel=true; DoubleClickSession=true; KruxAddition=true; ki_t=1605853481938%3B1606867361454%3B1606867403747%3B2%3B39; JSESSIONID=BB468E09EA7AA9D88172291F827AD3C4; userid=X|3|48434edd62245ad8%7C7%7CbEfD1POeeAM2471HYaR8oahmb0tQGvtq; ZILLOW_SID=1|AAAAAVVbFRIBVVsVEh60%2FX6%2BbnbKaYofhC6vRnZGFgzAvMe23sESkNNIXFVbmnAN%2FPf%2FD0JUQCcBWmwOzdNsfl%2FVgy%2Bd; _gat=1; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pxff_bsco=1; _derived_epik=dj0yJnU9SnlSUE1HRkFyV01kR0JsM1NYeERjTE14YkxZWlcwNEkmbj1xSFJsd0FrYkN3Uzk3SElPQ0xqOGZ3Jm09MSZ0PUFBQUFBRl9IRTlBJnJtPTEmcnQ9QUFBQUFGX0hFOUE; search=6|1609474269467%7Crect%3D50.62214%252C-68.327143%252C23.705962%252C-125.374896%09%09%09%09%09%09%09%09; _px3=5dc2f3e7afebe9926e20523916b926e94fef9b07564e93e8b60ad21527116f37:LX25uxOFVA4YKd7sPceYjej7oc6WwUigCq3cZMqBZBLeXVmHde3Zu8Ci6S8YVbUYDAcl8vkscig8vgSqnAmayg==:1000:iwxn/LEcEeBYBO+6a74PW5LcLixhNR36cNYy21iX2yRX5yqAaJE69hZvtgcEl/TIsfj8u9n9jukw56nT9zFKvsD5AHKhr2ZsDZpVrlYQRmKo4951fqYwq8c2qJD7XnAloWo5Fp/ypnWAmAIV0HWdrJbxfnRQfcushYOGqIC6sPo=; AWSALB=4INxfA5I1tqprh3hto4GY+WmUBzacrkz7fydWtUT8N1o+cr2HFp0YvdTV9M9a3tglBch8W38+M2KJMjH0JcYmdn7SRfjLIr5Zx8z85w1kbF29alIUVhwt8bUTpfg; AWSALBCORS=4INxfA5I1tqprh3hto4GY+WmUBzacrkz7fydWtUT8N1o+cr2HFp0YvdTV9M9a3tglBch8W38+M2KJMjH0JcYmdn7SRfjLIr5Zx8z85w1kbF29alIUVhwt8bUTpfg; _uetsid=b1b15080343111ebb7a2a5eb3bdbf8e4; _uetvid=125468902af911eb9c9fb13353a5bd3c"


def get_cookie():
    cookie = SimpleCookie()
    cookie.load(COOKIE_STR)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies


def parse_new_url(url, page_number):
    url_parsed = urlparse(url)
    query_string = parse_qs(url_parsed.query)
    search_query_state = json.loads(query_string.get('searchQueryState')[0])
    search_query_state['pagination'] = {"currentPage": page_number}
    query_string.get('searchQueryState')[0] = search_query_state
    encoded_qs = urlencode(query_string, doseq=1)
    new_url = f"{BASE_URL}{encoded_qs}"
    return new_url
