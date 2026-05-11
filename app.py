import streamlit as st
# Try the submodule path
try:
    from pyarud.arud import ArudAnalyzer
except ImportError:
    # Fallback/Diagnostic
    st.error("Could not find ArudAnalyzer. Printing library contents...")
    import pyarud
    st.write(dir(pyarud))
    st.stop()

st.title("📜 Arabic Poetic Analyzer")

verse = st.text_input("Enter Verse")
if verse:
    analyzer = ArudAnalyzer()
    # Note: Ensure the method name is 'analyze' 
    # (some versions use 'parse' or 'get_meter')
    result = analyzer.analyze(verse)
    st.write(result)
