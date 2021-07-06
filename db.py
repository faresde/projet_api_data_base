# %%
import psycopg2
from psycopg2 import Error
from newsapi import NewsApiClient
from requests import auth


connection = psycopg2.connect(host="localhost",
                              port="5432",
                              database="projectApi",
                              user="fares",
                              password="faresde")
# %%
cursor = connection.cursor()
# Print PostgreSQL details
print("PostgreSQL server information")
print(connection.get_dsn_parameters(), "\n")
# %%
cursor.execute("SELECT version();")
# %%
record = cursor.fetchone()
print("You are connected to - ", record, "\n")

newsapi = NewsApiClient(api_key='bcd9d845a8c04154abca2ef64021d47a')
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge,abc-news,abc-news-au,australian-financial-review,bloomberg',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-06-10',
                                      to='2021-07-05',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)

for articles in all_articles['articles']:
    date_article = articles['publishedAt']
    title = articles['title']
    author = articles['author']
    description = articles['description']
    source_name = articles['source']['name']
    url = articles['url']

    insert_query = """ INSERT INTO Articles (id,author,title,description,url,date_article,source_name) VALUES ()"""
