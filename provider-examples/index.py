import lumipy.provider as lp
import pandas as pd


df = pd.read_csv('data/big_prices.csv')
df['Date'] = pd.to_datetime(df['Date']).dt.tz_localize(tz='utc')

rets = lp.PandasProvider(df, 'stock.returns')
qprog = lp.QuadraticProgram()

lp.ProviderManager(rets, qprog, port=5007).run()

