import streamlit as st
from pyarud.processor import ArudhProcessor

# Page config
st.set_page_config(page_title="Arabic Poetic Analyzer", page_icon="📜")

st.title("📜 Arabic Poetic Analyzer")
st.markdown("Analyze Arabic poetry using the PyArud engine.")

# Initialize the processor
@st.cache_resource
def get_processor():
    return ArudhProcessor()

processor = get_processor()

# Input fields for the two halves of the verse (Sadr and 'Arud)
col1, col2 = st.columns(2)
with col1:
    sadr = st.text_input("First Half (Sadr):", placeholder="قِفَا نَبْكِ مِنْ ذِكْرَى حَبِيبٍ ومَنْزِلِ")
with col2:
    ajuz = st.text_input("Second Half (Ajuz):", placeholder="بِسِقْطِ اللِّوَى بَيْنَ الدَّخُول فَحَوْملِ")

if st.button("Analyze Meter"):
    if sadr and ajuz:
        try:
            # The library expects a list of tuples: [(sadr, ajuz)]
            verse_tuple = (ajuz, sadr) 
            results = processor.process_poem([verse_tuple])
            
            # Extract results (assuming the library returns a list or dict)
            # Based on your snippet, result is the dictionary for the poem
            st.divider()
            
            # Display Detected Meter
            meter = results.get('meter', 'Unknown')
            st.header(f"Detected Meter: {meter}")
            
            # Optional: Display more data if available in the results dictionary
            with st.expander("View Full Analysis Data"):
                st.write(results)
                
        except Exception as e:
            st.error(f"An error occurred during analysis: {e}")
    else:
        st.warning("Please enter both halves of the verse.")
