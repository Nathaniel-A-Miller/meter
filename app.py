import streamlit as st
from pyarud.arud import ArudAnalyzer

st.title("📜 Arabic Poetic Analyzer")

verse = st.text_input("Enter Verse")
if verse:
    analyzer = ArudAnalyzer()
    # Note: Ensure the method name is 'analyze' 
    # (some versions use 'parse' or 'get_meter')
    result = analyzer.analyze(verse)
    st.write(result)
