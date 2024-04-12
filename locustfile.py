from locust import HttpUser, task

class Catstagram(HttpUser):
    @task
    def catstagram(self):
        self.client.get("/admin")
        self.client.get("/")
