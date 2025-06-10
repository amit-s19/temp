#!/usr/bin/env python3

import pandas as pd
import time
from pathlib import Path

def efficient_read_and_process_data():
    """Efficient: Uses pandas for optimized CSV reading and processing"""
    start_time = time.time()
    
    df = pd.read_csv('data.csv')
    df['cvss'] = pd.to_numeric(df['cvss'], errors='coerce')
    df['level'] = df['level'].str.strip('"')
    
    end_time = time.time()
    print(f"Efficient read and preprocessing took: {end_time - start_time:.4f} seconds")
    print(f"DataFrame shape: {df.shape}")
    return df

def efficient_filter_critical_vulnerabilities(df):
    """Efficient: Uses pandas boolean indexing"""
    start_time = time.time()
    
    critical_vulns = df[df['level'] == 'CRITICAL']
    
    end_time = time.time()
    print(f"Efficient filtering took: {end_time - start_time:.4f} seconds")
    return critical_vulns

def efficient_calculate_severity_stats(df):
    """Efficient: Uses pandas value_counts for single-pass calculation"""
    start_time = time.time()
    
    severity_counts = df['level'].value_counts()
    percentages = df['level'].value_counts(normalize=True) * 100
    
    end_time = time.time()
    print(f"Efficient stats calculation took: {end_time - start_time:.4f} seconds")
    return severity_counts, percentages

def efficient_high_cvss_analysis(df):
    """Efficient: Vectorized operations, single pass through data"""
    start_time = time.time()
    
    high_cvss_mask = df['cvss'] >= 7.0
    high_cvss_vulns = df[high_cvss_mask]
    
    total_high_cvss = len(high_cvss_vulns)
    critical_high_cvss = len(high_cvss_vulns[high_cvss_vulns['level'] == 'CRITICAL'])
    
    end_time = time.time()
    print(f"Efficient CVSS analysis took: {end_time - start_time:.4f} seconds")
    return total_high_cvss, critical_high_cvss

def efficient_generate_comprehensive_analysis(df):
    """Efficient: Single-pass comprehensive analysis with vectorized operations"""
    start_time = time.time()
    
    analysis = {
        'total_vulnerabilities': len(df),
        'severity_counts': df['level'].value_counts().to_dict(),
        'severity_percentages': (df['level'].value_counts(normalize=True) * 100).to_dict(),
        'cvss_stats': {
            'mean': df['cvss'].mean(),
            'median': df['cvss'].median(),
            'std': df['cvss'].std(),
            'min': df['cvss'].min(),
            'max': df['cvss'].max()
        },
        'high_cvss_count': len(df[df['cvss'] >= 7.0]),
        'critical_high_cvss': len(df[(df['cvss'] >= 7.0) & (df['level'] == 'CRITICAL')]),
        'severity_cvss_crosstab': pd.crosstab(df['level'], df['cvss'] >= 7.0, margins=True)
    }
    
    end_time = time.time()
    print(f"Efficient comprehensive analysis took: {end_time - start_time:.4f} seconds")
    return analysis

def efficient_generate_report(analysis):
    """Efficient: Single file write with pre-computed analysis"""
    start_time = time.time()
    
    report_lines = [
        "Vulnerability Analysis Report (Efficient Version)",
        "=" * 50,
        "",
        f"Total vulnerabilities: {analysis['total_vulnerabilities']:,}",
        "",
        "Severity Distribution:",
    ]
    
    for level, count in analysis['severity_counts'].items():
        percentage = analysis['severity_percentages'][level]
        report_lines.append(f"  {level}: {count:,} ({percentage:.2f}%)")
    
    report_lines.extend([
        "",
        "CVSS Score Statistics:",
        f"  Mean: {analysis['cvss_stats']['mean']:.2f}",
        f"  Median: {analysis['cvss_stats']['median']:.2f}",
        f"  Standard Deviation: {analysis['cvss_stats']['std']:.2f}",
        f"  Range: {analysis['cvss_stats']['min']:.1f} - {analysis['cvss_stats']['max']:.1f}",
        "",
        f"High CVSS (>=7.0) vulnerabilities: {analysis['high_cvss_count']:,}",
        f"Critical vulnerabilities with high CVSS: {analysis['critical_high_cvss']:,}",
        "",
        "Severity vs High CVSS Cross-tabulation:",
        str(analysis['severity_cvss_crosstab'])
    ])
    
    with open('efficient_report.txt', 'w') as f:
        f.write('\n'.join(report_lines))
    
    end_time = time.time()
    print(f"Efficient report generation took: {end_time - start_time:.4f} seconds")

def efficient_export_filtered_data(df):
    """Efficient: Export critical vulnerabilities using pandas built-in methods"""
    start_time = time.time()
    
    critical_vulns = df[df['level'] == 'CRITICAL']
    critical_vulns.to_csv('critical_vulnerabilities.csv', index=False)
    
    high_cvss_vulns = df[df['cvss'] >= 7.0]
    high_cvss_vulns.to_csv('high_cvss_vulnerabilities.csv', index=False)
    
    end_time = time.time()
    print(f"Efficient data export took: {end_time - start_time:.4f} seconds")
    return len(critical_vulns), len(high_cvss_vulns)

def main():
    print("Running efficient vulnerability analysis...")
    print("=" * 50)
    
    total_start = time.time()
    
    df = efficient_read_and_process_data()
    analysis = efficient_generate_comprehensive_analysis(df)
    efficient_generate_report(analysis)
    critical_count, high_cvss_count = efficient_export_filtered_data(df)
    
    total_end = time.time()
    
    print(f"\nTotal efficient processing time: {total_end - total_start:.4f} seconds")
    print(f"Found {critical_count:,} critical vulnerabilities")
    print(f"Found {high_cvss_count:,} high CVSS vulnerabilities")
    print("Reports and filtered data exported successfully")

if __name__ == "__main__":
    main()
