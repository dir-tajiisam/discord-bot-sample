## 5. 課題

***<span style="color: red">※ Discordには機密情報・個人情報は絶対に入れないこと（迷ったらチューターに問い合わせ）</span>***

### 課題 4 会話っぽいものを作ってみよう

🚨忘れずに🚨  
VSCodeのターミナルを開いた際は、以下のコマンドを実行してください
```ps
pipenv shell
```
修正したあとは、VSCodeのターミナルから『Ctrl』+『C』でプログラムを停止し、以下のコマンドで実行してください<span style="color: red">（work4をつけること）</span>
```ps
python app.py work4
```

:point_right: ターミナルで十字キーの上を押すと直前に入力したコマンドが表示されるので、簡単にコマンド再実行ができます

---

#### 課題 4-1: 会話っぽいものを作ってみよう

すでにサンプルがあるのでそれの動作を確認してみよう

- どう動くのか？
  1. スラッシュコマンドを入力すると、Botがドロップダウンリストを表示してくれる
    - この関数の中でドロップダウンリストを作って、メッセージ送信している
    ```python
    async def on_slash_weather(interaction: discord.interactions.Interaction):
    ```
  2. ドロップダウンリストを選択すると、選択肢に応じた反応をBotがしてくれる
    - `on_slash_weather`の中で、選択肢が選択されたときの処理を設定している（`on_prefecture_selected`が該当）
    ```python
    select.callback = on_prefecture_selected
    ```
    - `on_prefecture_selected`の中の処理は↓の関数の中で定義している
    ```python
    async def on_prefecture_selected(interaction: discord.interactions.Interaction):
    ```
- 修正するコード
  - work4/on_slash.py
- やること
  - まずはそのまま動かして動作を確認してみよう
  - ドロップダウンリストの選択肢を追加してみよう
  - 選択後の動作（`async def on_prefecture_selected`）の中身を書き換えてみよう

#### 課題4-2: 自分なりのコマンドを作ってみよう

- 修正するコード
  - work4/on_slash.py
- やること
  - `weather`のように自分なりのSlashコマンドを作ってみよう
  - 🚨関数名はかぶらないようにしよう（以下は使用中）
    - async def on_slash_weather
    - async def on_prefecture_selected

[課題5(Work5.md)へ続く](./Work5.md)

