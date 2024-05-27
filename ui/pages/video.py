import streamlit as st


def get_health_tab():
    st.subheader("Health is above wealth")
    st.video("https://www.youtube.com/watch?v=jhKvRfcJDwQ")


def get_carrier_tab():
    with st.expander("Speak About Education in English: School, College, University Vocabulary"):
        st.video("https://www.youtube.com/watch?v=WVegMVtJsC4")
    with st.expander("University English: Expressions and Vocabulary"):
        st.video("https://www.youtube.com/watch?v=oqNOD2tF9Ec")
    with st.expander("How to Talk About University Life in English"):
        st.video("https://www.youtube.com/watch?v=Dr4I3nps3nc")
    with st.expander("Do you enjoy your job?"):
        st.video("https://www.youtube.com/watch?v=TSmxTx5d1sk")
    with st.expander("25 Academic English Words You Should Know | Perfect for University, IELTS, and TOEFL"):
        st.video("https://www.youtube.com/watch?v=BNL7qK09r7I")


def get_family_tab():
    st.subheader("Learn Basic English Vocabulary: FAMILY")
    st.video("https://www.youtube.com/watch?v=Tmr4492_wkA")


def main():
    # Video Section
    st.header('Video Corner')
    st.image("https://myviewboard.com/blog/wp-content/uploads/2020/04/Boosting-Student-Engagement-with-Video-assisted-Learning.png")

    tab1, tab2, tab3 = st.tabs(["Career", "Health", "Family"])

    with tab1:
        get_carrier_tab()

    with tab2:
        get_health_tab()
    
    with tab3:
        get_family_tab()


if __name__ == "__main__":
    main()
