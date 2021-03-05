import os
import logging
from stock_cons import *
import datetime

option_chain_ratio = {"NSE:NIFTY BANK":100}

def log(file_name):
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    now = datetime.date.today()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = str(dir_path)+"/logs/"+str(file_name)+"/"+str(now)
    #create directory
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    print("log file location:")
    log_dir = dir_path+"/"+str(file_name)+".log"
    logging.basicConfig(filename=log_dir, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
    print(log_dir)

def add_pre(name,li):
    final_li = []
    for i in li:
        tmp = str(name)+str(i)
        final_li.append(tmp)
    return final_li

def find_high_sl(dict1):
    high = dict1["ohlc"]["high"]
    prv_close = dict1["ohlc"]["close"]
    #find sl
    low_p = dict1["ohlc"]["low"]
    open_p = dict1["ohlc"]["open"]
    close_p = dict1["last_price"]
    li = [low_p,open_p,close_p]
    stop_loss = max(li)
    if high >= stop_loss:
        return high,stop_loss

def find_open_value(dict1):
    return dict1["ohlc"]["open"]


def get_ltp_value(dict1):
    return dict1["last_price"]

def find_no_wick(dick1):
    if dick1['ohlc']['open'] == dick1['ohlc']['low'] or dick1['ohlc']['open'] == dick1['ohlc']['high']:
        return True
    return False
#logic for get option chain
def get_option_chain(symbol,strick,side):
    ratio = option_chain_ratio[symbol[0]]
    left = strick % ratio
    if side == "CE":
        at_the_money = int(strick + (ratio - left))
    elif side == "PE":
        at_the_money = int(strick - left)
    #if at_the_money.is_integer():
    #    at_the_money = int(at_the_money)
    return at_the_money
