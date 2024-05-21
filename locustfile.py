from locust import HttpUser, task

class TasksUser(HttpUser):
    @task
    def test_fct(self):
        self.client.get("/tasks")
