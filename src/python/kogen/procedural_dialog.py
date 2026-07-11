# -*- coding: utf-8 -*-
import sys


DEMONSTRATIVES = [
    "이것",
    "저것",
    "그것",
]

OBJECTS = [
    "의자",
    "책",
    "우유",
    "책상",
    "공책",
    "연필",
    "펜",
    "가방",
    "문",
    "창문",
    "사과",
    "물",
    "커피",
    "컵",
    "시계",
    "전화",
    "열쇠",
    "모자",
    "구두",
    "사탕",
]

PLACES = [
    "학교",
    "집",
    "방",
    "교실",
    "책상 위",
    "가방 안",
]

QUESTION_PHRASES = [
    "#demostrative#은 #object#입니까?",
    "#demostrative#은 무엇입니까?",
    "#demostrative#은 어디에 있습니까?",
    "#object#은 누구의 것입니까?",
]

ANSWER_PHRASES = [
    "#demostrative#은 #object#입니다.",
    "네, #demostrative#은 #object#입니다.",
    "아니요, #demostrative#은 #object#가 아닙니다.",
    "#demostrative#은 #place#에 있습니다.",
    "#object#은 제 것입니다.",
]


def generate_dialog():
    from simplegrammar import SimpleGrammar

    dialog_grammar = {
        "text": ["#dialog#"],
        "dialog": [
            "가:#kaphrase_igo#\n나:#naphrase_igo#"
        ],
        "kaphrase_igo": QUESTION_PHRASES,
        "naphrase_igo": ANSWER_PHRASES,
        "demostrative": DEMONSTRATIVES,
        "object": OBJECTS,
        "place": PLACES,
    }

    print("%s\n" % (SimpleGrammar.parse(dialog_grammar),))


if __name__ == "__main__":
    total_dialogs = 1
    if len(sys.argv) > 1:
        total_dialogs = int(sys.argv[1])
    for dialog in range(total_dialogs):
        generate_dialog()
