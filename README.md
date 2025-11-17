# Mini Proyecto — Análisis de Contratos y Horas (Target Process)

Descripción
---
Este mini proyecto contiene un notebook (`main.ipynb`) que realiza análisis exploratorio y de riesgo sobre dos fuentes de datos:

- Contratos / procurement (`SMART_GEP_Procurement.csv`)
- Registros de horas por empleado / proyecto (`TARGET_PROCESS_Hours.csv`)

El objetivo es identificar overrun en contratos, evaluar % de ejecución por contrato, detectar riesgos por sub-ejecución y analizar consumo interno de horas por proyecto.

Estructura del repositorio
---
```
./
  main.ipynb
  README.md
  data/
    SMART_GEP_Procurement.csv
    TARGET_PROCESS_Hours.csv
  generadores/
    generador_SMART_GEP_Procurement.py
    generadorT_ARGET_PROCESS_Hours.py
  .venv/  (opcional — entorno virtual local)
```

Archivos clave
---
- `main.ipynb`: Notebook principal con análisis y visualizaciones.
- `data/SMART_GEP_Procurement.csv`: Datos de contratos (approved, invoiced, fechas, vendor, etc.).
- `data/TARGET_PROCESS_Hours.csv`: Registros sintéticos de horas por employee/project/week.
- `generadores/`: scripts para generar datasets sintéticos si quiere recrear o ampliar los CSVs.

Requisitos (sugeridos)
---
- Python 3.8+ (se recomienda usar un virtual environment)
- pandas
- numpy
- matplotlib
- jupyter
- jinja2 (opcional, para usar `.style` en DataFrames en el notebook)

Instalación (Windows PowerShell)
---
1. Abrir PowerShell en la carpeta del proyecto (`C:\Users\luisd\OneDrive\Desktop\SMART GEP`) y crear/activar un venv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias mínimas:

```powershell
python -m pip install --upgrade pip
python -m pip install pandas numpy matplotlib jupyter jinja2
```

Nota: si prefiere usar un archivo `requirements.txt`, cree uno con los paquetes listados y ejecute `python -m pip install -r requirements.txt`.

Cómo ejecutar
---
1. Con el venv activado, lanzar Jupyter Notebook:

```powershell
python -m jupyter notebook
```

2. Abrir `main.ipynb` en el navegador y ejecutar las celdas.

Regenerar / generar datos de ejemplo
---
Los scripts en `generadores/` pueden crear datasets sintéticos. Desde la carpeta raíz (con el venv activado):

```powershell
python .\generadores\generadorT_ARGET_PROCESS_Hours.py
python .\generadores\generador_SMART_GEP_Procurement.py
```

Advertencias y notas rápidas
---
- Algunas celdas del notebook usan el accesor `.style` de pandas para colorear o formatear tablas; esto requiere `jinja2` en el entorno. Si ve el error "The '.style' accessor requires jinja2", instale `jinja2` como se muestra arriba y reinicie el kernel.
- Los generadores pueden escribir archivos con nombres distintos (por ejemplo `contracts_data.csv`) — revise el nombre de salida y mueva/renombre el archivo a `data/SMART_GEP_Procurement.csv` o `data/TARGET_PROCESS_Hours.csv` para que el notebook los lea automáticamente.

Siguientes pasos sugeridos
---
- Añadir un `requirements.txt` al repo para reproducción exacta de dependencias.
- Agregar un pequeño script `run_all.py` para ejecutar checks y exportar tablas/resúmenes automáticamente.

Contacto
---
Si querés que lo deje en forma de repo listo para compartir (con `requirements.txt`, tests simples o archivos de salida), dime qué prefieres y lo preparo.
