import requests
import pandas as pd


class Stocks:
    def __init__(self, api_key) -> None:
        self.URL = "https://www.alphavantage.co/query"
        self.API_KEY = api_key

    def time_series_daily(self, symbol):
        '''Returns a pandas dataframe containing daily data for the given stock for the last 100 days'''
        payload = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.API_KEY,
        }
        
        response = requests.get(url=self.URL, params=payload)
        response.raise_for_status()
        
        df = pd.DataFrame(response.json()["Time Series (Daily)"])
        
        return df

    def two_day_close(self, symbol):
        """Returns the closing value of a given stock for yesterday and the day before"""
        df = self.time_series_daily(symbol)

        yesterday = df.iloc[3, 0]
        day_before = df.iloc[3, 1]

        return yesterday, day_before

    def difference(self, symbol):
        """Returns the percentual difference between a stock price for the last 2 days"""
        
        day1, day2 = self.two_day_close(symbol)
             
        diff = float(day1) - float(day2)
        diff_p = diff / float(day2) * 100
        diff_p = round(diff_p, 2)
        return diff_p

