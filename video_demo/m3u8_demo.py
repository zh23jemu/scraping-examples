import os
import requests
from m3u8 import M3U8
from concurrent.futures import ThreadPoolExecutor

# 设置请求头，模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def download_ts(url, save_path):
    """下载单个 TS 文件"""
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
            print(f"下载成功: {save_path}")
        else:
            print(f"下载失败: {url}")
    except Exception as e:
        print(f"下载异常: {url}, 错误: {e}")


def download_m3u8_video(m3u8_url, output_file):
    prefix = m3u8_url[:m3u8_url.rfind('/') + 1]
    """下载 M3U8 视频并合并为 MP4"""
    # 创建临时文件夹
    temp_dir = "temp_ts_files"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # 下载 M3U8 文件
    response = requests.get(m3u8_url, headers=headers)
    if response.status_code != 200:
        print("M3U8 文件下载失败")
        return

    # 解析 M3U8 文件
    m3u8_content = response.text
    m3u8_obj = M3U8(m3u8_content)
    ts_urls = [segment.uri for segment in m3u8_obj.segments]

    # 下载所有 TS 文件
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i, ts_url in enumerate(ts_urls):
            ts_name = f"{temp_dir}/{i:04d}.ts"
            executor.submit(download_ts, prefix + ts_url, ts_name)

    # 合并 TS 文件
    with open(output_file, "wb") as outfile:
        for i in range(len(ts_urls)):
            ts_name = f"{temp_dir}/{i:04d}.ts"
            if os.path.exists(ts_name):
                with open(ts_name, "rb") as infile:
                    outfile.write(infile.read())
                os.remove(ts_name)  # 删除临时文件
    print(f"视频合并完成: {output_file}")


# 示例调用
m3u8_url = "https://v.guancha.cn/34386e2dvodtranssh1251245530/2fe212541397757904724074982/video_10_4.m3u8"  # 替换为实际的 M3U8 文件链接
output_file = "output.mp4"
download_m3u8_video(m3u8_url, output_file)
