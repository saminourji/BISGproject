# BISG Project

## NC Analysis
### Requirements

- Download North Carolina voter registration database available here: https://www.ncsbe.gov/results-data/voter-registration-data
- Using the BISG implementation available here
  https://surgeo.readthedocs.io/en/dev/
- and the “weighted estimator” as described in this paper
  https://arxiv.org/pdf/1811.11154

### Task

Write code (in python preferably) to approximate the racial composition of each political party **(DEM, REP, LIB, IND)** using the weighted estimator and the BISG implementation as your proxy predictor. Do this for a county of your choosing. Also chose some appropriate visualization to show the error of your estimates and the true race proportions

### Some things to keep in mind

- You will need to do a little bit of data processing of the North Carolina voter registration dataset. Make sure that the code you write to do this is well-documented and easy to follow
- I would recommend wrapping the BISG library in a custom class since we will be implementing many other methods for prediction by proxy. Try writing a “ProxyPredictor” interface that contains an “inference” method
- Your subclass’s implementation of the “inference” method should take as input a pandas data frame, and should output a pandas data frame with race predictions
  Note: this method will not be complicated for this example, and should just interface the functionality of Surgeo (the BISG library) with the codebase that you are developing


## Folders:
-  `predictors`: Contains the predictor interface and BISG class
- `src`: Contains a Jupyter Notebook with the analysis

