# TimeSeries_analysis_forcasting
 Forecasting of count of ticket would be created next day/month by Time Series forecasting technique -

Goal - This project is about to forecast the count of tickets that may come in next month and day, based on the forecasted value, management can fix the number of manpower should be available, leave, vacation of team members be granted accordingly. That avoids shortage of manpower on peak time.

 Steps/Responsibilities- 

Collected data from Jira.
Cleaned data by various pre-processing techniques using Python, pandas, lambda.
Visualized data on some factors doing resampling using Matplotlib and Seaborn.
Tested time series data stationary by *ADF*, made stationary by differencing. 
Found p,q,d,s order by *PACF, ACF, Auto Arima*.
Built and trained models like *ARIMA, SARIMAX*, then forcasted. 
Evaluated model’s performance by R2 score, Adjusted R2 score, *rmse, mae*.
Deployed the model performing best on cloud platform.
