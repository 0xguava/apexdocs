import threading
import os

def job(link, time_limit):
    print(f"Task started for {link}")
    id = os.system(f"curl -f -s -m {time_limit} {link} >/dev/null 2>&1")

    if id == 0:
        print(f"Task completed for {link}")
    else:
        print(f"Task failed for {link}")


def con_exec(tasks, time_limit):
    threads = []

    for t in tasks:
        thread = threading.Thread(target=job, args=(t,), kwargs={'time_limit': time_limit})
        threads.append(thread) 

    for t in threads:
        t.start()

    for t in threads:
        t.join(timeout = time_limit)

tasks = [
    "https://httpbin.org/status/404",
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]

con_exec(tasks, time_limit=5)
