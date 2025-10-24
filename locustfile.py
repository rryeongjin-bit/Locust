from locust import HttpUser, task, between

# HttpUser : Http 요청을 시뮬레이션하는 가상 사용자 클래스
# task     : 사용자가 수행할 작업을 표시하는 데코레이터
# between  : 사용자가 작업 사이에 대기할 시간 범위를 지정하는 함수

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.get("/event/66782")

        ##