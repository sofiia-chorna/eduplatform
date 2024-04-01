import streamlit as st
from ui.pages.read_texts import american_edu_article, transform_edu_article, uk_edu_article

def get_american_edu_article():
    st.markdown("Steiner: The fundamental cause of poor outcomes is that policy leaders have eroded the instructional "
                "core & designed our education system for failure")
    st.markdown("By David Steiner July 20, 2023")
    st.write("------")
    st.markdown(american_edu_article)


def get_transform_edu_article():
    st.markdown("By The Hon. Minister David Sengeh and Rebecca Winthrop June 23, 2022")
    st.write("------")
    st.markdown(transform_edu_article)


def get_uk_edu_article():
    st.markdown(uk_edu_article)


def get_education_tab():
    st.title("Articles")
    with st.expander("America’s Education System Is a Mess, and It’s Students Who Are Paying the Price"):
        get_american_edu_article()

    with st.expander("Why we must transform our education systems now"):
        get_transform_edu_article()

    with st.expander("Facts about Education in the UK"):
        get_uk_edu_article()


def main():
    get_education_tab()


if __name__ == "__main__":
    main()
