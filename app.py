
import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

st.set_page_config(page_title="תחזית זהב ומניות - אמת", layout="centered")

st.title("🧠 תחזית אמת - מניות וזהב")
st.write("בחר נכס, טווח זמן וסכום השקעה - וקבל תחזית עם חיווי מיידי.")

stocks = {
    'נאסד"ק (NASDAQ)': '^IXIC',
    'S&P 500': '^GSPC',
    'זהב (Gold)': 'GC=F',
    'נאסד"ק 100 (NDX)': '^NDX',
    'ת"א 35': 'TA35.TA',
    'Nvidia': 'NVDA',
    'Bitcoin': 'BTC-USD',
    'זהב - Plus500': 'XAUUSD=X'
}

times = {
    '1 דקה': 1,
    '5 דקות': 5,
    '10 דקות': 10,
    '30 דקות': 30,
    'שעה': 60,
    'יום': 1440,
    'שבוע': 10080
}

selected_stock = st.selectbox("בחר נכס", list(stocks.keys()))
selected_time = st.selectbox("בחר טווח זמן", list(times.keys()))
amount = st.number_input("סכום השקעה ($)", min_value=1, step=1, value=1000)

def get_prediction(ticker):
    try:
        end = datetime.now()
        start = end - timedelta(days=2)
        data = yf.download(ticker, start=start, end=end, interval="1m")
        if data.empty:
            return "❌ לא נמצאו נתונים", "-"
        current = data["Close"][-1]
        trend = "קנייה 🔼" if data["Close"][-1] > data["Close"][-10] else "מכירה 🔽"
        return trend, current
    except Exception as e:
        return f"שגיאה: {str(e)}", "-"

if st.button("קבל תחזית"):
    ticker = stocks[selected_stock]
    trend, current_price = get_prediction(ticker)
    st.subheader(f"תחזית ל-{selected_stock}")
    st.write(f"טווח זמן: {selected_time}")
    st.write(f"מחיר נוכחי: {current_price}")
    st.success(f"המלצה: {trend}")
    if trend.startswith("קנייה"):
        expected_return = amount * 1.02
    else:
        expected_return = amount * 0.98
    st.info(f"רווח/הפסד צפוי: ${expected_return - amount:.2f} (סה"כ: ${expected_return:.2f})")
