from src.decorators import my_function

def test_loger(capsys):
    my_function(1, 1)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"



