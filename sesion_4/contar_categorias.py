vulnerabilidades = [
    {"title": "SQL Injection", "owasp_category": "A03:2021 - Injection", "severity": 9.8},
    {"title": "XSS", "owasp_category": "A03:2021 - Injection", "severity": 6.1},
    {"title": "Broken Access Control", "owasp_category": "A01:2021", "severity": 8.5},
    {"title": "Cryptographic Failures", "owasp_category": "A02:2021", "severity": 7.4},
    {"title": "Command Injection", "owasp_category": "A03:2021 - Injection", "severity": 9.1},
    {"title": "Security Misconfiguration", "owasp_category": "A05:2021", "severity": 6.5}
]

conteo = {}

for vuln in vulnerabilidades:
    categoria = vuln["owasp_category"]
    if categoria in conteo:
        conteo[categoria] += 1
    else:
        conteo[categoria] = 1

print("--- Conteo por Categoría OWASP ---")
for categoria, cantidad in conteo.items():
    print(f"{categoria}: {cantidad} vulnerabilidad(es)")