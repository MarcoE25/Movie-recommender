🎬 Movie Recommender AI: Collaborative Filtering & Memory Optimization
Este proyecto desarrolla un motor de recomendación de películas basado en Filtrado Colaborativo, optimizado para el despliegue en infraestructuras de recursos limitados. El sistema utiliza la Correlación de Spearman para identificar patrones de preferencia entre usuarios, priorizando la precisión estadística sobre datos ordinales.

🧠 Justificación Técnica
Como parte de mi enfoque en Ciencia de Datos y optimización algorítmica, este proyecto aborda dos retos fundamentales:

1. Rigor Estadístico: Spearman vs. Pearson
A diferencia de los enfoques tradicionales que utilizan la correlación de Pearson, este modelo implementa la Correlación de Spearman. Dado que los ratings de usuarios (escala 1-5) son datos ordinales, Spearman es superior al evaluar la relación monótona entre los rangos de preferencia, ignorando sesgos de magnitud y normalidad en las calificaciones.
 
2. Ingeniería de Datos y Optimización de Memoria
Uno de los mayores logros de este proyecto fue la gestión de la eficiencia computacional:

Reducción de Huella de Memoria: La matriz de afinidad original ocupaba ~600 MB.

Quantization (Cuantización): Mediante la conversión de tipos de datos de float64 a int8, se logró una reducción del 87% en el uso de RAM, dejando el artefacto final en 73 MB.

Thresholding: Se aplicaron filtros de significancia estadística (mínimo de 1,000 ratings por película y 200 por usuario) para eliminar el ruido y mejorar la densidad de la matriz.

🛠️ Tecnologías Utilizadas
Lenguaje: Python

Análisis de Datos: Pandas, NumPy, SciPy (Spearman Rank Correlation)

Deployment: Streamlit Cloud

Serialización: Pickle

🚀 Cómo ejecutarlo localmente
Clonar el repositorio:

Bash

git clone https://github.com/tu-usuario/movie-recommender.git
cd movie-recommender
Instalar dependencias:

Bash

pip install -r requirements.txt
Lanzar la aplicación:

Bash

streamlit run app.py
📂 Estructura del Proyecto
app.py: Interfaz de usuario y lógica de recomendación en tiempo real.

data/: Contiene la matriz de afinidad cuantizada (user_movie_matrix.pkl).

notebooks/: Documentación del proceso de ETL, análisis exploratorio y validación de modelos.

Desarrollado por Marco Elenes Maestro en Ciencias Computacionales | Aspirante a Científico de Datos
