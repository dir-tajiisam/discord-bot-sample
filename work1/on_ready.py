import discord


def on_ready(client: discord.Client, CHANNEL_ID: int):
    """botが起動したときの処理
    """
    # bot起動時の処理
    @client.event
    async def on_ready():
        # botが起動したときにターミナルに文字を表示してみる
        print('Work1: on_ready.py')
