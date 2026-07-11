# -*- coding: utf-8 -*-
import sys


DEMONSTRATIVES = [
    "그것",
    "이것",
    "저것",
]

SUBSTANTIVES = [
    "교회",
    "책",
    "책상",
    "공책",
    "의자",
    "구두",
    "문",
    "사탕",
    "연필",
    "펜",
    "가방",
    "창문",
    "사과",
    "물",
    "우유",
    "컵",
    "시계",
    "전화",
    "열쇠",
    "모자",
    "학교",
    "집",
    "방",
    "교실",
]

QUESTION_PATTERNS = [
    "나: #xgo#은 무엇입니까?\n가: #xgo#은 #substantive#입니다.",
    "나: #xgo#은 #substantive#입니까?\n가: 네, #xgo#은 #substantive#입니다.",
    "나: #xgo#은 #substantive#입니까?\n가: 아니요, #xgo#은 #substantive#가 아닙니다.",
]


def build_questions_grammar():
    from simplegrammar import SimpleGrammar

    return SimpleGrammar() \
        .set_text("#goseun_question#")\
        .add_tag("goseun_question", QUESTION_PATTERNS)\
        .add_tag("substantive", SUBSTANTIVES)


def build_demonstrative_grammar():
    from simplegrammar import SimpleGrammar

    return SimpleGrammar() \
        .set_text("#xgo#")\
        .add_tag("xgo", DEMONSTRATIVES)


def generate_questions(total_questions=10):
    xgo = build_demonstrative_grammar()
    goseun_questions = build_questions_grammar()

    for q in range(0, total_questions):
        print(goseun_questions.add_tag("xgo", [str(xgo)]))
        print("\n")


if __name__ == "__main__":
    total_questions = 10
    if len(sys.argv) > 1:
        total_questions = int(sys.argv[1])

    generate_questions(total_questions)
