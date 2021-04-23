"""

"""
import pandas as pd
from datetime import datetime, timedelta
import traceback
import sqlite3

BINANCE_DB = 'app/jarvis_binance.db'
BINANCE_CREDENTIALS_TABLE = 'BINANCE_CREDENTIALS'
BINANCE_ORDERS_TABLE = 'BINANCE_ORDERS'
BINANCE_POSITIONS_TABLE = 'BINANCE_POSITIONS'
BINANCE_TRADES_TABLE = 'BINANCE_TRADES'
BINANCE_STATUS_TABLE = 'BINANCE_STATUS'
BINANCE_BAN_TABLE = 'BINANCE_BAN'
BINANCE_BALANCE_TABLE = 'BINANCE_BALANCE'
LOGIN_TABLE = 'LOGIN_TABLE'


def get_table_df(table_name):
    db = sqlite3.connect(BINANCE_DB)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", db)
    return df


def authenticate(user_name, password):
    try:
        login_df = get_table_df(table_name=LOGIN_TABLE)
        if len(login_df) > 0:
            user_df = login_df[(login_df['user_name'] == user_name) & (login_df['password'] == password)]
            if len(user_df) > 0:
                return True
        return False
    except:
        traceback.print_exc()
        return False


def get_net_worth(user_name):
    balance = 0
    try:
        balance_df = get_table_df(table_name=BINANCE_BALANCE_TABLE)
        if len(balance_df) > 0:
            ub_df = balance_df[balance_df['user'] == user_name]
            if len(ub_df) > 0:
                balance = float(ub_df['balance'].sum())
        return balance
    except:
        traceback.print_exc()
        return balance


def get_pnl(user_name):
    pnl_dict = {'all_pnl': 0, 'week_pnl': 0, 'month_pnl': 0}
    try:
        pnl_df = get_table_df(table_name=BINANCE_TRADES_TABLE)
        if len(pnl_df) > 0:
            up = pnl_df[pnl_df['user'] == user_name]
            if len(up) > 0:
                up['net_pnl_usd'] = up['net_pnl_usd'].astype(float)
                pnl_dict['all_pnl'] = up['net_pnl_usd'].sum()
                up['exit_time'] = pd.to_datetime(up['exit_time'])
                week_start = datetime.utcnow() - timedelta(days=7)
                pnl_dict['week_pnl'] = up[up['exit_time'] > week_start]['net_pnl_usd'].sum()
                month_start = datetime.utcnow() - timedelta(days=30)
                pnl_dict['month_pnl'] = up[up['exit_time'] > month_start]['net_pnl_usd'].sum()
        return pnl_dict
    except:
        traceback.print_exc()
        return pnl_dict


def get_open_positions(user):
    try:
        cols = ['exchange', 'symbol', 'entry_time_utc', 'price', 'side', 'open_pos',
                'dollar_qty']

        pos_df = get_table_df(table_name=BINANCE_POSITIONS_TABLE)
        if len(pos_df) > 0:
            udf = pos_df[pos_df['user'] == user]
            return udf[cols]
        return pd.DataFrame()
    except:
        traceback.print_exc()
        return pd.DataFrame()


def get_trades_history(user):
    try:
        cols = ['exchange', 'symbol', 'entry_time', 'entry_price', 'qty',
                'exit_time', 'exit_price', 'net_pnl_usd', 'net_pnl_percent', 'result']
        pos_df = get_table_df(table_name=BINANCE_TRADES_TABLE)
        if len(pos_df) > 0:
            udf = pos_df[pos_df['user'] == user]
            return udf[cols]
        return pd.DataFrame()
    except:
        traceback.print_exc()
        return pd.DataFrame()

def update_status(user, strategy, status):
    try:
        status_df = get_table_df(BINANCE_STATUS_TABLE)
        if len(status_df) > 0:
            udf = status_df[(status_df['user'] == user) & (status_df['strategy'] == strategy)]
            if len(udf) > 0:
                id = udf.iloc[0]['id']
                update_table(table_name=BINANCE_STATUS_TABLE, col='id', value=id, in_dict=dict(status=status))
                return True
        return False
    except:
        traceback.print_exc()
        return False


def get_strategy_list_status(user):
    try:
        status_df = get_table_df(BINANCE_STATUS_TABLE)
        if len(status_df) > 0:
            udf = status_df[(status_df['user'] == user)]
            return udf[['strategy', 'status']]
        return pd.DataFrame()
    except:
        traceback.print_exc()
        return pd.DataFrame()


def start_strategy(user, strategy):
    return update_status(user, strategy, status=STARTING)


def stop_strategy(user, strategy):
    return update_status(user, strategy, status=STOPPING)


def close_all_positions(user, exchange):
    ""


def get_table_df(table_name):
    db = sqlite3.connect(BINANCE_DB)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", db)
    return df


def update_table(table_name, col, value, in_dict):
    db = sqlite3.connect(BINANCE_DB)
    cursor = db.cursor()
    for this_col in in_dict:
        if this_col != col:
            cursor.execute(f'UPDATE {table_name} SET {this_col} = ? WHERE {col} = ?', (in_dict[this_col], value))
            db.commit()
            print(f"Successfully updated : {table_name}")
