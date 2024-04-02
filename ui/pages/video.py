import streamlit as st


def main():
    # Video Section
    st.header('Video Corner')
    st.image("https://myviewboard.com/blog/wp-content/uploads/2020/04/Boosting-Student-Engagement-with-Video-assisted-Learning.png")

    with st.expander("Speak About Education in English: School, College, University Vocabulary"):
        st.video("https://www.youtube.com/watch?v=WVegMVtJsC4")

    with st.expander("University English: Expressions and Vocabulary"):
        st.video("https://www.youtube.com/watch?v=oqNOD2tF9Ec")

    with st.expander("How to Talk About University Life in English"):
        st.video("https://www.youtube.com/watch?v=Dr4I3nps3nc")

    with st.expander("25 Academic English Words You Should Know | Perfect for University, IELTS, and TOEFL"):
        st.video("https://www.youtube.com/watch?v=BNL7qK09r7I")


if __name__ == "__main__":
    main()
