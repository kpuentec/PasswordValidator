import backend.pass_strength as pass_strength
import backend.brute_force_sim as brute_force_sim
import string

def test_check_pass_valid_password():
    result = pass_strength.check_pass("Valid1Password!")
    assert result == "Your password is Very Strong!"

def test_estimate_brute_force_time():
    charset = string.ascii_lowercase + string.digits
    password = "abcd"
    estimated_hours = brute_force_sim.estimate_brute_force_time(password, charset)
    assert isinstance(estimated_hours, float)
    assert estimated_hours > 0