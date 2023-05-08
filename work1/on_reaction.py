import discord


def on_reaction(client: discord.Client, CHANNEL_ID: int):
    """投稿にリアクションがついたときの処理
    """
    @client.event
    async def on_raw_reaction_add(event: discord.RawReactionActionEvent):
        # 自分のチャンネル以外でのメンションは無視する
        if event.channel_id != CHANNEL_ID:
            return

        # 下準備
        # channel
        channel = client.get_channel(CHANNEL_ID)
        # message
        message = channel.get_partial_message(event.message_id)

        ########################################
        # 課題
        ########################################
        # TODO 課題1-3: リアクションを贈られたときに反応する
        await message.reply(f'{event.emoji}のリアクションありがとう')
        await channel.send('みなさんもリアクションを送ってみてね！🎅')
