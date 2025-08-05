import joblib, numpy as np, pandas as pd, pathlib

root = pathlib.Path(__file__).resolve().parents[1]
data_dir   = root /  "data"
model_dir  = root /  "models"

class BattlePredictorService:
    def __init__(self):
        self.model   = joblib.load(model_dir / "ben10_battle_predictor.pkl")
        self.scaler  = joblib.load(model_dir / "ben10_feature_scaler.pkl")
        self.aliens  = joblib.load(model_dir / "ben10_aliens_clean.pkl")
        self.cols    = ["strength_level","speed_level","intelligence","power"]

    def get_all_aliens(self): return self.aliens["alien_name"].tolist()

    def get_alien_stats(self, name):
        row = self.aliens[self.aliens.alien_name==name]
        return None if row.empty else row[self.cols].iloc[0].to_dict()

    def _vector(self, a, b):
        a = self.get_alien_stats(a); b = self.get_alien_stats(b)
        if not a or not b: return None
        feats = np.array([
            *a.values(), *b.values(),
            a["power"]-b["power"],
            a["strength_level"]-b["strength_level"],
            a["speed_level"]-b["speed_level"],
            a["intelligence"]-b["intelligence"]
        ]).reshape(1,-1)
        return self.scaler.transform(feats)

    def predict_winner(self, a, b):
        vec = self._vector(a,b)
        if vec is None: return {"error":"Unknown alien"}
        proba = self.model.predict_proba(vec)[0]
        winner = a if self.model.predict(vec)[0]==1 else b
        return {
            "alien1_name":a,"alien2_name":b,
            "predicted_winner":winner,
            "confidence":float(max(proba)),
            "alien1_win_probability":float(proba[1]),
            "alien2_win_probability":float(proba[0])
        }
