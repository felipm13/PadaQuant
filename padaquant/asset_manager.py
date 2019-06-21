import datetime
import pandas_datareader as pd_dr

class asset_manager:
    def __init__(self, symbol, start=None, end=None):
        self.symbol = symbol
        self.data =  pd_dr.get_data_yahoo(symbol, start, end)

    def get_symbol(self):
        return self.symbol


    def get_return(self):
         return self.data['Adj Close'].diff()
