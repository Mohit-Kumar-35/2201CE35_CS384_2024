#Part-1:
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

df = pd.read_csv('/content/infy_stock.csv', index_col='Date', parse_dates=True)
print(df.head(10))
df.isnull().sum()

#Part-2:
plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Closing Price', color='blue')
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

mpf.plot(df.head(500), type='candle', title='Candlestick Chart', style='yahoo',xlabel='Date', ylabel='Price', volume=False)

#Part-3:
df['Daily_Return'] = ((df['Close'] - df['Open']) / df['Open']) * 100

average_return = df['Daily_Return'].mean()
median_return = df['Daily_Return'].median()
standard_deviation = df['Close'].std()


print(df.head(10))
print('\n')
print(f"Average Daily Return: {average_return:.2f}%")
print(f"Median Daily Return: {median_return:.2f}%")
print('\n')
print(f"Standard Deviation of Closing Prices: {standard_deviation:.2f}")

# plt.figure(figsize=(12, 6))
# plt.plot(df['Daily_Return'].head(500), label='Daily Return', color='blue')
# plt.title('Daily Return Over Time')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.legend()
# plt.show()

df.to_csv('/content/output_stock.csv', index=False)

#Part-4:
df['50_Day_MA'] = df['Close'].rolling(window=50).mean()
df['200_Day_MA'] = df['Close'].rolling(window=200).mean()

print(df[['Close', '50_Day_MA', '200_Day_MA']].tail())
print('\n')

plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Closing Price', color='blue')
plt.plot(df['50_Day_MA'], label='50 Day MA', color='red')
plt.plot(df['200_Day_MA'], label='200 Day MA', color='green')
plt.title('Closing Price with 50-day & 200-day Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

df.to_csv('/content/output_stock.csv', index=False)

#Part-5:
df['Daily_Return'] = ((df['Close'] - df['Open']) / df['Open']) * 100
df['30_Day_Volatility'] = df['Close'].rolling(window=30).std()

print(df[['Close', 'Daily_Return', '30_Day_Volatility']].tail())
print('\n')

plt.figure(figsize=(12, 6))
plt.plot(df['30_Day_Volatility'], label='Closing Price', color='blue')
plt.title('Closing Price Over Time with 30 day volatility')
plt.xlabel('Date')
plt.ylabel('30_Day_Volatility')
plt.legend()
plt.show()

df.to_csv('/content/output_stock.csv', index=False)

#Part-6:
df['Bullish_Trend'] = df['50_Day_MA'] > df['200_Day_MA']
df['Bearish_Trend'] = df['50_Day_MA'] < df['200_Day_MA']

print(df[['Close', '50_Day_MA', '200_Day_MA', 'Bullish_Trend', "Bearish_Trend"]].tail())

df.to_csv('/content/output_stock.csv', index=False)