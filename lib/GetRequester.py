import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
    
    def load_json(self):
        response_list = []
        response = json.loads(self.get_response_body())
        for el in response:
            response_list.append(el)

        return(response_list)