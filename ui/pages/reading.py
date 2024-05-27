import streamlit as st
from ui.pages.reading_texts_tab1 import american_edu_article, transform_edu_article, uk_edu_article
from ui.pages.reading_texts_tab2 import carrier_article
from ui.pages.reading_texts_tab3 import health_article

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

    def display_questions():
        for i in range(1, 11):
            st.write(f"Question {i}: {questions[i]}")

    def calculate_score():
        score = 0
        for i in range(1, 11):
            user_answer = st.session_state[f'q_{i}']
            if user_answer == answers[i]:
                score += 1
        st.write(f"Your score is: {score}/10")

    def show_answers():
        for i in range(1, 11):
            st.write(f"Answer {i}: {answers[i]}")

    def restart_quiz():
        for i in range(1, 11):
            if f'q_{i}' not in st.session_state:
                st.session_state[f'q_{i}'] = None

    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False

    if not st.session_state.quiz_started:
        st.button("Start Quiz", on_click=lambda: st.session_state.update(quiz_started=True))
    else:
        for i in range(1, 11):
            user_answer = st.radio(f"Question {i}: {questions[i]}", ('T', 'F'), key=f'q_{i}')

        if st.button("Get Score", key="calc_score_button"):
            calculate_score()

        if st.button("Show Answers", key="show_answers_button"):
            show_answers()

        # if st.button("Restart Quiz", key="restart_quiz_button"):
        #     restart_quiz()

def get_health_article():
    st.markdown(health_article)

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
