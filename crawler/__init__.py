import requests
import gzip
import socket
import ssl
import threading
import os
import queue
import time


exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, name, q, queue_lock, file_lock, output=None):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = q
        self.queueLock = queue_lock
        self.fileLock = file_lock
        self.output = output

    def run(self):
        print("Starting {}".format(self.name))
        self._check_ssl()
        print("Exiting: {}".format(self.name))

    def _check_ssl(self):
        while not exitFlag:
            self.queueLock.acquire()
            if not self.queue.empty():
                domain = self.queue.get()
                self.queueLock.release()
                context = ssl.create_default_context()
                try:
                    with socket.create_connection((domain, 443), timeout=0.5) as sock:
                        with context.wrap_socket(sock, server_hostname=domain) as ssock:
                            message = "{}".format(ssock.version())
                except Exception as e:
                    message = getattr(e, "message", str(e))
                finally:
                    print("{} {:>70}: {:>30}".format(self.name, domain, message))
                    if self.output:
                        self.fileLock.acquire()
                        with open(self.output, "a") as csvfile:
                            csvfile.write("{};{}\n".format(domain, message))
                        self.fileLock.release()
            else:
                self.queueLock.release()
                time.sleep(1)


def main():
    # zones = ["ru", "rf", "su"]
    zones = ["ru"]
    for zone in zones:
        zone_url = "https://partner.r01.ru/zones/{}_domains.gz".format(zone)
        zone_file = "{}_zone.gz".format(zone)
        output_file = "{}_zone.csv".format(zone)
        resp = requests.get(zone_url, stream=True)
        resp.raise_for_status()

        # with open(zone_file, "wb") as zone_file:
        #     for chunk in resp.iter_content(chunk_size=128):
        #         zone_file.write(chunk)

        with gzip.open(zone_file, "rt") as zone_file:
            domains = [line.split("\t")[0] for line in zone_file]
            print(
                "Registered domains: {} in zone {}".format(len(domains), zone.upper())
            )
        # create lock for queue
        queueLock = threading.Lock()
        # create lock for writing file
        fileLock = threading.Lock()

        # maxSize of queue
        workQueue = queue.Queue(len(domains))

        # fill the Queue
        queueLock.acquire()
        for domain in domains:
            workQueue.put(domain)
        queueLock.release()

        # check_ssl(domains, output_file)
        threads = []
        threadsCount = 200

        for thread_id in range(threadsCount):
            threadName = "MyThread-{}".format(thread_id)
            t = MyThread(threadName, workQueue, queueLock, fileLock, output_file)
            t.start()
            threads.append(t)

        # blocking main thread while workers will not empty queue
        while not workQueue.empty():
            pass

        exitFlag = 1

        # wait while all threads complete there work
        for thread in threads:
            thread.join()

        print("All done")


# def _resolve(domain):
#     try:
#         sockets_info = socket.getaddrinfo(domain, None, proto=socket.IPPROTO_TCP)
#         ip_addresses = [socket_info[-1][0] for socket_info in sockets_info]
#         print("{} => {}".format(domain, ip_addresses))
#         return ip_addresses
#     except socket.gaierror as e:
#         print("{} => {}".format(domain, e.strerror))
#
#
# def resolvable(domains, limit=None):
#     count = 0
#     for domain in domains:
#         if limit is not None and count == limit:
#             break
#         domains[domain] = _resolve(domain)
#         count += 1


def check_ssl(domains, output=None):
    # clean output file before first run
    if output is not None:
        os.unlink(output)

    for domain in domains:
        context = ssl.create_default_context()
        try:
            with socket.create_connection((domain, 443), timeout=0.5) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    message = "{}".format(ssock.version())
        except Exception as e:
            message = getattr(e, "message", str(e))
        finally:
            print("{:>70}: {:>30}".format(domain, message))
            domains[domain] = message
            if output is not None:
                with open(output, "a") as csvfile:
                    csvfile.write("{};{}\n".format(domain, message))


if __name__ == "__main__":
    main()
