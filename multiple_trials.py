import sorting_test
import time
import json

def run_multiple_trials(num_trials=5):
    all_results = []
    
    for trial in range(num_trials):
        print(f"Running trial {trial + 1}/{num_trials}...")
        results, input_sizes = sorting_test.run_experiments()
        all_results.append(results)
        time.sleep(1)  
    
    algorithms = list(all_results[0].keys())
    averaged_results = {name: [] for name in algorithms}
    
    for size_idx in range(len(input_sizes)):
        for algo in algorithms:
            times = [result[algo][size_idx] for result in all_results]
            avg_time = sum(times) / len(times)
            averaged_results[algo].append(avg_time)
    
    with open('../data/averaged_results.json', 'w') as f:
        json.dump({
            'averaged_results': averaged_results,
            'input_sizes': input_sizes
        }, f, indent=2)
    
    return averaged_results, input_sizes

if __name__ == "__main__":
    avg_results, sizes = run_multiple_trials(3)
    sorting_test.create_graphs(avg_results, sizes)