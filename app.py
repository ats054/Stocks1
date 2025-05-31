
import streamlit as st

st.set_page_config(page_title="תחזית זהב ומניות - אמת", layout="centered")

st.title("🧠 תחזית אמת - מניות וזהב")
st.write("בחר נכס, טווח זמן וסכום השקעה - וקבל תחזית עם חיווי מיידי.")

stocks = {
    'נאסד"ק (NASDAQ)': '^IXIC',
    'S&P 500': '^GSPC',
    'זהב (Gold)': 'GC=F',
    'נאסד"ק 100 (NDX)': '^NDX',
    'ת"א 35': 'TA35.TA',
    'Nvidia': 'NVDA'
}

times = ['1 דקה', '5 דקות', '10 דקות', '30 דקות', 'שעה', 'יום', 'שבוע']

selected_stock = st.selectbox("בחר נכס", list(stocks.keys()))
selected_time = st.selectbox("בחר טווח זמן", times)
amount = st.number_input("סכום השקעה ($)", min_value=1, step=1, value=1000)

if st.button("קבל תחזית"):
    expected_return = amount * 1.02  # חיזוי רווח פשוט לדוגמה
    st.success(f"תחזית ל-{selected_stock} בטווח {selected_time} עבור ${amount}: קנייה 🔼 (רווח צפוי של כ-2%)")
    st.info(f"רווח/הפסד צפוי: ${expected_return - amount:.2f} (סה\"כ: ${expected_return:.2f})")
