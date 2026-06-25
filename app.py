import streamlit as st

st.set_page_config(page_title="Dein Geburtstagsgeschenk 🎁", page_icon="🎁", layout="centered")

if "hinweise_aufgedeckt" not in st.session_state:
    st.session_state.hinweise_aufgedeckt = 0
    st.session_state.erraten = False
    st.session_state.loesung_gezeigt = False
    st.session_state.falsche_versuche = 0

HINWEISE = [
    "Es verschlägt uns nicht allzu weit. Wir kommen mit dem Rad dorthin.",
    "Das Pokemon-Duo hierzu waren Enton und Gengar.",
    "Enton ist tollpatschig und Gengar macht gerne Späße.",
    "In der Nähe der Züge soll es ganz schön sein.",
    "Und wir sollten eine Menge lachen können.",
]

SCHLUESSEL_WOERTER = ["oldenburg", "comedy", "lachen", "gleispark", "komische nacht"]

# ==========================================
# STARTSEITE
# ==========================================
st.title("🎁 Dein Geburtstagsgeschenk wartet!")
st.markdown("""
Hey mein Schatz! 😊

Du hast das Quiz abgeschlossen und dein Ergebnis ist klar!
Aber ich verrate dir nicht einfach so, was dein Geschenk ist. Ich gebe dir Hinweise –
kannst du es erraten? 🕵️
""")

st.divider()
st.subheader("🔍 Was könnte es sein?")

aufgedeckt = st.session_state.hinweise_aufgedeckt

for i in range(aufgedeckt):
    st.info(f"**Hinweis {i + 1}:** {HINWEISE[i]}")

# ==========================================
# RICHTIG GERATEN
# ==========================================
if st.session_state.erraten:
    st.success("🎉 Richtig geraten!")
    st.markdown("""
    ### 😂 Dein Geschenk: 3. Junge & Wilde komische Nacht Oldenburg"!

    Der Gleispark ruft! Lass uns in der Abendsonne in schöner Location entspannen und zusammen lachen! 😊
    """)
    st.balloons()

# ==========================================
# LÖSUNG ANGEZEIGT
# ==========================================
elif st.session_state.loesung_gezeigt:
    st.markdown("### 😂 Dein Geschenk: 3. Junge & Wilde komische Nacht Oldenburg!")
    st.warning("""
    Der Gleispark ruft! Lass uns in der Abendsonne in schöner Location entspannen und zusammen lachen! 😊
    """)
    st.balloons()

# ==========================================
# NOCH AM RATEN
# ==========================================
else:
    rateversuch = st.text_input(
        "Dein Tipp:",
        key=f"tipp_{aufgedeckt}",
        placeholder="Was könnte es sein...?"
    )

    col_rate, col_hinweis = st.columns(2)

    with col_rate:
        if st.button("✅ Raten", use_container_width=True, key=f"btn_raten_{aufgedeckt}"):
            if rateversuch.strip():
                tipp_lower = rateversuch.strip().lower()
                if any(kw in tipp_lower for kw in SCHLUESSEL_WOERTER) and 'comedy'.lower() in tipp_lower:
                    st.session_state.erraten = True
                    st.rerun()
                else:
                    #st.session_state.falsche_versuche += 1
                    #if aufgedeckt < len(HINWEISE):
                        #st.session_state.hinweise_aufgedeckt += 1
                    st.rerun()
            else:
                st.warning("Gib erst einen Tipp ein!")

    with col_hinweis:
        if aufgedeckt < len(HINWEISE):
            if st.button("💡 Nächsten Hinweis aufdecken", use_container_width=True, key=f"btn_hinweis_{aufgedeckt}"):
                st.session_state.hinweise_aufgedeckt += 1
                st.rerun()
        else:
            if st.button("🎁 Lösung anzeigen", use_container_width=True, key=f"btn_loesung_{aufgedeckt}"):
                st.session_state.loesung_gezeigt = True
                st.rerun()

    if st.session_state.falsche_versuche > 0:
        verbleibend = len(HINWEISE) - aufgedeckt
        if verbleibend > 0:
            st.caption(f"Noch nicht ganz – neuer Hinweis aufgedeckt! ({verbleibend} weitere verfügbar)")
        else:
            st.caption("Alle Hinweise sind aufgedeckt. Weiter raten oder Lösung anzeigen lassen.")
