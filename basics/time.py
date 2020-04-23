import time
start_time = time.time()

x = 0
for i in range(1,1000000):
  x = x + 3
print(x)

print("--- %s seconds ---" % (time.time() - start_time))