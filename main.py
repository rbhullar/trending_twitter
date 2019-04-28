import config
import tweepy
import datetime as dt
import pandas as pd
from sqlalchemy import create_engine

# connect to Twitter API
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tweepy.API(auth)

# connect to SQL Server
engine = create_engine('mssql://localhost/PLAYGROUND?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0')

# set woeid to Canada (country)
woeid = 23424775

# hit api and get Canada's data
trends = api.trends_place(woeid)

# insert raw data into dataframe, add custom date columns
log_dict = [{'json': str(trends), 'date': f"{dt.datetime.now():%A, %B %d, %Y}", 'timestamp': dt.datetime.now()}]
log_df = pd.DataFrame(log_dict)

# insert trending data into dataframe, add custom date columns
v = pd.DataFrame(trends[0]['trends'])
v['date']       = f"{dt.datetime.now():%A, %B %d, %Y}"
v['timestamp']  = dt.datetime.now()

# push dataframes to sql server tables
log_df.to_sql(name='trending_log', con=engine, if_exists='append')
v.to_sql(name='trending_daily', con=engine, if_exists='replace')
v.to_sql(name='trending_historical', con=engine, if_exists='append')
