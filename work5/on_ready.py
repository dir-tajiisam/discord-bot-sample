import discord


def on_ready(client: discord.Client, tree: discord.app_commands.CommandTree, CHANNEL_ID: int, SERVER_ID: int):
    """botが起動したときの処理
    """
    # bot起動時の処理
    @client.event
    async def on_ready():
        # botが起動したときにターミナルに文字を表示してみる
        print('Work5: on_ready.py')
        await tree.sync(guild=discord.Object(id=SERVER_ID))
