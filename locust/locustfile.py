import random
from locust import HttpUser, task, between

class JsonPlaceholderUser(HttpUser):
    """
    Simulates a user interacting with the JSONPlaceholder API.
    Used for load and performance testing portfolio demonstration.
    """
    # Simulate realistic delay between user actions
    wait_time = between(1, 3)

    @task(3)
    def get_all_posts(self):
        """Simulates browsing the feed / list of posts."""
        self.client.get("/posts", name="/posts")

    @task(2)
    def get_single_post(self):
        """Simulates viewing specific post details (using aggregated metrics name)."""
        post_id = random.randint(1, 100)
        self.client.get(f"/posts/{post_id}", name="/posts/[id]")

    @task(2)
    def get_user_profile(self):
        """Simulates viewing a user profile (using aggregated metrics name)."""
        user_id = random.randint(1, 10)
        self.client.get(f"/users/{user_id}", name="/users/[id]")

    @task(1)
    def create_post(self):
        """Simulates creating a new post."""
        payload = {
            "title": f"Locust Test Post {random.randint(100, 999)}",
            "body": "This post was created automatically during load testing simulation.",
            "userId": random.randint(1, 10)
        }
        self.client.post("/posts", json=payload, name="/posts (POST)")
