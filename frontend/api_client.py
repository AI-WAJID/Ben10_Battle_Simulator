import requests, os
API = os.getenv("API_URL","http://localhost:8000")

def get_aliens():        return requests.get(f"{API}/aliens").json()
def get_stats(name):     return requests.get(f"{API}/aliens/{name}").json()
def predict(a,b):        return requests.post(f"{API}/predict",
                                json={"alien1_name":a,"alien2_name":b}).json()
