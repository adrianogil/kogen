import sys
from simplegrammar import SimpleGrammar


def generate_dialog():
    dialog = SimpleGrammar() \
             .set_text("#dialog#")\
             .add_tag("dialog", [
                      "가:#kaphrase_igo#\n나:#naphrase_igo#"
        ])\
             .add_tag("kaphrase_igo", [
                      "#demostrative#은#object#입니까?"
                ])\
             .add_tag("naphrase_igo", [
                       "#demostrative#은#object#입니다.",
                       "#demostrative#은#object#가아닙니다.",
                ])\
             .add_tag("demostrative", [
                        "이것", "저것", "그것"
                ])\
             .add_tag("object", [
                        "의자", "책", "어유"
                ])

    print("%s\n" % (dialog,))


if __name__ == "__main__":
    total_dialogs = 1
    if len(sys.argv) > 1:
        total_dialogs = int(sys.argv[1])
    for dialog in range(total_dialogs):
        generate_dialog()
