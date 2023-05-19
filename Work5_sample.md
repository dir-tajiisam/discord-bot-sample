## 課題 5 サンプル

### 連続する会話
- select.callbackで選択されたあとの処理の中でもう一回
    - ドロップダウンリストを作成
    - 選択されたあとの処理を追加
    - Viewを作成し、ドロップダウンリストを追加
    - ドロップダウンリストを送信
- 例)on_slash.pyのon_prefecture_selectedを改修する形で。。。
```python
    async def evaluation(interaction: discord.interactions.Interaction):
        valuation = interaction.data['values'][0]

        await interaction.response.send_message(f"高評価ありがとうございます！", ephemeral=False)

    async def on_prefecture_selected(interaction: discord.interactions.Interaction):
        # 選択されたものを取り出す
        prefecture = interaction.data['values'][0]

        # メッセージを送信する
        text = weather(prefecture)
        await interaction.response.send_message(text, ephemeral=False)

        # 新規にドロップダウンリストを作成
        select2 = discord.ui.Select(placeholder="評価をお願いします！")
        # ドロップダウンリストに選択肢を追加
        select2.add_option(
            label="良かった",
            value="good"
        )
        select2.add_option(
            label="良くなかった",
            value="bad"
        )
        # 選択されたあとの処理を追加
        select2.callback = evaluation

        # Viewを作成し、ドロップダウンリストを追加
        view = discord.ui.View()
        view.add_item(select2)

        # ドロップダウンリストを送信
        await interaction.followup.send("いかがでしたか？", view=view)
```


### リマインダーbot
- on_readyにリマインダー機能を記述する
```python
#on_ready.py
from discord.ext import tasks
from work5.on_slash import get_remind_list
import datetime
import math

    #リマインド機能
    #一秒ごとに処理を実行する
    @tasks.loop(seconds=1)
    async def push_remind():
        channel =  client.get_channel(CHANNEL_ID)
        remind_list = get_remind_list()
        # リマインド時刻一覧を取得
        keys = remind_list.keys()
        for key in keys:
            now_time = round(datetime.datetime.now().timestamp())
            key_time = round(datetime.datetime.strptime(key, '%Y-%m-%d %H:%M:%S').timestamp())
            if (now_time == key_time):
                remind = remind_list.get(key) 
                text = f"{remind[0].mention} さん{remind[1]}の時間です！！！"
                await channel.send(text)
```
- on_slash.pyにリマインダーを登録するスラッシュコマンドを記述する
```python
#on_slash.py
remind_list = {}
def on_slash(client: discord.Client, tree: discord.app_commands.CommandTree, commands: discord.app_commands, CHANNEL_ID: int, SERVER_ID: int):

    #リマインダー登録
    # 時刻は '2012-12-29 13:49:37'のような形式で入力します
    @tree.command(
        name="add_remind",  # コマンド名
        description="リマインドを登録します"  # コマンドの説明
    )
    @commands.describe(remind="リマインド内容を入力してください")
    @commands.describe(remind_time="リマインド時刻を入力してください")
    @commands.guilds(SERVER_ID)
    async def on_slash_add_remind(interaction: discord.interactions.Interaction, remind : str, remind_time: str):
        # 特定のチャンネル外での実行は無視する
        if interaction.channel.id != CHANNEL_ID:
            await interaction.response.send_message("このチャンネルでは使用できません", ephemeral=True)
            return

        #例）宛先：リマインド内容
        remind_value = (interaction.user, remind)
        
        
        #同じ時間に登録されると上書きされるので注意
        remind_list[remind_time] = remind_value

        # メッセージを送信する
        text = f"リマインダーを登録しました。時刻：{remind_time} : {remind}"
        await interaction.response.send_message(text, ephemeral=False)

# リマインド一覧を返却する関数
def get_remind_list():
    return remind_list
```

### ChatGptを組み込む
- openaiのAPI_KEYを取得する。
- 取得方法は[こちら](https://auto-worker.com/blog/?p=6988)
- .envに追記（！！！！ソースコード上にAPI_KEYを直接書かないこと！！！！）
```
API_KEY = <openaiのAPI_KEY>
```
- openaiにpackage追加
    - Pipfileの[packages]の下にopenai = "*"を記載
    - pipenv installを実行
    - pipenv shellを実行

```python
#on_message.py
import os
import openai

# .envにOPENAI_IDを定義し、取得したapikeyを記述しておく
openai.api_key = os.environ['API_KEY']
def on_message(client: discord.Client, CHANNEL_ID: int):

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

        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message.content},
        ],
        )
        await message.reply(response.choices[0]["message"]["content"].strip())
```
## ローカルの画像を表示する
- 「file=discord.File('画像ファイルのパス')」で表示できる
- 表示したい画像ファイルをDISCORD‐BOT―SAMPLEフォルダ配下に配置する
- 画像ファイルを右クリック→「相対パスをコピー」を選択
― コピーしたパスを画像ファイルのパスの部分に貼り付ける
- 例）
``` python
        await interaction.followup.send(file=discord.File('sorajiro.jpg'), ephemeral=False)

```