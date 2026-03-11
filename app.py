import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import base64
from pathlib import Path

# ==================== CONFIGURACIÓN ====================
st.set_page_config(
    page_title="BOSS Structures - Análisis Estructural Profesional",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== FUNCIÓN PARA CARGAR IMAGEN ====================
def get_image_base64(image_path):
    """Convierte una imagen a base64 para incrustarla en HTML"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Intentar cargar la imagen del logo
logo_path = Path("logo.png")
logo_base64 = get_image_base64(logo_path)

# ==================== CSS TEMA OSCURO MEJORADO ====================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .stApp { 
        background-color: #0E1117 !important; 
    }
    
    /* ===== TEXTOS PRINCIPALES EN BLANCO ===== */
    .main h1 {
        color: #FFFFFF !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 700 !important;
    }
    
    .main h2, .main h3, .main h4, .main h5, .main h6,
    .main p, .main span, .main li,
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] h1,
    div[data-testid="stMarkdownContainer"] h2,
    div[data-testid="stMarkdownContainer"] h3,
    div[data-testid="stMarkdownContainer"] h4 {
        color: #FFFFFF !important;
        font-family: 'Poppins', sans-serif;
    }
    
    /* ===== ELEMENTOS ESPECÍFICOS SOLICITADOS ===== */
    .main h2:contains("📐 Predimensionamiento Rápido de Elementos"),
    .main h3:contains("Vigas"),
    .main h3:contains("Columnas"),
    .main h3:contains("Losas y Aligerados") {
        color: #FFFFFF !important;
    }
    
    .main h2:contains("🔲 Evaluación y Diseño de Zapatas Aisladas"),
    .main h3:contains("📥 Datos de entrada"),
    .main h3:contains("📊 Resultados de verificación") {
        color: #FFFFFF !important;
    }
    
    .main h2:contains("🏛️ Análisis y Diseño de Columnas y Placas"),
    .main h3:contains("📥 Datos de la columna"),
    .main h4:contains("Dimensiones"),
    .main h4:contains("Cargas"),
    .main h4:contains("Acero"),
    .main h3:contains("📊 Resultados") {
        color: #FFFFFF !important;
    }
    
    .main h2:contains("➖ Análisis y Diseño de Vigas"),
    .main h3:contains("📥 Datos de la viga"),
    .main h4:contains("Geometría"),
    .main h4:contains("Cargas"),
    .main h4:contains("Acero"),
    .main h3:contains("📊 Resultados") {
        color: #FFFFFF !important;
    }
    
    .main h2:contains("🧱 Análisis de Losas y Prelosas"),
    .main h3:contains("📥 Datos de la losa"),
    .main h4:contains("Cargas"),
    .main h3:contains("📊 Resultados"),
    .main strong:contains("Acero por temperatura") {
        color: #FFFFFF !important;
    }
    
    .main h2:contains("🤖 Consultor Técnico Estructural"),
    .main h3:contains("📌 Cuantía mínima (E.060)"),
    .main h3:contains("📌 Límites de deriva"),
    .main h3:contains("📌 Zapatas (E.060)") {
        color: #FFFFFF !important;
    }
    
    /* Inputs y selects - Mantener fondo intacto */
    div[data-baseweb="input"], 
    div[data-baseweb="base-input"], 
    div[data-baseweb="select"] > div { 
        background-color: #262730 !important; 
        border: 1px solid #4A4A4A !important; 
        border-radius: 8px !important;
        transition: all 0.3s ease;
    }
    
    div[data-baseweb="input"]:hover, 
    div[data-baseweb="select"] > div:hover {
        border-color: #FF4B4B !important;
    }
    
    /* Inputs numéricos */
    div[data-baseweb="input"] input { 
        color: #FFFFFF !important; 
        -webkit-text-fill-color: #FFFFFF !important; 
        caret-color: #FF4B4B !important; 
        font-weight: 500 !important; 
        background-color: transparent !important; 
    }
    
    /* ===== ESTILOS PARA SELECT BOX ===== */
    /* ATAQUE DIRECTO AL TEXTO DEL VALOR SELECCIONADO */
    
    /* Selector para el elemento singleValue (el texto seleccionado) */
    div[data-baseweb="select"] div[class*="singleValue"],
    div[data-baseweb="select"] div[class*="SingleValue"],
    div[data-baseweb="select"] span[class*="singleValue"],
    div[data-baseweb="select"] span[class*="SingleValue"],
    div[data-baseweb="select"] [class*="singleValue"],
    div[data-baseweb="select"] [class*="SingleValue"] {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        opacity: 1 !important;
        fill: #FFFFFF !important;
        text-shadow: none !important;
    }
    
    /* Selector para cualquier span que contenga texto dentro del select */
    div[data-baseweb="select"] span:not([class*="indicator"]):not([class*="dropdown"]):not(svg *) {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        opacity: 1 !important;
    }
    
    /* Selector para el div contenedor del texto */
    div[data-baseweb="select"] div[role="combobox"] div:first-of-type {
        color: #FFFFFF !important;
    }
    
    /* ESTILOS PARA SELECT DISABLED - MÁS ESPECÍFICOS AÚN */
    div[data-baseweb="select"][aria-disabled="true"] div[class*="singleValue"],
    div[data-baseweb="select"][aria-disabled="true"] [class*="singleValue"],
    div[data-baseweb="select"][disabled] div[class*="singleValue"],
    div[data-baseweb="select"][disabled] [class*="singleValue"],
    .stSelectbox[aria-disabled="true"] div[class*="singleValue"],
    .stSelectbox[disabled] div[class*="singleValue"],
    .stSelectbox[aria-disabled="true"] [class*="singleValue"],
    .stSelectbox[disabled] [class*="singleValue"] {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        opacity: 1 !important;
    }
    
    /* Forzar spans dentro de selects disabled */
    div[data-baseweb="select"][aria-disabled="true"] span,
    div[data-baseweb="select"][disabled] span,
    .stSelectbox[aria-disabled="true"] span,
    .stSelectbox[disabled] span {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        opacity: 1 !important;
    }
    
    /* Eliminar cualquier opacidad heredada */
    div[data-baseweb="select"][aria-disabled="true"],
    div[data-baseweb="select"][disabled],
    .stSelectbox[aria-disabled="true"],
    .stSelectbox[disabled] {
        opacity: 1 !important;
    }
    
    /* Forzar el color del texto en el elemento que realmente lo muestra */
    div[data-baseweb="select"] div:not([class*="indicator"]):not([class*="dropdown"]) {
        color: #FFFFFF !important;
    }
    
    /* Flecha del select */
    div[data-baseweb="select"] svg {
        fill: #FFFFFF !important;
        opacity: 1 !important;
    }
    
    /* ===== ESTILOS PARA EXPANDERS ===== */
    div[data-testid="stExpander"] {
        background-color: #262730 !important;
        border: 1px solid #4A4A4A !important;
        border-radius: 12px !important;
        margin: 1rem 0 !important;
    }
    
    /* Título del expander - siempre blanco */
    div[data-testid="stExpander"] details summary span,
    div[data-testid="stExpander"] details summary p {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    
    /* Expander abierto - contenido interno NEGRO (excepto selects) */
    div[data-testid="stExpander"] details[open] .stMarkdown p,
    div[data-testid="stExpander"] details[open] div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stExpander"] details[open] .element-container p,
    div[data-testid="stExpander"] details[open] label p {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }
    
    /* EXCEPCIÓN: Los selects dentro del expander mantienen texto blanco (incluyendo disabled) */
    div[data-testid="stExpander"] details[open] div[data-baseweb="select"] [class*="singleValue"],
    div[data-testid="stExpander"] details[open] div[data-baseweb="select"] [class*="SingleValue"],
    div[data-testid="stExpander"] details[open] div[data-baseweb="select"] [class*="single-value"] {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }
    
           /* ===== FORZAR TEXTOS ESPECÍFICOS A BLANCO ===== */
    /* Estos textos deben ser blancos SÍ O SÍ */
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Área tributaria de columna"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Evaluando con"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Capacidad portante"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("qₐ"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Ancho B"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Largo L"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Peralte h"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Diámetro de acero"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Espaciamiento"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("@"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Recubrimiento"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Lado de columna"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Otro lado") {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        background-color: transparent !important;
    }
    
    /* RESTAURAR color negro para los títulos de los expanders si es necesario */
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Cargas y suelo"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Dimensiones de zapata"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Acero de refuerzo"),
    div[data-testid="stExpander"] details[open] .stMarkdown p:contains("Columna soportada") {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }
            
    /* Botones */
    .stButton > button {
        background: linear-gradient(135deg, #FF4B4B 0%, #FF6B6B 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(255,75,75,0.3) !important;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] { 
        background-color: #1E1E1E !important;
        border-right: 1px solid #333 !important;
    }
    
    section[data-testid="stSidebar"] * { 
        color: #FFFFFF !important; 
    }
    
    /* Logo personalizado */
    .sidebar-logo { 
        text-align: center; 
        padding: 1.5rem 1rem; 
        background: linear-gradient(135deg, rgba(255,75,75,0.1) 0%, rgba(255,107,107,0.05) 100%);
        border-radius: 12px; 
        margin-bottom: 2rem; 
        border: 1px solid rgba(255,75,75,0.2);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    .sidebar-logo img {
        max-width: 100%;
        height: auto;
        max-height: 100px;
        object-fit: contain;
    }
    
    .sidebar-logo h2 { 
        font-weight: 800; 
        font-size: 2.5rem; 
        margin: 0; 
        color: #FF4B4B !important;
        text-shadow: 0 2px 10px rgba(255,75,75,0.3);
        line-height: 1.2;
    }
    
    .sidebar-logo .subtitle { 
        font-size: 0.9rem; 
        letter-spacing: 3px; 
        text-transform: uppercase; 
        margin: 0; 
        color: #A0AEC0 !important; 
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] { 
        background-color: transparent !important; 
        border-bottom: 2px solid #333;
        gap: 2rem;
        padding: 0 1rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 0.5rem 1rem !important;
    }
    
    .stTabs [data-baseweb="tab"] p { 
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover p {
        color: #FF4B4B !important;
    }
    
    .stTabs [aria-selected="true"] { 
        background-color: transparent !important; 
        border-bottom: 3px solid #FF4B4B !important;
    }
    
    .stTabs [aria-selected="true"] p { 
        color: #FFFFFF !important; 
        -webkit-text-fill-color: #FFFFFF !important; 
    }
    
    /* Metrics */
    div[data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: #FF4B4B !important;
    }
    
    div[data-testid="stMetricLabel"] p {
        font-size: 0.9rem !important;
        color: #FFFFFF !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    /* Cards para resultados */
    .result-card {
        background: linear-gradient(135deg, #1E1E1E 0%, #262730 100%);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #FF4B4B;
    }
    
    .result-card h4 {
        color: #FF4B4B !important;
        margin-top: 0 !important;
    }
    
    .result-card p {
        color: #FFFFFF !important;
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    
    .badge-success {
        background: rgba(0, 200, 0, 0.2);
        color: #00FF00 !important;
        border: 1px solid #00FF00;
    }
    
    .badge-error {
        background: rgba(255, 0, 0, 0.2);
        color: #FF4B4B !important;
        border: 1px solid #FF4B4B;
    }
    
    .badge-warning {
        background: rgba(255, 165, 0, 0.2);
        color: #FFA500 !important;
        border: 1px solid #FFA500;
    }
    
    .badge-info {
        background: rgba(255, 75, 75, 0.1);
        color: #FF4B4B !important;
        border: 1px solid #FF4B4B;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #FFFFFF !important;
        font-size: 0.85rem;
        border-top: 1px solid #333;
        margin-top: 3rem;
    }
    
    /* Fallback */
    .main .element-container p,
    .main .stMarkdown p,
    .main .stText p,
    .main div:not([data-baseweb]) p {
        color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)


# ==================== FUNCIONES DE UTILIDAD ====================
def area_acero(diametro):
    areas = {
        "1/4\"": 0.32, "3/8\"": 0.71, "1/2\"": 1.29,
        "5/8\"": 2.00, "3/4\"": 2.84, "1\"": 5.10
    }
    return areas.get(diametro, 0)

def validar_numero_positivo(valor, nombre):
    if valor <= 0:
        st.error(f"❌ {nombre} debe ser mayor a cero")
        return False
    return True

def verificar_acero_minimo(b, h, tipo_elemento="viga", fpc=210, fy=4200):
    if tipo_elemento == "viga":
        d = 0.9 * h
        As_min = 0.24 * (fpc**0.5) / fy * b * 100 * d * 100
    elif tipo_elemento == "columna":
        Ag = b * 100 * h * 100
        As_min = 0.01 * Ag
    else:
        As_min = 0.0018 * b * 100 * h * 100
    return As_min

def verificar_punzonamiento(P_u, b_col, t_col, B_zap, L_zap, h_zap, fpc):
    d = h_zap * 100 - 7.5
    b0 = 2 * (b_col + d + t_col + d)
    vc = 0.53 * (fpc**0.5)
    Vc = vc * b0 * d / 1000
    q_actuante = P_u / (B_zap * L_zap)
    area_punzonamiento = (B_zap * L_zap) - ((b_col/100 + h_zap) * (t_col/100 + h_zap))
    Vu = q_actuante * area_punzonamiento
    return {
        "Vu": Vu,
        "Vc": Vc,
        "cumple": Vu <= Vc * 0.85,
    }

def predimensionar_viga(luz, tipo="principal"):
    if luz <= 0:
        return None
    if tipo == "principal":
        h = luz / 10
    elif tipo == "secundaria":
        h = luz / 12
    else:
        h = luz / 11
    b_min = h / 3
    b_max = h / 2
    return {
        "h_sugerido": round(h * 20) / 20,
        "b_min": round(b_min * 20) / 20,
        "b_max": round(b_max * 20) / 20,
    }

def predimensionar_columna(P_servicio, fpc=210, tipo="central"):
    if P_servicio <= 0:
        return None
    if tipo == "central":
        coeficiente = 0.30
    elif tipo == "borde":
        coeficiente = 0.25
    elif tipo == "esquinada":
        coeficiente = 0.20
    else:
        coeficiente = 0.25
    P_servicio_kg = P_servicio * 1000
    Ac_necesaria = P_servicio_kg / (coeficiente * fpc)
    lado = Ac_necesaria**0.5
    lado_redondeado = round(lado / 5) * 5
    return {
        "Ac_necesaria": Ac_necesaria,
        "lado_sugerido": lado_redondeado,
    }

def calcular_espesor_losa(L, tipo="aligerada"):
    if L <= 0:
        return None
    if tipo == "aligerada":
        h = L * 100 / 25
        if L <= 5:
            h = max(h, 17)
        else:
            h = max(h, 20)
    elif tipo == "maciza":
        h = L * 100 / 30
        h = max(h, 12)
    elif tipo == "prelosa":
        h = 5 + (L * 100 / 35)
    else:
        h = L * 100 / 28
    return round(h * 4) / 4

# ==================== BASES DE DATOS ====================
materiales_concreto = {
    "210": {"fpc": 210, "nombre": "f'c = 210 kg/cm²", "uso": "Viviendas hasta 5 pisos"},
    "280": {"fpc": 280, "nombre": "f'c = 280 kg/cm²", "uso": "Edificios medios (5-10 pisos)"},
    "350": {"fpc": 350, "nombre": "f'c = 350 kg/cm²", "uso": "Edificios altos (10-20 pisos)"}
}

aceros = {
    "Grado 60": {"fy": 4200, "nombre": "Grado 60 (fy=4200 kg/cm²)"},
    "Grado 40": {"fy": 2800, "nombre": "Grado 40 (fy=2800 kg/cm²)"}
}

tipos_suelo = {
    "S1 (Roca dura)": {"S": 1.0, "qa_tipica": 4.0},
    "S2 (Suelo intermedio)": {"S": 1.2, "qa_tipica": 2.0},
    "S3 (Suelo blando)": {"S": 1.4, "qa_tipica": 1.0},
}

# ==================== ESTADO GLOBAL ====================
if 'zona' not in st.session_state: st.session_state['zona'] = 0.45
if 'S' not in st.session_state: st.session_state['S'] = 1.2
if 'tipo_suelo' not in st.session_state: st.session_state['tipo_suelo'] = "S2 (Suelo intermedio)"
if 'R0' not in st.session_state: st.session_state['R0'] = 8.0
if 'irregular' not in st.session_state: st.session_state['irregular'] = False
if 'num_pisos' not in st.session_state: st.session_state['num_pisos'] = 5
if 'h_piso' not in st.session_state: st.session_state['h_piso'] = 2.8
if 'fpc' not in st.session_state: st.session_state['fpc'] = 210
if 'fy' not in st.session_state: st.session_state['fy'] = 4200

# ==================== BARRA LATERAL ====================
with st.sidebar:
    if logo_base64:
        st.markdown(f"""
        <div class="sidebar-logo">
            <img src="data:image/png;base64,{logo_base64}" alt="BOSS - Building Operator System">
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="sidebar-logo">
            <h2>BOSS</h2>
            <p class="subtitle">Structures</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 🏢 Parámetros Globales del Proyecto")
    
    st.markdown("#### Materiales")
    fpc_seleccionado = st.selectbox(
        "Resistencia del concreto (f'c)",
        list(materiales_concreto.keys()),
        format_func=lambda x: materiales_concreto[x]["nombre"],
        index=0
    )
    st.session_state['fpc'] = int(fpc_seleccionado)
    
    acero_seleccionado = st.selectbox(
        "Tipo de acero",
        list(aceros.keys()),
        format_func=lambda x: aceros[x]["nombre"],
        index=0
    )
    st.session_state['fy'] = aceros[acero_seleccionado]["fy"]
    
    st.divider()
    
    st.markdown("#### Parámetros Sísmicos (E.030)")
    tipo_suelo_seleccionado = st.selectbox(
        "Tipo de Suelo",
        list(tipos_suelo.keys()),
        index=1
    )
    st.session_state['tipo_suelo'] = tipo_suelo_seleccionado
    st.session_state['S'] = tipos_suelo[tipo_suelo_seleccionado]["S"]
    
    zona_sismica = st.selectbox(
        "Zona Sísmica (Z)",
        [0.45, 0.35, 0.25, 0.10],
        format_func=lambda x: f"Zona {4 - [0.45,0.35,0.25,0.10].index(x)} (Z={x})",
        index=0
    )
    st.session_state['zona'] = zona_sismica
    
    st.session_state['R0'] = st.number_input(
        "Coef. Básico de Reducción (R0)",
        value=st.session_state['R0'],
        step=1.0
    )
    
    st.session_state['irregular'] = st.checkbox(
        "Edificación Irregular",
        value=st.session_state['irregular']
    )
    
    st.divider()
    
    st.markdown("#### Geometría del Edificio")
    st.session_state['num_pisos'] = st.number_input(
        "Número de Pisos",
        value=st.session_state['num_pisos'],
        step=1,
        min_value=1
    )
    
    st.session_state['h_piso'] = st.number_input(
        "Altura de piso (m)",
        value=st.session_state['h_piso'],
        step=0.1,
        min_value=2.0,
        max_value=5.0
    )
    
    st.divider()
    st.markdown(f"""
    <div style="background: #262730; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
        <p style="color: #FFFFFF; font-size: 0.8rem; margin: 0;">
        📋 Resumen del Proyecto<br>
        • {st.session_state['num_pisos']} pisos | H total: {st.session_state['num_pisos'] * st.session_state['h_piso']:.1f}m<br>
        • f'c = {st.session_state['fpc']} kg/cm² | fy = {st.session_state['fy']} kg/cm²<br>
        • Suelo: {st.session_state['tipo_suelo']}<br>
        • Z= {st.session_state['zona']} | S= {st.session_state['S']} | R= {st.session_state['R0']}
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== ÁREA PRINCIPAL ====================
st.title("🏗️ Sistema de Análisis y Predimensionamiento Estructural")
st.markdown("""
<div style="background: #262730; padding: 1rem; border-radius: 8px; margin-bottom: 2rem;">
    <p style="margin: 0; color: #FFFFFF; font-weight: 500;">
        Verificación normativa según <strong>E.030 (Diseño Sismorresistente)</strong>, 
        <strong>E.050 (Suelos y Cimentaciones)</strong> y <strong>E.060 (Concreto Armado)</strong>
    </p>
</div>
""", unsafe_allow_html=True)

tab_predim, tab_zapatas, tab_columnas, tab_vigas, tab_losas, tab_consultas = st.tabs([
    "📐 Predimensionamiento", 
    "🔲 Zapatas", 
    "🏛️ Columnas/Placas", 
    "➖ Vigas", 
    "🧱 Losas y Prelosas", 
    "🤖 Consultor Técnico"
])

# -----------------------------------------------------------------------------
# PESTAÑA 1: PREDIMENSIONAMIENTO
# -----------------------------------------------------------------------------
with tab_predim:
    st.header("📐 Predimensionamiento Rápido de Elementos")
    st.markdown("Estimación inicial de dimensiones según norma E.060")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Vigas")
        luz_viga = st.number_input("Luz libre de viga (m)", value=5.0, step=0.5, min_value=2.0, key="luz_pred_viga")
        tipo_viga = st.selectbox("Tipo de viga", ["principal", "secundaria"], key="tipo_pred_viga")
        
        if st.button("Dimensionar Viga", key="btn_pred_viga"):
            resultado = predimensionar_viga(luz_viga, tipo_viga)
            if resultado:
                st.markdown(f"""
                <div class="result-card">
                    <h4>📏 Dimensiones sugeridas</h4>
                    <p><strong>Peralte (h):</strong> {resultado['h_sugerido']:.2f} m</p>
                    <p><strong>Ancho mínimo (b):</strong> {resultado['b_min']:.2f} m</p>
                    <p><strong>Ancho máximo (b):</strong> {resultado['b_max']:.2f} m</p>
                    <p style="color: #FFFFFF;">Sugerencia: 25x{resultado['h_sugerido']*100:.0f}cm, 30x{resultado['h_sugerido']*100:.0f}cm</p>
                </div>
                """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("Columnas")
        P_col = st.number_input("Carga de servicio por piso (Ton)", value=100.0, step=10.0, key="carga_pred_col")
        tipo_col = st.selectbox("Tipo de columna", ["central", "borde", "esquinada"], key="tipo_pred_col")
        
        if st.button("Dimensionar Columna", key="btn_pred_col"):
            resultado = predimensionar_columna(P_col, st.session_state['fpc'], tipo_col)
            if resultado:
                st.markdown(f"""
                <div class="result-card">
                    <h4>📏 Dimensiones sugeridas</h4>
                    <p><strong>Área de concreto necesaria:</strong> {resultado['Ac_necesaria']:.0f} cm²</p>
                    <p><strong>Lado sugerido:</strong> {resultado['lado_sugerido']:.0f} cm</p>
                    <p style="color: #FFFFFF;">Considerando ρ ≈ 1-2% de cuantía</p>
                </div>
                """, unsafe_allow_html=True)
    
    st.divider()
    
    st.subheader("Losas y Aligerados")
    col3, col4 = st.columns(2)
    
    with col3:
        luz_losa = st.number_input("Luz mayor de losa (m)", value=4.5, step=0.5, key="luz_pred_losa")
        tipo_losa = st.selectbox("Tipo de losa", ["aligerada", "maciza", "prelosa"], key="tipo_pred_losa")
        
        if st.button("Calcular Espesor", key="btn_pred_losa"):
            espesor = calcular_espesor_losa(luz_losa, tipo_losa)
            if espesor:
                st.markdown(f"""
                <div class="result-card">
                    <h4>📏 Espesor recomendado</h4>
                    <p><strong>h = {espesor:.1f} cm</strong></p>
                    <p style="color: #FFFFFF;">Para losa {tipo_losa} con luz de {luz_losa}m</p>
                </div>
                """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# PESTAÑA 2: ZAPATAS
# -----------------------------------------------------------------------------
with tab_zapatas:
    st.header("🔲 Evaluación y Diseño de Zapatas Aisladas")
    st.markdown("Verifica si las dimensiones y el acero de la zapata soportan la edificación según E.060")
    
    qa_sugerido = tipos_suelo[st.session_state['tipo_suelo']]["qa_tipica"]
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📥 Datos de entrada")
        
        with st.expander("Cargas y suelo", expanded=True):
            area_trib = st.number_input("Área tributaria de columna (m²)", value=16.0, step=1.0, min_value=1.0)
            st.info(f"📊 Evaluando con {st.session_state['num_pisos']} pisos")
            qa_suelo = st.number_input("Capacidad portante qₐ (kg/cm²)", value=qa_sugerido, step=0.1, min_value=0.1)
        
        with st.expander("Dimensiones de zapata", expanded=True):
            B_zap = st.number_input("Ancho B (m)", value=1.8, step=0.1, min_value=0.5)
            L_zap = st.number_input("Largo L (m)", value=1.8, step=0.1, min_value=0.5)
            h_zap = st.number_input("Peralte h (m)", value=0.6, step=0.05, min_value=0.3)
        
        with st.expander("Acero de refuerzo", expanded=True):
            diametro_zap = st.selectbox("Diámetro de acero", ["1/2\"", "5/8\"", "3/4\"", "1\""], index=1)
            espaciado_zap = st.number_input("Espaciamiento @ (cm)", value=20, step=5, min_value=5)
            recubrimiento = st.number_input("Recubrimiento (cm)", value=7.5, step=0.5, min_value=5.0)
        
        with st.expander("Columna soportada", expanded=False):
            lado_col = st.number_input("Lado de columna (cm)", value=40, step=5, min_value=15)
            t_col = st.number_input("Otro lado (cm)", value=40, step=5, min_value=15)
    
    with col2:
        st.subheader("📊 Resultados de verificación")
        
        if st.button("🔍 EVALUAR ZAPATA", type="primary", use_container_width=True):
            if not all([validar_numero_positivo(x, "dimensión") for x in [B_zap, L_zap, h_zap, area_trib, qa_suelo]]):
                st.stop()
            
            peso_por_piso = 1.0
            if area_trib <= 10:
                peso_por_piso = 0.9
            elif area_trib <= 20:
                peso_por_piso = 1.0
            else:
                peso_por_piso = 1.1
            
            P_axial = area_trib * peso_por_piso * st.session_state['num_pisos']
            volumen_zap = B_zap * L_zap * h_zap
            peso_zap = volumen_zap * 2.4
            P_total = P_axial + peso_zap
            Area_zap = B_zap * L_zap
            presion = P_total / Area_zap
            factor_seguridad = qa_suelo / presion if presion > 0 else 0
            
            As_colocado = area_acero(diametro_zap) * (100 / espaciado_zap)
            As_min = verificar_acero_minimo(1.0, h_zap, "losa", st.session_state['fpc'], st.session_state['fy'])
            
            ld_requerida = 0.06 * area_acero(diametro_zap) * st.session_state['fy'] / (st.session_state['fpc']**0.5)
            ld_disponible = (B_zap * 100 - lado_col) / 2 - recubrimiento
            
            P_u = 1.5 * P_total
            punzonamiento = verificar_punzonamiento(P_u, lado_col, t_col, B_zap, L_zap, h_zap, st.session_state['fpc'])
            
            st.markdown(f"""
            <div class="result-card">
                <h4>Cargas</h4>
                <p><strong>Carga axial:</strong> {P_axial:.1f} Ton</p>
                <p><strong>Peso zapata:</strong> {peso_zap:.1f} Ton</p>
                <p><strong>Carga total:</strong> {P_total:.1f} Ton</p>
            </div>
            """, unsafe_allow_html=True)
            
            if presion <= qa_suelo:
                st.success(f"✅ **PRESIÓN ADECUADA** - {presion:.2f} kg/cm² ≤ {qa_suelo:.2f} kg/cm²")
            else:
                st.error(f"❌ **PRESIÓN EXCESIVA** - {presion:.2f} kg/cm² > {qa_suelo:.2f} kg/cm²")
            
            if h_zap >= 0.40:
                st.success("✅ **PERALTE ADECUADO** (≥ 0.40m)")
            else:
                st.error("❌ **PERALTE INSUFICIENTE** - Mínimo 0.40m")
            
            if As_colocado >= As_min:
                st.success(f"✅ **ACERO MÍNIMO CUMPLE** ({As_colocado:.2f} cm²/m ≥ {As_min:.2f} cm²/m)")
            else:
                st.error(f"❌ **ACERO INSUFICIENTE** - Requerido: {As_min:.2f} cm²/m")
            
            if ld_disponible >= ld_requerida:
                st.success(f"✅ **LONGITUD DE DESARROLLO ADECUADA**")
            else:
                st.warning(f"⚠️ **LONGITUD INSUFICIENTE** - Requiere {ld_requerida:.0f}cm")
            
            if punzonamiento["cumple"]:
                st.success(f"✅ **PUNZONAMIENTO OK**")
            else:
                st.error(f"❌ **FALLA POR PUNZONAMIENTO** - Aumentar peralte h")

# -----------------------------------------------------------------------------
# PESTAÑA 3: COLUMNAS
# -----------------------------------------------------------------------------
with tab_columnas:
    st.header("🏛️ Análisis y Diseño de Columnas y Placas")
    st.markdown("Verificación de columnas según norma E.060")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📥 Datos de la columna")
        
        tipo_columna = st.selectbox(
            "Tipo de elemento",
            ["Columna central", "Columna de borde", "Columna esquinada", "Placa (muro de corte)"]
        )
        
        st.markdown("#### Dimensiones")
        b_col = st.number_input("Ancho b (cm)", value=30, step=5, min_value=15)
        h_col = st.number_input("Peralte h (cm)", value=40, step=5, min_value=15)
        
        st.markdown("#### Cargas")
        P_u = st.number_input("Carga axial última Pu (Ton)", value=100.0, step=10.0)
        
        st.markdown("#### Acero")
        num_barras = st.number_input("Número de barras", value=6, step=2, min_value=4)
        diametro_col = st.selectbox("Diámetro de barras", ["1/2\"", "5/8\"", "3/4\"", "1\""], index=1, key="diam_col")
    
    with col2:
        st.subheader("📊 Resultados")
        
        fpc = st.session_state['fpc']
        fy = st.session_state['fy']
        
        if st.button("🔍 VERIFICAR COLUMNA", type="primary", use_container_width=True):
            Ag = b_col * h_col
            As_colocado = num_barras * area_acero(diametro_col)
            cuantia = (As_colocado / Ag) * 100
            
            k = 1.0
            Lu = st.session_state['h_piso'] * 100
            r = 0.3 * max(b_col, h_col)
            esbeltez = k * Lu / r
            
            Pn = 0.85 * fpc * (Ag - As_colocado) + fy * As_colocado
            Pn_max = 0.80 * Pn
            phi = 0.70
            phiPn = phi * Pn_max / 1000
            
            m1, m2, m3 = st.columns(3)
            m1.metric("Área bruta Ag", f"{Ag:.0f} cm²")
            m2.metric("Acero colocado As", f"{As_colocado:.2f} cm²")
            m3.metric("Cuantía ρ", f"{cuantia:.2f}%")
            
            st.markdown(f"""
            <div class="result-card">
                <h4>Capacidad axial</h4>
                <p><strong>Resistencia de diseño φPn:</strong> {phiPn:.1f} Ton</p>
                <p><strong>Demanda Pu:</strong> {P_u:.1f} Ton</p>
            </div>
            """, unsafe_allow_html=True)
            
            if cuantia < 1.0:
                st.error(f"❌ **CUANTÍA MÍNIMA NO CUMPLE**: {cuantia:.2f}% < 1%")
            elif cuantia > 6.0:
                st.error(f"❌ **CUANTÍA MÁXIMA EXCEDIDA**: {cuantia:.2f}% > 6%")
            else:
                st.success(f"✅ **CUANTÍA ADECUADA**: {cuantia:.2f}%")
            
            if phiPn >= P_u:
                st.success(f"✅ **RESISTENCIA SUFICIENTE**")
            else:
                st.error(f"❌ **RESISTENCIA INSUFICIENTE**")
            
            if esbeltez <= 22:
                st.success(f"✅ **COLUMNA CORTA** (λ={esbeltez:.1f})")
            elif esbeltez <= 50:
                st.warning(f"⚠️ **COLUMNA INTERMEDIA** (λ={esbeltez:.1f})")
            else:
                st.error(f"❌ **COLUMNA ESBELTA** (λ={esbeltez:.1f})")

# -----------------------------------------------------------------------------
# PESTAÑA 4: VIGAS
# -----------------------------------------------------------------------------
with tab_vigas:
    st.header("➖ Análisis y Diseño de Vigas")
    st.markdown("Verificación de vigas de concreto armado según E.060")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📥 Datos de la viga")
        
        st.markdown("#### Geometría")
        b_viga = st.number_input("Ancho b (cm)", value=25, step=5, min_value=15)
        h_viga = st.number_input("Peralte h (cm)", value=50, step=5, min_value=20)
        L_viga = st.number_input("Luz libre (m)", value=5.0, step=0.5, min_value=2.0)
        
        st.markdown("#### Cargas")
        w_D = st.number_input("Carga muerta wD (Ton/m)", value=2.0, step=0.2)
        w_L = st.number_input("Carga viva wL (Ton/m)", value=1.0, step=0.2)
        
        st.markdown("#### Acero")
        num_sup = st.number_input("Barras superiores", value=3, step=1, min_value=2)
        num_inf = st.number_input("Barras inferiores", value=2, step=1, min_value=2)
        diametro_viga = st.selectbox("Diámetro de barras", ["1/2\"", "5/8\"", "3/4\"", "1\""], index=2, key="diam_viga")
    
    with col2:
        st.subheader("📊 Resultados")
        
        fpc = st.session_state['fpc']
        fy = st.session_state['fy']
        
        if st.button("🔍 VERIFICAR VIGA", type="primary", use_container_width=True):
            d = h_viga - 6
            As_sup = num_sup * area_acero(diametro_viga)
            As_inf = num_inf * area_acero(diametro_viga)
            
            As_min = verificar_acero_minimo(b_viga/100, h_viga/100, "viga", fpc, fy)
            
            w_u = 1.4 * w_D + 1.7 * w_L
            Mu = w_u * L_viga**2 / 8
            
            a = As_sup * fy / (0.85 * fpc * b_viga)
            Mn = As_sup * fy * (d - a/2) / 100000
            phiMn = 0.9 * Mn
            
            relacion_as = As_sup / As_inf if As_inf > 0 else 0
            
            col_m1, col_m2, col_m3 = st.columns(3)
            col_m1.metric("Peralte efectivo d", f"{d:.0f} cm")
            col_m2.metric("As superior", f"{As_sup:.2f} cm²")
            col_m3.metric("As inferior", f"{As_inf:.2f} cm²")
            
            h_min = L_viga * 100 / 10
            if h_viga >= h_min:
                st.success(f"✅ **PERALTE ADECUADO** ({h_viga:.0f} cm ≥ {h_min:.0f} cm)")
            else:
                st.error(f"❌ **PERALTE INSUFICIENTE** (mínimo {h_min:.0f} cm)")
            
            if As_sup >= As_min and As_inf >= As_min:
                st.success(f"✅ **ACERO MÍNIMO CUMPLE** (≥ {As_min:.2f} cm²)")
            else:
                st.error(f"❌ **ACERO MÍNIMO NO CUMPLE**")
            
            if phiMn >= Mu:
                st.success(f"✅ **RESISTENCIA SUFICIENTE**")
            else:
                st.error(f"❌ **RESISTENCIA INSUFICIENTE**")
            
            if relacion_as >= 0.5:
                st.success(f"✅ **RELACIÓN AS SUP/INF ADECUADA** ({relacion_as:.2f})")
            else:
                st.warning(f"⚠️ **RELACIÓN AS SUP/INF BAJA** ({relacion_as:.2f})")

# -----------------------------------------------------------------------------
# PESTAÑA 5: LOSAS
# -----------------------------------------------------------------------------
with tab_losas:
    st.header("🧱 Análisis de Losas y Prelosas")
    st.markdown("Verificación de espesores y acero en losas según E.060")
    
    tipo_losa_analisis = st.selectbox(
        "Tipo de losa a analizar",
        ["Losa aligerada", "Losa maciza", "Prelosa (vigueta + bovedilla)"]
    )
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📥 Datos de la losa")
        
        L_losa = st.number_input("Luz mayor (m)", value=4.5, step=0.5, min_value=2.0)
        
        if tipo_losa_analisis == "Losa aligerada":
            espesor_losa = st.selectbox("Espesor de losa (cm)", [17, 20, 25, 30], index=1)
        elif tipo_losa_analisis == "Losa maciza":
            espesor_losa = st.number_input("Espesor de losa (cm)", value=15, step=1, min_value=10)
        else:
            espesor_total = st.number_input("Espesor total losa (cm)", value=20, step=1)
            espesor_losa = espesor_total
        
        st.markdown("#### Cargas")
        s_c = st.number_input("Sobrecarga (kg/m²)", value=250, step=50)
        acabados = st.number_input("Acabados (kg/m²)", value=100, step=25)
    
    with col2:
        st.subheader("📊 Resultados")
        
        if st.button("🔍 VERIFICAR LOSA", type="primary", use_container_width=True):
            
            if tipo_losa_analisis == "Losa aligerada":
                h_min = calcular_espesor_losa(L_losa, "aligerada")
            elif tipo_losa_analisis == "Losa maciza":
                h_min = calcular_espesor_losa(L_losa, "maciza")
            else:
                h_min = calcular_espesor_losa(L_losa, "prelosa")
            
            col_r1, col_r2 = st.columns(2)
            with col_r1:
                st.metric("Espesor mínimo normativo", f"{h_min:.1f} cm")
            with col_r2:
                st.metric("Espesor ingresado", f"{espesor_losa:.1f} cm")
            
            if espesor_losa >= h_min:
                st.success(f"✅ **ESPESOR ADECUADO**")
            else:
                st.error(f"❌ **ESPESOR INSUFICIENTE** (necesita mínimo {h_min:.1f} cm)")
            
            if tipo_losa_analisis == "Losa aligerada":
                if espesor_losa <= 17:
                    peso_propio = 280
                elif espesor_losa <= 20:
                    peso_propio = 300
                elif espesor_losa <= 25:
                    peso_propio = 350
                else:
                    peso_propio = 420
            elif tipo_losa_analisis == "Losa maciza":
                peso_propio = espesor_losa * 24
            else:
                peso_propio = 280
            
            carga_total = peso_propio + acabados + s_c
            st.metric("Carga total por m²", f"{carga_total:.0f} kg/m²")
            
            st.divider()
            st.markdown("#### Acero por temperatura")
            
            As_temp = 0.0018 * 100 * espesor_losa
            espaciamiento_14 = area_acero("1/4\"") * 100 / As_temp
            espaciamiento_38 = area_acero("3/8\"") * 100 / As_temp
            
            st.markdown(f"""
            <div style="background: #262730; padding: 1rem; border-radius: 8px;">
                <p style="color: #FFFFFF;"><strong>Acero requerido:</strong> {As_temp:.2f} cm²/m</p>
                <p style="color: #FFFFFF;"><strong>Opción 1:</strong> Ø 1/4" @ {espaciamiento_14:.0f} cm</p>
                <p style="color: #FFFFFF;"><strong>Opción 2:</strong> Ø 3/8" @ {espaciamiento_38:.0f} cm</p>
            </div>
            """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# PESTAÑA 6: CONSULTAS
# -----------------------------------------------------------------------------
with tab_consultas:
    st.header("🤖 Consultor Técnico Estructural")
    st.markdown("Responde consultas técnicas sobre normas E.030, E.050 y E.060")
    
    consulta = st.text_area(
        "Escribe tu consulta técnica",
        placeholder="Ej: ¿Cuál es la cuantía mínima para columnas? ¿Cómo verifico derivas?",
        height=100
    )
    
    preguntas_frecuentes = st.selectbox(
        "Preguntas frecuentes",
        ["Selecciona una pregunta", 
         "Cuantía mínima en columnas",
         "Límites de deriva E.030",
         "Peralte mínimo de zapatas",
         "Acero en losas"]
    )
    
    if preguntas_frecuentes != "Selecciona una pregunta":
        consulta = preguntas_frecuentes
    
    if st.button("🔍 Consultar", type="primary", use_container_width=True):
        consulta_lower = consulta.lower()
        
        respuestas = {
            "cuantía mínima": """
            ### 📌 Cuantía mínima (E.060)
            - **Columnas:** 1% del área bruta
            - **Vigas:** 0.24√f'c/fy × b × d
            - **Losas:** 0.18% del área
            """,
            "deriva": """
            ### 📌 Límites de deriva (E.030)
            - Concreto armado: **0.007**
            - Muros estructurales: **0.005**
            - Albañilería: **0.005**
            """,
            "zapata": """
            ### 📌 Zapatas (E.060)
            - Peralte mínimo: **40 cm**
            - Acero mínimo: **0.18%** de b×h
            """,
        }
        
        for key, value in respuestas.items():
            if key in consulta_lower:
                st.markdown(f"""
                <div class="result-card">
                    {value}
                </div>
                """, unsafe_allow_html=True)
                break