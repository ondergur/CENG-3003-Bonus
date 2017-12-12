import heapq
import sys
import timeit
file = sys.argv[1]
f = open(file, "r")
heap = []

all_names = ""
for line in f:
    all_names = all_names + line

asd = all_names.splitlines()

start_time = timeit.default_timer()
for i in asd:
    heapq.heappush(heap, i)
end_time = timeit.default_timer()

print("Time spent when inserting all names :" + str((end_time - start_time)*1000000))


start_time = timeit.default_timer()
heapq.heappush(heap, "Ali")
end_time = timeit.default_timer()
print("Time spent when inserting 'Ali' :" + str((end_time - start_time)*1000000))

start_time = timeit.default_timer()
heapq.heappush(heap, "Zeynep")
end_time = timeit.default_timer()
print("Time spent when inserting 'Zeynep' :" + str((end_time - start_time)*1000000))

