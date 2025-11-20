import time
import random
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def test_algorithm(algorithm, data):
    start_time = time.time()
    algorithm(data.copy())
    end_time = time.time()
    return end_time - start_time

def run_experiments():
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort, 
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort
    }
    
    input_sizes = [100, 500, 1000, 2000, 5000]
    
    results = {name: [] for name in algorithms.keys()}
    
    print("Starting experiments...")
    print("Size\tBubble\tSelection\tInsertion\tMerge")
    print("-" * 50)
    
    for size in input_sizes:
        data = [random.randint(1, 10000) for _ in range(size)]
        
        times = []
        for name, algorithm in algorithms.items():
            time_taken = test_algorithm(algorithm, data)
            times.append(time_taken)
            results[name].append(time_taken)
            
        print(f"{size}\t{times[0]:.4f}\t{times[1]:.4f}\t{times[2]:.4f}\t{times[3]:.4f}")
    
    return results, input_sizes

def detailed_n2_comparison(results, input_sizes):
    plt.figure(figsize=(10, 6))
    
    # Plot only the O(n²) algorithms
    algorithms = ['Bubble Sort', 'Selection Sort', 'Insertion Sort']
    colors = ['red', 'blue', 'green']
    
    for i, algo in enumerate(algorithms):
        plt.plot(input_sizes, results[algo], marker='o', 
                label=algo, color=colors[i], linewidth=2)
    
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Detailed O(n²) Algorithms Comparison\n(Selection vs Insertion Sort)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Add annotation at the crossover point
    if len(input_sizes) >= 3:
        crossover_idx = 2  # Around 1000 elements based on your data
        plt.annotate('Performance Crossover', 
                    xy=(input_sizes[crossover_idx], results['Selection Sort'][crossover_idx]),
                    xytext=(input_sizes[crossover_idx] + 500, results['Selection Sort'][crossover_idx] + 0.02),
                    arrowprops=dict(arrowstyle='->', color='black'))
    
    plt.savefig('../results/detailed_n2_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_graphs(results, input_sizes):
    plt.figure(figsize=(12, 8))
    
    # Plot 1: All algorithms together
    plt.subplot(2, 2, 1)
    for name, times in results.items():
        plt.plot(input_sizes, times, marker='o', label=name)
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.grid(True)
    
    # Plot 2: Only O(n^2) algorithms
    plt.subplot(2, 2, 2)
    for name, times in results.items():
        if name != 'Merge Sort':
            plt.plot(input_sizes, times, marker='o', label=name)
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('O(n²) Algorithms Comparison')
    plt.legend()
    plt.grid(True)
    
    # Plot 3: Merge Sort only
    plt.subplot(2, 2, 3)
    plt.plot(input_sizes, results['Merge Sort'], marker='o', color='red')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Merge Sort Performance')
    plt.grid(True)
    
    # Plot 4: Bar chart for largest input size
    plt.subplot(2, 2, 4)
    final_times = [times[-1] for times in results.values()]
    algorithms = list(results.keys())
    plt.bar(algorithms, final_times, color=['blue', 'orange', 'green', 'red'])
    plt.xlabel('Algorithms')
    plt.ylabel('Time (seconds)')
    plt.title(f'Performance for {input_sizes[-1]} elements')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('../results/sorting_performance.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    results, input_sizes = run_experiments()
    detailed_n2_comparison(results, input_sizes)
    create_graphs(results, input_sizes)
