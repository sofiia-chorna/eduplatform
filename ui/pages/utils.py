import streamlit as st


def display_quiz(questions, answers, prefix="quiz"):
    def calculate_score():
        score = 0
        for i in range(1, len(questions) + 1):
            user_answer = st.session_state.get(f'{prefix}_q_{i}', None)
            if user_answer == answers[i]:
                score += 1
        st.write(f"Your score is: {score}/{len(questions)}")

    def show_answers():
        for i in range(1, len(questions) + 1):
            st.write(f"Answer {i}: {answers[i]}")

    if f'{prefix}_quiz_started' not in st.session_state:
        st.session_state[f'{prefix}_quiz_started'] = False

    if not st.session_state[f'{prefix}_quiz_started']:
        st.button("Start Quiz", key=f"{prefix}_start_button", on_click=lambda: st.session_state.update({f'{prefix}_quiz_started': True}))
    else:
        for i in range(1, len(questions) + 1):
            st.radio(f"Question {i}: {questions[i]}", ('T', 'F'), key=f'{prefix}_q_{i}')

        if st.button("Get Score", key=f"{prefix}_calc_score_button"):
            calculate_score()

        if st.button("Show Answers", key=f"{prefix}_show_answers_button"):
            show_answers()
