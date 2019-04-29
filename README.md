# Canadian Twitter Trends

## Introduction

The goal of this project is to showcase daily Twitter trends in Canada. Via the python code in this project, Canada's trending Twitter data is pulled into Microsoft SQL Server. Currently this data feeds Power BI visualizations on my local desktop. Data is updated daily via a scheduled task that ultimately runs this python code. 

## High Level Overview of Code

1. Connect to Twitter API and local SQL Server
2. Pull in top 50 Twitter trends in Canada (in json format)
3. Append raw json format for today's entry into 'trending_log' table
4. Append today's processed data to 'trending_historical' table 
5. Replace 'trending_daily' table with today's processed data

## Notes

To use, create a config.py file with your own authentication.
