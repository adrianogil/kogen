import sys
from simplegrammar import SimpleGrammar


def generate_dialog():

    dialog_grammar = {
        "text": ["#dialog#"],
        "dialog": [
            "가:#kaphrase_igo#\n나:#naphrase_igo#"
        ],
        "kaphrase_igo": [
            "#demostrative#은#object#입니까?"
        ],
        "naphrase_igo": [
            "#demostrative#은#object#입니다.",
            "#demostrative#은#object#가아닙니다.",
        ],
        "demostrative": [
            "이것", "저것", "그것"
        ],
        "object": [
            "의자", "책", "어유"
        ]
    }

    dialog = SimpleGrammar()
    print("%s\n" % (dialog.parse(dialog_grammar),))


if __name__ == "__main__":
    total_dialogs = 1
    if len(sys.argv) > 1:
        total_dialogs = int(sys.argv[1])
    for dialog in range(total_dialogs):
        generate_dialog()
