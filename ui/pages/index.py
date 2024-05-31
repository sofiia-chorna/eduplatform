from st_pages import Page, show_pages, add_page_title
import streamlit as st

class UI:
    @staticmethod
    def setup_pages(show_title=True):

        if show_title:
            add_page_title()

        pages = [
            Page("ui/pages/reading.py", "Reading", "📖"),  # Book
            Page("ui/pages/vocabulary.py", "Vocabulary", "📚"),  # Books
            Page("ui/pages/grammar.py", "Grammar", "📝"),  # Memo
            Page("ui/pages/video.py", "Video", "🎥"),  # Movie Camera
            # Page("ui/pages/about.py", "About", "ℹ️"),  # Information
        ]
        show_pages(pages)
