## 5. 課題

***<span style="color: red">※ Discordには機密情報・個人情報は絶対に入れないこと（迷ったらチューターに問い合わせ）</span>***

### 課題 3 スラッシュコマンドを使ってみよう

🚨忘れずに🚨  
修正したあとは、VSCodeのターミナルから『Ctrl』+『C』でプログラムを停止し、以下のコマンドで実行してください
```ps
python app.py work3
```

🤖Slashコマンドとは🤖  
テキストチャット内でSlash(/)で始まる命令をBotに処理させる方法で、これを利用することで、通常のメッセージに対してBotが不用意に反応することを防ぐことができる

---

#### 課題 3-1: Slashコマンドを試しに使ってみる
- 修正するコード
  - work3/on_slash.py
- やること
  - `/hello`が使えるようになっているので試してみよう
  - ただ、他の人のアプリのスラッシュコマンドとかぶってしまい、候補がたくさん出てきてしまう場合は、以下の`hello`を自分なりのものに変更しよう
  ``` Python
  @tree.command(
      name="hello",  # コマンド名
      description="Send Hello world."  # コマンドの説明
  )
  ```
  - ex. hello_by_自分の名前
  - これまでメッセージ送信に使っていた関数とは異なるので注意。違いを確認してみよう。またephemeralをTrueにすると、自分にしか見えなくなるので、これも試してみよう
  ```python
  await interaction.response.send_message("***", ephemeral=False)
  ```
  ```python
  await interaction.followup.send("***", ephemeral=False)
  ```

---

#### 課題 3-2: Slashコマンドに引数を渡してみよう
- 修正するコード
  - work3/on_slash.py
- やること
  - `/weather`が使えるようになっているので試してみよう
  - `def weather...`は先程の課題2−3で作成したものと既存のものを上書きしておこう
  - ただ、他の人のアプリのスラッシュコマンドとかぶってしまい、候補がたくさん出てきてしまう場合は、以下の`weather`を自分なりのものに変更しよう
  ``` Python
  @tree.command(
      name="weather",  # コマンド名
      description="てんきをよほーします"  # コマンドの説明
  )
  ```
  - 引数を追加する場合には2箇所修正が必要です。ここも違う名前にしてみたりして確認してみよう。以下は`prefecture`を追加する場合の例
    - コマンドの定義
    ```python
    @commands.describe(prefecture="都道府県名を入力してください")
    ```
    - 関数の引数
    ```python
    async def on_slash_weather(interaction, prefecture: str):
    ```

---

#### 課題3-3: 自分なりのSlashコマンドを作ってみよう
- 修正するコード
  - work3/on_slash.py
- やること
  - `hello`, `weather`のように自分なりのSlashコマンドを作ってみよう
  - 🚨関数名はかぶらないようにしよう（以下は使用中）
    - async def on_slash_hello
    - async def on_slash_weather

[課題4(Work4.md)へ続く](./Work4.md)
