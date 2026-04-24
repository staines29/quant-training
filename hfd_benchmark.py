import time
import random
import numpy as np

python_list = [random.random() for _ in range(1000000)]

start_time_a = time.perf_counter()
new_list = [x * 1.05 for x in python_list]
end_time_a = time.perf_counter()
elapsed_time_a = end_time_a - start_time_a
print("python loop time:", elapsed_time_a)
start_time_b = time.perf_counter()
my_array = np.random.rand(1000000)
new_array = my_array * 1.05

end_time_b = time.perf_counter()
elapsed_time_b = end_time_b - start_time_b

print("numpy vectorized time:", elapsed_time_b)
speedup = elapsed_time_a / elapsed_time_b
print(f"speedup:{speedup:.2f}x")