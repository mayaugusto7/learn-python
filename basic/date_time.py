import time

ticks = time.time()

print("Number of ticks since 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print("Local current time: ", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("Local current time format: ", localtime)
