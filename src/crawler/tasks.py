import urllib.request

from celeryapp import app
from crawler.models import WEBSiteResponse


@app.task(ignore_result=True)
def parse_web_site(url: str) -> None:
    with urllib.request.urlopen(url) as response:
        body = response.read()
        WEBSiteResponse.objects.create(url=url, body=body)
