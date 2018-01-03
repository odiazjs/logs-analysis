import news_service

news_service = news_service.NewsService()
articles = news_service.get_popular_articles(3)
print('---- MOST POPULAR ARTICLES ----')
print(articles)
print('---- MOST POPULAR AUTHORS ----')
authors = news_service.get_popular_authors(3)
print(authors)
print('---- MOST ERROR DATES ----')
error_dates = news_service.get_most_error_dates()
print(error_dates)

