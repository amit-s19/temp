#!/usr/bin/env python3

import csv
import time
from collections import defaultdict

def inefficient_read_all_data():
    """Inefficient: Reads entire large CSV into memory at once"""
    start_time = time.time()
    
    all_data = []
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            all_data.append(row)
    
    end_time = time.time()
    print(f"Inefficient read took: {end_time - start_time:.4f} seconds")
    print(f"Memory usage: {len(all_data)} records in memory")
    return all_data

def inefficient_filter_critical_vulnerabilities(data):
    """Inefficient: Uses nested loops and string comparisons"""
    start_time = time.time()
    
    critical_vulns = []
    for row in data:
        if row['level'].strip('"') == 'CRITICAL':
            critical_vulns.append(row)
    
    end_time = time.time()
    print(f"Inefficient filtering took: {end_time - start_time:.4f} seconds")
    return critical_vulns

def inefficient_calculate_severity_stats(data):
    """Inefficient: Multiple passes through data, repeated string operations"""
    start_time = time.time()
    
    severity_counts = {}
    
    for row in data:
        level = row['level'].strip('"')
        if level not in severity_counts:
            severity_counts[level] = 0
        severity_counts[level] += 1
    
    total_count = 0
    for count in severity_counts.values():
        total_count += count
    
    percentages = {}
    for level, count in severity_counts.items():
        percentages[level] = (count / total_count) * 100
    
    end_time = time.time()
    print(f"Inefficient stats calculation took: {end_time - start_time:.4f} seconds")
    return severity_counts, percentages

def inefficient_high_cvss_analysis(data):
    """Inefficient: String to float conversion in loop, multiple iterations"""
    start_time = time.time()
    
    high_cvss_vulns = []
    for row in data:
        try:
            cvss_score = float(row['cvss'].strip('"'))
            if cvss_score >= 7.0:
                high_cvss_vulns.append(row)
        except ValueError:
            continue
    
    total_high_cvss = len(high_cvss_vulns)
    
    critical_high_cvss = 0
    for vuln in high_cvss_vulns:
        if vuln['level'].strip('"') == 'CRITICAL':
            critical_high_cvss += 1
    
    end_time = time.time()
    print(f"Inefficient CVSS analysis took: {end_time - start_time:.4f} seconds")
    return total_high_cvss, critical_high_cvss

def inefficient_generate_report(data):
    """Inefficient: Multiple file writes, repeated data processing"""
    start_time = time.time()
    
    with open('inefficient_report.txt', 'w') as f:
        f.write("Vulnerability Analysis Report\n")
        f.write("=" * 30 + "\n\n")
        
        f.write(f"Total vulnerabilities: {len(data)}\n\n")
        
        severity_counts, percentages = inefficient_calculate_severity_stats(data)
        f.write("Severity Distribution:\n")
        for level, count in severity_counts.items():
            f.write(f"{level}: {count} ({percentages[level]:.2f}%)\n")
        
        f.write("\n")
        
        critical_vulns = inefficient_filter_critical_vulnerabilities(data)
        f.write(f"Critical vulnerabilities: {len(critical_vulns)}\n")
        
        high_cvss_total, critical_high_cvss = inefficient_high_cvss_analysis(data)
        f.write(f"High CVSS (>=7.0) vulnerabilities: {high_cvss_total}\n")
        f.write(f"Critical vulnerabilities with high CVSS: {critical_high_cvss}\n")
    
    end_time = time.time()
    print(f"Inefficient report generation took: {end_time - start_time:.4f} seconds")

def main():
    print("Running inefficient vulnerability analysis...")
    print("=" * 50)
    
    total_start = time.time()
    
    data = inefficient_read_all_data()
    critical_vulns = inefficient_filter_critical_vulnerabilities(data)
    severity_counts, percentages = inefficient_calculate_severity_stats(data)
    high_cvss_total, critical_high_cvss = inefficient_high_cvss_analysis(data)
    inefficient_generate_report(data)
    
    total_end = time.time()
    
    print(f"\nTotal inefficient processing time: {total_end - total_start:.4f} seconds")
    print(f"Found {len(critical_vulns)} critical vulnerabilities")
    print(f"Found {high_cvss_total} high CVSS vulnerabilities")
    print("Report saved to inefficient_report.txt")

if __name__ == "__main__":
    main()
