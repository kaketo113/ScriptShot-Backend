from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql # PyMySQLをインポート（インストール済み）

# Flaskアプリの初期化
app = Flask(__name__)

# --- データベース接続設定 ---
# (プロのシステムエンジニアとして、ここは重要な設定です)
#
# "mysql+pymysql://[ユーザー名]:[パスワード]@[ホスト名]/[データベース名]"
#
# [ユーザー名]: MySQLに設定したユーザー名 (例: 'root')
# [パスワード]: MySQLに設定したパスワード (例: 'password')
# [ホスト名]: あなたのPC (例: 'localhost' または '127.0.0.1')
# [データベース名]: さっき作ったDB名 ( 'scriptshot_db' )
#
# ★★★↓自分の環境に合わせて必ず書き換えてください↓★★★
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/scriptshot_db'
# ★★★↑自分の環境に合わせて必ず書き換えてください↑★★★

# データベースとアプリを連携させる
db = SQLAlchemy(app)


# --- データベースの「設計図（モデル）」 ---
# (プロのWebデザイナーとして、ここの設計がアプリの骨格になります)

# 「User」テーブルの設計図
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # ユーザーID (自動で増える)
    username = db.Column(db.String(80), unique=True, nullable=False) # ユーザー名
    email = db.Column(db.String(120), unique=True, nullable=False) # Eメール
    password_hash = db.Column(db.String(128), nullable=False) # ハッシュ化されたパスワード
    # (今後、プロフィール情報、ポイント、所持アイテムなどもここに追加します)

# 「Post」テーブルの設計図
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 投稿ID (自動で増える)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # 投稿者のID
    caption = db.Column(db.Text, nullable=True) # キャプション（説明文）
    source_code = db.Column(db.Text, nullable=False) # ソースコード
    screenshot_url = db.Column(db.String(255), nullable=False) # スクショ画像のURL
    created_at = db.Column(db.DateTime, server_default=db.func.now()) # 投稿日時
    # (今後、いいね数などもここに追加します)

# --- APIのエンドポイント ---

@app.route("/")
def hello_world():
    return "Hello, Backend! データベース接続準備完了！"


# サーバーを起動
if __name__ == '__main__':
    app.run(debug=True)