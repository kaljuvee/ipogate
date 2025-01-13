import pandas as pd
import yfinance as yf
from typing import List, Dict
import time

def get_sp500_tickers() -> List[str]:
    """Get list of S&P 500 tickers using yfinance."""
    # You can get this from ^GSPC (S&P 500 index)
    sp500 = yf.Ticker("^GSPC")
    return sp500.components

def get_available_sectors() -> List[str]:
    """Get list of unique sectors from S&P 500 companies."""
    tickers = get_sp500_tickers()
    sectors = set()
    
    # Process in batches to avoid rate limiting
    batch_size = 100
    for i in range(0, len(tickers), batch_size):
        batch = tickers[i:i + batch_size]
        
        # Download info for batch of tickers
        for ticker in batch:
            try:
                stock = yf.Ticker(ticker)
                sector = stock.info.get('sector')
                if sector:
                    sectors.add(sector)
            except Exception as e:
                print(f"Error fetching sector for {ticker}: {str(e)}")
            time.sleep(0.1)  # Rate limiting
    
    return sorted(list(sectors))

def get_tickers_for_sector(sector: str) -> pd.DataFrame:
    """Get companies for a specific sector from S&P 500."""
    tickers = get_sp500_tickers()
    companies = []
    
    # Process in batches to avoid rate limiting
    batch_size = 100
    for i in range(0, len(tickers), batch_size):
        batch = tickers[i:i + batch_size]
        
        # Download info for batch of tickers
        for ticker in batch:
            try:
                stock = yf.Ticker(ticker)
                info = stock.info
                if info.get('sector') == sector:
                    companies.append({
                        'Symbol': ticker,
                        'Name': info.get('longName', 'N/A')
                    })
            except Exception as e:
                print(f"Error fetching data for {ticker}: {str(e)}")
            time.sleep(0.1)  # Rate limiting
    
    return pd.DataFrame(companies)

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
 