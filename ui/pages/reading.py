import streamlit as st


def main():
    # Reading Section
    st.header('Reading Corner')
    st.write('In this section, let\'s explore some interesting reading materials!')

    # Expander for Book Recommendations
    with st.expander("Book Recommendations"):
        st.write('Discover some fascinating books to enhance your reading experience!')
        st.markdown(
            '* **"To Kill a Mockingbird" by Harper Lee** - A classic novel that explores themes of racial injustice and moral growth.')
        st.markdown(
            '* **"1984" by George Orwell** - A dystopian novel that portrays a totalitarian regime and its impact on society.')
        st.markdown(
            '* **"The Great Gatsby" by F. Scott Fitzgerald** - An American classic that delves into themes of wealth, love, and the American Dream.')

    # Expander for Reading Strategies
    with st.expander("Reading Strategies"):
        st.write('Improve your reading skills with these effective strategies:')
        st.markdown('* **Preview the Text**: Skim through the text to get an overview of the content.')
        st.markdown('* **Use Context Clues**: Infer the meaning of unfamiliar words from the context of the sentence.')
        st.markdown('* **Take Notes**: Summarize key points and jot down questions as you read.')

    # Expander for Reading Comprehension Exercise
    with st.expander("Reading Comprehension Exercise"):
        st.write('Test your comprehension skills with the following passage:')
        st.markdown("""
        **Passage:**

        The sun was setting behind the mountains, casting a warm glow across the valley. Sarah sat by the window, 
        sipping her tea as she watched the colors of the sky change. She felt a sense of peace wash over her, 
        grateful for moments like these amidst the chaos of daily life.

        **Question:**

        What was Sarah doing as she watched the sunset?
        """)
        user_answer = st.text_input("Your Answer:")
        correct_answer = "sipping her tea"
        if user_answer.lower() == correct_answer:
            st.success("Correct! Sarah was indeed sipping her tea.")
        elif user_answer != "":
            st.error("Incorrect. Sarah was sipping her tea.")

    # Interactive Word Cloud
    st.header("Word Cloud")
    st.write("Explore the most frequently occurring words in the passage:")
    passage = """
    The sun was setting behind the mountains, casting a warm glow across the valley. Sarah sat by the window, 
    sipping her tea as she watched the colors of the sky change. She felt a sense of peace wash over her, 
    grateful for moments like these amidst the chaos of daily life.
    """
    st.write(passage)
    word_cloud_btn = st.button("Generate Word Cloud")
    if word_cloud_btn:
        # Generate word cloud
        # Your code to generate word cloud goes here
        st.image("ui/images/word_cloud.jpg", use_column_width=True, caption="Word Cloud")


if __name__ == "__main__":
    main()
