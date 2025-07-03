# 🏃 Evaluador Deportivo

Este proyecto permite registrar, analizar y comparar el rendimiento físico de un grupo de alumnos o jugadores. A través del cálculo de velocidad e IMC (Índice de Masa Corporal), el programa brinda estadísticas útiles para evaluar el estado físico de los participantes.

## 📌 Funcionalidades principales

✅ Carga de datos de alumnos de dos formas:
- Manualmente desde consola.
- Automáticamente desde un archivo `.csv`.

✅ Cálculo automático de:
- IMC por alumno.
- Velocidad promedio (distancia/tiempo).
- Promedio general de velocidad.

✅ Reportes y análisis:
- Detección de posibles casos de sobrepeso (según OMS).
- Identificación del alumno más rápido.
- Top 3 de mejores velocidades.
- Filtro de alumnos por edad mínima.
- Resumen general con IMC y velocidad de todos los alumnos.

---

## 🖥️ Cómo ejecutar el programa

1. **Asegurate de tener Python instalado.**  
   Requiere Python 3.6 o superior.

2. **Instalá la librería `pandas` si no la tenés (para leer archivos CSV):**

   ```bash
   pip install pandas

## Si elegís importar los datos desde un archivo .csv, el formato debe ser el siguiente (separado por ;):
nombre;peso;altura;edad;distancia;tiempo  
Juan;70;1.75;20;100;12  
Ana;60;1.65;22;120;15  
Pedro;80;1.80;25;200;20  

## 🗃️ Archivo incluido:
**corredores.csv** (opcional): Archivo de ejemplo para cargar jugadores desde CSV.
