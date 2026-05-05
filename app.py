import streamlit as st

st.set_page_config(page_title="Aï4 Engine", layout="wide")
st.markdown("<style>.stApp {background-color: #000000; color: #00FFFF;}</style>", unsafe_allow_html=True)

st.title("🏛️ Aï4 : ANALYSEUR DE RÉSULTATS")

# 3 Zones Historique
st.subheader("1. Historique (3 Journées)")
h_col = st.columns(3)
with h_col[0]: st.file_uploader("N-2", type=['png', 'jpg'], key="n2")
with h_col[1]: st.file_uploader("N-1", type=['png', 'jpg'], key="n1")
with h_col[2]: st.file_uploader("N (Dernière)", type=['png', 'jpg'], key="n0")

# 2 Zones Affiches
st.subheader("2. Prochaines Affiches (Anglais)")
a_col = st.columns(2)
with a_col[0]: st.file_uploader("Affiche 1", type=['png', 'jpg'], key="p1")
with a_col[1]: st.file_uploader("Affiche 2", type=['png', 'jpg'], key="p2")

if st.button("🚀 CALCULER SCORE EXACT"):
    st.success("Analyse en cours...")                                                                                                            st.sidebar.write("**Langue :** Anglais (EN)")
