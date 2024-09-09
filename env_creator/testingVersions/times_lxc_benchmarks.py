import numpy as np

def getStatistics(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            real_lines = [line.strip() for line in lines if line.startswith("real")]
            times = [line.split("\t")[-1] for line in real_lines]
            times = [float(time[time.index("m")+1:time.index("s")]) for time in times]

            average_time = np.mean(times)
            standard_deviation = np.std(times)
            standard_error_mean = np.std(times) / np.sqrt(len(times))

            print("\n")
            print(f"File: {file_path}")
            print(f"Samples: {len(times)}")
            print(f"Average time: {average_time}")
            print(f"Standard deviation: {standard_deviation}")
            print(f"Standard Error of the Mean (SEM): {standard_error_mean}")
            print(f"Coefficient of interval with 95% confidence: {1.96 * standard_error_mean}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")


print("Single LXC benchmark")
# file_path = 'single_benchmark_ubuntu'
# getStatistics(file_path)
# file_path = 'single_benchmark_alpine'
# getStatistics(file_path)
# file_path = 'single_benchmark_debian'
# getStatistics(file_path)
# file_path = 'single_benchmark_fedora'
# getStatistics(file_path)
# print("Single LXC benchmark")
file_path = 'parallel_1_benchmarking_ubuntu.txt'
getStatistics(file_path)
file_path = 'parallel_1_benchmarking_alpine.txt'
getStatistics(file_path)
file_path = 'parallel_1_benchmarking_debian.txt'
getStatistics(file_path)
file_path = 'parallel_1_benchmarking_fedora.txt'
getStatistics(file_path)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("All 1 LXC together")
file_path = 'parallel_1_benchmarking_all.txt'
getStatistics(file_path)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")
print("2 Parallel LXC benchmarks")
print("Single LXC benchmark")
file_path = 'parallel_2_benchmarking.txt' # change name
getStatistics(file_path)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")
print("3 Parallel LXC benchmarks")
print("Single LXC benchmark")
file_path = 'parallel_3_benchmarking.txt' # change name
getStatistics(file_path)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")
print("4 Parallel LXC benchmarks")
print("Single LXC benchmark")
file_path = 'parallel_4_benchmarking.txt' # change name 
getStatistics(file_path)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")