from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(height_feet, height_inches, weight_pounds):
    total_height_inches = height_feet * 12 + height_inches
    weight_kg = weight_pounds * 0.453
    height_meters = total_height_inches * 0.0254
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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    if request.method == "POST":
        user_height_feet = float(request.form["feet"])
        user_height_inches = float(request.form["inches"])
        user_weight = float(request.form["weight"])
        if user_height_feet == 0 or user_weight == 0:
            return render_template("error.html")
        bmi = calculate_bmi(user_height_feet, user_height_inches, user_weight)
        bmi_category = categorize_bmi(bmi)
        return render_template("result.html", bmi=bmi, bmi_category=bmi_category)

if __name__ == "__main__":
    app.run(debug=True)
