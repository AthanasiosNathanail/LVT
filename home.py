import streamlit as st

def home():
    
    sm_li = """<a href='https://www.linkedin.com/in/athanasiosnathanail/' target="_blank"><img src='https://cdn.exclaimer.com/Handbook%20Images/linkedin-icon_32x32.png'></a>"""
    

    st.title('LAS Visualization Tool - Version 1.0')
    
    st.write('## What Can You Do Here?')
    st.write('''LAS Visualization Tool is a tool designed using an integration of Python and Streamlit to help you view and gain an understanding of the contents within
    your LAS files.''')
    st.write('To load your LAS file, start by uploading the file using the "Browse files" option found in the sidebar.')
    st.write('Use the Navigation menu to explore with ease the following sections.')
    st.write('## Sections')
    st.write('**Header Info:** Explore crucial information stored in the LAS file header.')
    st.write('**Data Information:** Dive into the curve details, including well names, property names, details and units.')
    st.write('**Data Visualisation:** Visualize LAS file data like with log plots, crossplots, and histograms.')
    st.write('**Missing Data Visualisation:** Gain insights into data completeness and spot areas with missing values.')
    st.write('## Get in Touch')
    st.write(f'\nNeed assistance or have questions? Do not hesitate to reach out. You can drop me an email at athanasios.nathanail@mines.edu or contact me via Linkedin at https://www.linkedin.com/in/athanasiosnathanail/.')
