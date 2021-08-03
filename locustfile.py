from locust import HttpUser, constant, task, SequentialTaskSet

class MyReqRes(SequentialTaskSet):

    @task
    def get_users(self):
        res= self.client.get("/")
        print("Get method status is", res.status_code)

    @task
    def post_status(self):
        res= self.client.post("/?status=success")
        print("post method status is", res.status_code)

class MySeqTest(HttpUser):
    wait_time = constant(1)
    host = "http://demo.com"


    tasks = [MyReqRes]