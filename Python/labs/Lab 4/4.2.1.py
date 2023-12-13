def calculate(**k):
    if k["income"] >= 30000 and k["income"] <= 40000 and k["children"] > 2:
        return k["children"] * 1000
    elif k["income"] >= 20000 and k["income"] <= 30000 and k["children"] > 2:
        return k["children"] * 1500
    elif k["income"] <= 20000:
        return k["children"] * 2000


while True:
    income = input("Your income: ")
    children = input("Amount of childrens: ")
    value = calculate(income= int(income), children= int(children))
    print(f"Total Subsidy: {value}")
