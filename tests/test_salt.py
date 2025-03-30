import pass_strength
import pass_salt_hash
import bcrypt

def test_hash():
    password = "TestPassword1!"
    result = pass_salt_hash.hash(password)
    assert "salt" in result
    assert "hashed_pass" in result
    assert result["hashed_pass"] != password.encode("utf-8")

def test_check_pass_valid_password():
    result = pass_strength.check_pass("Valid1Password!")
    assert result == "Your password is Very Strong!"