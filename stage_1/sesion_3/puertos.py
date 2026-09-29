puertos = list()

puertos.append({"port": 22, "service": "SSH", "status": "open"})
puertos.append({"port": 80, "service": "HTTP", "status": "open"})
puertos.append({"port": 443, "service": "HTTPS", "status": "open"})
puertos.append({"port": 3306, "service": "MySQL", "status": "closed"})
puertos.append({"port": 8080, "service": "Proxy", "status": "closed"})
puertos.append({"port": 21, "service": "FTP", "status": "open"})

puertos_abiertos = list()

print("--- Escaneo de Puertos ---")
for puerto in puertos:
    if puerto["status"] == "open":
        puertos_abiertos.append(puerto)
        print(f"Puerto: {puerto['port']} | Servicio: {puerto['service']} | Estado: {puerto['status']}")

print(f"\nTotal de puertos abiertos encontrados: {len(puertos_abiertos)}")