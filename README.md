# 🛸 Ben 10 Battle Simulator : https://ben10-battle-simulator.onrender.com/ 
An interactive battle simulator inspired by Ben 10, powered by Machine Learning, a FastAPI backend, and a Streamlit frontend.
Predict who wins in alien face-offs using real stats, trained models, and a fun web interface!

| Component        | Description                                                     |
| ---------------- | --------------------------------------------------------------- |
| 🔧 **Backend**   | FastAPI REST API serving predictions from a trained ML model.   |
| 🎮 **Frontend**  | Streamlit web app for selecting aliens and simulating battles.  |
| 🧠 **ML Models** | Pre-trained models (saved with `joblib`) for battle prediction. |
| 📊 **Data**      | Cleaned alien and battle datasets stored in CSV format.         |
| 🏗 **Structure** | Minimal, modular, and easy to extend or modify.                 |

# Project Structure
Ben10_Battle_Simulator/
├── backend/                 
│   ├── main.py                # FastAPI main server
│   ├── battle_service.py      # Core prediction logic
│   ├── requirements.txt       
│   └── __init__.py
│
├── frontend/                
│   ├── app.py                 # Streamlit frontend UI
│   ├── api_client.py          # Connects to FastAPI backend
│   └── requirements.txt
│
├── data/                     
│   ├── ben10_aliens.csv
│   ├── ben10_enemies.csv
│   └── ben10_battles.csv
│
├── models/                   
│   ├── ben10_battle_predictor.pkl
│   ├── ben10_feature_scaler.pkl
│   └── ben10_aliens_clean.pkl
│
├── notebook/                 
│   └── cleaning_training.ipynb  # Data cleaning + model training
│
├── run_backend.py            # Script to run FastAPI server
├── run_frontend.py           # Script to run Streamlit app
└── README.md                 # Project documentation


# 💻 Prerequisites
Python 3.11+
Git (optional)

# 🔧 Setup Instructions (Run Locally)

1. Clone the Repository
git clone https://github.com/AI-WAJID/Ben10_Battle_Simulator.git
cd Ben10_Battle_Simulator

2. Create and Activate a Virtual Environment
   Windows (PowerShell):
   python -m venv venv
   .\venv\Scripts\Activate
   
3. Upgrade Tools
   python -m pip install --upgrade pip setuptools wheel

4. Install and Run the Backend (FastAPI)
   pip install -r backend/requirements.txt
   python run_backend.py
   📍 Backend will start at: http://localhost:8000
5. Open a New Terminal → Activate Environment → Run Frontend (Streamlit)
   pip install -r frontend/requirements.txt
   python run_frontend.py
   📍 Frontend will start at: http://localhost:8501


# 🎮 How to Use
Go to http://localhost:8501.
Select two aliens from the dropdown menus.
Click Simulate Battle.

View:
Alien stat comparison
Prediction confidence
Declared winner
Backend handles logic via API, frontend shows results.

# 📬 Contact
GitHub: AI-WAJID

Email: wajidthephenom@gmail.com

├── run_backend.py            # Script to run FastAPI server
├── run_frontend.py           # Script to run Streamlit app
└── README.md                 # Project documentation
