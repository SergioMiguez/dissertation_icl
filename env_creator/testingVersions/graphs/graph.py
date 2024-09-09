import matplotlib.pyplot as plt

# Benchmark titles
benchmarks = [
    "1 Ubuntu LXC", "1 Alpine LXC", "1 Debian LXC", 
    "1 Fedora LXC", "2 Parallel LXC", "3 Parallel LXC", "4 Parallel LXC"
]

# Average times
average_times = [
    5.98072, 5.97460, 5.96122, 
    5.97910, 7.20334, 8.26198, 9.78704
]

# Coefficients of interval with 95% confidence (errors)
confidence_intervals = [
    0.05444, 0.05624, 0.04332, 
    0.03785, 0.13817, 0.21162, 0.43075
]

# Plotting the data
plt.figure(figsize=(10, 6))

# Plot the average times with error bars
plt.errorbar(benchmarks, average_times, yerr=confidence_intervals, fmt='o', capsize=5, color='blue', ecolor='red', elinewidth=2, markeredgewidth=2)

# Add titles and labels
plt.title("Benchmark 50 Times Average with 95% Confidence Intervals")
plt.xlabel("Benchmark Type")
plt.ylabel("Average Time (seconds)")
plt.xticks(rotation=45, ha="right")

# Display the grid for easier readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5)


# Show the plot
plt.tight_layout()
plt.show()
