import streamlit as st
from ui.pages.read_texts import american_edu_article, transform_edu_article, uk_edu_article

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
    for term, definition in words_definitions.items():
        st.markdown(f"**{term}**: {definition}")
        st.write("------")

    for term, definition in definitions.items():
        st.markdown(f"**{term}**: {definition}")


def get_education_tab():
    display_terms()
