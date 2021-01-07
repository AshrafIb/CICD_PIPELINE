from locust import HttpLocust, TaskSet, task

class CheckSite(TaskSet):

    @task
    def get_tests(self):
        self.client.get("http://localhost:5000")
        
    @task
    def put_tests(self):
        self.client.post("http://localhost:5000/predict"")