import streamlit as st
import pyarud

# Access the logic via the module directly
from pyarud.pyarud import ArudAnalyzer

st.title("📜 Arabic Poetic Analyzer")

# Let's add a diagnostic check to see what's actually there
if st.checkbox("Show Library Debug Info"):
    st.write("Package path:", pyarud.__file__)
    st.write("Available sub-modules:", dir(pyarud))

verse = st.text_input("Enter your verse:", "خليلَيَّ رُبَّ الموتِ فيهِ حياةُ")

if verse:
    try:
        # We instantiate the class from the nested module
        analyzer = ArudAnalyzer()
        result = analyzer.analyze(verse)
        
        st.success(f"Meter: {result.meter_name}")
        st.info(f"Scansion: {result.parts}")
    except Exception as e:
        st.error(f"Error: {e}")
