import streamlit as st

tab1_definitions = {
    "Adopt": "To legally agree to permanently look after someone else's child",
    "Black sheep of the family": "A member of the family considered bad or rebellious in some way",
    "Breadwinner": "The person who earns money to support a family",
    "Fall out with": "To have an argument or disagreement with someone",
    "Family man": "A man who is highly dedicated to his family",
    "Own flesh and blood": "Emphasising that you are referring to a member of your family.",
    "Blood is thicker than water": "Family relationships are the most important",
    "Foster": "To legally agree to temporarily look after someone else's child",
    "Get on well/badly with": "Have a good/bad relationship with someone",
    "Get round someone": "To persuade someone. Often a child 'gets round' their parents",
    "Give a telling off": "To discipline someone. Usually, parents tell off their children.",
    "Hereditary": "Something that is passed from one generation to the next",
    "Look alike": "To have a similar appearance to someone",
    "Look up to": "To admire",
    "Look after": "To take care of",
    "Named after": "To be given a name because of someone else in your family",
    "Older generation": "A group of people not classed as young. Generally, they have children/grandchildren.",
    "Run in the family": "When traits are shared amongst family members.",
    "Sibling rivalry": "Fighting or conflict between brothers and sisters",
    "Single-parent": "A parent raising a child by themselves",
    "Take after someone": "Something you inherit from an older family member",
    "To raise/bring up a child/children": "To take care of children from childhood to adulthood",
    "To support a family": "To provide food and resources for a family to survive",
    "Upbringing": "The way that a person was raised from childhood to adulthood",
    "Wears the trousers": "The person who is in control",
    "Widow / Widower": "A woman/man whose husband/wife has died",
    "Younger generation": "A group of people not considered old. Generally young people, students and young adults"
}


def tab1_generate_exercise():
    exercise_text = """
    Yes I would like to see more of my family, especially my _______ (1) who I get on well often. 
    I was also brought up like my cousins, _______ (2) with. 
    We have always had a good relationship but we don't see each other because my _______ (3) divorced when 
    I was younger. My father lives quite far away but I would like to see him more often because I 
    really _______ (4) to him. 
    Should people rely on their families or be more independent? 
    I think that it is better for people to become independent as soon as possible. 
    I _______ (5) in that respect because she has always been independent ever since she became a 
    _______ (6) after my father died. That meant that she had to become the main _______ (7) in the house and she 
    _______ (8) me and my _______ (9). 
    She _______ (10) herself. 
    I will never abandon my family because as they say, _______ (11). 
    I don't want to pressure my mother by depending on her to _______ (12).
    """
    return exercise_text


def tab1_generate_answers():
    answers = {
        "1": "extended family",
        "2": "get on well",
        "3": "parents",
        "4": "look up to",
        "5": "widow",
        "6": "take after",
        "7": "mother",
        "8": "breadwinner",
        "9": "supported",
        "10": "siblings",
        "11": "supports",
        "12": "blood is thicker than water",
        "13": "support"
    }
    return answers


def get_family_life_tab():
    # Expander for vocabulary
    with st.expander("Vocabulary"):
        for term, definition in tab1_definitions.items():
            st.markdown(f"**{term}**: {definition}")

    st.title("Lexical Exercise")

    exercise_text = tab1_generate_exercise()
    answers = tab1_generate_answers()

    st.write(exercise_text)

    # Input boxes for user's answers
    col1, col2 = st.columns(2)
    user_answers = {}
    for key, value in answers.items():
        with col1 if int(key) % 2 != 0 else col2:
            user_answers[key] = st.text_input(f"Enter your answer for number {key}:", "")

    correct_answers = 0

    # Button to show score
    if st.button("Show Score"):
        for key, value in answers.items():
            if user_answers[key].strip().lower() == value.lower():
                correct_answers += 1
        st.write(f"Your score: {correct_answers}/{len(answers)}")

    # Button to check answers
    if st.button("Check Answers"):
        for key, value in answers.items():
            if user_answers[key].strip().lower() == value.lower():
                st.write(f"Answer {key}: Correct!")
            else:
                st.write(f"Answer {key}: Incorrect. Correct answer is '{value}'.")

