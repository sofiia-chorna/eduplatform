import streamlit as st
from ui.pages.reading_texts_tab1 import american_edu_article, transform_edu_article, uk_edu_article
from ui.pages.reading_texts_tab2 import carrier_article
from ui.pages.reading_texts_tab3 import health_article
from ui.pages.utils import display_quiz


def get_american_edu_article():
    st.markdown("Steiner: The fundamental cause of poor outcomes is that policy leaders have eroded the instructional "
                "core & designed our education system for failure")
    st.markdown("By David Steiner July 20, 2023")
    st.write("------")
    st.markdown(american_edu_article)
    questions = {
        1: "Math and reading scores for 13-year-olds have reached their highest scores in decades.",
        2: "Even with almost $200 billion in emergency federal funding for K-12 schooling, students' performance has declined over the past ten years.",
        3: "The news was received as 'reassuring,' 'encouraging' and 'hopeful.",
        4: "Political scientist Vladimir Kogan emphasises the need to improve based on the new federal data.",
        5: "Diane Ravitch suggested that politicians should invest more in charter schools, vouchers, high-stakes testing and Cybercharters.",
        6: "External factors such as race-based redlining, underfunding of healthcare, lack of support for child care and parental leave, and other social and economic policies have a significant impact.",
        7: "American teenagers spend minimal time on social media, resulting in decreased loneliness and depression."
    }
    answers = {
        1: "F",
        2: "T",
        3: "F",
        4: "T",
        5: "F",
        6: "T",
        7: "F"
    }
    display_quiz(questions, answers, prefix="us_edu")


def get_transform_edu_article():
    st.markdown("By The Hon. Minister David Sengeh and Rebecca Winthrop June 23, 2022")
    st.write("------")
    st.markdown(transform_edu_article)


def get_uk_edu_article():
    st.markdown(uk_edu_article)
    
    questions = {
        1: "Education in the UK is highly regarded worldwide.",
        2: "International students in the UK receive no language support.",
        3: "Obtaining a degree in the UK is more time-consuming than in other countries.",
        4: "UK students can gain work experience while studying.",
        5: "International students in the UK receive no benefits or discounts.",
        6: "Numerous scholarships are available in the UK for students at all levels.",
        7: "International students in the UK do not have access to free healthcare."
    }

    answers = {
        1: "T",
        2: "F",
        3: "F",
        4: "T",
        5: "F",
        6: "T",
        7: "F"
    }

    display_quiz(questions, answers, prefix="uk")


def get_education_tab():
    st.header("Articles about Education Systems")
    st.image("https://www.freevector.com/uploads/vector/preview/28057/edu_bg.jpg")
    with st.expander("America’s Education System Is a Mess, and It’s Students Who Are Paying the Price"):
        get_american_edu_article()

    with st.expander("Why we must transform our education systems now"):
        get_transform_edu_article()

    with st.expander("Facts about Education in the UK"):
        get_uk_edu_article()


def get_carrier_tab():
    st.header("10 Most Profitable Careers In England, UK")
    st.image("https://cdn.seeklearning.com.au/media/images/career-guide/article/career-advice/web_images/blogs"
             "/214/6730/2023.000_NOV-CANDI_Blog_List_of_Careers_1280x660.jpg")
    st.markdown(carrier_article)
    
    questions = {
        1: "It is impossible to work as a Marketing Specialist on a freelance basis.",
        2: "A Doctor can easily find a job in England.",
        3: "You don’t need to complete the Dentist training to become an Orthodontist.",
        4: "Working as a Geologist is for people who don’t like being outside.",
        5: "Completing an investment banking internship is not necessary for an Investment Banker.",
        6: "You can’t become an Aircraft Pilot if you have health problems.",
        7: "As an Advertising and Public Relations Director you will be managing clients at the same time.",
        8: "To become an Electrical Engineer, all you need is excellent communication skills.",
        9: "A Higher Education Teacher needs the knowledge of a subject and can do without teaching techniques.",
        10: "Psychiatrists train as medical doctors but don't have the opportunity to work in hospital wards."
    }

    answers = {
        1: "F",
        2: "T",
        3: "F",
        4: "F",
        5: "T",
        6: "T",
        7: "T",
        8: "F",
        9: "F",
        10: "F"
    }

    display_quiz(questions, answers, prefix="career")


def get_health_article():
    st.markdown(health_article)
    questions = {
        1: "The Be Active scheme started up earlier this year.",
        2: "Everyone in Birmingham is eligible for Be Active.",
        3: "Participants must pay a one-off fee to register.",
        4: "Participants can use the leisure facilities at any time of day.",
        5: "Participants can use their Be Active membership cards at any sports centre in Birmingham.",
        6: "Participants can only use the leisure facilities for two hours per week.",
        7: "Some sports centres dedicate over half their opening hours to Be Active members.",
        8: "Some Be Active activities take place outside leisure centres.",
        9: "The Be Active scheme was not as popular as the council hoped.",
        10: "The Be Active scheme attracts both slim and overweight people.",
        11: "The majority of participants are White British.",
        12: "The scheme is saving the government money in health costs.",
        13: "Less money is available for Be Active now than in the past.",
        14: "The Be Active Scheme is currently only available in Birmingham."
    }
    answers = {
        1: "F",
        2: "F",
        3: "F",
        4: "F",
        5: "F",
        6: "F",
        7: "T",
        8: "T",
        9: "F",
        10: "T",
        11: "F",
        12: "T",
        13: "T",
        14: "T"
    }
    display_quiz(questions, answers, prefix="health")


def get_health_tab():
    get_health_article()


def main():
    st.title("Articles")
    tab1, tab2, tab3 = st.tabs(["Education", "Careers", "Health"])

    with tab1:
        get_education_tab()

    with tab2:
        get_carrier_tab()
    
    with tab3:
        get_health_tab()


if __name__ == "__main__":
    main()
