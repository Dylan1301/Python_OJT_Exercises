import threading
import json
from urllib.request import urlopen, Request


link = "https://passwordinator.herokuapp.com/generate"
passwordDict = {}
def getpass(link):
    req = Request(link,  method='GET')
    try:
        with urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data["data"]
    except:
        return None
    # Incase No data Found


def threadJob(lock, iteration = 100, link = link, passDict = passwordDict):
    for i in range(iteration):
        password = getpass(link)
        lock.acquire()
        if password in passDict:
            passDict[password] = False
        else:
            passDict[password] = True
        lock.release()
#  Another way maybe Using the many producer and  1 consumer where many producer will get the passwords and
#  1 producer will do the actual update  - the above function use different approach.


def MainThread(job = threadJob, threads = 10):
    threadsList = []
    # Define Lock for synchronization
    lock = threading.Lock()

    # Add Threads into ThreadList
    for i in range(threads):
        thread = threading.Thread(target= job, args=(lock,))
        threadsList.append(thread)
        thread.start()
        print("Thread {} has started".format(i))


    print("")
    # Wait for all threads
    for i in range(len(threadsList)):
        threadsList[i].join()
        print("Thread {} has stopped".format(i))

    print("MainThread Finished")

MainThread()
print(len(passwordDict))
print(passwordDict)
# We can either loop MainThreads 10 times or Config the ThreadJob with wanted iterations

#
# if __name__ == "__main__":
#     for i in range(10):
#         MainThread()
#         dictlen = len(passwordDict)
#         print("Iteration {} :  - DictLen: {}".format(i, dictlen))
#
#     print(passwordDict)
