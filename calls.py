from dataclasses import dataclass
import requests
env='UAT'
class BASE_URL():
    DIT = 'url.dit.com'
    SIT = 'url.sit.com'
    UAT = 'https://reqres.in/api/users?page=1'
    PRD = 'url.prd.com'


class APIRequest(object):
    def __init__(self,env):
        self.env = env
        self.url=None
        #if self.env in {Environment.DIT, Environment.PRD}:
         #   raise Exception(f"Not supported env ({self.env}).")
        if env=='UAT':
            self.url=BASE_URL.UAT

    def get(self,payload = None, headers=None):
        response = requests.get(self.url, data=payload, headers=headers)
        return self.__get_responses(response)

    def post(self, payload, headers):
        response = requests.post(self.url, data=payload, headers=headers)
        return self.__get_responses(response)

    def delete(self, payload = None, headers=None):
        response = requests.delete(self.url)
        return self.__get_responses(response)

    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text
        return status_code, text



a=APIRequest('UAT')

output=a.get()
print(output)
