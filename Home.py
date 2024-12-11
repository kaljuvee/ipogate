import streamlit as st

st.title('IPOGate')
st.subheader('Your Gateway to Public Markets')

# Add call-to-action button in the sidebar
with st.sidebar:
    st.header("Get Started")
    if st.button("Begin Your IPO Journey", type="primary"):
        st.switch_page("pages/00_Document_Analysis.py")

# Main content
st.markdown("""
## Your Path to Going Public

IPOGate guides you through every step of your IPO journey with our AI-powered tools and analytics.

### 1. Document Analysis 📄
Transform your company documents into a professional prospectus:
- Upload your company documents (PDF, DOCX, or TXT)
- AI-powered extraction of key company information
- Automated prospectus generation with standardized formatting
- Review and edit capabilities for accuracy

### 2. Multiplier Valuation 📊
Determine your company's market value using industry standards:
- Industry-specific multiple analysis
- Peer comparison metrics
- Automated valuation calculations
- Customizable parameters for precise estimates

### 3. Comparative Analysis 📈
Benchmark your company against industry peers:
- Comprehensive peer group analysis
- Market positioning assessment
- Competitive advantage evaluation
- Growth potential analysis

### Additional Tools & Resources

#### Financial Analysis
- Detailed financial statement analysis
- Key performance indicators
- Growth projections
- Cash flow analysis

#### Risk Assessment
- Industry-specific risk factors
- Market condition analysis
- Regulatory compliance checks
- Mitigation strategies

#### Market Intelligence
- Industry trends and insights
- Market sentiment analysis
- Investor preference tracking
- Timing recommendations

## Why Choose IPOGate?

- **AI-Powered Analysis**: Advanced algorithms for accurate data extraction and analysis
- **Time Efficiency**: Automate manual processes and focus on strategic decisions
- **Professional Output**: Generate investor-ready documents and presentations
- **Expert Guidance**: Step-by-step assistance throughout your IPO journey

Ready to take your company public? Click "Begin Your IPO Journey" to start.
""")

# Footer with additional information
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <small>
        For more information about our services, please visit our 
        <a href='?page=About_Us'>About Us</a> page or contact our team.
    </small>
</div>
""", unsafe_allow_html=True)
