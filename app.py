import streamlit as st

st.set_page_config(page_title="ALPHA-V ENGINE", layout="wide")

# Style CSS
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FFFF; }
    h1, h2, h3 { color: #00FFFF !important; font-family: 'Courier New', monospace; }
    .box-bleu { border: 2px solid #00FFFF; padding: 15px; background-color: #050505; border-radius: 10px; }
    .texte-or { color: #FFD700 !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Groupes d'équipes
FORCE_GROUP = ["Algeria", "Nigeria", "Morocco", "Cameroon", "Ghana", "Tunisia", "South Africa", "Zambia"]
DEBT_GROUP = ["Senegal", "Mali", "Ivory Coast", "DRC", "Guinea", "Uganda", "Angola", "Benin"]
ROOT_GROUP = ["Egypt", "Burkina Faso", "Gabon", "Togo", "Cape Verde", "Kenya", "Tanzania", "Zimbabwe"]
ALL_TEAMS = sorted(FORCE_GROUP + DEBT_GROUP + ROOT_GROUP)

if 'historique' not in st.session_state:
    st.session_state.historique = {eq: [] for eq in ALL_TEAMS}

def calculer_pronostic(equipe, journee):
    if journee <= 15: return "OBSERVATION", "Attente stabilisation.", "SAUT"
    histo = st.session_state.historique.get(equipe, [])
    if equipe in DEBT_GROUP:
        if any(sum(x) == 0 for x in histo[-3:]): return "DETTE ACTIVE", "Purge imminente.", "2-0 / 2-1"
    if equipe in FORCE_GROUP:
        if sum(sum(x) for x in histo[-3:]) >= 7: return "SURCHAUFFE", "Blocage imminent.", "0-0 / 1-0"
    return "NEUTRE", "Aucune anomalie.", "SAUT"

st.title("🏛️ ALPHA-V : SYSTÈME PRÉDICTIF")

with st.sidebar:
    st.header("⚙️ CONFIG")
    num_j = st.number_input("Journée", 1, 46, 15)
    if st.button("RAZ Historique"): st.session_state.historique = {eq: [] for eq in ALL_TEAMS}

st.markdown("#### 🕒 SAISIE DES RÉSULTATS")
c1, c2, c3 = st.columns(3)
with c1:
    eq_sel = st.selectbox("Équipe", ALL_TEAMS)
with c2:
    sc_sel = st.text_input("Score (ex: 1-0)", "0-0")
with c3:
    if st.button("ENREGISTRER"):
        try:
            st.session_state.historique[eq_sel].append([int(x) for x in sc_sel.split('-')])
            st.success(f"{eq_sel} mis à jour.")
        except: st.error("Format invalide.")

st.markdown("#### 🔮 VERDICT")
eq_p = st.selectbox("Analyser une affiche", ALL_TEAMS)
et, inf, pr = calculer_pronostic(eq_p, num_j)

st.markdown(f'<div class="box-bleu">', unsafe_allow_html=True)
st.write(f"**Équipe :** {eq_p} | **État :** {et}")
if pr != "SAUT":
    st.markdown(f'<p class="texte-or">PRONOSTIC : {pr}</p>', unsafe_allow_html=True)
else:
    st.markdown('<p style="color: #FF003F;">ACTION : SAUT</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
