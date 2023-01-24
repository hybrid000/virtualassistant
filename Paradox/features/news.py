import requests
import json



def get_news():
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=398b4b92a8284fcd89c542f5fbe1a514'
    # url = 'https://newsapi.org/v2/top-headlines/source=google-news-in?&apiKey=398b4b92a8284fcd89c542f5fbe1a514'
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getNewsUrl():
    return 'https://newsapi.org/v2/top-headlines?country=in&apiKey=398b4b92a8284fcd89c542f5fbe1a514'
    # return 'https://newsapi.org/v2/top-headlines?source=google-news-in?&apiKey=398b4b92a8284fcd89c542f5fbe1a514'
