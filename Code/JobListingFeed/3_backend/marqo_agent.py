import marqo

class MarqoAgent:
    def __init__(self, url=None, index=None):
        if url is None:
            raise ValueError("URL cannot be None")
        if index is None:
            raise ValueError("Index cannot be None")
        self.url = url
        self.index = index
        self.connect()
        
    def connect(self):
        try:
            self.mq = marqo.Client(url=self.url)
            # Perform a simple request to check if the connection is valid
            self.mq.index(self.index).get_stats()
        except Exception as e:
            raise ValueError(f"Error connecting to Marqo database: {e}")
        
    def search(self, query):
        try:
            search_results = self.mq.index(self.index).search(query)
            return search_results
        except Exception as e:
            raise ValueError(f"Error searching Marqo index: {e}")
        
        
    