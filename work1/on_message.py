import discord


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
        # Check!
        # message.mentions は メンションされた人のリスト
        # client.user は bot 自身の名前
        # message.author.mention は呼びかけた人の名前
        # message.content は投稿されたメッセージの内容

        # 課題1-1: メンションに反応する
        # メンションされた場合の処理
        if client.user in message.mentions:
            # TODO 返信用の文面を作る
            text = f'{message.author.mention} さん、お呼びでしょうか？'
            # スレッドで返信する
            await message.reply(text)

        # TODO 課題1-2: 送られたメッセージをそのまま返却
        # メンションされていない場合の処理
        else:
            # 投稿用の文面を作る
            text = message.content
            await channel.send(text)
