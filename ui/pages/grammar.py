import streamlit as st
from ui.pages.grammar_tab1 import get_family_life_tab
from ui.pages.grammar_tab2 import get_education_tab


def main():
    # Grammar Section
    st.header('English Grammar Corner')
    st.write('In this section, let\'s explore some interesting aspects of English grammar!')

    tab1, tab2 = st.tabs(["Family life", "Me and My Education"])

    with tab1:
        get_family_life_tab()

    with tab2:
        get_education_tab()


if __name__ == "__main__":
    main()
