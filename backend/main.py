import jwt
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 推測可能な弱い秘密鍵をハードコード
SECRET_KEY = "secret123"

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/api/login")
def login(req: LoginRequest):
    # 誰でも「一般ユーザー」としてログイン成功とする
    payload = {
        "sub": req.username,
        "role": "user"
    }
    # JWTを生成
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return {"token": token}

@app.get("/api/admin")
def admin_data(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="トークンがありません")
    
    token = authorization.replace("Bearer ", "")
    
    try:
        # JWT検証
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        
        # 権限チェック
        if decoded.get("role") != "admin":
            raise HTTPException(status_code=403, detail="管理者権限がありません。")
            
        return {"message": "管理者アクセス成功"}
        
    except jwt.InvalidSignatureError:
        raise HTTPException(status_code=401, detail="署名が不正です")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="無効なトークンです")