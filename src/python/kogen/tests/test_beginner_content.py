from kogen import goseun_questions
from kogen import procedural_dialog


def test_procedural_dialog_has_expanded_beginner_objects():
    expected_objects = {
        "책",
        "우유",
        "연필",
        "가방",
        "사과",
        "시계",
        "전화",
        "열쇠",
    }

    assert expected_objects.issubset(set(procedural_dialog.OBJECTS))
    assert "어유" not in procedural_dialog.OBJECTS


def test_procedural_dialog_has_beginner_question_and_answer_patterns():
    assert "#demostrative#은 무엇입니까?" in procedural_dialog.QUESTION_PHRASES
    assert "#demostrative#은 어디에 있습니까?" in procedural_dialog.QUESTION_PHRASES
    assert "네, #demostrative#은 #object#입니다." in procedural_dialog.ANSWER_PHRASES
    assert "아니요, #demostrative#은 #object#가 아닙니다." in procedural_dialog.ANSWER_PHRASES


def test_goseun_questions_has_expanded_beginner_substantives():
    expected_substantives = {
        "책상",
        "공책",
        "연필",
        "가방",
        "물",
        "우유",
        "학교",
        "집",
    }

    assert expected_substantives.issubset(set(goseun_questions.SUBSTANTIVES))


def test_goseun_questions_has_yes_no_patterns():
    assert (
        "나: #xgo#은 #substantive#입니까?\n"
        "가: 네, #xgo#은 #substantive#입니다."
    ) in goseun_questions.QUESTION_PATTERNS
    assert (
        "나: #xgo#은 #substantive#입니까?\n"
        "가: 아니요, #xgo#은 #substantive#가 아닙니다."
    ) in goseun_questions.QUESTION_PATTERNS
