from locust import HttpUser, TaskSet, task

class CheckSite(HttpUser):

    @task
    def get_site(self):
        self.client.get("/")
        
    @task
    def get_oredict(self):
        self.client.post("predict")

class Locusttest(HttpUser):
    task_set =CheckSite
    min_wait = 2000