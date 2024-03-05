if __name__ == '__main__':
    #user inputs
    print("Enter your height (press Enter after each): _____ foot _____ inches")
    user_height_feet = float(input())
    user_height_inches = float(input())

    user_weight = float(input("Enter your weight in pounds: "))

    #calculations
    weight_kg = user_weight * 0.45
    total_height_inches = (user_height_feet * 12) + user_height_inches

    height_meters = total_height_inches * 0.025
    height_squared = height_meters * height_meters

    userBMI = weight_kg / height_squared

    #BMI indexing and output
    if userBMI < 18.5:
        print("You are considered underweight with a BMI of: ", userBMI)

    elif userBMI >= 18.5 and userBMI < 25:
        print("You are considered normal weight with BMI of: ", userBMI)

    elif userBMI >= 25 and userBMI < 30:
        print("You are considered overweight with BMI of: ", userBMI)
    
    else:
        print("You are considered obese with BMI of: ", userBMI)
