from src.decorators import log


def test_log_correct(capsys):
    @log(0)
    def my_function(x=1, y=1):
        return x / y

    my_function()
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_uncorrect(capsys):
    @log(0)
    def my_function(x=1, y=0):
        return x / y

    my_function()
    captured = capsys.readouterr()
    assert captured.out == "my_function error: ZeroDivisionError. Inputs: (), {}\n"
