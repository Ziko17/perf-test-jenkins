from locust import HttpUser, TaskSet, task, between, tag
import re
import random
import string

class UserBehavior(TaskSet):



    def generate_random_string(length):
        """Generate a random string of specified length."""
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(length))
    
    @tag("get")
    @task
    def get(self):
        with self.client.get('/tasks', catch_response=True) as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure("Failed to create the get task with response code {}".format(resp.status_code))    
    @tag("create")
    @task
    def create(self):
        # Step 1: Make a GET request to retrieve the CSRF token
        
        response = self.client.get("/tasks/create/")
        csrf_token = re.search(r'name="csrfmiddlewaretoken" value="(.+?)"', response.text).group(1)
        
        # Step 2: Use the retrieved CSRF token in the POST request
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "csrfmiddlewaretoken": csrf_token,
            "name": UserBehavior.generate_random_string(10),
            "status": "o"
        }
        
        # Step 3: Make the POST request with the CSRF token
        with self.client.post("/tasks/create/", headers=headers, data=data, catch_response=True) as resp:
            if resp.status_code == 200:
                resp.success()
            else:
                resp.failure("Failed to create task. Status code: {}".format(resp.status_code))

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)