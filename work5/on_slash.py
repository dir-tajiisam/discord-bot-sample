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
    forecast = requests.get(url).json()
    text = "\n".join(forecast["text"].split())

    return text


def on_slash(client: discord.Client, tree: discord.app_commands.CommandTree, commands: discord.app_commands, CHANNEL_ID: int, SERVER_ID: int):
    """Slashコマンドが送られたときの処理
    """

    # TODO 課題4-1: 会話っぽいものを作ってみよう
    async def on_prefecture_selected(interaction: discord.interactions.Interaction):
        # 選択されたものを取り出す
        prefecture = interaction.data['values'][0]

        # メッセージを送信する
        text = weather(prefecture)
        await interaction.response.send_message(text, ephemeral=False)

    @tree.command(
        name="weather",  # コマンド名
        description="てんきをよほーします",  # コマンドの説明
    )
    @commands.guilds(SERVER_ID)
    async def on_slash_weather(interaction: discord.interactions.Interaction):
        if interaction.channel.id != CHANNEL_ID:
            await interaction.response.send_message("このチャンネルでは使用できません", ephemeral=True)
            return

        # ドロップダウンリストを作成
        select = discord.ui.Select(placeholder="都道府県を選択してください")
        # ドロップダウンリストに選択肢を追加
        select.add_option(
            label="東京(とうきょう)",
            value="東京",
            description="東京についておしらべいたします",
        )
        select.add_option(
            label="福岡(ふくおか)",
            value="福岡",
            description="福岡についておしらべいたします",
        )
        # 選択されたあとの処理を追加
        select.callback = on_prefecture_selected

        # Viewを作成し、ドロップダウンリストを追加
        view = discord.ui.View()
        view.add_item(select)

        # メッセージを送信する
        await interaction.response.send_message("天気をお調べいたします！", view=view)

    # TODO 課題4-2: 自分なりのコマンドを作ってみよう
