"""
---------
ENSEMBLE METHODS
----------------

BAGGING : combining results of various models in some aggregating fashion
BOOSTING : combing models via regions of best fit


ADABOOST : 
where with each subsequent model you weight the incorrect predictions
the

"""
import math
weight1 = math.log((7/8)/(1-7/8))
weight2 = math.log((4/8)/(1-4/8))
weight3 = math.log((2/8)/(1-2/8))

print(weight1, weight2, weight3)