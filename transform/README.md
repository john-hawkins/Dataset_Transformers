Dataset Transformer Codebase 
----------------------------

There are several Transformers functions in this project. 

# Lagged Feature Transformer

This a transformer that takes a dataset of values at a given point in time
and will transform it into a set of rows that permit prediction using a variety
of lagged values.

DatasetGenerator.py  



# Normaliser

This is a set of functions used to normalise the values of a set of columns in a dataset.
You first need to generate the normalisation parameters using training data, and then
apply that normalisation to both training, testing and scoring data. 

 Normalizer.py 




# Technical Analysis Transformer

## NOT IMPLEMENTED

This is a transformer that continues that approach above, transforming time
series data into targets, windowed and lagged features. But the Technical Analysis version
creates a range of higher order features that are typically used in the
technical analysis of market data.


## Ichimoku Clouds

These indicators form the basis of what is often graphically displayed as a Ichimoku Clouds

* Tenkan-sen (Conversion Line): (9-period high + 9-period low)/2))

* Kijun-sen (Base Line): (26-period high + 26-period low)/2))

* Senkou Span A (Leading Span A): (Conversion Line + Base Line)/2))

* Senkou Span B (Leading Span B): (52-period high + 52-period low)/2))


## Crosses

Calculate the following features

* 50 Day Moving Average
* 200 Day Moving Average
* 100 Day Exponetial Moving Average
* Golden Cross -- Did the 50 day MA rise over the 200 day MA 
* Death Cross -- Did the 200 day MA rise over the 50 day MA
* Silver Cross -- Did the 50 day MA rise over the 100 day EMA



## Bollinger Bands

Calculate a 20 Day Moving Average

Calculate the standard deviation using the same data

Generate the following features

* MBB. Middle Bollinger Band = 20 Day MA
* UBB. Upper Bollinger band = MBB + 2 x standard deviation
* LBB. Lower Bollinger band = MBB - 2 x standard deviation
* %b. Percent b = (current − LBB) / (UBB − LBB)
* Bandwidth = (UBB − LBB) / MBB 

https://www.bollingerbands.com/bollinger-bands


## Relative Strength Index (RSI)

To calculate this indicator we need to look at the point to point changes
over each of the discrete points within the period of analysis.

The period is typically 14 days.

Within this period you calculate the average percentage change for all the
upward movements, and the average absolute percentage change for all the downward
movements. This is will give you Average Upward Change AUC and 
Average Downward Change ADC. 

These two values are then avaraged again once we have derived the AUC and ADC 
for 14 periods. This gives you Average AUC and Average ADC.

The calculation consists of 2 indicators.

* RSI_1 = 100 – [100 / ( 1 + (Average Upward Change / Average Downward Change ) ) ]

* RSI_2 = 100 – [100 / ( 1 + ( Average AUC / Average ADC ) ) ]

