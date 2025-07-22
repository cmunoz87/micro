
import streamlit as st
from PIL import Image

# --- Cargar imágenes ---
logo_hospital = Image.open("Captura_de_pantalla_2025-07-22_a_las_3.25.30.png")
logo_frascos = Image.open("Captura_de_pantalla_2025-07-22_a_las_3.25.05.png")

# --- Mostrar los logos ---
col1, col2 = st.columns([1, 1])
with col1:
    st.image(logo_hospital, use_container_width=True)
with col2:
    st.image(logo_frascos, use_container_width=True)

# --- Título ---
st.markdown("<h1 style='text-align: center; color: #003366;'>Calculadora de Volumen para Frascos BacT/ALERT Plus</h1>", unsafe_allow_html=True)

# --- Mensaje de ayuda ---
st.markdown("""
<p style='background-color: #f0f8ff; padding: 10px; border-left: 5px solid #003366;'>
<strong>📌 Peso mínimo por tipo de frasco:</strong><br>
🍼 Pediátrico PLUS: 61,6 g<br>
🌬️ Aeróbico PLUS: 62,0 g<br>
🌑 Anaeróbico PLUS: 71,5 g
</p>
""", unsafe_allow_html=True)

# --- Datos desde la imagen ---
volumenes = [i * 0.5 for i in range(31)]  # 0 a 15 ml

pediatric_plus = [61.6, 62.1, 62.6, 63.1, 63.1, 63.6, 64.1, 64.6, 65.1, 65.6, 66.1, 66.6, 67.6,
                  68.1, 68.6, 69.1, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.5, 74.5, 75.0,
                  75.5, 76.0, 76.5, 77.0, 77.0]
aerobic_plus = [62.0, 62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.5,
                69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.5, 75.0, 75.5,
                76.0, 76.5, 77.0, 77.5, 77.0]
anaerobic_plus = [71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5, 75.0, 75.5, 76.0, 76.5, 77.5, 78.0,
                  78.5, 79.0, 79.5, 80.0, 80.5, 81.0, 81.5, 82.0, 82.5, 83.0, 83.5, 84.0, 84.5,
                  85.0, 85.5, 86.0, 86.5, 86.5]

tablas = {
    "Pediátrico PLUS": pediatric_plus,
    "Aeróbico PLUS": aerobic_plus,
    "Anaeróbico PLUS": anaerobic_plus
}

# --- Entrada de datos ---
frasco = st.selectbox("Selecciona el tipo de frasco", list(tablas.keys()))
peso = st.number_input("Ingresa el peso del frasco (en gramos)", min_value=60.0, max_value=90.0, step=0.1)

# --- Función para estimar volumen ---
def estimar_volumen(peso, pesos_tabla):
    diferencias = [abs(p - peso) for p in pesos_tabla]
    idx = diferencias.index(min(diferencias))
    return volumenes[idx], pesos_tabla[idx]

# --- Resultado ---
if peso:
    volumen, peso_ref = estimar_volumen(peso, tablas[frasco])
    st.markdown(f"<h3 style='color: green;'>Volumen estimado: {volumen:.1f} ml</h3>", unsafe_allow_html=True)
    st.caption(f"Peso de referencia más cercano en tabla: {peso_ref} g")
