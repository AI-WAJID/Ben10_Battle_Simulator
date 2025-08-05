import os, subprocess, pathlib, sys
os.chdir(pathlib.Path(__file__).parent/"frontend")
subprocess.run([sys.executable,"-m","streamlit","run","app.py"])
