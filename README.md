Dataset_Transformers
--------------------

This repository contains a collection of functions that can be used to transform data in order to apply machine learning.

This is predominantly about taking data that has a simple time-series structure and creating the lagged/aggregated 
feature that make it applicable to standard machine learning approaches.


# Examples

In the data directory there is [Run Script](data/run.sh) to grab the example data set.

After you have executed it you can execute one of these examples

## Example One - Lagged Features Only

[python code](examples/example_one_lagged_features.py)

This will apply only the lagging and first order differences differences


## Example Two - Moving Average Features Only

[python code](examples/example_two_moving_average_features.py)

This will apply only the lagging and first order differences differences



# Core Functions

The Normalizer object exposes methods for creating normalization/standardization configurations for a dataset
including min/max or mean/std methods. The Min/Max methods also supprt the application of padding values to 
push the normlized vales away from the extremes. The rationale being that a model trained on targets normalised
in this fashion could potentially extrapolate to make predictions beyond the observed min and max.




