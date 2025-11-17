import pandas as pd
import random
from datetime import datetime, timedelta

# Lista de proveedores y categorías
vendors = ["Accenture", "IBM", "Globant", "Deloitte", "EY", "Capgemini", "Oracle", "SAP", "Microsoft", "PwC"]
categories = ["IT Services", "Cloud Support", "Software Dev", "Risk Audit", "Finance Ops", "Consulting", "Software Licensing", "ERP Implementation", "Cloud Services"]

# Función para generar fechas aleatorias dentro de un rango específico
def random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Generar datos
data = []

for i in range(2000):
    contract_id = f"C-{1001 + i}"
    vendor = random.choice(vendors)
    category = random.choice(categories)
    approved_amount = random.randint(50000, 1000000)
    invoiced_amount = random.randint(int(approved_amount * 0.8), int(approved_amount * 1.2))
    status = random.choice(["Active", "Active (Overrun)", "Closed"])
    start_date = random_date(datetime(2023, 1, 1), datetime(2024, 1, 1)).date()
    end_date = random_date(datetime(2024, 1, 1), datetime(2025, 1, 1)).date()
    
    data.append([contract_id, vendor, category, approved_amount, invoiced_amount, status, start_date, end_date])

# Crear DataFrame
df = pd.DataFrame(data, columns=["Contract_ID", "Vendor", "Category", "Approved_Amount_USD", 
                                 "Invoiced_Amount_USD", "Contract_Status", "Start_Date", "End_Date"])

# Guardar en un archivo CSV
csv_file_path = "contracts_data.csv"
df.to_csv(csv_file_path, index=False)

print("Archivo CSV generado: contracts_data.csv")
