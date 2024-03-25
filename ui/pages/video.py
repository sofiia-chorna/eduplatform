import streamlit as st


def main():
    # Video Section
    st.header('Video Corner')
    st.write('In this section, let\'s explore some engaging videos related to English grammar!')

    # Video Recommendation
    st.subheader('Video Recommendation')
    st.write('Watch this informative video about English grammar:')
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    # Interactive Quiz
    st.header('Grammar Quiz')
    st.write('Test your grammar knowledge with this interactive quiz:')

    # Multiple Choice Question
    st.subheader('Choose the Correct Answer')
    st.markdown('What is the correct past tense of the verb "to go"?')
    options = ['Went', 'Goed', 'Gone', 'Going']
    user_answer_mc = st.radio("Select your answer:", options, key='multiple_choice_button')
    if st.button('Check Answer - MC'):
        correct_answer_mc = 'Went'
        if user_answer_mc == correct_answer_mc:
            st.success("Correct! 'Went' is the correct past tense of the verb 'to go'.")
        else:
            st.error(f"Incorrect. The correct answer is '{correct_answer_mc}'.")

    # True/False Question
    st.subheader('True or False')
    st.markdown('English articles "a" and "an" are examples of indefinite articles.')
    user_answer_tf = st.radio("Select True or False:", ['True', 'False'], key='true_false_button')
    if st.button('Check Answer - TF'):
        correct_answer_tf = 'True'
        if user_answer_tf == correct_answer_tf:
            st.success("Correct! 'True'. 'A' and 'an' are indeed indefinite articles in English.")
        else:
            st.error(f"Incorrect. The correct answer is '{correct_answer_tf}'.")

    # Fill in the Blank Question
    st.subheader('Fill in the Blank')
    st.markdown('Complete the following sentence with the correct word:')
    st.markdown('"She ___ to the store every day."')
    user_answer_fill = st.text_input("Your Answer:", key='fill_in_button')
    if st.button('Check Answer - Fill'):
        correct_answer_fill = 'goes'
        if user_answer_fill.lower() == correct_answer_fill:
            st.success("Correct! 'Goes' is the correct word.")
        elif user_answer_fill != "":
            st.error(f"Incorrect. The correct answer is '{correct_answer_fill}'.")


if __name__ == "__main__":
    main()
