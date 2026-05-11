import streamlit as st
import pyarud
from pyarud import ArudAnalyzer

st.title("📜 Arabic Poetic Analyzer")

# This will help us see if the import finally worked
try:
    analyzer = ArudAnalyzer()
    st.success("Library loaded successfully!")
except Exception as e:
    st.error(f"Initialization error: {e}")

verse = st.text_input("Enter your verse:")

if verse:
    try:
        result = analyzer.analyze(verse)
        st.write(f"**Meter:** {result.meter_name}")
        st.write(f"**Scansion:** {result.parts}")
    except Exception as e:
        st.error(f"Analysis error: {e}")
