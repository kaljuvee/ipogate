import streamlit as st
import pandas as pd
import plotly.express as px
from utils.yf_util import (
    get_available_sectors,
    get_tickers_for_sector,
    get_company_details
)
import time
import logging

st.set_page_config(page_title="Comparative Analysis", page_icon="📊", layout="wide")

st.title("S&P 500 Sector Analysis 📊")

# Initialize session state
if 'companies_df' not in st.session_state:
    st.session_state.companies_df = None
if 'market_data_df' not in st.session_state:
    st.session_state.market_data_df = None
if 'debug_info' not in st.session_state:
    st.session_state.debug_info = []

# Main content layout
st.write("### Select Sector")

# Step 1: Sector selection
selected_sector = st.selectbox(
    "1. Select Sector",
    get_available_sectors(),
    index=0,
    help="Choose the sector to analyze"
)

# Step 2: Get companies button
if st.button("2. Get Companies List 📋", type="primary", use_container_width=True):
    with st.spinner("Fetching companies..."):
        # Clear previous debug info
        st.session_state.debug_info = []
        
        # Log the request parameters
        st.session_state.debug_info.append(f"Request Parameters:")
        st.session_state.debug_info.append(f"- Sector: {selected_sector}")
        
        try:
            companies_df = get_tickers_for_sector(selected_sector)
            
            # Log the response
            st.session_state.debug_info.append(f"\nResponse:")
            st.session_state.debug_info.append(f"- Number of companies found: {len(companies_df) if companies_df is not None else 0}")
            
            if companies_df is not None and not companies_df.empty:
                st.session_state.companies_df = companies_df
            else:
                st.session_state.companies_df = None
                st.error("No companies found for the selected sector.")
            
        except Exception as e:
            st.session_state.debug_info.append(f"\nError occurred:")
            st.session_state.debug_info.append(f"- {str(e)}")
            st.error(f"Error fetching companies: {str(e)}")
        
        st.session_state.market_data_df = None  # Reset market data

# Display debug information in an expander
with st.expander("Debug Information"):
    st.code("\n".join(st.session_state.debug_info))

# Display companies if available
if st.session_state.companies_df is not None:
    st.write(f"### Companies in {selected_sector} sector")
    st.dataframe(st.session_state.companies_df, use_container_width=True)
    
    # Step 3: Get Market Data button
    if st.button("3. Get Market Data"):
        market_data = []
        progress_bar = st.progress(0)
        total_companies = len(st.session_state.companies_df)
        
        for idx, row in st.session_state.companies_df.iterrows():
            # Ensure progress stays between 0 and 1
            progress = min(idx / (total_companies - 1), 1.0) if total_companies > 1 else 1.0
            progress_bar.progress(progress)
            
            with st.spinner(f"Fetching data for {row['Symbol']}..."):
                company_data = get_company_details(row['Symbol'])
                if company_data:
                    market_data.append(company_data)
                time.sleep(0.1)  # Rate limiting
        
        progress_bar.progress(1.0)  # Ensure we end at 100%
        st.session_state.market_data_df = pd.DataFrame(market_data)
        progress_bar.empty()

# Display market data if available
if st.session_state.market_data_df is not None and not st.session_state.market_data_df.empty:
    st.write("### Market Data Analysis")
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Number of Companies", len(st.session_state.market_data_df))
    with col2:
        st.metric("Total Market Cap", f"${st.session_state.market_data_df['Market Cap (B)'].sum():,.2f}B")
    with col3:
        st.metric("Avg P/E Ratio", f"{st.session_state.market_data_df['P/E Ratio'].mean():,.2f}")
    
    # Display detailed data table
    st.dataframe(
        st.session_state.market_data_df.style.format({
            'Market Cap (B)': '${:,.2f}B',
            'Price': '${:,.2f}',
            'P/E Ratio': '{:,.2f}',
            'Revenue (TTM)': '${:,.2f}B',
            'Net Income (TTM)': '${:,.2f}B',
            'Profit Margin': '{:.1%}'
        }),
        use_container_width=True
    )
    
    # Visualizations
    st.write("### Market Cap Comparison")
    fig = px.treemap(
        st.session_state.market_data_df,
        path=[px.Constant("Companies"), 'Name'],
        values='Market Cap (B)',
        title=f'Market Cap Distribution in {selected_sector} Sector'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Download data option
    csv = st.session_state.market_data_df.to_csv(index=False)
    st.download_button(
        label="Download Market Data as CSV",
        data=csv,
        file_name=f"SP500_{selected_sector}_market_data.csv",
        mime="text/csv"
    )
