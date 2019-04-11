#
# TAKE A DATAFRAME WITH A DATETIME COLUMN THAT REPRESENTS TIME SERIES DATA
# AND THEN PERFORM THE FOLLOWING ACTIONS:
# 1. ORDER IT BY TIME
# 2. ADD ROWS OF NULL FOR MISSING OBSERVATIONS
# 3. ADD AN INTERGER INDEX COLUMN FOR OTHER FUNCTIONS IN THE LIBRARY
# 
def apply_order_fill_index( df, datetime_column, index_col_name, expected_interval ):
     min_date = min(df[datetime_column])
     max_date = max(df[datetime_column])
     mydates = pd.date_range(min_date, max_date)
     index_col = range( 0, len(mydates) )
     data = {index_col_name:index_col, datetime_column:mydates}
     newdf = pd.DataFrame(data)
     new_df = pd.merge( newdf, df, how='left', left_on=[datetime_column], right_on = [datetime_column] )
     return new_df

