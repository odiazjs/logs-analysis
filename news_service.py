import db_connection_factory as db

class NewsService():
    def __init__(self):
        self.db_factory = db.DbConnectionFactory("news")
    
    def get_popular_articles(self, no_of_articles):
        """Return the most popular articles sorted by popularity."""
        query = '''SELECT title, count(*) || ' views' as views
                    FROM articles a INNER JOIN log l 
                    ON a.slug=substring(l.path, 10) 
                    GROUP BY title 
                    ORDER BY views DESC 
                    LIMIT 3;'''
        c = self.db_factory.executeQuery(query)
        articles = c.fetchall()
        return articles

    def get_popular_authors(self, no_of_articles):
        """Return the most popular authors sorted by popularity."""
        query = '''SELECT at.name, count(*) || ' views' as views
                    FROM authors at INNER JOIN articles a
                    ON at.id = a.author
                    INNER JOIN log l 
                    ON a.slug=substring(l.path, 10)
                    GROUP BY name 
                    ORDER BY views DESC 
                    LIMIT 3;'''
        c = self.db_factory.executeQuery(query)
        authors = c.fetchall()
        return authors

    def get_most_error_dates(self):
        """Return the most popular authors sorted by popularity."""
        total_count_view = '''CREATE TEMP VIEW total_count AS 
                            SELECT count(*) AS total
                            FROM log'''
        self.db_factory.executeQuery(total_count_view)
        total_requests_view = '''CREATE TEMP VIEW total_req_no AS
                            SELECT SUM(total) AS t
                            FROM total_count'''  
        self.db_factory.executeQuery(total_requests_view)
        totals_view = '''CREATE TEMP VIEW total_reqs AS
                            SELECT to_char(l.time, 'MON DD, YYYY') as time, CAST (count(*) AS decimal(10,2)) as total
                            FROM log l
                            GROUP BY to_char(l.time, 'MON DD, YYYY')
                            ORDER BY total DESC'''
        self.db_factory.executeQuery(totals_view)
        errors_view = '''CREATE TEMP VIEW total_errors AS
                            SELECT to_char(l.time, 'MON DD, YYYY') as time, CAST (count(*) AS decimal(10,2)) as total
                            FROM log l
                            WHERE l.status != '200 OK'
                            GROUP BY to_char(l.time, 'MON DD, YYYY')
                            ORDER BY total DESC'''
        self.db_factory.executeQuery(errors_view)
        errors_query = '''SELECT requests.time, CAST (errors.total * 100 / requests.total AS decimal(10,2)) || '% errors' FROM total_reqs requests
                            JOIN total_errors errors
                            ON requests.time = errors.time
                            WHERE (errors.total * 100 / requests.total > 1)'''
        c = self.db_factory.executeQuery(errors_query)
        errors = c.fetchall()
        return errors