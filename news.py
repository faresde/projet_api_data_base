# %%
# import requests
# response = requests.get(
#     'https://newsapi.org/v2/everything?q=bitcoin&from=2021-06-16&sortBy=popularity&apiKey=bcd9d845a8c04154abca2ef64021d47a')

# print(response)
# print(response.json())
# %%
from newsapi import NewsApiClient
from requests import auth
newsapi = NewsApiClient(api_key='bcd9d845a8c04154abca2ef64021d47a')
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge,abc-news,abc-news-au,australian-financial-review,bloomberg',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-06-10',
                                      to='2021-07-05',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)

# print(f"all_articles:{all_articles['articles']}")


#sources_name = []
for articles in all_articles['articles']:
    date_article = articles['publishedAt']
    title = articles['title']
    author = articles['author']
    description = articles['description']
    source_name = articles['source']['name']
    url = articles['url']

    # print(
    #     "date_article: {}, title: {}, author: {}, description: {}, source_name: {}".format(date_article, title, author, description, source_name))
    # print(url)

# for data in elem:
#     print(data)
#     articles[data] = elem[data]

# %%
