def inch_to_m(inch):
    # 1″ = 0.0254 m
    return inch * 0.0254

def cm_to_m(cm):
    # 1 cm = 0.01 m
    return cm * 0.01

def lbs_to_kg(lbs):
    # 1 pound [lbs] = 0.45359237 kilogram [kg]
    return lbs * 0.45359237

def calc_BMI(weight, height):
    # BMI = kg/m^2
    return weight / height**2

def classify_BMI_2(bmi):
    classes = ["healthy", "unhealthy"]
    if bmi < 25.0:
        return 0 # classes[0]
    elif bmi >= 25.0:
        return 1 # classes[1]
    else:
        return -1 # "No categories"

def classify_BMI_4(bmi):
    classes = ["underweight", "normal", "overweight", "obese"]
    if bmi < 18.5:
        return 0 # classes[0]
    elif (bmi >= 18.5) & (bmi < 25.0):
        return 1 # classes[1]
    elif (bmi >= 25.0) & (bmi < 30.0):
        return 2 # classes[2]
    elif bmi > 30.0:
        return 3 # classes[3]
    else:
        return -1 # "No categories"