import db_connection_factory as db

class NewsService():
    def __init__(self):
        self.db_factory = db.DbConnectionFactory("news")
    
    def get_popular_articles(self, no_of_articles):
        """Return the most popular articles sorted by popularity."""
        query = '''SELECT title, count(*) as views 
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
        query = '''SELECT at.name, count(*) as views
                    FROM authors at INNER JOIN articles a
                    ON at.id = a.author
                    INNER JOIN log l 
                    ON a.slug=substring(l.path, 10)
                    GROUP BY name 
                    ORDER BY views DESC 
                    LIMIT 3;'''
        c = self.db_factory.executeQuery(query)
        articles = c.fetchall()
        return articles

    def insert(self):
        """Add a a new item to the 'database'"""