import pandas as pd
import yfinance as yf
import time

def get_available_sectors():
    """Get list of sectors from S&P 500."""
    sp500_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    df = pd.read_html(sp500_url)[0]
    sectors = sorted(df['GICS Sector'].unique().tolist())
    return sectors

def get_tickers_for_sector(sector):
    """Get companies for a specific sector from S&P 500."""
    sp500_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    df = pd.read_html(sp500_url)[0]
    
    # Filter companies by sector
    sector_companies = df[df['GICS Sector'] == sector]
    
    # Create DataFrame with Symbol and Name
    companies_df = sector_companies[['Symbol', 'Security']].copy()
    companies_df.columns = ['Symbol', 'Name']
    
    return companies_df

def get_company_details(ticker):
    """Get market data for a specific ticker."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        return {
            'Symbol': ticker,
            'Name': info.get('longName', 'N/A'),
            'Market Cap (B)': info.get('marketCap', 0) / 1e9,
            'Price': info.get('currentPrice', 0),
            'P/E Ratio': info.get('forwardPE', 0),
            'Revenue (TTM)': info.get('totalRevenue', 0) / 1e9,
            'Net Income (TTM)': info.get('netIncomeToCommon', 0) / 1e9,
            'Profit Margin': info.get('profitMargins', 0)
        }
    except Exception as e:
        print(f"Error fetching data for {ticker}: {str(e)}")
        return None
 