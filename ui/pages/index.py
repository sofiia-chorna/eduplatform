from st_pages import Page, show_pages, add_page_title

class UI:
    @staticmethod
    def setup_pages(show_title=True):
        if show_title:
            add_page_title()

        pages = [
            Page("ui/pages/reading.py", "Чтение", "📖"),  # Book
            Page("ui/pages/grammar.py", "Грамматика", "📝"),  # Memo
            Page("ui/pages/video.py", "Видео", "🎥"),  # Movie Camera
            Page("ui/pages/vocabulary.py", "Лексика", "📚"),  # Books
            Page("ui/pages/about.py", "About", "ℹ️"),  # Information
        ]

        show_pages(pages)
