import discord
import random
import requests


# おみくじの結果を返すメソッドを定義
def omikuji():
    number = random.randint(0, 5)
    if number == 0:
        result = '大吉'
    elif number == 1:
        result = '吉'
    elif number == 2:
        result = '中吉'
    elif number == 3:
        result = '小吉'
    elif number == 4:
        result = '凶'
    elif number == 5:
        result = '大凶'
    return result


# 天気予報を返すメソッド
def weather(area_name: str = "東京"):
    # 他のエリア番号は https://zenn.dev/inoue2002/articles/2e07da8d0ca9ca
    area_dict = {
        "東京": "130000",
        "福岡": "400000"
    }
    area_id = area_dict.get(area_name, '130000')

    # 天気概況
    url = f"https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{area_id}.json"
    forecast = requests.get(url).json()
    text = "\n".join(forecast["text"].split())

    return text


def on_message(client: discord.Client, CHANNEL_ID: int):
    """チャンネルにメッセージが投稿されたときの処理
    """
    @client.event
    async def on_message(message: discord.message.Message):
        # 自分のチャンネル以外でのメンションは無視する
        if message.channel.id != CHANNEL_ID:
            return

        # メッセージ送信者がBotだった場合は無視する
        if message.author.bot:
            return

        # 下準備
        # channel
        channel = client.get_channel(CHANNEL_ID)
        # message
        message = message

        ########################################
        # 課題
        ########################################
        # TODO 課題2
        # 占いまたはうらないから始まる場合は占いの結果を返す
        if message.content.startswith(('占い', 'うらない')):
            result = omikuji()
            text = f'{message.author.mention} さんの運勢は{result}です'
            await message.reply(text)
        # 天気または予報から始まる場合は天気を返す(東京)
        elif message.content.startswith(('天気', '予報')):
            result = weather(message.content)
            text = f"天気概況 : {result}"
            await message.reply(text)
        # 都道府県名がメッセージだった場合はその都道府県の天気を返す
        elif message.content.startswith(('東京', '福岡')):
            result = weather(message.content)
            text = f"天気概況 : {result}"
            await message.reply(text)
        else:
            await message.reply("占い、うらない、天気、予報、都道府県名のいずれかを入力してください")
