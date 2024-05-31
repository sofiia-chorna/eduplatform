import streamlit as st
from ui.pages.vocabulary_tab1 import get_family_life_tab
from ui.pages.vocabulary_tab2 import get_education_tab
from ui.pages.vocabulary_tab3 import get_health_tab

def main():
    st.header('English Vocabulary Corner')
    st.write('In this section, let\'s explore some interesting aspects of English vocabulary!')

    tab1, tab2, tab3 = st.tabs(["Family life", "Me and My Education", "Health"])

    with tab1:
        get_family_life_tab()

    with tab2:
        get_education_tab()
    
    with tab3:
        get_health_tab()


if __name__ == "__main__":
    main()
