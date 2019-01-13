if [ -z "$KOGEN_PYTHON_PATH" ]
then
    export KOGEN_PYTHON_PATH=$KOGEN_DIR/python/
    export PYTHONPATH=$KOGEN_PYTHON_PATH:$PYTHONPATH
fi

alias kogen="python2 -m kogen.kogen"
alias kogen-goseun-questions="python2 -m kogen.goseun_questions"