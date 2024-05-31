import streamlit as st
from ui.pages.utils import display_questionaire


def display_vocabulary(vocabulary, prefix="vocab"):
    for i, word in enumerate(vocabulary, 1):
        st.write(f"{i}. {word}")


def get_health_tab():
    st.header("Health Vocabulary and Exercises")
    st.image()
    vocabulary = ["Healthy", "Wellness", "Fitness", "Nutrition", "Exercise", "Well-being", "Hygiene", "Balance", "Strength", "Immunity"]
    display_vocabulary(vocabulary, prefix="health_vocab")

    questions = [
        ("What is the state of being free from illness or injury?", ["Wellness", "Fitness", "Health"]),
        ("What is the practice of maintaining and improving one's health through diet and exercise?", ["Nutrition", "Fitness", "Hygiene"]),
        ("Which term refers to the overall condition of a person's body or mind?", ["Well-being", "Immunity", "Balance"]),
        ("What is the ability of the body to resist infection and disease?", ["Strength", "Immunity", "Balance"]),
        ("Which term refers to the state of being physically active and strong?", ["Exercise", "Wellness", "Strength"])
    ]

    correct_answers = [
        "Health",
        "Nutrition",
        "Well-being",
        "Immunity",
        "Strength"
    ]

    display_questionaire(questions, correct_answers, prefix="health_test")

