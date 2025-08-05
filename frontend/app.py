import streamlit as st, pandas as pd, plotly.express as px
from api_client import get_aliens, get_stats, predict

st.set_page_config("Ben 10 Battle Sim",":alien:")
st.title("🛸 Ben 10 – Battle Simulator")

aliens = get_aliens()
col1,col2 = st.columns(2)
a = col1.selectbox("Alien 1",aliens)
b = col2.selectbox("Alien 2",aliens,index=1)

if st.button("🔥 BATTLE!"):
    res = predict(a,b)
    st.subheader(f"🏆 Winner: **{res['predicted_winner']}** "
                 f"(confidence {res['confidence']:.2%})")
    st.progress(res['alien1_win_probability'])
    st.json(res)
    
    stats = pd.DataFrame([
        {"Alien":a,**get_stats(a)},
        {"Alien":b,**get_stats(b)}
    ]).set_index("Alien")
    st.table(stats)

