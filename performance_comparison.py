#!/usr/bin/env python3

import time
import subprocess
import sys
from pathlib import Path

def run_script_and_measure(script_name):
    """Run a script and measure its execution time"""
    print(f"\n{'='*60}")
    print(f"Running {script_name}")
    print(f"{'='*60}")
    
    start_time = time.time()
    
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True, timeout=300)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        return execution_time, result.returncode == 0
    
    except subprocess.TimeoutExpired:
        print(f"Script {script_name} timed out after 5 minutes")
        return None, False
    except Exception as e:
        print(f"Error running {script_name}: {e}")
        return None, False

def compare_file_sizes():
    """Compare output file sizes"""
    files_to_check = [
        'inefficient_report.txt',
        'efficient_report.txt',
        'critical_vulnerabilities.csv',
        'high_cvss_vulnerabilities.csv'
    ]
    
    print(f"\n{'='*60}")
    print("Output File Analysis")
    print(f"{'='*60}")
    
    for filename in files_to_check:
        path = Path(filename)
        if path.exists():
            size = path.stat().st_size
            print(f"{filename}: {size:,} bytes")
        else:
            print(f"{filename}: Not found")

def main():
    print("Performance Comparison: Inefficient vs Efficient Data Processing")
    print("="*80)
    
    if not Path('data.csv').exists():
        print("Error: data.csv not found in current directory")
        return
    
    inefficient_time, inefficient_success = run_script_and_measure('inefficient_processing.py')
    efficient_time, efficient_success = run_script_and_measure('efficient_processing.py')
    
    print(f"\n{'='*60}")
    print("PERFORMANCE COMPARISON RESULTS")
    print(f"{'='*60}")
    
    if inefficient_time and efficient_time:
        improvement = ((inefficient_time - efficient_time) / inefficient_time) * 100
        speedup = inefficient_time / efficient_time
        
        print(f"Inefficient approach: {inefficient_time:.4f} seconds")
        print(f"Efficient approach:   {efficient_time:.4f} seconds")
        print(f"Performance improvement: {improvement:.1f}%")
        print(f"Speedup factor: {speedup:.2f}x")
        
        if improvement > 0:
            print("✅ Efficient approach is faster!")
        else:
            print("⚠️  Inefficient approach was faster (unexpected)")
    else:
        print("❌ Could not complete performance comparison")
        if not inefficient_success:
            print("   - Inefficient script failed")
        if not efficient_success:
            print("   - Efficient script failed")
    
    compare_file_sizes()
    
    print(f"\n{'='*60}")
    print("Key Efficiency Improvements Demonstrated:")
    print("• Pandas vectorized operations vs manual loops")
    print("• Single-pass data processing vs multiple iterations")
    print("• Efficient data structures vs basic Python collections")
    print("• Built-in statistical functions vs manual calculations")
    print("• Optimized I/O operations vs repeated file access")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
