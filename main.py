import json
import sys
import requests
import os

from SnsInfo import SnsInfo, Profile
from discord_message import Embed, Author, Image, Message


# 自定义 JSON 编码函数
def custom_encoder(obj):
    if isinstance(obj, (Author, Image, Embed, Message)):
        return obj.__dict__
    else:
        raise TypeError("Object is not JSON serializable")


# 發送訊息到 Discord
def send_message(webhook_url: str, sns_info: SnsInfo):
    embeds = []
    # 圖片訊息，Embed 的 url 如果一樣，最多可以 4 張以下的合併在一個區塊
    for index, url in enumerate(sns_info.images):
        if index == 0:
            embeds.append(
                Embed(Author(sns_info.profile.name, sns_info.profile.url), sns_info.content, image=Image(url),
                      url=sns_info.profile.url))
        else:
            embeds.append(Embed(image=Image(url), url=sns_info.profile.url))

    # 將 JSON 數據轉換為字符串
    data_json = json.dumps(Message(sns_info.post_link, embeds), default=custom_encoder)
    # data_json = json.dumps(Message("", embeds), default=custom_encoder)
    print(data_json)

    # 使用 POST 請求將消息發送到 Webhook
    response = requests.post(webhook_url, data=data_json, headers={'Content-Type': 'application/json'})

    # 檢查是否成功發送消息
    if response.status_code == 204:
        print('消息已成功發送到 Discord 頻道！')
    else:
        print('消息發送失敗。HTTP 響應碼：', response.status_code)
        print('響應內容：', response.text)


try:
    DISCORD_WEBHOOK = os.environ["DISCORD_WEBHOOK"]
except KeyError:
    DISCORD_WEBHOOK = "Token not available!"
    # or raise an error if it's not available so that the workflow fails

send_message(DISCORD_WEBHOOK, SnsInfo("https://www.google.com", Profile("測試", ""),
                                      "測試發送訊息", []))
