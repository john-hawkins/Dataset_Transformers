import numpy as np
import pandas as pd

import sys
sys.path.append('../')

from transform import DatasetPreparer as dp

df = pd.read_csv('../data/Daily_Demand_Forecasting_Orders.csv', sep=';')

# ###########################################################################################################
# RENAME FOR CONVENIENCE
df.columns = ['Week', 'Day', 'NonUrgent', 'Urgent', 'TypeA', 'TypeB', 'TypeC',
       'Fiscal', 'Traffic', 'Banking1', 'Banking2', 'Banking3', 'Total']

df['No'] = range( 0, len(df) )
df['Month'] = np.where(df['No']>38, 3, 2)
df['Month'] = np.where(df['No']<19, 1, df['Month'])

df['dayofmonth'] = 7*(df['Week']-1)+(df['Day']-2)

df['dayofmonth'] = np.where( df['No']>38,df['dayofmonth']-2, df['dayofmonth'] )
 
df['daystring'] = pd.to_string(df['dayofmonth'])

df['daystring'] = np.where( df['dayofmonth']<10, "0"+str(df['dayofmonth']), str(df['dayofmonth'] ) )

df['datetime_string'] = "1999-" + str(df['Month']) + "-" + df['daystring']

df['datetime'] = pd.to_datetime(df1['Actual Settlement Date'], format='%Y-%m-%d')

new_df = dp.apply_order_fill_index( df, datetime_column, index_col_name, expected_interval )


# ###########################################################################################################
# CREATE AN INDEX COLUMN TO MANIPULATE
# IN MANY SCENARIOS YOU MIGHT WANT TO MAKE THIS AWARE OF THE GAPS IN THE
# DATA - FOR EXAMPLE IN THIS DATA THERE ARE MISSING WEEKENDS AND PUBLIC HOLIDAYS
df['No'] = range(0, len(df) )

index_column = "No"
forecast_column = "Total"
forecast_period = 1
list_of_lags = [1,2,3,4]

new_df = dg.generate_time_dependent_features( df, index_column, forecast_column, forecast_period, 
                                              list_of_lags)

# NEED TO KNOW THIS FOR THE MOMENT -- BETTER SOLUTION NEEDED
target_column_name="TARGET_Total_1_DIFF"

# ###########################################################################################################
# SPLIT IT INTO TRAIN AND TEST
# ###########################################################################################################
trainset = 30
train_df = new_df.loc[0:trainset,:]
test_df = new_df.loc[trainset+1:,:]

# ###########################################################################################################
# WRITE OUT THE FULL UN-NORMALISED VERSION
# ###########################################################################################################
train_df.to_csv('results/Train_set_full.csv', sep=',', encoding='utf-8', index=False, header=True)
test_df.to_csv('results/Test_set_full.csv', sep=',', encoding='utf-8', index=False, header=True)

# ###########################################################################################################
#  REMOVE UNWANTED COLUMNS, NORMALISE AND WRITE TO DISK
# ###########################################################################################################
features = train_df.columns.tolist()
unwanted = ["No"] 
for x in unwanted : features.remove(x)

train_df2 = train_df.loc[:,features]
test_df2 = test_df.loc[:,features]

config = nzr.create_normalization_config(train_df2)

nzr.write_normalization_config(config, 'results/Normalisation.yaml')
nzr.write_field_config(config,target_column_name, 'results/Target_nzr_config.yaml')

train_df_norm = nzr.normalize(train_df2, config, ['Week', 'Day'])
test_df_norm = nzr.normalize(test_df2, config, ['Week', 'Day'])

train_df_norm.to_csv('results/Train_set_normalised.csv', sep=',', encoding='utf-8', index=False, header=True)
test_df_norm.to_csv('results/Test_set_normalised.csv', sep=',', encoding='utf-8', index=False, header=True)


