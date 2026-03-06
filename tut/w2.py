""" Lightweight concurrent execution framework """

import threading
import os
import time

start_time = time.time()
s = f = 0

tasks = [
    "https://httpbin.org/status/404",
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]

class concurrentExec:
    def __init__(self, tasks):
        self.tasks = tasks

    def job(link, time_limit):
        global s, f
        print(f"Task started for {link}")
        id = os.system(f"curl -f -s -m {time_limit} {link} >/dev/null 2>&1")

        if id == 0:
            print(f"Task completed for {link}")
            s += 1
        else:
            print(f"Task failed for {link}")
            f += 1


    def con_exec(self, tasks, time_limit):
        threads = []

        for t in self.tasks:
            thread = threading.Thread(target=concurrentExec.job, args=(t,), kwargs={'time_limit': time_limit})
            threads.append(thread) 

        for t in threads:
            t.start()

        for t in threads:
            t.join()

if __name__ == "__main__":
    exe = concurrentExec(tasks)
    exe.con_exec(tasks, time_limit=2)

    print(f"""Execution audit:
    tasks completed: {s}
    tasks failed: {f}
    total runtime: {time.time() - start_time :.2f}""")
