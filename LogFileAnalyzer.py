import re
from collections import Counter

def analyze_log(file_path):
    # Regular expression for matching log entries
    log_pattern = re.compile(
        r'(?P<ip>[\d\.]+) - - \[.*\] "(?P<method>GET|POST|PUT|DELETE) (?P<request>[^\s]+) HTTP/\d\.\d" (?P<status>\d{3})'
    )

    status_404_count = 0
    page_requests = Counter()
    ip_requests = Counter()

    # Read the log file
    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                ip = match.group('ip')
                request = match.group('request')
                status = match.group('status')

                # Count 404 errors
                if status == '404':
                    status_404_count += 1

                # Count requests per page
                page_requests[request] += 1
                
                # Count requests per IP
                ip_requests[ip] += 1

    # Generate report
    report = {
        "Total 404 Errors": status_404_count,
        "Most Requested Pages": page_requests.most_common(5),
        "Top IP Addresses": ip_requests.most_common(5),
    }

    return report

def print_report(report):
    print("Web Server Log Analysis Report")
    print("=" * 40)
    print(f"Total 404 Errors: {report['Total 404 Errors']}")
    print("\nMost Requested Pages:")
    for page, count in report["Most Requested Pages"]:
        print(f"  {page}: {count} requests")
    prin

