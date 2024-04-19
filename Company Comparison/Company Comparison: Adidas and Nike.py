# Why adidas and Nike ?
#Both companies operate in the athletic apparel and footwear industry, and their stock prices can be influenced by
#similar market factors, such as changes in consumer preferences,
#economic conditions, and global supply chain issues. However, the weak negative correlation might suggest that there are other, perhaps company-specific factors influencing their stock prices independently.


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
adidas_df = pd.read_csv('ADS.DE.csv')
nike_df = pd.read_csv('NKE.csv')

# Convert 'Date' columns to datetime type
adidas_df['Date'] = pd.to_datetime(adidas_df['Date'])
nike_df['Date'] = pd.to_datetime(nike_df['Date'])

# Set 'Date' as the index for both dataframes
adidas_df.set_index('Date', inplace=True)
nike_df.set_index('Date', inplace=True)

# Plot the adjusted close prices of both stocks
plt.figure(figsize=(14, 7))
plt.plot(adidas_df['Adj Close'], label='Adidas')
plt.plot(nike_df['Adj Close'], label='Nike')
plt.title('Adjusted Close Prices of Adidas and Nike')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()
plt.grid(True)
plt.show()

# Calculate the correlation between the adjusted close prices of Adidas and Nike
correlation = adidas_df['Adj Close'].corr(nike_df['Adj Close'])
print('Correlation coefficient:', correlation)


#Interpretation:
# 1. Visual Trend Comparison: The graph of the adjusted close prices of Adidas and Nike over the given time period showed their price movements.
# Visually, there was no strong synchronicity in their trends, suggesting that the stock prices did not move in tandem consistently.
# 2. Correlation Coefficient: The calculated correlation coefficient was approximately -0.21. This indicates a weak negative correlation between the stock prices of Adidas and Nike during the period covered by your data.
# A negative correlation coefficient suggests that when one stock’s price went up, the other’s slightly tended to go down, and vice versa. However, the correlation was weak, meaning the relationship was not strongly negative.
# The weak negative correlation might suggest that market factors affecting one company did not have a similar effect on the other, despite both being major players in the athletic apparel and footwear industry. This could be due to differences in market strategies, geographic focus, product lines, or other business factors.
# External factors, such as regional economic conditions, global events, or industry-specific trends, could have influenced their stock prices differently.
