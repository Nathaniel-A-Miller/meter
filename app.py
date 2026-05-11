import streamlit as st
from pyarud import ArudAnalyzer

# Page configuration
st.set_page_config(page_title="PyArud Poetic Analyzer", page_icon="📜")

st.title("📜 PyArud: Arabic Prosody Analyzer")
st.markdown("Analyze Arabic poetic verses, detect meters (Buhur), and identify variations.")

# User Input
verse = st.text_input("Enter an Arabic poetic verse:", placeholder="قفا نبك من ذكرى حبيب ومنزل...")

if verse:
    analyzer = ArudAnalyzer()
    result = analyzer.analyze(verse)
    
    # Display Results
    st.subheader("Analysis Results")
    st.write(f"**Detected Meter:** {result.meter_name}")
    
    # Display foot-by-foot analysis
    st.write("**Taf'ila Analysis:**")
    for foot in result.parts:
        st.code(f"{foot.tafeela} -> {foot.pattern}")
        
    if result.zihaf:
        st.info(f"Detected Zihaf/Illah: {', '.join(result.zihaf)}")
