from locust import HttpUser, task

class TasksUser(HttpUser):
    @task
    def tasks(self):
        self.client.get("/tasks")
