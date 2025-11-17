import pandas as pd
import random
from datetime import datetime, timedelta

# Lista de proyectos, tipos de tareas y tarifas por hora
projects = ["Migration2024", "SAPUpgrade", "HelpDeskOps", "CloudMigration", "DigitalTransformation"]
task_types = ["Development", "QA", "Design", "Support", "Testing", "Research"]
hourly_rates = [30, 35, 40, 45, 50, 55, 60]

# Generar datos
data = []

for i in range(2000):
    employee_id = f"E{random.randint(1, 10):03d}"
    project = random.choice(projects)
    task_type = random.choice(task_types)
    hours_logged = random.randint(5, 50)  # Horas entre 5 y 50
    hourly_rate = random.choice(hourly_rates)
    cost_usd = hours_logged * hourly_rate
    week = random.randint(1, 52)  # Semana entre 1 y 52
    
    data.append([employee_id, project, task_type, hours_logged, hourly_rate, cost_usd, week])

# Crear DataFrame
df = pd.DataFrame(data, columns=["Employee_ID", "Project", "Task_Type", "Hours_Logged", 
                                 "Hourly_Rate", "Cost_USD", "Week"])

# Guardar en un archivo CSV
csv_file_path = "TARGET_PROCESS_Hours.csv"
df.to_csv(csv_file_path, index=False)
    
print("Archivo CSV generado: TARGET_PROCESS_Hours.csv")