from typing import Union
import requests
from fastapi import FastAPI
import uvicorn

app = FastAPI()


def allsave(url):
    urls = "https://save-from.net/api/convert"
    headers = {
        'Origin': 'https://save-from.net',
        'Referer': 'https://save-from.net/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    payload = {'url': url}
    response = requests.post(urls, headers=headers, data=payload)
    return response.json()


@app.get("/")
def read_root():
    return {"url": "Paste Video URL."}


@app.get("/convert/{video}")
def read_item(video: str, url: Union[str, None] = None):
    url = allsave(url)
    return {"url": url}


@app.get("/convert/{instagram}")
def Instagram_Downloader(instagram: str, url: Union[str, None] = None):
    url = allsave(url)
    return {"url": url}

@app.get("/convert/{youtube}")
def YouTube_Downloader(youtube: str, url: Union[str, None] = None):
    url = allsave(url)
    return {"url": url}


@app.get("/convert/{facebook}")
def FaceBook_Downloader(facebook: str, url: Union[str, None] = None):
    url = allsave(url)
    return {"url": url}



@app.get("/convert/{reddit}")
def Reddit_Downloader(reddit: str, url: Union[str, None] = None):
    url = allsave(url)
    return {"url": url}



@app.get("/convert/{tiktok}")
def TikTok_Downloader(tiktok: str, url: Union[str, None] = None):
    url = allsave(url)
    return {"url": url}


@app.get("/convert/{vimeo}")
def Vimeo_Downloader(vimeo: str, url: Union[str, None] = None):
    url = allsave(url)
    return {"url": url}



@app.get("/about")
def AboutMe():
    return {"data":{'Creators' : "Barot, Xudoberdi", 'Technology' : 'Python, FastAPI', 'TELEGRAM-LINK' : "@MrGayratov --- @ai_junior"}}


if __name__ == "__main__":
    uvicorn.run(app)