import threading
import time

from collections import deque

class Request:
    ms_since_unix_epoch: int

    def __init__(self, timestamp):
        self.ms_since_unix_epoch = timestamp

class RateLimiter:

    requests_per_second: int

    def __init__(self, rps):
        self.requests_per_second = int(rps + (0.25 * rps))
        self.q = deque()

    def consumer(self):
        """Dummy consumer for requests
        """
        while True:
            for _ in range(self.requests_per_second//4):
                if self.q:
                    self.q.popleft() # FIFO
            time.sleep(0.25)

    def should_rate_limit(self, request : Request) -> bool:
        """
        Initialize a queue, 3 req per second. queue size = 3
        If queue is full - drop the request /return false
        Another function - for every 250ms, pop the queue (rps/4) loop and pop
        """
        # TODO(candidate) implement me
        if len(self.q) < self.requests_per_second:
            self.q.append(request)
            return False
        return True
        
# Example behavior
rl = RateLimiter(3) # only allow 3 requests per second as a rate
thread = threading.Thread(target=rl.consumer)
thread.start()
print("spun off thread")
requests = []
requests.append(Request(100)) # 100ms since unix epoch, i.e. 100ms since January 1, 1970
requests.append(Request(200)) # this is how we represent the time our proxy received the request
requests.append(Request(300))
requests.append(Request(800))
requests.append(Request(1200))
for r in requests:
    # input:        100,   200,   300,   800,  1200
    # should return False, False, False, True, False
    print("request received at time {0}: {1} \n".format(r.ms_since_unix_epoch, rl.should_rate_limit(r)))
