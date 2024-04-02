import streamlit as st

def present_simple():
    st.write("The Present Simple tense is used to express habits, general truths, repeated actions, or unchanging situations.")
    st.write("Structure:")
    st.latex(r"\text{Affirmative:} \quad \text{subject} + \text{base form of the verb (s/es for 3rd person singular)}")
    st.latex(r"\text{Negative:} \quad \text{subject} + \text{do/does not + base form of the verb}")
    st.latex(r"\text{Question:} \quad \text{do/does + subject + base form of the verb}")

def present_continuous():
    st.write("The Present Continuous tense is used to express actions happening at the moment of speaking, temporary actions, or future plans.")
    st.write("Structure:")
    st.latex(r"\text{Affirmative:} \quad \text{subject} + \text{am/is/are + present participle (-ing form)}")
    st.latex(r"\text{Negative:} \quad \text{subject} + \text{am/is/are not + present participle (-ing form)}")
    st.latex(r"\text{Question:} \quad \text{am/is/are + subject + present participle (-ing form)}")

def past_simple():
    st.write("The Past Simple tense is used to express completed actions in the past.")
    st.write("Structure:")
    st.latex(r"\text{Affirmative:} \quad \text{subject} + \text{past form of the verb}")
    st.latex(r"\text{Negative:} \quad \text{subject} + \text{did not + base form of the verb}")
    st.latex(r"\text{Question:} \quad \text{did + subject + base form of the verb}")

def past_continuous():
    st.write("The Past Continuous tense is used to express actions that were happening at a specific moment in the past or actions that were in progress.")
    st.write("Structure:")
    st.latex(r"\text{Affirmative:} \quad \text{subject} + \text{was/were + present participle (-ing form)}")
    st.latex(r"\text{Negative:} \quad \text{subject} + \text{was/were not + present participle (-ing form)}")
    st.latex(r"\text{Question:} \quad \text{was/were + subject + present participle (-ing form)}")

def future_simple():
    st.write("The Future Simple tense is used to express predictions, promises, or plans.")
    st.write("Structure:")
    st.latex(r"\text{Affirmative:} \quad \text{subject} + \text{will + base form of the verb}")
    st.latex(r"\text{Negative:} \quad \text{subject} + \text{will not + base form of the verb}")
    st.latex(r"\text{Question:} \quad \text{will + subject + base form of the verb}")

def conditionals():
    st.write("The Conditional tense is used to express hypothetical situations and their outcomes.")
    st.write("Structure:")
    st.write("Zero Conditional:")
    st.latex(r"\text{If + present simple, present simple}")
    st.write("First Conditional:")
    st.latex(r"\text{If + present simple, will + base form of the verb}")
    st.write("Second Conditional:")
    st.latex(r"\text{If + past simple, would + base form of the verb}")
    st.write("Third Conditional:")
    st.latex(r"\text{If + past perfect, would have + past participle}")

def reported_speech():
    st.write("Reported Speech is used to report what someone else has said.")
    st.write("Structure:")
    st.latex(r"\text{Direct Speech:} \quad \text{He said, 'I am happy.'}")
    st.latex(r"\text{Reported Speech:} \quad \text{He said that he was happy.}")

def passive_voice():
    st.write("The Passive Voice is used when the focus is on the action rather than the doer of the action.")
    st.write("Structure:")
    st.latex(r"\text{Affirmative:} \quad \text{subject + was/were + past participle}")
    st.latex(r"\text{Negative:} \quad \text{subject + was/were not + past participle}")
    st.latex(r"\text{Question:} \quad \text{was/were + subject + past participle}")

def modals():
    st.write("Modal verbs are used to express ability, possibility, permission, or obligation.")
    st.write("Common modal verbs include: can, could, may, might, must, shall, should, will, would.")

tabs = {
    "Present Simple": present_simple,
    "Present Continuous": present_continuous,
    "Past Simple": past_simple,
    "Past Continuous": past_continuous,
    "Future Simple": future_simple,
    "Conditionals": conditionals,
    "Reported Speech": reported_speech,
    "Passive Voice": passive_voice,
    "Modal Verbs": modals
}

def main():
    st.title("Grammar page")
    st.image("https://img.freepik.com/free-vector/english-book-illustration-design_23-2149507600.jpg")
    st.sidebar.title("English Grammar Guide")
    selected_tab = st.sidebar.radio("Select Grammar Topic", list(tabs.keys()))
    tabs[selected_tab]()


if __name__ == "__main__":
    main()
