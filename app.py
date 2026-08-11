import streamlit as st
import pandas as pd
import joblib
import base64


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="SENTINELA",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# FUNÇÃO PARA IMAGEM
# ============================================================

def imagem_base64(caminho):
    try:
        with open(caminho, "rb") as arquivo:
            return base64.b64encode(arquivo.read()).decode()
    except:
        return None


logo = imagem_base64("logo-sentinela.")
logos = imagem_base64("logo-cetam.png")


# ============================================================
# CSS — Estilo Suave e Moderno
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ==========================================================
   RESET E FUNDO SUAVE
   ========================================================== */
.stApp {
    background: linear-gradient(160deg, #e0f2fe 0%, #dbeafe 40%, #bfdbfe 100%);
    font-family: 'Inter', sans-serif;
}

/* Ocultar elementos padrão do Streamlit */
#MainMenu, header, footer, [data-testid="stToolbar"] {
    visibility: hidden;
    display: none !important;
}

/* ==========================================================
   CONTAINER PRINCIPAL
   ========================================================== */
.block-container {
    max-width: 720px !important;
    padding-top: 20px !important;
    padding-bottom: 40px !important;
}

/* ==========================================================
   CABEÇALHO
   ========================================================== */
.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.logo-sentinela {
    width: 180px;
    height: auto;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.08));
}

.logo-institucional {
    width: 260px;
    height: auto;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.06));
}

/* ==========================================================
   TÍTULOS
   ========================================================== */
.title {
    text-align: center;
    color: #1e3a5f;
    font-size: 26px;
    font-weight: 800;
    margin-top: 4px;
    margin-bottom: 6px;
    letter-spacing: -0.3px;
}

.subtitle {
    text-align: center;
    color: #475569;
    font-size: 14px;
    font-weight: 500;
    margin-bottom: 24px;
}

/* ==========================================================
   CARDS — Estilo suave da referência
   ========================================================== */
.card {
    background: rgba(255, 255, 255, 0.92) !important;
    backdrop-filter: blur(12px);
    border-radius: 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.8) !important;
    box-shadow: 0 4px 20px rgba(30, 58, 95, 0.06),
                0 1px 3px rgba(30, 58, 95, 0.04) !important;
    padding: 28px !important;
    margin-bottom: 20px !important;
}

/* Forçar estilo nos containers do Streamlit */
[data-testid="stVerticalBlockBorderWrapper"] > div {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* ==========================================================
   TÍTULO DO CARD
   ========================================================== */
.section-title {
    color: #1e293b;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.section-description {
    color: #64748b;
    font-size: 13px;
    margin-bottom: 22px;
    font-weight: 400;
}

/* ==========================================================
   DIVISÓRIAS SUAVES
   ========================================================== */
hr.soft {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
    margin: 16px 0;
}

/* ==========================================================
   LABELS
   ========================================================== */
label, .stNumberInput label, .stSelectbox label {
    color: #334155 !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    margin-bottom: 6px !important;
}

/* ==========================================================
   INPUTS — Estilo clean e arredondado
   ========================================================== */
div[data-baseweb="input"] {
    border: 1.5px solid #cbd5e1 !important;
    border-radius: 12px !important;
    background: #ffffff !important;
    transition: all 0.2s ease !important;
}

div[data-baseweb="input"]:focus-within {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important;
}

div[data-baseweb="select"] {
    border: 1.5px solid #cbd5e1 !important;
    border-radius: 12px !important;
    background: #ffffff !important;
}

div[data-baseweb="select"]:focus-within {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important;
}

/* ==========================================================
   BOTÃO — Estilo primário suave
   ========================================================== */
.stButton > button {
    width: 100%;
    height: 52px;
    margin-top: 16px;
    border: none;
    border-radius: 14px;
    background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
    color: white;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.3px;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.25);
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: pointer;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.35);
    transform: translateY(-2px);
}

.stButton > button:active {
    transform: translateY(0);
}

/* ==========================================================
   RESULTADO — Card flutuante
   ========================================================== */
.result-box {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 28px;
    margin-top: 20px;
    box-shadow: 0 8px 30px rgba(30, 58, 95, 0.08),
                0 2px 8px rgba(30, 58, 95, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.9);
    animation: fadeInUp 0.5s ease-out;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}

.result-title {
    color: #1e293b;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 20px;
}

/* ==========================================================
   STATUS NORMAL — Verde suave
   ========================================================== */
.normal-box {
    background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
    border: 1px solid #86efac;
    border-radius: 16px;
    padding: 20px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
}

.normal-icon {
    width: 40px;
    height: 40px;
    background: #22c55e;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 20px;
    flex-shrink: 0;
    box-shadow: 0 4px 10px rgba(34, 197, 94, 0.25);
}

.normal-title {
    color: #14532d;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 4px;
}

.normal-text {
    color: #166534;
    font-size: 13px;
    line-height: 1.5;
    font-weight: 500;
}

/* ==========================================================
   STATUS FALHA — Vermelho suave
   ========================================================== */
.failure-box {
    background: linear-gradient(135deg, #fef2f2 0%, #fff1f2 100%);
    border: 1px solid #fca5a5;
    border-radius: 16px;
    padding: 20px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
}

.failure-icon {
    width: 40px;
    height: 40px;
    background: #ef4444;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 20px;
    flex-shrink: 0;
    box-shadow: 0 4px 10px rgba(239, 68, 68, 0.25);
}

.failure-title {
    color: #7f1d1d;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 4px;
}

.failure-text {
    color: #991b1b;
    font-size: 13px;
    line-height: 1.5;
    font-weight: 500;
}

/* ==========================================================
   PROBABILIDADE — Destaque circular suave
   ========================================================== */
.probability-container {
    text-align: center;
    padding: 20px;
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    border-radius: 20px;
    border: 1px solid #e2e8f0;
}

.probability-label {
    color: #64748b;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 8px;
}

.probability-value {
    color: #0f172a;
    font-size: 36px;
    font-weight: 800;
    letter-spacing: -1px;
}

.probability-value.low { color: #15803d; }
.probability-value.medium { color: #b45309; }
.probability-value.high { color: #b91c1c; }

/* ==========================================================
   BARRA DE PROGRESSO
   ========================================================== */
.stProgress > div > div {
    background: linear-gradient(90deg, #3b82f6, #60a5fa) !important;
    border-radius: 10px !important;
}

.stProgress > div {
    background: #e2e8f0 !important;
    border-radius: 10px !important;
    height: 10px !important;
}

/* ==========================================================
   ALERTAS — TEXTO PRETO PARA MÁXIMA LEGIBILIDADE
   ========================================================== */
.stAlert {
    border-radius: 14px !important;
    border: 1.5px solid !important;
    padding: 16px 20px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    color: #0f172a !important;
}

.stAlert p, .stAlert span, .stAlert div {
    color: #0f172a !important;
}

/* Info — azul suave */
div[data-testid="stAlertContainer"][data-kind="info"] {
    background: #dbeafe !important;
    border-color: #93c5fd !important;
}

/* Warning — amarelo suave */
div[data-testid="stAlertContainer"][data-kind="warning"] {
    background: #fef3c7 !important;
    border-color: #fcd34d !important;
}

/* Error — vermelho suave */
div[data-testid="stAlertContainer"][data-kind="error"] {
    background: #fee2e2 !important;
    border-color: #fca5a5 !important;
}

/* ==========================================================
   EXPANDER
   ========================================================== */
.streamlit-expanderHeader {
    font-size: 13px !important;
    font-weight: 600 !important;
    color: #334155 !important;
    border-radius: 12px !important;
}

.streamlit-expanderContent {
    background: #f8fafc !important;
    border-radius: 0 0 12px 12px !important;
    border: 1px solid #e2e8f0 !important;
    border-top: none !important;
}

/* ==========================================================
   DATAFRAME
   ========================================================== */
[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    overflow: hidden !important;
    border: 1px solid #e2e8f0 !important;
}

/* ==========================================================
   RODAPÉ
   ========================================================== */
.footer {
    text-align: center;
    color: #64748b;
    font-size: 11px;
    font-weight: 500;
    margin-top: 30px;
    padding-bottom: 20px;
}

/* ==========================================================
   RESPONSIVIDADE
   ========================================================== */
@media (max-width: 700px) {
    .logo-sentinela { width: 140px; }
    .logo-institucional { width: 180px; }
    .title { font-size: 20px; }
    .card { padding: 20px !important; }
    .result-box { padding: 20px; }
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# CABEÇALHO
# ============================================================

col_logo, col_institucional = st.columns([1, 1])

with col_logo:
    if logo:
        st.markdown(
            f'<img src="data:image/png;base64,{logo}" class="logo-sentinela">',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div style="color:#1e3a5f;font-size:26px;font-weight:800;">🛡️ SENTINELA</div>',
            unsafe_allow_html=True
        )

with col_institucional:
    if logos:
        st.markdown(
            f'<div style="text-align:right;"><img src="data:image/png;base64,{logos}" class="logo-institucional"></div>',
            unsafe_allow_html=True
        )


# ============================================================
# TÍTULO
# ============================================================

st.markdown(
    '<div class="title">Sistema Inteligente de Previsão de Falhas</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Informe os parâmetros do equipamento para estimar o risco de falha</div>',
    unsafe_allow_html=True
)


# ============================================================
# CARD PRINCIPAL
# ============================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">⚙️ Dados do equipamento</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">Preencha os parâmetros operacionais abaixo</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------------
# TIPO
# --------------------------------------------------------

tipo = st.selectbox(
    "Tipo da máquina",
    ["L", "M", "H"],
    help="L = Leve | M = Média | H = Pesada"
)

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

# --------------------------------------------------------
# TEMPERATURAS
# --------------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    temperatura_ar = st.number_input(
        "🌡️ Temperatura do ar (K)",
        min_value=250.0,
        max_value=350.0,
        value=298.0,
        step=0.1,
        format="%.1f"
    )

with col2:
    temperatura_processo = st.number_input(
        "🌡️ Temperatura do processo (K)",
        min_value=250.0,
        max_value=400.0,
        value=308.0,
        step=0.1,
        format="%.1f"
    )

# --------------------------------------------------------
# RPM + TORQUE
# --------------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    rpm = st.number_input(
        "↻ Velocidade de rotação (RPM)",
        min_value=0,
        max_value=5000,
        value=1500,
        step=10
    )

with col2:
    torque = st.number_input(
        "⚙️ Torque (Nm)",
        min_value=0.0,
        max_value=100.0,
        value=40.0,
        step=0.1,
        format="%.1f"
    )

# --------------------------------------------------------
# DESGASTE
# --------------------------------------------------------

desgaste = st.number_input(
    "🔧 Desgaste da ferramenta (min)",
    min_value=0,
    max_value=300,
    value=100,
    step=1
)

# --------------------------------------------------------
# BOTÃO
# --------------------------------------------------------

analisar = st.button(
    "🔍  Analisar equipamento",
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# MODELO
# ============================================================

if analisar:

    try:
        modelo = joblib.load("modelo.pkl")
    except Exception as e:
        st.error("Erro ao carregar o modelo `modelo.pkl`. Verifique se o arquivo está no diretório do app.")
        st.stop()

    # --------------------------------------------------------
    # TIPO
    # --------------------------------------------------------

    tipo_numerico = {"H": 0, "L": 1, "M": 2}

    # --------------------------------------------------------
    # DADOS
    # --------------------------------------------------------

    dados = pd.DataFrame({
        "Type": [tipo_numerico[tipo]],
        "Air temperature [K]": [temperatura_ar],
        "Process temperature [K]": [temperatura_processo],
        "Rotational speed [rpm]": [rpm],
        "Torque [Nm]": [torque],
        "Tool wear [min]": [desgaste]
    })

    # --------------------------------------------------------
    # PREVISÃO
    # --------------------------------------------------------

    previsao = modelo.predict(dados)
    probabilidades = modelo.predict_proba(dados)

    classes = list(modelo.classes_)

    if 1 in classes:
        indice_falha = classes.index(1)
        probabilidade_falha = probabilidades[0][indice_falha]
    else:
        probabilidade_falha = 0

    percentual = probabilidade_falha * 100

    # Define classe de cor para a probabilidade
    prob_class = "low" if percentual < 20 else ("medium" if percentual < 50 else "high")

    # ========================================================
    # RESULTADO
    # ========================================================

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.markdown(
        '<div class="result-title">📊 Resultado da análise</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # STATUS
    # --------------------------------------------------------

    if previsao[0] == 0:
        st.markdown("""
            <div class="normal-box">
                <div class="normal-icon">✓</div>
                <div>
                    <div class="normal-title">Equipamento operando normalmente</div>
                    <div class="normal-text">O modelo não identificou condições compatíveis com falha para os parâmetros informados.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="failure-box">
                <div class="failure-icon">!</div>
                <div>
                    <div class="failure-title">Risco de falha detectado</div>
                    <div class="failure-text">O modelo identificou condições compatíveis com uma possível falha no equipamento.</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # PROBABILIDADE
    # --------------------------------------------------------

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(
            f"""
            <div class="probability-container">
                <div class="probability-label">Probabilidade estimada de falha</div>
                <div class="probability-value {prob_class}">{percentual:.2f}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.write(f"**Nível de risco: {percentual:.2f}%**")
        st.progress(min(max(probabilidade_falha, 0.0), 1.0))

    # --------------------------------------------------------
    # INTERPRETAÇÃO
    # --------------------------------------------------------

    if percentual < 20:
        st.info("O risco estimado é **baixo**. As condições informadas apresentam baixa probabilidade de falha segundo o modelo.")
    elif percentual < 50:
        st.warning("O risco estimado é **moderado**. Recomenda-se acompanhar as condições operacionais do equipamento.")
    else:
        st.error("O risco estimado é **elevado**. Recomenda-se realizar uma inspeção técnica no equipamento.")

    # --------------------------------------------------------
    # DADOS
    # --------------------------------------------------------

    with st.expander("🔎 Visualizar dados utilizados na análise"):
        dados_visualizacao = dados.copy()
        dados_visualizacao["Type"] = tipo
        st.dataframe(dados_visualizacao, use_container_width=True, hide_index=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# RODAPÉ
# ============================================================

st.markdown(
    '<div class="footer">SENTINELA • Sistema Inteligente de Previsão de Falhas em Equipamentos Elétricos</div>',
    unsafe_allow_html=True
)