from main import * 


def test():
    assert xo('xo123123')== True
    assert xo('xo')== True
    assert xo('XO')==True
    assert xo('xo0')== True
    assert xo('xxxoo')== False
    assert xo('')==True
    assert xo('xxxxxoooxooo')== True
    assert xo('xxxxxoooXooo')==True
    assert xo('abcdefghijklmnopqrstuvwxyz')== True