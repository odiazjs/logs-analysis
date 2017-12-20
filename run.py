import news_service

news_service = news_service.NewsService()
articles = news_service.get_popular_articles(3)
print(articles)
