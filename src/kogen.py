# -*- coding: utf-8 -*-
from grammar import SimpleGrammar

poetry = SimpleGrammar() \
    .set_text("#main_structure#")\
    .add_tag("main_structure", [\
        "#begin#\n\n#problem#\n\n#solution#\n\n#ending#"\
        ])\
    .add_tag("begin", [\
        "안녕하세요","안녕"\
        "안녕히 주무세요"
        ])\
    .add_tag("problem", [\
        "안녕하세요",\
        "#iamproblem#"
        ])\
    .add_tag("iamproblem", [\
        "저는 #problematic_noun# 입니다"
        ])\
    .add_tag("problematic_noun", [\
        "선생",
        ])\
    .add_tag("solution", [\
        "안녕하세요"\
        ])\
    .add_tag("ending", [\
        "안녕하세요"\
        ])
print(str(poetry))
