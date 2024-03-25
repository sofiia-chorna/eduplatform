import streamlit as st


def main():
    # Vocabulary Section
    st.header('Vocabulary Corner')
    st.write('Expand your vocabulary with these interesting words and their meanings!')

    # Vocabulary List
    st.subheader('Word of the Day')
    word_of_the_day = {
        'Word': 'Serendipity',
        'Part of Speech': 'Noun',
        'Meaning': 'The occurrence of events by chance in a happy or beneficial way.'
    }
    st.write(f"**{word_of_the_day['Word']}**")
    st.write(f"*{word_of_the_day['Part of Speech']}*")
    st.write(f"Definition: {word_of_the_day['Meaning']}")

    # Synonyms and Antonyms
    st.subheader('Synonyms and Antonyms')
    st.write('Expand your vocabulary by exploring synonyms and antonyms:')
    word = st.text_input("Enter a word:")
    if word:
        synonyms = ["fortune", "luck", "chance", "happenstance"]
        antonyms = ["misfortune", "disaster", "tragedy"]
        st.write(f"**Synonyms:** {', '.join(synonyms)}")
        st.write(f"**Antonyms:** {', '.join(antonyms)}")

    # Vocabulary Quiz
    st.subheader('Vocabulary Quiz')
    st.write('Test your vocabulary with this quiz:')

    # Quiz Question 1
    st.markdown('**Question 1:** What is the synonym of the word "Serendipity"?')
    options_q1 = ['Luck', 'Misfortune', 'Tragedy', 'Chance']
    correct_answer_q1 = 'Luck'
    user_answer_q1 = st.radio("Select your answer:", options_q1)
    if st.button('Check Answer - Q1'):
        if user_answer_q1 == correct_answer_q1:
            st.success("Correct! 'Luck' is the synonym of the word 'Serendipity'.")
        else:
            st.error(f"Incorrect. The correct answer is '{correct_answer_q1}'.")

    # Quiz Question 2
    st.markdown('**Question 2:** What is the antonym of the word "Serendipity"?')
    options_q2 = ['Misfortune', 'Luck', 'Chance', 'Happenstance']
    correct_answer_q2 = 'Misfortune'
    user_answer_q2 = st.radio("Select your answer:", options_q2)
    if st.button('Check Answer - Q2'):
        if user_answer_q2 == correct_answer_q2:
            st.success("Correct! 'Misfortune' is the antonym of the word 'Serendipity'.")
        else:
            st.error(f"Incorrect. The correct answer is '{correct_answer_q2}'.")

    # Quiz Question 3
    st.markdown('**Question 3:** Which of the following is a type of tropical fruit?')
    options_q3 = ['Apple', 'Banana', 'Grapes', 'Orange']
    correct_answer_q3 = 'Banana'
    user_answer_q3 = st.selectbox("Select your answer:", options_q3)
    if st.button('Check Answer - Q3'):
        if user_answer_q3 == correct_answer_q3:
            st.success("Correct! 'Banana' is a type of tropical fruit.")
        else:
            st.error(f"Incorrect. The correct answer is '{correct_answer_q3}'.")

    # Progress Bar
    progress = 0
    if user_answer_q1 == correct_answer_q1:
        progress += 1
    if user_answer_q2 == correct_answer_q2:
        progress += 1
    if user_answer_q3 == correct_answer_q3:
        progress += 1
    progress_percentage = progress / 3
    st.write(f"Quiz Progress: {progress} out of 3 questions completed")
    st.progress(progress_percentage)


if __name__ == "__main__":
    main()
