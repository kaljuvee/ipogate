import streamlit as st

# Set page config
st.set_page_config(
    page_title="IPOLabs - Your Gateway to Public Markets",
    page_icon="📈"
)

# Language selector in sidebar
language = st.sidebar.selectbox('Language / Язык', ['English', 'Русский'])
st.session_state['language'] = 'en' if language == 'English' else 'ru'

# Hero section
st.title("IPOLabs")
st.header("Your Gateway to Public Markets")
st.write("IPOGate guides you through every step of your IPO journey with our AI-powered tools and analytics.")
if st.button("Begin Your IPO Journey"):
    st.switch_page("pages/document_analysis.py")

# Main features section
st.header("Your Path to Going Public")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Document Analysis 📄")
    st.write("Transform your company documents into a professional prospectus:")
    st.markdown("""
    - Upload your company documents (PDF, DOCX, or TXT)
    - AI-powered extraction of key company information
    - Automated prospectus generation with standardized formatting
    - Review and edit capabilities for accuracy
    """)

with col2:
    st.subheader("2. Multiplier Valuation 📊")
    st.write("Determine your company's market value using industry standards:")
    st.markdown("""
    - Industry-specific multiple analysis
    - Peer comparison metrics
    - Automated valuation calculations
    - Customizable parameters for precise estimates
    """)

with col3:
    st.subheader("3. Comparative Analysis 📈")
    st.write("Benchmark your company against industry peers:")
    st.markdown("""
    - Comprehensive peer group analysis
    - Market positioning assessment
    - Competitive advantage evaluation
    - Growth potential analysis
    """)

# Additional tools section
st.header("Additional Tools & Resources")

tool_col1, tool_col2, tool_col3 = st.columns(3)

with tool_col1:
    st.subheader("Financial Analysis")
    st.markdown("""
    - Detailed financial statement analysis
    - Key performance indicators
    - Growth projections
    - Cash flow analysis
    """)

with tool_col2:
    st.subheader("Risk Assessment")
    st.markdown("""
    - Industry-specific risk factors
    - Market condition analysis
    - Regulatory compliance checks
    - Mitigation strategies
    """)

with tool_col3:
    st.subheader("Market Intelligence")
    st.markdown("""
    - Industry trends and insights
    - Market sentiment analysis
    - Investor preference tracking
    - Timing recommendations
    """)

# Why choose us section
st.header("Why Choose IPOLabs?")
st.markdown("""
- **AI-Powered Analysis**: Advanced algorithms for accurate data extraction and analysis
- **Time Efficiency**: Automate manual processes and focus on strategic decisions
- **Professional Output**: Generate investor-ready documents and presentations
- **Expert Guidance**: Step-by-step assistance throughout your IPO journey
""")

if st.button("Begin Your IPO Journey", key="bottom_cta"):
    st.switch_page("pages/document_analysis.py")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
For more information about our services, please visit our 
<a href="/about">About Us</a> page or contact our team.
</div>
""", unsafe_allow_html=True)

# Custom CSS
st.markdown("""
<style>
    .stButton button {
        background-color: #007bff;
        color: white;
        border-radius: 4px;
        padding: 0.8rem 1.6rem;
        border: none;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
</style>
""", unsafe_allow_html=True)
