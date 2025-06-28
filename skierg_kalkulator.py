import streamlit as st

def kalkuler_snittfart(tid_minutter: int, tid_sekunder: int, distanse_meter: int = 5000):
    total_tid_sek = tid_minutter * 60 + tid_sekunder
    antall_intervaller = distanse_meter / 500
    snitt_tid_per_500m = total_tid_sek / antall_intervaller

    min_per_500 = int(snitt_tid_per_500m // 60)
    sek_per_500 = round(snitt_tid_per_500m % 60, 1)

    return f"Du må ha en snittfart på {min_per_500}:{sek_per_500:04.1f} per 500 meter."

st.title("SkiErg Snittfart Kalkulator")
st.write("Beregn hvilken snittfart per 500 meter du må holde for å nå en ønsket tid på en gitt distanse.")

minutter = st.number_input("Ønsket minutter", min_value=0, value=19)
sekunder = st.number_input("Ønsket sekunder", min_value=0, max_value=59, value=30)
distanse = st.selectbox("Distanse (meter)", [1000, 2000, 5000, 10000, 21097, 42195], index=2)

if st.button("Beregn"):
    resultat = kalkuler_snittfart(minutter, sekunder, distanse)
    st.success(resultat)
