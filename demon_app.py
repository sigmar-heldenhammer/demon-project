

import streamlit as st
from Cacodemon_Generator import generate_cacodemon_base, format_cacodemon_statblock



st.title("Cacodemon Generator")

rank = st.selectbox("Choose Cacodemon Rank", [
    "Spawn", "Imp", "Gremlin", "Hellion", "Incubus",
    "Demon", "Dybbuk", "Devil", "Fiend", "Archfiend"
])

# Initialize session state for storing generated output
if "statblock" not in st.session_state:
    st.session_state.statblock = ""

# When button is clicked, regenerate and store the new statblock
if st.button("Generate Cacodemon"):
    demon = generate_cacodemon_base(rank)
    st.session_state.statblock = format_cacodemon_statblock(demon)

# Show the current statblock from session state (even if dropdown is changed)
if st.session_state.statblock:
    st.subheader("Generated Cacodemon")
    st.text(st.session_state.statblock)

