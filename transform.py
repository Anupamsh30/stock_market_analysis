##IMPORTING libraries
import pandas as pd
import glob
import os
import configparser
import pickle


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__),'constants.ini'))
path = str(config['input_path']['indian_stock_data'])
pickle_created = int(config['pickle']['pickle_created'])
pickle_path = str(config['pickle']['pickle_path'])
stock_code = str(config['stock']['stock_code'])
date_start = str(config['stock']['date_start'])
date_end = str(config['stock']['date_end'])

def read_file(path):
    #read the data
    return pd.read_csv(path)

def run_agg(data, date_start, date_end):
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data['date'] = data['timestamp'].dt.date
    data_agg = data.groupby('date', as_index=False).agg({'open':'first','close':'last','high':'max','low':'min','volume':'sum'})
    data_agg = data_agg.loc[(data_agg['date'] >= pd.Timestamp(date_start)) & (data_agg['date'] <= pd.Timestamp(date_end))]
    return data_agg

def save_file(data,path):
    data.to_csv(path)
    
if __name__ == "__main__":
    
    stock_data = read_file(os.path.join(path,str(stock_code)+'.csv'))
    stock_data_agg = run_agg(stock_data, date_start, date_end)
    
    save_file(stock_data_agg,os.path.join('/Users/anupam.sharma/Documents/stock_market_analysis/data',str(stock_code)+'-agg.csv'))

 
