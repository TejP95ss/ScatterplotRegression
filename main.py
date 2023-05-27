import matplotlib.pyplot as plt
import pandas as pd
import math
import statistics
import numpy as np
import yfinance as yf
from datetime import datetime
'''
start_date = '1990-01-01'
end_date = '2023-01-01'
ticker = '^SPX'
Spy = yf.download(ticker, start_date, end_date)['Close']
Spy.to_csv(f"{ticker}.csv")
ticker2 = '^VIX'
Vix = yf.download(ticker2, start_date, end_date)['Close']
Vix.to_csv(f"{ticker2}.csv")
VIXDates = []
SPXDates = []
for x in range(8314):
    VIXdate = Vix.iloc[x, 0]
    SPXdate = SPX.iloc[x, 0]
    ParsedVIXDate = datetime.strptime(VIXdate, '%Y-%m-%d')
    ParsedSPXDate = datetime.strptime(SPXdate, '%Y-%m-%d')
    VIXDates.append(ParsedVIXDate)
    SPXDates.append(ParsedSPXDate)
'''

SPX = pd.read_csv(r"C:\Users\ashis\PycharmProjects\TestProject\^SPX.csv")
Vix = pd.read_csv(r"C:\Users\ashis\PycharmProjects\TestProject\^VIX.csv")
PercentChanges = []
for x in range(8314):
    j = SPX.iloc[x, 1]
    i = SPX.iloc[x+1, 1]
    PercentChange = ((i/j) - 1) * 100
    PercentChanges.append(round(PercentChange, 3))
PercentChanges.insert(0, 1.78)
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
for i in range(8295):
    j = Vix.iloc[i, 1]
    k = HistoricalVol[i]
    if j > 0:
        VIXList.append(round(j, 3))
        NewHVOL.append(HistoricalVol[i])
matrix = np.corrcoef(VIXList, NewHVOL)
corr = matrix[0,  1]
print(corr*corr)
print(NewHVOL)
print(VIXList)
counter = 0
for j in range(len(VIXList)):
    if NewHVOL[j] > VIXList[j] + 10:
        counter += 1
print(round(counter/len(VIXList), 3))
a, b = np.polyfit(VIXList, NewHVOL, 1)
ArrayVix = np.array(VIXList)
plt.plot(ArrayVix, (a*ArrayVix) + b, color="red")
plt.scatter(VIXList, NewHVOL, c=np.random.rand(1, len(NewHVOL)))
plt.title("20 Day Realized Volatility SPX vs. VIX from 1/1/2000 to 12/1/2022")
plt.xlabel("VIX")
plt.ylabel("20 Day Realized Volatility SPX")
plt.show()
