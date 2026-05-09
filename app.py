import streamlit as st

st.title("Welcome to the guessing game!")

if "p1" not in st.session_state:
    st.session_state.p1 = ""
if "p2" not in st.session_state:
    st.session_state.p2 = ""


p1_input = st.text_input("Player 1: Type a 4-digit number (unique digits):", type="password", key="set_p1")
if p1_input:
    if len(p1_input) == 4 and len(set(p1_input)) == 4 and p1_input.isdigit():
        st.session_state.p1 = p1_input
        st.success("Player 1 set!")
    else:
        st.error("Error: Must be 4 unique digits.")


p2_input = st.text_input("Player 2: Type a 4-digit number (unique digits):", type="password", key="set_p2")
if p2_input:
    if len(p2_input) == 4 and len(set(p2_input)) == 4 and p2_input.isdigit():
        st.session_state.p2 = p2_input
        st.success("Player 2 set!")
    else:
        st.error("Error: Must be 4 unique digits.")


if st.session_state.p1 and st.session_state.p2:
    st.divider()

    p1_guess = st.text_input("Player 1: Guess P2's number", key="g1")
    if p1_guess:
        if p1_guess == st.session_state.p2:
            st.balloons()
            st.success("You win!")
        else:
            st.error("Lower" if int(p1_guess) > int(st.session_state.p2) else "Higher")

    p2_guess = st.text_input("Player 2: Guess P1's number", key="g2")
    if p2_guess:
        if p2_guess == st.session_state.p1:
            st.balloons()
            st.success("You win!")
        else:
            st.error("Lower" if int(p2_guess) > int(st.session_state.p1) else "Higher")
