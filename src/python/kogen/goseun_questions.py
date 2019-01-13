import sys
from simplegrammar.grammar import SimpleGrammar


total_questions = 10
if len(sys.argv) > 1:
    total_questions = int(sys.argv[1])

xgo = SimpleGrammar() \
    .set_text("#xgo#")\
    .add_tag("xgo", [\
        "그것","이것","저것" \
        ])


goseun_questions = SimpleGrammar() \
    .set_text("#goseun_question#")\
    .add_tag("goseun_question", [\
        "나: #xgo#은 무엇입니까?\n가: #xgo#은 #substantive#입니다." \
        ])\
    .add_tag("substantive", [
        "교회", "책", "책상", "공책", "의자", "구두", "문", "사탕"
        ])

for q in xrange(0, total_questions):
    print(goseun_questions.add_tag("xgo", [str(xgo)]))
    print("\n")
