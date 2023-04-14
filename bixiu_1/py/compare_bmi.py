bmi = float(input("请输入BMI指数："))
bmi = round(bmi, 1)
if bmi >= 18.5 and bmi <= 25:
    print("正常")
else:
    print("需注意")