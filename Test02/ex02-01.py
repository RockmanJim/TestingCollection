# 1、输入一个人的身高\(m\)和体重\(kg\)，根据BMI公式（体重除以身高的平方）计算他的BMI指数。
height = float(input("Plz input your height: "))
weight = float(input("Plz input your weight: "))
bmi = weight / pow(height, 2)
print("Your BMI is %f" % bmi)
if bmi < 18.5:
    print("Too light")
elif 18.5 <= bmi < 25:
    print("normal")
elif 25 <= bmi < 28:
    print("Overweight")
elif 28 <= bmi < 32:
    print("Obesity")
else:
    print("Severe obesity")
