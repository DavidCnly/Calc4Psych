import streamlit as st

st.title("Calc 4 Psych 🧘")
st.write("Note that all inputs should be in the form of a percentage.")

def grade_calc(fyp_grade, overall_grade):
    return 1.5*(overall_grade - fyp_grade/3)

fyp_input = st.text_input("Please input the percentage received for the FYP.")
overall_input = st.text_input("Please input the percentage received overall.")

if st.button("Calculate Grade!"):
    result = grade_calc(float(fyp_input), float(overall_input))
    st.write(f"The percentage received in the 40 non-FYP credits was **{result}**!")

