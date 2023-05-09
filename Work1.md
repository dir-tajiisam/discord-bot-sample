## 5. 課題

***<span style="color: red">※ Discordには機密情報・個人情報は絶対に入れないこと（迷ったらチューターに問い合わせ）</span>***

### 課題 1 DiscordBotの基本動作を確認する

🚨忘れずに🚨  
修正したあとは、VSCodeのターミナルから『Ctrl』+『C』でプログラムを停止し、以下のコマンドで実行してください
```ps
python app.py work1
```

---

#### 課題 1-1: メンションに反応する

- 修正するコード
  - work1/on_message.py
- やること
  - 以下のコードを修正して好きな言葉でBotに返信させよう！
  ```python
  text = f'{message.author.mention} さん、お呼びでしょうか？'
  ```  
- 備考（もっと詳しく知りたい人向け）
  - サーバーにメッセージが投稿されると以下の関数が起動する  
  ``` Python
   @client.event
   async def on_message(message: discord.message.Message):
  ```  
  - 送信されたメッセージの情報は引数の **message** に入っている  
  詳細は[こちら](https://discordpy.readthedocs.io/ja/latest/api.html#discord.Message)を参照

---

#### 課題 1-2: 送られたメッセージをそのまま返却
- 修正するコード
  - work1/on_message.py
- やること
  - 課題1-1では`メンションされた場合の処理`を実装したので、今度は`メンションされていなかった場合の処理`を実装しよう
  - 送られてきたメッセージは、`message.content`で取得できる。これを使ってそのまま返却してみよう
  - 以下の2つは両方とも投稿できるメソッドです。違いを確認してみよう    
   ```python
   await message.reply(text)
   ```
   ```python
   await channel.send(text)
   ```

---

#### 課題 1-3: リアクションに応答する

- 修正するコード
  - work1/on_reaction.py
- やること
  - コードを追加して好きなリアクションでBotに返信させよう！
  - `await message.reply(text)`でも`await channel.send(text)`でもどちらを使ってもOK
  - 文字列に絵文字（😊や🐍など）を入れて送ると、Discord 側の絵文字に変換されるので、それを使ってもOK
  - 絵文字は[こちら](https://fromkato.com/emoji)からコピー可能です
  - (もっとやりたい人向け)押されたリアクションを元に、返信内容を変えて見ることにもチャレンジしてみよう
  ```python
  if str(reaction.emoji) == '🐍':
    # 処理を書く
  ```
- 備考（もっと詳しく知りたい人向け）
  - サーバーにメッセージが投稿されると以下の関数が起動する  
  ``` Python
   @client.event
   async def on_raw_reaction_add(event: discord.RawReactionActionEvent):
  ```  
  - リアクションの情報は引数の **event** に入っている  
  詳細は[こちら](https://discordpy.readthedocs.io/ja/latest/api.html#discord.Reaction)を参照


[課題2(Work2.md)へ続く](./Work2.md)