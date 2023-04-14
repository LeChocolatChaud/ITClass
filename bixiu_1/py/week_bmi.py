weekdays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
height = float(input("请输入身高(m): "))
weights = input("请输入一周的体重(kg)，用空格分隔：").split()

bmis = []
for weight in weights:
    bmis.append(round(float(weight)/height**2, 1))

for i in range(7):
    print(weekdays[i], "- BMI =", bmis[i])