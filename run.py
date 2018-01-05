#!/usr/bin/python
import news_service

news_service = news_service.NewsService()
articles = news_service.get_popular_articles(3)

print('1. What are the most popular three articles of all time?')
for article in articles:
    output = '-- {title} -- {views} views.'.format(
        title=article[0], views=article[1]
    )
    print(output)
print('\n')

print('2. Who are the most popular article authors of all time? \t')
authors = news_service.get_popular_authors(3)
for author in authors:
    output = '-- {name} -- {views} views.'.format(
        name=author[0], views=author[1]
    )
    print(output)
print('\n')

print('3. On which days did more than 1% of requests lead to errors?')
error_dates = news_service.get_most_error_dates()
output = '{date} -- {percentage}% errors.'.format(
    date=error_dates[0][0], percentage=error_dates[0][1]
)
print(output)
