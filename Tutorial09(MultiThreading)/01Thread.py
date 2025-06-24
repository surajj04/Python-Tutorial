from threading import Thread
from time import sleep

# ==================== Thread subclass for "Hello" ====================
class Hello(Thread):
    def run(self):
        # The `run()` method contains the code that will execute in this thread
        for i in range(5):
            print("Hello")
            sleep(1)  # Simulate some delay


# ==================== Thread subclass for "Hi" ====================
class Hi(Thread):
    def run(self):
        # The `run()` method contains the code that will execute in this thread
        for i in range(5):
            print("Hi")
            sleep(1)  # Simulate some delay


# ==================== Create thread instances ====================
t1 = Hello()
t2 = Hi()

# If we call `t1.run()` and `t2.run()` directly, they will execute sequentially
# To run them in PARALLEL, we must use the `start()` method
t1.start()
sleep(0.2)  # small delay to offset output so it's easier to see interleaving
t2.start()

# ==================== Wait for threads to finish ====================
# join() will wait until the thread is completed
t1.join()
t2.join()

print("bye")  # This will print after both threads have completed
