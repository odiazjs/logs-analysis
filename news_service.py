import db_connection_factory as db

class NewsService():
    def __init__(self):
        self.db_factory = db.DbConnectionFactory("news")
    
    def get_popular_articles(self, no_of_articles):
        """Return the most popular articles sorted by popularity."""
        query = '''SELECT title, count(*) as views
                    FROM articles a INNER JOIN log l 
                    ON '/article/' || a.slug = l.path 
                    GROUP BY title 
                    ORDER BY views DESC 
                    LIMIT 3;'''
        c = self.db_factory.executeQuery(query)
        articles = c.fetchall()
        return articles

    def get_popular_authors(self, no_of_articles):
        """Return the most popular authors sorted by popularity."""
        query = '''SELECT at.name, count(*) as views
                    FROM authors at INNER JOIN articles a
                    ON at.id = a.author
                    INNER JOIN log l 
                    ON '/article/' || a.slug = l.path
                    GROUP BY name 
                    ORDER BY views DESC 
                    LIMIT 3;'''
        c = self.db_factory.executeQuery(query)
        authors = c.fetchall()
        return authors

    def get_most_error_dates(self):
        """Return the dates with the most errors."""
        totals_view = '''CREATE TEMP VIEW total_reqs AS
                            SELECT l.time::date AS time, CAST (count(*) AS decimal(10,2)) as total
                            FROM log l
                            GROUP BY l.time::date
                            ORDER BY total DESC'''
        self.db_factory.executeQuery(totals_view)
        errors_view = '''CREATE TEMP VIEW total_errors AS
                            SELECT l.time::date AS time, CAST (count(*) AS decimal(10,2)) as total
                            FROM log l
                            WHERE l.status != '200 OK'
                            GROUP BY l.time::date
                            ORDER BY total DESC'''
        self.db_factory.executeQuery(errors_view)
        errors_query = '''SELECT to_char(requests.time, 'FMMonth DD, YYYY') AS time, CAST (errors.total * 100 / requests.total AS decimal(10,2)) AS percentage FROM total_reqs requests
                            JOIN total_errors errors
                            ON requests.time = errors.time
                            WHERE (errors.total * 100 / requests.total > 1)'''
        c = self.db_factory.executeQuery(errors_query)
        errors = c.fetchall()
        return errors
    
