# Import and clean data

# modules
import sys, os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
import statsmodels.api as sm
import scipy as sp
import sklearn as sk
import patsy
from statsmodels.formula.api import ols

pd.set_option("display.max_rows", 10)
pd.set_option("display.max_columns", 200)

# global variables
pathData = 'C:/Users/Weller/Dropbox/SportAnalytics/3rdAnd4thDown/Data'
dataFile = '2003_2014pbp.csv'

# import data and read csv
data = pathData + '/' + dataFile
dm = pd.read_csv(data, low_memory=False)  # read csv

# Make the first column so that it's not unnamed
dm = dm.rename(columns={'Unnamed: 0': 'unique'})

# trim data set
dm = dm[dm.Quarter != 5]

#Create columns for each play and game to have a unique number/id
dm['MinFromStart'] = 60 - dm['MinutesRemaining']
dm['unique'] = dm["season"].map(str) + dm["GameKey"].map(str) + dm["MinFromStart"].map(str)
dm['gameid'] = dm["season"].map(str) + dm["GameKey"].map(str) + dm["VisitTeam"].map(str) + dm["HomeTeam"].map(str)

dme = dm[
    ['unique', 'season', 'gameid', 'HomeTeam', 'VisitTeam', 'HomeHeadCoach', 'VisitorHeadCoach', 'PossessionTeam',
     'NonPossessionTeam', 'OffSpread', 'OverUnder', 'OffHeadCoach', 'DefHeadCoach', 'Quarter', 'Down', 'YardsToGo','YardsGained',
     'AbsoluteYardline', 'ClockTime', 'MinutesRemaining', 'MinFromStart', 'Score_Home', 'Score_Visitor', 'Score_Offense',
     'Score_Defense', 'OffScoreMargin', 'DefScoreMargin', 'TimeoutsRemaining_Home', 'TimeoutsRemaining_Visitor', 'TimeoutsRemaining_Offense',
     'TimeoutsRemaining_Defense', 'OffWinInd', 'OffLossInd', 'OffTieInd', 'PlayCall','Down4Success']]

# export data as csv
dme.to_csv("C:/Users/Weller/Dropbox/SportAnalytics/3rdAnd4thDown/Data/trimmedThesisData2003_2014.csv")  
