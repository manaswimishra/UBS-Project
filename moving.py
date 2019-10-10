import numpy as np
import pandas as pd
import datetime
import matplotlib
import matplotlib.pyplot as plt
import os

# create a list for the sector dataframes
sectors = []

# read and format sector dataframes
for file in os.listdir('Sectors/'):
    tmp = pd.read_csv('Sectors/{}'.format(file))
    tmp = tmp.drop(['Unnamed: 0'], axis=1)
    tmp = tmp.drop(['date'], axis=1)
    new_index = pd.date_range('2016-11-01', periods=len(tmp), freq="D")
    tmp.index = new_index
    sectors.append(tmp)


sectors.plot()
# create lists of moving average dataframes
# moving7 = []
# moving14 = []
# moving30 = []
# moving60 = []
#
# movingsd7 = []
# movingsd14 = []
# movingsd30 = []
# movingsd60 = []
#
# movingdd7 = []
# movingdd14 = []
# movingdd30 = []
# movingdd60 = []
#
# movingdif7 = []
# movingdif14 = []
# movingdif30 = []
# movingdif60 = []
#
# dist = [7, 14, 30, 60] # define sizes of moving averages
# i = 0 # iterator across sizes
#
# # build moving average dataframes
# for x in [moving7, moving14, moving30, moving60]:
#     for y in sectors:
#         df = y.rolling(window=dist[i]).mean() # create moving average
#         # make dates consistent
#         new_index = pd.date_range('2016-11-01', periods=len(df), freq="D")
#         df.index = new_index
#         x.append(df)
#     i += 1 # move to next window
#
# i = 0 # reset counter
#
# for x in [movingsd7, movingsd14, movingsd30, movingsd60]:
#     for y in sectors:
#         df = y.rolling(window=dist[i]).std() # create moving standard deviation
#         # make dates consistent
#         new_index = pd.date_range('2016-11-01', periods=len(df), freq="D")
#         df.index = new_index
#         x.append(df)
#     i += 1 # move to next window
#
# i = 0
#
# for x in [movingdd7, movingdd14, movingdd30, movingdd60]:
#     for y in sectors:
#         df = y.rolling(window=dist[i]).max() - y.rolling(window=dist[i]).min() # create moving drawdown
#         # make dates consistent
#         new_index = pd.date_range('2016-11-01', periods=len(df), freq="D")
#         df.index = new_index
#         x.append(df)
#     i += 1 # move to next window
#
# i = 0
#
# for x in [movingdif7, movingdif14, movingdif30, movingdif60]:
#     for y in sectors:
#         df = y.diff(periods=dist[i]) # create differences
#         # make dates consistent
#         new_index = pd.date_range('2016-11-01', periods=len(df), freq="D")
#         df.index = new_index
#         x.append(df)
#     i += 1 # move to next window
#
# ric = 'AAP' # stock ticker to display
#
# # plot
# plt.plot(sectors[0][ric])
# plt.plot(moving7[0][ric])
# plt.plot(moving14[0][ric])
# plt.plot(moving30[0][ric])
# plt.plot(moving60[0][ric])
# plt.legend([ric,'{} days'.format(dist[0]),'{} days'.format(dist[1]),'{} days'.format(dist[2]),'{} days'.format(dist[3])])
# plt.show()
#
# plt.plot(sectors[0][ric])
# plt.plot(movingsd7[0][ric])
# plt.plot(movingsd14[0][ric])
# plt.plot(movingsd30[0][ric])
# plt.plot(movingsd60[0][ric])
# plt.legend([ric,'{} days'.format(dist[0]),'{} days'.format(dist[1]),'{} days'.format(dist[2]),'{} days'.format(dist[3])])
# plt.show()
#
# plt.plot(sectors[0][ric])
# plt.plot(movingdd7[0][ric])
# plt.plot(movingdd14[0][ric])
# plt.plot(movingdd30[0][ric])
# plt.plot(movingdd60[0][ric])
# plt.legend([ric,'{} days'.format(dist[0]),'{} days'.format(dist[1]),'{} days'.format(dist[2]),'{} days'.format(dist[3])])
# plt.show()
#
# plt.plot(sectors[0][ric])
# plt.plot(movingdif7[0][ric])
# plt.plot(movingdif14[0][ric])
# plt.plot(movingdif30[0][ric])
# plt.plot(movingdif60[0][ric])
# plt.legend([ric,'{} days'.format(dist[0]),'{} days'.format(dist[1]),'{} days'.format(dist[2]),'{} days'.format(dist[3])])
# plt.show()