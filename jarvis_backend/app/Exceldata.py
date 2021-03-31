import xlrd
import pandas as pd

class ReadExcel:
    def __init__(self, filepath):
        self.filpath = filepath
    
    def get_trade_data(self):
        try:
            print(self.filpath)
            data = pd.read_excel(self.filpath, nrows= 10)
            df = pd.DataFrame(data, columns=['mode','strategyId','setting','symbol','entry_time','entry_price'])
            # Extracting number of rows
            df['entry_time'] = df['entry_time'].astype(str)
            final_data = df.T.to_dict().values()
            return final_data

        except Exception as e:
            print('error', e)
    
    def get_bar_data(self):
        data = pd.read_excel(self.filpath, nrows= 200)
        df = pd.DataFrame(data, columns=['entry_time','entry_qty'])
        df['entry_time'] = df["entry_time"].dt.strftime("%Y-%m-%d")
        final_data = df.T.to_dict().values()
        return final_data

    def get_line_data(self):
        data = pd.read_excel(self.filpath, nrows= 50)
        df = pd.DataFrame(data, columns=['entry_time','entry_qty'])
        df['entry_time'] = df["entry_time"].dt.strftime("%Y-%m-%d")
        final_data = df.T.to_dict().values()
        return final_data