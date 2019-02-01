# importing url of amazon
# converting to html5 text
import requests

url = "https://www.amazon.com/s/ref=sr_pg_1?rh=n%3A283155%2Cp_28%3Alife&sort=salesrank&unfiltered=1&ie=UTF8&qid=1548744755"
headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1'
    }
)
page = requests.get(url,headers = headers)
html_contents = page.text

import bs4