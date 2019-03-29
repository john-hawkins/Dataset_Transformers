import numpy as np
import pandas as pd

# ####################################################################################
# TAKE A DATASET OF INDIVIDUAL TIME RECODS AND RESHAPE AS A SET OF PREDICTORS
# AND A SINGLE TARGET COLUMN
# ASSUMPTIONS
#  --- REGULAR TIME PERIOD DATA
#  --- THERE WILL BE ROWS FOR MISSING VALUES
#  --- DATAFRAME IS ORDERED IN TIME
#  --- THERE IS AN INTEGER INDEX COLUMN THAT INDICATES THE SEQUENCE IN TIME
# ###################################################################################
def generate_time_series_dataset( df, index_column, forecast_column, forecast_period, list_of_lags):
    df_f = df[0:len(df)-forecast_period]
    df_t = df[forecast_period:].copy()
    df_t[index_column] = df_t[index_column]-forecast_period

    # FIRST WE JOIN THE DATA AGAINST ITSELF ONCE OVER THE FORECAST PERIOD TO CREATE A DIFF VALUE
    # -- FORECASTING FIRST ORDER DIFFERENCE IS A BETTER TARGET FOR MANY TIME SERIES PROBLEMS
    TARGET_COL_NAME = "TARGET" + "_" + forecast_column + "_" + str(forecast_period) + "_VALUE"
    df_t = df_t.rename(columns={forecast_column: TARGET_COL_NAME})
    df_targs = df_t.loc[:,[index_column, TARGET_COL_NAME]]

    TARGET_DIFF_COL_NAME = "TARGET" + "_" + forecast_column + "_" + str(forecast_period) + "_DIFF"
    final_df = pd.merge(df_f, df_targs, left_on=index_column, right_on=index_column)
    final_df[ TARGET_DIFF_COL_NAME ] = final_df[ TARGET_COL_NAME ] - final_df[forecast_column]

    # JOIN AGAIN TO GET THE PREVIOUS DIFF AS A FEATURE
    df_pd =  final_df[0:len(final_df)-forecast_period].copy()
    df_pd[index_column] = df_pd[index_column]+forecast_period
    df_main = final_df[forecast_period:].copy()
    diff_col_name = "CURRENT_" + forecast_column + "_" + str(forecast_period) + "_DIFF"
    df_pd = df_pd.rename(columns={TARGET_DIFF_COL_NAME: diff_col_name})
    df_pd_only = df_pd.loc[:,[index_column, diff_col_name]]
    final_df2 = pd.merge(df_pd_only, df_main, left_on=index_column, right_on=index_column)
    df_main = final_df2

    # NOW WE JOIN THE TABLE AGAINST ITSELF REPEATEDLY TO GET MULTIPLE LAGGED OBSERVATIONS
    # TO BE USED AS FEATURES FOR PREDICTION.
    # FOR EFFICIENCY WE START FROM THE SMALLEST LAG AND INCREASE BY EACH SUBSEQUENT DIFFERENCE
    list_of_lags.sort()
    previous_lag = 0
    lag_diff = 0
    target_col_to_lag = forecast_column
    target_diff_col_to_lag = diff_col_name
    for lag in list_of_lags:
        lag_diff = lag - previous_lag
        df_feat = df_main[0:len(df_main)-lag_diff].copy()
        df_feat[index_column] = df_feat[index_column] + lag_diff
        df_targ = df_main[lag_diff:].copy()
        new_col_name = "LAG_" + str(lag) + "_" + forecast_column 
        new_col_name_diff = "LAG_" + str(lag) + "_" + forecast_column + "_" + str(forecast_period) + "_DIFF"
        df_feat = df_feat.rename(columns={target_diff_col_to_lag: new_col_name_diff, target_col_to_lag: new_col_name})
        df_feat_only = df_feat.loc[:,[index_column, new_col_name, new_col_name_diff]]
        df_main = pd.merge(df_feat_only, df_targ, left_on=index_column, right_on=index_column)
        previous_lag = lag
        target_col_to_lag = new_col_name
        target_diff_col_to_lag = new_col_name_diff

    # NOW REMOVE ALL ROWS WHERE THE TARGET VALUE IS MISSING
    # IN EITHER TARGET OR PREVIOUS VALUE
    nonull_df = df_main[np.isfinite(df_main[TARGET_COL_NAME])]
    nonull_df2 = nonull_df[np.isfinite(nonull_df[TARGET_DIFF_COL_NAME])]

    return nonull_df2


