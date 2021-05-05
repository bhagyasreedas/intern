from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    host = "http://0.0.0.0:5002"

    @task
    def index(self):  
        self.client.get("users/")
    @task
    def login(self):  
        self.client.get("users/login/")
    @task
    def token(self):  
        self.client.get("tokens/<key>/")