from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .battle_service import BattlePredictorService

app = FastAPI(title="Ben 10 Battle Predictor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

service = BattlePredictorService()

class BattleReq(BaseModel):
    alien1_name: str
    alien2_name: str

class BattleRes(BaseModel):
    alien1_name: str; alien2_name: str
    predicted_winner: str
    confidence: float
    alien1_win_probability: float
    alien2_win_probability: float

@app.get("/aliens")
def list_aliens(): return service.get_all_aliens()

@app.get("/aliens/{name}")
def alien_stats(name: str):
    stats = service.get_alien_stats(name)
    if not stats: raise HTTPException(404, f"Alien '{name}' not found")
    return stats

@app.post("/predict", response_model=BattleRes)
def predict(req: BattleReq):
    res = service.predict_winner(req.alien1_name, req.alien2_name)
    if "error" in res: raise HTTPException(400, res["error"])
    return res
