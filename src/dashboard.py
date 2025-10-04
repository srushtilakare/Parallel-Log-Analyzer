import streamlit as st
import pandas as pd
import re
import time  # ✅ Add this line

st.title("📊 Parallel Real-Time Log Analysis Dashboard")

log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).*"(.*?) (.*?) HTTP.*" (\d+) ([\d.]+)')
LOG_FILE = "data/sample_logs.log"

def read_logs():
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
    logs = []
    for line in lines[-200:]:  # show recent logs only
        match = log_pattern.search(line)
        if match:
            ip, method, url, status, response_time = match.groups()
            logs.append({
                "IP": ip,
                "Method": method,
                "URL": url,
                "Status": int(status),
                "ResponseTime": float(response_time)
            })
    return pd.DataFrame(logs)

while True:
    df = read_logs()
    st.dataframe(df.tail(10))
    st.bar_chart(df["Status"].value_counts())
    time.sleep(2)
    st.rerun()
