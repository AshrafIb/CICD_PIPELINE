from locust import HttpUser, TaskSet, task

class CheckSite(HttpUser):

    @task
    def get_tests(self):
        self.client.get("http://localhost:5000")
        
    @task
    def put_tests(self):
        self.client.post("http://localhost:5000/predict")