from work1 import on_reaction as on_reaction1
from work1 import on_message as on_message1
from work1 import on_ready as on_ready1
from work2 import on_reaction as on_reaction2
from work2 import on_message as on_message2
from work2 import on_ready as on_ready2
from work3 import on_reaction as on_reaction3
from work3 import on_message as on_message3
from work3 import on_ready as on_ready3
from work3 import on_slash as on_slash3
import discord
from dotenv import load_dotenv
import sys
import os

# 個人ごとの設定
"""個人ごとの設定
TOKEN: botのトークン。botの設定画面から確認できる。
    1. https://discord.com/developers/applications にアクセス
    2. 既存のアプリケーション or 右上のNew Applicationをクリック
    3. Botを選択し、Add Botをクリック
    4. TOKENの下のCopyをクリックし、TOKENをコピー or Reset Tokenをクリックし、TOKENを再生成
    
SERVER_ID: botを動かしているサーバーのID
    1. Discordの設定から該当のチャンネルを開く
    2. URLの真ん中にある数字がサーバーID https://discord.com/channels/<Server ID>/<Channel ID>

CHANNEL_ID: botを動かしたいチャンネルのID。チャンネルを右クリックし、IDをコピーで取得できる。
    1. Discordの設定から該当のチャンネルを開く
    2. URLの最後の方にある数字がチャンネルID https://discord.com/channels/<Server ID>/<Channel ID>
"""
load_dotenv()
TOKEN = os.environ['TOKEN']
SERVER_ID = int(os.environ['SERVER_ID'])
CHANNEL_ID = int(os.environ['CHANNEL_ID'])


# Bot起動
client = discord.Client(intents=discord.Intents.all())

# get args
work = sys.argv[1]

# 課題3
if work == 'work3':
    tree = discord.app_commands.CommandTree(client)
    commands = discord.app_commands
    # 起動時に動作する処理
    on_ready3(client, tree, CHANNEL_ID, SERVER_ID)
    # メッセージ受信時に動作する処理
    on_message3(client, CHANNEL_ID)
    # リアクション受信時に動作する処理
    on_reaction3(client, CHANNEL_ID)
    # スラッシュコマンド受信時に動作する処理
    on_slash3(client, tree, commands, CHANNEL_ID, SERVER_ID)
# 課題2
elif work == 'work2':
    # 起動時に動作する処理
    on_ready2(client, CHANNEL_ID)
    # メッセージ受信時に動作する処理
    on_message2(client, CHANNEL_ID)
    # リアクション受信時に動作する処理
    on_reaction2(client, CHANNEL_ID)
# 課題1
else:
    # 起動時に動作する処理
    on_ready1(client, CHANNEL_ID)
    # メッセージ受信時に動作する処理
    on_message1(client, CHANNEL_ID)
    # リアクション受信時に動作する処理
    on_reaction1(client, CHANNEL_ID)


# Botの起動
client.run(TOKEN)
