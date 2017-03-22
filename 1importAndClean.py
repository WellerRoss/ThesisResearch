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
#dm = dm[dm.season >= 2013]
#d4 = dm[dm['Down']==4]
#dfg = d4[d4['PlayCall']=='FG']
#dpt = d4[d4['PlayCall']=='PUNT']
#dfg = dfg[['PlayDescription','AbsoluteYardline']]
#dpt = dpt[['PlayDescription','AbsoluteYardline']]
#dfg.to_csv("C:/Users/Weller/Dropbox/SportAnalytics/3rdAnd4thDown/Data/dfg.csv")  # export data as csv
#dpt.to_csv("C:/Users/Weller/Dropbox/SportAnalytics/3rdAnd4thDown/Data/dpt.csv")  # export data as csv
#dpt['AbsoluteYardline'].describe()
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
dme.to_csv("C:/Users/Weller/Dropbox/SportAnalytics/3rdAnd4thDown/Data/trimmedThesisData2003_2014.csv")  # export data as csv

# Eliminate overtime
#dm = dm[dm.Quarter != 5]

# Make everything in the description column lowercase
# dm['PlayDescription'] = dm['PlayDescription'].str.lower()

# sort the data so it's in chronological order
#dm['MinFromStart'] = 60 - dm['MinutesRemaining']
#dm = dm.sort(['season', 'GameKey', 'MinFromStart'], ascending=[True, True, True])
#dm = dm[dm.season >= 2013]
#dm.to_csv("C:/Users/Weller/Dropbox/SportAnalytics/3rdAnd4thDown/Data/thesisData2013_2014.csv")  # export data as csv
