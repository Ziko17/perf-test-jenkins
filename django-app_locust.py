from locust import task, run_single_user
from locust import FastHttpUser


class localhost_django_app(FastHttpUser):
    host = "http://localhost:8100"
    default_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "csrftoken=vuBbtjJ2jM9OykYxEpmTaKc1Zrp0HUlI",
        "Host": "localhost:8100",
        "Referer": "http://localhost:8100/tasks/create/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
    }

    @task
    def t(self):
        with self.client.request(
            "POST",
            "/tasks/create/",
            headers={
                "Content-Length": "411",
                "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryOQQqySBvXOejjsLS",
                "Origin": "http://localhost:8100",
            },
            data="",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request("GET", "/tasks/", catch_response=True) as resp:
            pass


if __name__ == "__main__":
    run_single_user(localhost_django_app)
