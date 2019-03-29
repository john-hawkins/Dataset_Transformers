Dataset Transformer Codebase 
----------------------------

There are several Transformers functions in this project. 

# Lagged Feature Transformer

This a transformer that takes a dataset of values at a given point in time
and will transform it into a set of rows that permit prediction using a variety
of lagged values.

DatasetGenerator.py  



# Normaliser

This is a function to normalise the values of a set of columns in a dataset. 

 Normalizer.py 




# Technical Analysis Transformer

This is a transformer that continues that approach above, transforming time
series into targets and lagged features. But the Technical Analysis version
creates a range of higher order fetaures that are typically used in the
technical analysis of market data.


# THIS CODE WILL TAKE A TIME SERIES DATA SET AND GENERATE SOME 
# FEATURES THAT ARE INDICATORS USED BY TECHNICAL ANALYSTS
# MANY OF THESE REQUIRE FIRST CALCULATING THE HIGHS AND LOWS ON A DAILY BASIS
# THAT CAN THEN BE USED FOR THE INDICATORS 
#
# THESE INDICATORS FORM THE BASIS OF THE 
# Ichimoku Clouds
# Tenkan-sen (Conversion Line): (9-period high + 9-period low)/2))
#
# Kijun-sen (Base Line): (26-period high + 26-period low)/2))
#
# Senkou Span A (Leading Span A): (Conversion Line + Base Line)/2))
#
# Senkou Span B (Leading Span B): (52-period high + 52-period low)/2))


