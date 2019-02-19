import os
import time
import logging
from locust import HttpLocust, TaskSet, task

logger = logging.getLogger(__name__)
logger.setLevel(os.getenv("LOCUST_LOG_LEVEL", "INFO").upper())

class DummyTaskSet(TaskSet):

    @task
    def get_dummy_datetime(self):
        time_start = time.time()
        response = self.client.get("/datetime")
        time_end = time.time()
        logger.info("Response - URL: {url}. Status code: {status}. "
                    "Latency: {duration}".format(url=response.url,
                                                 status=response.status_code,
                                                 duration=round(time_end - time_start, 3)))


class DummyLoadTester(HttpLocust):
    host = os.getenv("LOCUST_TARGET_HOST", "localhost:8080")
    task_set = DummyTaskSet
    min_wait = 5000
    max_wait = 15000

