vulnerabilidades = [
    {"title": "SQL Injection", "severity": 9.8},
    {"title": "XSS", "severity": 6.1},
    {"title": "RCE", "severity": 10.0},
    {"title": "CSRF", "severity": 4.3},
    {"title": "Directory Traversal", "severity": 7.5}
]

ordenadas = sorted(vulnerabilidades, key=lambda x: x["severity"], reverse=True)

print("--- Vulnerabilidades ordenadas por severidad (mayor a menor) ---")
for vuln in ordenadas:
    print(f"Severity: {vuln['severity']} | Title: {vuln['title']}")