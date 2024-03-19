from locust import HttpUser, task, between
import os

class NextcloudUser(HttpUser):
    wait_time = between(1, 5)  # Random wait time between tasks for each user
    
    def on_start(self):
        # Read credentials from file
        self.login()

    def login(self):
        credentials_path = os.path.expanduser('~/nextcloud/credentials.txt')
        with open(credentials_path, "r") as file:
            users_credentials = [line.strip().split(',') for line in file.readlines()]
            username, password = users_credentials.pop()
            self.client.post("/login", {"user": username, "password": password})

    @task
    def download_file(self):
        # This is the path where your Nextcloud stores files, adjust if necessary
        self.client.get("/index.php/apps/files/ajax/download.php?dir=/&files=1GB_file.txt", name="Download")

