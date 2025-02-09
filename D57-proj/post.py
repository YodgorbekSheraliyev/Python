import requests
class Post:
    def __init__(self, url):
        response = requests.get(url)
        self.data = requests.get(url).json()

    def get_by_id(self, id):
        for item in self.data:
            if item["id"] == id:
                return item
        return None
            
