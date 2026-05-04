import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Aï4 - ENGINE V3", layout="wide")

# Style visuel Aï4 (Noir, Cyan, Or)
st.markdown("""
    <style>
        .stApp { background-color: #000000; color: #00FFFF; }
            .box-verdict { border: 2px solid #FFD700; padding: 20px; background-color: #050505; border-radius: 10px; margin-bottom: 20px; }
                .instruction { color: #00FFFF; font-style: italic; font-size: 0.9em; border-left: 3px solid #FFD700; padding-left: 10px; }
                    .score-exact { color: #FFD700; font-size: 1.8em; font-weight: bold; }
                        .section-title { color: #FFFFFF; background-color: #008B8B; padding: 5px 15px; border-radius: 5px; }
                            </style>
                            """, unsafe_allow_html=True)

                            st.title("🏛️ Aï4 : SYSTÈME D'ANALYSE D'IMAGES")

                            # --- SECTION 1 : HISTORIQUE DES RÉSULTATS (3 JOURNÉES) ---
                            st.markdown("<h3 class='section-title'>1. HISTORIQUE : Captures des Résultats Passés</h3>", unsafe_allow_html=True)
                            col_h1, col_h2, col_h3 = st.columns(3)

                            with col_h1:
                                img_n2 = st.file_uploader("📸 Journée N-2 (Résultats)", type=['jpg', 'png', 'jpeg'], key="n2")
                                with col_h2:
                                    img_n1 = st.file_uploader("📸 Journée N-1 (Résultats)", type=['jpg', 'png', 'jpeg'], key="n1")
                                    with col_h3:
                                        img_n0 = st.file_uploader("📸 Journée N (Derniers Résultats)", type=['jpg', 'png', 'jpeg'], key="n0")

                                        st.markdown("---")

                                        # --- SECTION 2 : ANALYSE DES PROCHAINES AFFICHES ---
                                        st.markdown("<h3 class='section-title'>2. PRÉVISIONS : Captures des Prochaines Affiches</h3>", unsafe_allow_html=True)
                                        col_p1, col_p2 = st.columns(2)

                                        with col_p1:
                                            img_next1 = st.file_uploader("📸 Capture Affiche n°1 (À venir)", type=['jpg', 'png', 'jpeg'], key="p1")
                                            with col_p2:
                                                img_next2 = st.file_uploader("📸 Capture Affiche n°2 (À venir)", type=['jpg', 'png', 'jpeg'], key="p2")

                                                # --- LOGIQUE PRÉDICTIVE ---
                                                def calculer_score_exact():
                                                    # Cette fonction sera liée au moteur OCR plus tard
                                                        return "2 - 1", "1 - 0"

                                                        # --- SECTION 3 : VERDICT Aï4 ---
                                                        st.markdown("---")
                                                        if st.button("🚀 GÉNÉRER LES PRONOSTICS OR"):
                                                            if not (img_n2 and img_n1 and img_n0 and img_next1 and img_next2):
                                                                    st.error("ERREUR : Il manque des captures d'écran pour valider l'analyse mathématique.")
                                                                        else:
                                                                                st.balloons()
                                                                                        sc1, sc2 = calculer_score_exact()
                                                                                                
                                                                                                        # ZONE DE RÉSULTAT 1
                                                                                                                st.markdown('<div class="box-verdict">', unsafe_allow_html=True)
                                                                                                                        st.write("### 🏁 PREMIÈRE ANALYSE (Affiche n°1)")
                                                                                                                                st.markdown(f"SCORE EXACT PRÉDIT : <span class='score-exact'>{sc1}</span>", unsafe_allow_html=True)
                                                                                                                                        st.markdown("<p class='instruction'>⚠️ SI CE SCORE EST VALIDÉ : Le flux de but confirme la rupture d'équilibre. Préparez la mise pour l'affiche suivante.</p>", unsafe_allow_html=True)
                                                                                                                                                st.markdown('</div>', unsafe_allow_html=True)

                                                                                                                                                        # ZONE DE RÉSULTAT 2
                                                                                                                                                                st.markdown('<div class="box-verdict">', unsafe_allow_html=True)
                                                                                                                                                                        st.write("### 🏁 DEUXIÈME ANALYSE (Affiche n°2)")
                                                                                                                                                                                st.markdown(f"SCORE EXACT PRÉDIT : <span class='score-exact'>{sc2}</span>", unsafe_allow_html=True)
                                                                                                                                                                                        st.markdown("<p class='instruction'>✅ CONFIRMATION : Ce pronostic est lié au résultat de l'affiche n°1. Ne misez que si l'affiche 1 a suivi la logique Aï4.</p>", unsafe_allow_html=True)
                                                                                                                                                                                                st.markdown('</div>', unsafe_allow_html=True)

                                                                                                                                                                                                st.sidebar.markdown("### ⚙️ PARAMÈTRES Aï4")
                                                                                                                                                                                                st.sidebar.write("**Saison :** 45 Journées")
                                                                                                                                                                                                st.sidebar.write("**Cycle :** 3 min")
                                                                                                                                                                                                st.sidebar.write("**Langue :** Anglais (EN)")