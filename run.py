import news_service

news_service = news_service.NewsService()
articles = news_service.get_popular_articles(3)
print('---- MOST POPULAR ARTICLES ----')
print(articles)
print('---- MOST POPULAR AUTHORS ----')
authors = news_service.get_popular_authors(3)
print(authors)

