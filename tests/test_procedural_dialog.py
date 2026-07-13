import re
import sys
import types


def test_generate_dialog_output(capsys):
    class SimpleGrammar:
        @staticmethod
        def parse(grammar):
            pattern = re.compile(r'#(.*?)#')

            def expand(text):
                while True:
                    match = pattern.search(text)
                    if not match:
                        return text
                    key = match.group(1)
                    replacement = expand(grammar[key][0])
                    text = pattern.sub(replacement, text, count=1)

            return expand(grammar['text'][0])

    module = types.ModuleType('simplegrammar')
    module.SimpleGrammar = SimpleGrammar
    sys.modules['simplegrammar'] = module

    from kogen.procedural_dialog import generate_dialog

    generate_dialog()
    captured = capsys.readouterr()
    assert captured.out == '가:이것은의자입니까?\n나:이것은의자입니다.\n\n'
