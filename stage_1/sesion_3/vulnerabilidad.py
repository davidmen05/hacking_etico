class Vulnerability:
    def __init__(self, title, owasp_category, severity):
        self.title = title
        self.owasp_category = owasp_category
        self.severity = severity

    def summary(self):
        return f"[{self.owasp_category}] {self.title} (Severidad: {self.severity})"


vuln1 = Vulnerability("SQL Injection", "A03:2021 - Injection", 9.8)
vuln2 = Vulnerability("Cross-Site Scripting (XSS)", "A03:2021 - Injection", 6.1)
vuln3 = Vulnerability("Broken Access Control", "A01:2021", 8.5)

vulnerabilidades = [vuln1, vuln2, vuln3]

print("--- Reporte de Vulnerabilidades ---")
for vuln in vulnerabilidades:
    print(vuln.summary())