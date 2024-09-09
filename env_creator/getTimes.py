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


file_path = 'raw_benchmark'
getStatistics(file_path)


file_path = 'p_start_benchmark'
getStatistics(file_path)

file_path = 'p_clone_start_benchmark'
getStatistics(file_path)
