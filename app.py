import streamlit as st
import pickle
import pandas as pd
import os

# 1. Configuración de la página (Aesthetic)
st.set_page_config(page_title="Movie Recommender AI", page_icon="🎬", layout="centered")

st.title("🎬 Sistema de Recomendación de Películas")
st.markdown("""
Esta aplicación utiliza **Filtrado Colaborativo** con la **Correlación de Spearman** para encontrar patrones de preferencia entre usuarios.
""")

# 2. Cargar datos con manejo de rutas robusto
@st.cache_resource 
def cargar_datos():
    # Usamos os.path para que funcione igual en Windows (local) y Linux (Streamlit Cloud)
    base_path = os.path.dirname(__file__)
    ruta_archivo = os.path.join(base_path, 'data', 'user_movie_matrix.pkl')
    
    try:
        with open(ruta_archivo, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        st.error(f"⚠️ No se encontró el archivo en: {ruta_archivo}")
        return None

user_movie_matrix = cargar_datos()

# 3. Interfaz de usuario mejorada
if user_movie_matrix is not None:
    st.sidebar.header("⚙️ Configuración")
    
    # Buscador con autocompletado
    pelicula_seleccionada = st.sidebar.selectbox(
        "Busca una película:",
        user_movie_matrix.columns
    )

    num_recomendaciones = st.sidebar.slider("¿Cuántas recomendaciones quieres?", 5, 15, 10)

    if st.button("🚀 Generar Recomendaciones"):
        with st.spinner('Analizando patrones de calificación...'):
            # Lógica de Spearman
            ratings_pelicula = user_movie_matrix[pelicula_seleccionada]
            similares = user_movie_matrix.corrwith(ratings_pelicula, method='spearman')
            
            # Limpieza y ordenado
            df_recom = pd.DataFrame(similares, columns=['Similitud'])
            df_recom.dropna(inplace=True)
            
            # Resultados finales: quitamos la película buscada y formateamos
            recomendaciones = df_recom.sort_values('Similitud', ascending=False).head(num_recomendaciones + 1).iloc[1:]
            
            # TOQUE PRO: Redondear a 2 decimales para que se vea limpio
            recomendaciones['Similitud'] = recomendaciones['Similitud'].map(lambda n: f"{n:.2f}")

            st.subheader(f"Basado en tu interés por '{pelicula_seleccionada}':")
            
            # Mostramos la tabla con un estilo más limpio
            st.table(recomendaciones)
            
            st.success("Análisis completado con éxito.")
else:
    st.warning("Por favor, asegúrate de que el archivo 'user_movie_matrix.pkl' esté en la carpeta 'data'.")