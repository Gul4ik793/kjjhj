from calc import summ


def test_summ():
    assert summ(2, 3) == 5

def test_notsumm():
    assert summ(2, 3) == 6
