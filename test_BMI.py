from BMI import calculate_bmi, categorize_bmi

#underweight test
def test_underweight():
    bmi = 18.4
    assert categorize_bmi(bmi) == "underweight"

#normal weight test lower bound
def test_normal_weight_lower():
    bmi = 18.5
    assert categorize_bmi(bmi) == "normal"

#normal weight test upper bound
def test_normal_weight_upper():
    bmi = 24.9
    assert categorize_bmi(bmi) == "normal"

#overweight test lower bound
def test_overweight_lower():
    bmi = 25
    assert categorize_bmi(bmi) == "overweight"

#overweight test upper bound
def test_overweight_upper():
    bmi = 29.9
    assert categorize_bmi(bmi) == "overweight"

#obese test
def test_obese():
    bmi = 30
    assert categorize_bmi(bmi) == "obese"

#math calculation test
def test_calculation():
    assert calculate_bmi(5, 8, 175) == 26.6