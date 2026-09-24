vulnerabilidades = [
    {"name": "SQL Injection", "severity": 9.8},
    {"name": "XSS", "severity": 6.1},
    {"name": "RCE", "severity": 10.0},
    {"name": "CSRF", "severity": 4.3},
    {"name": "Directory Traversal", "severity": 7.5}
]

vulnerabilidades_ordenadas = sorted(vulnerabilidades, key=lambda x: x["severity"], reverse=True)

print("--- Reporte de Severidad de Vulnerabilidades ---")
for vuln in vulnerabilidades_ordenadas:
    print(f"Severity: {vuln['severity']} | Name: {vuln['name']}")