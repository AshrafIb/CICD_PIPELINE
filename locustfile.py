from locust import HttpUser, TaskSet, task
import json

with open('data.json') as f:
    data = json.loads(f.read())

class CheckSite(HttpUser):

    @task
    def get_site(self):
        self.client.get("/")
        
    @task
    def get_predict(self):
        self.client.post("/predict",json= data)

class Locusttest(HttpUser):
    task_set =CheckSite
    min_wait = 2000