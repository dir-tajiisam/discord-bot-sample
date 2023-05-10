import discord
import random
import requests


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
    forecast = requests.get(url, verify=False).json()
    text = "\n".join(forecast["text"].split())

    return text


def on_slash(client: discord.Client, tree: discord.app_commands.CommandTree, commands: discord.app_commands, CHANNEL_ID: int, SERVER_ID: int):
    """Slashコマンドが送られたときの処理
    """

    # TODO 課題3-1: Slashコマンドを試しに使ってみる
    @tree.command(
        name="hello",  # コマンド名
        description="Send Hello world."  # コマンドの説明
    )
    @commands.guilds(SERVER_ID)
    async def on_slash_hello(interaction: discord.interactions.Interaction):
        # 特定のチャンネル外での実行は無視する
        if interaction.channel.id != CHANNEL_ID:
            await interaction.response.send_message("このチャンネルでは使用できません", ephemeral=True)
            return

        # 1つはresponse.send_messageにする。ephemeral=Trueにすると実行した人にのみ見える
        await interaction.response.send_message("実行していない人にも見える", ephemeral=False)
        # await interaction.response.send_message("実行した人にのみ見える", ephemeral=True)

        # 2つ目以降送る場合はfollowup.sendにする
        await interaction.followup.send("実行していない人にも見える", ephemeral=False)
        await interaction.followup.send("実行した人にのみ見える", ephemeral=True)

    # TODO 課題3-2: Slashコマンドに引数を追加してみよう
    @tree.command(
        name="weather",  # コマンド名
        description="てんきをよほーします",  # コマンドの説明
    )
    @commands.describe(prefecture="都道府県名を入力してください")
    @commands.guilds(SERVER_ID)
    async def on_slash_weather(interaction: discord.interactions.Interaction, prefecture: str):
        # 特定のチャンネル外での実行は無視する
        if interaction.channel.id != CHANNEL_ID:
            await interaction.response.send_message("このチャンネルでは使用できません", ephemeral=True)
            return

        # メッセージを送信する
        text = weather(prefecture)
        await interaction.response.send_message(text, ephemeral=False)

    # TODO 課題3-3: 自分なりのSlashコマンドを作ってみよう
