from locust import HttpUser, TaskSet, task

class CheckSite(HttpUser):

    @task
    def get_site(self):
        self.client.get("/")
        
    @task
    def get_predict(self):
        self.client.post("/predict",json={
   "CHAS":{
      "0":0
   },
   "RM":{
      "0":6.575
   },
   "TAX":{
      "0":296.0
   },
   "PTRATIO":{
      "0":15.3
   },
   "B":{
      "0":396.9
   },
   "LSTAT":{
      "0":4.98
   })

class Locusttest(HttpUser):
    task_set =CheckSite
    min_wait = 2000