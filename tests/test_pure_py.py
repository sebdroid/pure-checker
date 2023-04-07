import pure_checker

def test_zip_bomb():
    with open("zbsm.zip", "rb") as f:
        purity = pure_checker.pure_zip(f.read())
        assert purity == 7
        assert pure_checker.pure_error_code(purity) == "PURE_E_ZIP_BOMB_FIFIELD"
        assert pure_checker.pure_error_string(purity) == "zip bomb: local file header overlap (see research by David Fifield)"

def test_pure_error_code():
    assert pure_checker.pure_error_code(5) == "PURE_E_ZIP_BOMB_ARCHIVES"

def test_pure_error_string():
    assert pure_checker.pure_error_string(5) == "zip bomb: too many archives"