import streamlit as st
import joblib

model = joblib.load('yapay_zeka_beyni.pkl')

st.title("🛍️ Müşteri Satın Alma Tahmini")
st.write("Müşterinin bilgilerini girerek satın alma ihtimalini tahmin edin.")

yas = st.number_input("Müşteri Yaşı", min_value=18, max_value=100, value=25)
dakika = st.number_input("Sitede Kaldığı Süre (Dakika)", min_value=1, max_value=300, value=10)

if st.button("Tahmin Et"):
    tahmin = model.predict([[yas, dakika]])[0]
    if tahmin == 1:
        st.success("🛒 Sonuç: Müşteri SATIN ALACAK!")
    else:
        st.error("❌ Sonuç: Müşteri SATIN ALMAYACAK.")
      
