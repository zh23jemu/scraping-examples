import requests

video_url = 'https://www.pearvideo.com/video_1797772'

videoId = video_url.split('_')[-1]
videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={videoId}&mrd=0.6689366231857594"

headers = {
    "Referer": video_url
}

response = requests.get(videoStatusUrl, headers=headers)
dic = response.json()

srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']

srcUrl = srcUrl.replace(systemTime, f"cont-{videoId}")

with open(f"downloads/{videoId}.mp4", "wb") as f:
    f.write(requests.get(srcUrl).content)

response.close()
