
def calculate_bmi(height_feet, height_inches, weight_pounds):
    # Convert height to total inches
    total_height_inches = height_feet * 12 + height_inches
    
    # Convert weight from pounds to kilograms
    weight_kg = weight_pounds * 0.45
    
    # Convert height from inches to meters
    height_meters = total_height_inches * 0.025
    
    # Calculate BMI
    bmi = weight_kg / (height_meters ** 2)
    bmi = round(bmi, 1)

    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 25:
        return "normal"
    elif 25 <= bmi < 30:
        return "overweight"
    else:
        return "obese"

if __name__ == '__main__':
    # User inputs
    print("Enter your height (press Enter after each): _____ foot _____ inches")
    user_height_feet = float(input())
    user_height_inches = float(input())

    user_weight = float(input("Enter your weight in pounds: "))

    # Calculations
    bmi = calculate_bmi(user_height_feet, user_height_inches, user_weight)

    # BMI indexing and output
    print("Your BMI is: ", bmi)
    print("You are considered", categorize_bmi(bmi))
