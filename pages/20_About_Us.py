import streamlit as st
from pathlib import Path

st.set_page_config(page_title="About Us", page_icon="ℹ️", layout="wide")

# Read PDF file
try:
    with open("docs/IPOGate-Product-Deck.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
except FileNotFoundError:
    pdf_bytes = None

st.markdown("""
# IPOGate - Your Gateway to Public Markets

## Our Vision
IPOGate was created with a vision to fill the funding gap and provide European small and medium sized enterprises 
with a better access to public equity and fixed-income capital markets. While we focus primarily on the Northern 
and Eastern European region, we can also find innovative financing solutions for companies across the European 
Economic Area (EEA).

## Our Product
Our platform empowers the origination, structuring, and execution of public equity, convertible and fixed-income 
products with a focus on the Baltic and Nordic markets. This includes, but is not limited to, initial public 
offerings, and follow on offerings.
""")

if pdf_bytes is not None:
    st.download_button(
        label="📥 Download IPOGate Product Deck",
        data=pdf_bytes,
        file_name="IPOGate-Product-Deck.pdf",
        mime="application/pdf"
    )
else:
    st.error("Product deck PDF file not found.")

st.markdown("""
## IPO Benefits to Companies
There are numerous benefits for companies to be public globally such as:
* Greater brand recognition
* Investor trust 
* Lower cost of loans and debt capital

## Get in Touch
If you would like to discuss your financing needs and how to access public equity markets in particular, 
please get in touch with our business development team at info@ipogate.co to get the process started.

---

### Disclaimer
*IPOGate is partnering with various service providers including the Certified Advisors on the Nasdaq Baltic Market. 
While we can currently offer advice regarding private funding, offering any services to issuers regarding public 
listings will be subject to the approval of this status by Nasdaq Baltic Market.*

You can learn more about Certified Advisors and raising funding on Nasdaq Baltic Market 
[here](https://nasdaqbaltic.com/services/companies/certified-adviser/).
""")
