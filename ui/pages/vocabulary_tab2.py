import streamlit as st

words_definitions = {
    "study": "изучение (исследование)\n\nI learn Russian because I want to be able to read academic studies. – Я изучаю русский язык, потому что хочу научиться читать научные работы.",
    "campus": "кампус\n\nThe students live on the University campus. – Студенты живут в университетском кампусе.",
    "curriculum": "учебный план\n\nWhere can I see the school curriculum? – Где я могу посмотреть школьный учебный план?\n\nThey added math to the curriculum. – Они добавили математику в расписание.",
    "laboratory (lab)": "лаборатория\n\nThe chemistry teacher is working in the school lab now. – Учитель химии сейчас работает в школьной лаборатории.",
    "graduate": "выпускник\n\nHe is an Oxford graduate. – Он выпускник Оксфорда.",
    "mark, score (US), grade (UK)": "оценка, отметка\n\nYou have good marks (grades) in (for) English. – У тебя хорошие оценки по английскому.",
    "library": "библиотека\n\nI should return the book to the library. – Я должен вернуть книги в библиотеку.",
    "discipline": "дисциплина\n\nA teacher must maintain classroom discipline. – Учитель должен поддерживать дисциплину в классе.",
    "major": "специальность (в учебе)\n\nWhat is your major? – Какая у вас специальность?",
    "educator": "педагог\n\nThe politician used to be writer and educator. – Политик раньше был писателем и педагогом.",
    "testing": "тестирование\n\nTesting is the process of giving tests. – Тестирование – это процесс проведения тестов.",
    "specialist": "специалист\n\nShe is a specialist in modern Russian literature. – Она специалист по современной русской литературе.",
    "teacher": "учитель\n\nI have learnt it from my teacher. – Я научился этому у своего учителя.",
    "professor": "профессор\n\nIndiana Johns is an archeology professor. – Индиана Джонс – профессор археологии.",
    "school": "школа\n\nI went to school in this town. – Я ходил в школу (учился) в этом городе.\n\nПримечание: в США под “school” могут подразумевать не только школу в нашем понимании, но и колледж, университет. Выражение “to go to school” значит не только буквально «ходить в школу», но и «учиться».",
    "student": "студент\n\nStudents have to read a lot. – Студентам приходится много читать.\n\nПримечание: под “students” могут пониматься не только студенты колледжей, университетов, но и школьники, учащиеся на курсах.",
    "history": "история\n\nShe studied American history in the college. – Она изучает американскую историю в колледже.",
    "education": "образование\n\nYou have a chance to get a good education. – У тебя есть возможность получить хорошее обучение.",
    "college": "колледж\n\nShe is an Art college graduate. – Она выпускница колледжа искусств.",
    "class": "класс, урок\n\nI take English classes. – Я хожу на уроки английского языка.\n\nI have to go to the next class. – Мне нужно идти на следующий урок.",
    "test": "тест\n\nHave I passed the test? – Я прошел тест?\n\nYou will have to take a test. – Вам придется пройти тест.",
    "degree": "степень (в т.ч. ученая степень)\n\nI am finishing my degree this year. – Я заканчиваю учебу в этом году (получаю образование).\n\nShe has a master degree. – У нее магистерская степень.",
    "training": "обучение\n\nThe soldiers spent two months in training. – Солдаты провели два месяца в тренировках.",
    "knowledge": "знание\n\nKnowledge is power. – Знания – сила.",
    "coach": "тренер\n\nWe hired another football coach. – Мы наняли другого тренера по футболу.",
    "university": "университет\n\nMoscow State University. – Московский государственный университет.",
    "lesson": "урок\n\nHe gives math lessons. – Он дает уроки математики.",
    "failure": "неудача\n\nTheir work ended in failure. – Их работа закончилась неудачей.",
    "learning": "изучение, процесс учебы\n\nApps make learning fun. – Приложения делают учебу интересной (веселой).",
    "classroom": "класс (помещение)\n\nWe used the office as a classroom. – Мы использовали офис в качестве класса.",
    "session": "сеанс, период работы, деятельности, учебы\n\nHe taught German during the summer session. – Он преподавал немецкий во время летнего периода учебы.\n\nПримечание: под “session” подразумевается любой период учебы, а не экзаменационная сессия.",
    "preparation": "подготовка\n\nThe teacher hasn’t done much preparation for the class. – Учитель не особо подготовился к уроку.",
    "draft": "набросок (черновик)\n\nThis is a rough draft of the article. – Это грубый набросок статьи.",
    "set": "набор\n\nA set of pencils. – Набор карандашей.",
}

definitions = {
    "dean's office": "деканат",
    "dean": "декан",
    "principal": "ректор",
    "principal's office": "ректорат",
    "vice-principal": "проректор",
    "audience": "аудитория",
    "an office": "кабинет",
    "laboratory": "лаборатория",
    "syllabus": "план лекций",
    "education": "образование, обучение",
    "compulsory education": "обязательное образование",
    "general education": "общее образование",
    "National Curriculum": "Государственный образовательный стандарт",
    "educational purposes": "образовательные цели",
    "pre-school education": "дошкольное образование",
    "primary education": "начальное образование",
    "secondary education": "среднее образование",
    "vocational education": "профессиональное образование",
    "higher education": "высшее образование",
    "nursery (school)": "ясли",
    "kindergarten": "детский сад",
    "preparatory school": "подготовительная школа",
    "state school": "государственная школа",
    "primary school": "начальная школа",
    "secondary school (BrE) / high school (AmE)": "средняя школа",
    "special school": "специальная школа",
    "gymnasium": "гимназия",
    "lyceum": "лицей",
    "boarding school": "школа-интернат",
    "an English language school": "школа с углубленным изучением английского языка",
    "grammar school": "грамматическая школа (в Великобритании)",
    "private school": "частная школа (в Америке)",
    "public school": "частная школа (в Великобритании)",
    "college": "колледж",
    "technical college (school)": "техникум",
    "vocational school": "профессиональное училище",
    "medical school": "медицинское училище",
    "military school": "военное училище",
    "art school (college)": "художественное училище",
    "teacher-training college": "педагогическое училище",
    "institute": "институт",
    "university": "университет",
    "academy": "академия",
    "literacy": "грамотность",
    "comprehensive education": "всестороннее образование",
    "student loans": "образовательный кредит",
    "gap year": "академический отпуск",
    "scholarship": "стипендия"
}


def display_terms():
    with st.expander("Vocabulary"):
        for term, definition in words_definitions.items():
            st.markdown(f"**{term}**: {definition}")
            st.write("------")

        for term, definition in definitions.items():
            st.markdown(f"**{term}**: {definition}")


def get_meaning_quiz_ex():
    with st.expander('I. Connect the Expressions with Their Meanings'):

        # Define expressions, meanings, and correct answers
        expressions = {
            'a': "Enroll/Sign up for",
            'b': "Hit the books",
            'c': "Hand out assignment",
            'd': "Pull an all-nighter",
            'e': "Hands in paper/assignment",
            'f': "Cut class",
            'g': "Fall behind (in)",
            'h': "Get caught up",
            'i': "Withdraw from the course",
            'j': "Plagiarize",
            'k': "Expel/kick out",
        }

        meanings = {
            1: "To decide to go to university or to take a certain class",
            2: "Get on the same level with everybody",
            3: "To skip class",
            4: "To study hard",
            5: "To give students homework",
            6: "To get discarded from the university",
            7: "To get your paper done by somebody else",
            8: "To give the professor your work for assessment",
            9: "To leave a course before you finish it",
            11: "Staying up all night to finish something or Can't keep up with the school curriculum",
        }

        correct_answers = {
            'a': 1, 'b': 4, 'c': 5, 'd': 11, 'e': 8, 'f': 3, 'g': 11, 'h': 2, 'i': 9, 'j': 7, 'k': 6
        }

        # Initialize or reset session state variables
        if 'answers_shown_ex1' not in st.session_state:
            st.session_state.answers_shown_ex1 = False

        for key in expressions.keys():
            if f'select_{key}_ex1' not in st.session_state:
                st.session_state[f'select_{key}_ex1'] = "Select an option"

        # Function to show correct answers
        def show_correct_answers():
            st.session_state.answers_shown_ex1 = not st.session_state.answers_shown_ex1

        # Function to clear selections
        def clear_selections():
            for key in expressions.keys():
                st.session_state[f'select_{key}_ex1'] = "Select an option"
            st.session_state.answers_shown_ex1 = False

        # Function to calculate and show the score
        def show_score():
            score = 0
            for letter, expression in expressions.items():
                if st.session_state[f'select_{letter}_ex1'] == meanings[correct_answers[letter]]:
                    score += 1
            st.write(f"Your score: {score}/{len(expressions)}")

        # UI for matching expressions to meanings
        for letter, expression in expressions.items():
            options = ["Select an option"] + list(meanings.values())
            index = 0 if not st.session_state.answers_shown_ex1 else options.index(meanings[correct_answers[letter]])
            selected_option = st.selectbox(expression, options, index=index, key=f'select_{letter}_ex1')

        # Buttons for user actions
        st.button("Toggle Show Answers", on_click=show_correct_answers, key="show_correct_answers_button_ex1")
        st.button("Clear Selections", on_click=clear_selections, key="clear_selection_button_ex1")

        # Button to show score
        if st.button("Show Score", key="show_score_button_ex1"):
            show_score()


def get_colocation_quiz_ex():
    with st.expander("II. Choose the right word to form a collocation: school/goals/year/education"):
        # Define expressions, meanings, and correct answers
        expressions = {
            'a': "Private ...",
            'b': "School ...",
            'c': "Learning ...",
            'd': "Formal ...",
        }

        meanings = {
            1: "school",
            2: "goals",
            3: "year",
            4: "education",
        }

        correct_answers = {
            'a': 1, 'b': 3, 'c': 2, 'd': 4
        }

        # Initialize or reset session state variables
        if 'answers_shown_ex2' not in st.session_state:
            st.session_state.answers_shown_ex2 = False

        for key in expressions.keys():
            if f'select_{key}_ex2' not in st.session_state:
                st.session_state[f'select_{key}_ex2'] = "Select an option"

        # Function to show correct answers
        def show_correct_answers():
            st.session_state.answers_shown_ex2 = not st.session_state.answers_shown_ex2

        # Function to clear selections
        def clear_selections():
            for key in expressions.keys():
                st.session_state[f'select_{key}_ex2'] = "Select an option"
            st.session_state.answers_shown_ex2 = False

        # Function to calculate and show the score
        def show_score():
            score = 0
            for letter, expression in expressions.items():
                if st.session_state[f'select_{letter}_ex2'] == meanings[correct_answers[letter]]:
                    score += 1
            st.write(f"Your score: {score}/{len(expressions)}")

        # UI for matching expressions to meanings
        for letter, expression in expressions.items():
            options = ["Select an option"] + list(meanings.values())
            index = 0 if not st.session_state.answers_shown_ex2 else options.index(meanings[correct_answers[letter]])
            selected_option = st.selectbox(expression, options, index=index, key=f'select_{letter}_ex2')

        # Buttons for user actions
        st.button("Toggle Show Answers", on_click=show_correct_answers, key="show_correct_answers_button_ex2")
        st.button("Clear Selections", on_click=clear_selections, key="clear_selection_button_ex2")

        # Button to show score
        if st.button("Show Score", key="show_score_button_ex2"):
            show_score()


def get_suitable_option_ex():
    with st.expander(
            "III. Choose the most suitable option to complete these sentences. You can use each option ONLY ONCE."):
        options = {
            1: ["Select an option", "grade", "grade", "grade", "grade", "grade", "grade", "grade", "grade", "grade"],
            2: ["Select an option", "failed", "failed", "failed", "failed", "failed", "failed", "failed", "failed",
                "failed"],
            3: ["Select an option", "graduates", "graduates", "graduates", "graduates", "graduates", "graduates",
                "graduates", "graduates", "graduates"],
            4: ["Select an option", "research", "research", "research", "research", "research", "research", "research",
                "research", "research"],
            5: ["Select an option", "sitting", "sitting", "sitting", "sitting", "sitting", "sitting", "sitting",
                "sitting",
                "sitting"],
            6: ["Select an option", "expelled", "expelled", "expelled", "expelled", "expelled", "expelled", "expelled",
                "expelled", "expelled"],
            7: ["Select an option", "hand in", "hand in", "hand in", "hand in", "hand in", "hand in", "hand in",
                "hand in",
                "hand in"],
            8: ["Select an option", "study", "study", "study", "study", "study", "study", "study", "study", "study"],
            9: ["Select an option", "enrolled", "enrolled", "enrolled", "enrolled", "enrolled", "enrolled", "enrolled",
                "enrolled", "enrolled"],
            10: ["Select an option", "revising", "revising", "revising", "revising", "revising", "revising", "revising",
                 "revising", "revising"]
        }

        sentences = {
            1: "I hope I get a good ___ for my essay.",
            2: "I was disappointed when I found out that I’d ___ my exam.",
            3: "After Luke ___ from high school, he’ll go to university.",
            4: "I had to do a lot of ___ for my geography project.",
            5: "Students who are ___ exams must leave their phones in their bags.",
            6: "Larry was ___ for his rude and anti-social behaviour.",
            7: "We have to ___ our assignments by 4 p.m. on Friday.",
            8: "If I could ___ abroad, I’d like to go to France.",
            9: "When I ___ in the course, I had to fill in a lot of forms.",
            10: "I really don’t enjoy ___ for exams."
        }

        def display_quiz():
            for i in range(1, 11):
                selected_option = st.selectbox(sentences[i], options[i])
                if selected_option != "Select an option":
                    st.session_state[f'select_{i}_ex3'] = selected_option

        def show_answers():
            for i in range(1, 11):
                st.write(f"Answer {i}: {st.session_state[f'select_{i}_ex3']}")

        def clear_selections():
            for i in range(1, 11):
                st.session_state[f'select_{i}_ex3'] = "Select an option"

            # Initialize or reset session state variables

        if 'answers_shown_ex3' not in st.session_state:
            st.session_state.answers_shown_ex3 = False
        for key in sentences.keys():
            if f'select_{key}_ex3' not in st.session_state:
                st.session_state[f'select_{key}_ex3'] = "Select an option"

        display_quiz()

        st.button("Show Answers", on_click=show_answers)
        st.button("Clear Selections", on_click=clear_selections)


def display_exercise():
    st.title("Lexical Exercise")
    st.image("https://img.freepik.com/free-vector/scientists-studying-neural-connections-programmers-writing-codes-machine-brain_74855-14157.jpg")
    get_meaning_quiz_ex()
    get_colocation_quiz_ex()


def get_education_tab():
    # Initialize session state for showing answers if not already done
    if 'answers_shown_ex1' not in st.session_state:
        st.session_state["answers_shown_ex1"] = False
    if 'answers_shown_ex2' not in st.session_state:
        st.session_state["answers_shown_ex2"] = False

    display_terms()
    display_exercise()
