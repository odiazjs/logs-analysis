import db_connection_factory as db

class NewsService():
    def __init__(self):
        self.db_factory = db.DbConnectionFactory("news")
    
    def get_popular_articles(self, no_of_articles):
        """Return the (no_of_articles) most popular articles sorted by popularity."""
        query = '''SELECT a.* FROM log l
                    JOIN articles a
                    ON l.path = ('/article/' || a.slug) LIMIT 100'''
        c = self.db_factory.executeQuery(query)
        articles = c.fetchall()
        return articles

    def insert(self):
        """Add a a new item to the 'database'"""