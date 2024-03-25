import streamlit as st


def main():
    # Grammar Section
    st.header('English Grammar Corner')
    st.write('In this section, let\'s explore some interesting aspects of English grammar!')

    # Expander for Subject-Verb Agreement
    with st.expander("Subject-Verb Agreement"):
        st.write(
            'One important aspect of English grammar is subject-verb agreement. Make sure that the verb agrees with the subject in terms of number (singular or plural). For example:')
        st.code('The cat **sleeps** on the mat. (singular subject)')
        st.code('The cats **sleep** on the mats. (plural subject)')

    # Expander for Tenses
    with st.expander("Tenses"):
        st.write('English language has various tenses which indicate the time of an action or event. For example:')
        st.code('Present Simple: She **walks** to school every day.')
        st.code('Past Continuous: They **were playing** football when it started to rain.')
        st.code('Future Perfect: By next year, he **will have completed** his degree.')

    # Expander for Parts of Speech
    with st.expander("Parts of Speech"):
        st.write(
            'Parts of speech categorize words according to their syntactic functions. Some common parts of speech include nouns, verbs, adjectives, adverbs, etc.')
        st.write('Example:')
        st.code('Noun: The **dog** barks loudly.')
        st.code('Verb: She **runs** every morning.')
        st.code('Adjective: It was a **beautiful** day.')

    # Expander for Punctuation
    with st.expander("Punctuation"):
        st.write(
            'Punctuation marks are used to clarify meaning and separate structural elements within sentences. Some common punctuation marks include commas, periods, question marks, etc.')
        st.write('Example:')
        st.code('Sentence with a comma: After dinner, we went for a walk.')
        st.code('Sentence with a question mark: Where are you going?')

    # Exercise
    st.header('Practice Exercise')
    st.write('Test your knowledge with this exercise:')
    exercise_options = ['Choose the correct verb form for each sentence.',
                        'Fill in the blanks with the correct verb form.']
    exercise_type = st.radio('Select the exercise type:', exercise_options)

    if exercise_type == 'Choose the correct verb form for each sentence.':
        st.write('Sentence 1: The dog ___ (bark/barks) loudly every night.')
        st.write('Sentence 2: My friend and I ___ (go/goes) to the movies every weekend.')
        st.write('Sentence 3: The birds ___ (sing/sings) beautifully in the morning.')
        # Add more sentences as needed...
    elif exercise_type == 'Fill in the blanks with the correct verb form.':
        st.write('Sentence 1: The students ___ (study) hard for their exams.')
        st.write('Sentence 2: She ___ (write) a novel for the past year.')
        st.write('Sentence 3: They ___ (play) soccer every Saturday.')
        # Add more sentences as needed...


if __name__ == "__main__":
    main()
