import httpx
from bs4 import BeautifulSoup
from html2text import html2text


def text_from_url(url:str) -> str:
    html_text = httpx.get(url).content.decode()
    soup = BeautifulSoup(html_text)

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()
    return text


def md_from_url(url:str) -> str:
    html_text = httpx.get(url).content.decode()
    text = html2text(html_text)
    return text
