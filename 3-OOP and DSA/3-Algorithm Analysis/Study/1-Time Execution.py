import time
start=time.time()

for i in range(1,100000):
    print(i)

end=time.time()
elapsed=end-start

print("Time Execution of Algorithm",elapsed)