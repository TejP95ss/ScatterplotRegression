import matplotlib.pyplot as plt
import pandas as pd
import math
import statistics
import numpy as np
import scipy
import yfinance as yf
# The following 8 lines gather the 33 years worth of close data in SPX and VIX
'''start_date = '1990-01-01'
end_date = '2023-01-01'
ticker = '^SPX'
Spx = yf.download(ticker, start_date, end_date)['Close']
Spx.to_csv(f"{ticker}.csv")
ticker2 = '^VIX'
Vix = yf.download(ticker2, start_date, end_date)['Close']
Vix.to_csv(f"{ticker2}.csv")'''
# next 2 lines assigns variables to the 2 different CSV files containing the data
SPX = pd.read_csv(r"C:\Users\ashis\PycharmProjects\ScatterplotRegression\^SPX.csv")
Vix = pd.read_csv(r"C:\Users\ashis\PycharmProjects\ScatterplotRegression\^VIX.csv")
# Following 7 lines calculate the daily percent changes and add them to a list
PercentChanges = []
for x in range(8314):
    j = SPX.iloc[x, 1]
    i = SPX.iloc[x+1, 1]
    PercentChange = ((i/j) - 1) * 100
    PercentChanges.append(round(PercentChange, 3))
PercentChanges.insert(0, 1.78)
# Next 11 lines calculate the 20-day historical volatility in SPX over the past 33 years.
HistoricalVol = []
for y in range(8295):
    Changes = []
    for z in range(20):
        g = SPX.iloc[z+y, 1]
        k = SPX.iloc[z+y+1, 1]
        LogChange = math.log(k/g) * 100
        Changes.append(LogChange)
    StandardDeviation = statistics.stdev(Changes)
    HVOL = math.sqrt(252) * StandardDeviation
    HistoricalVol.append(round(HVOL, 3))
VIXList = []
NewHVOL = []
# Following for loop appends values into new Historical Vol. and Vix lists based if a certain criteria is met
Counter = 0
for i in range(8295):
    j = Vix.iloc[i, 1]
    k = HistoricalVol[i]
    if (j-500) < k < (j+500):
        VIXList.append(round(j, 3))
        NewHVOL.append(HistoricalVol[i])
        Counter += 1
    if i == 8294:
        print(Counter/8295)
ArrayVIX = np.array(VIXList)
LinearRegression = scipy.stats.linregress(VIXList, NewHVOL)
print(LinearRegression.rvalue**2)
# The following lines are there to plot the line of best fit and the scatter plot.
# Labels and title are also provided to the graph by the following lines
plt.plot(ArrayVIX, (LinearRegression.slope*ArrayVIX) + LinearRegression.intercept, color="red")
plt.scatter(VIXList, NewHVOL, c=np.random.rand(1, len(NewHVOL)))
plt.title("20 Day Realized Volatility SPX vs. VIX from 1/2/1990 to 12/1/2022")
plt.xlabel("VIX")
plt.ylabel("20 Day Realized Volatility SPX")
plt.show()
