# Match Case
a = str(input("Enter Fruit Name: "))
a = a.lower()

match a:
    case "apple":
        print("Price of Apple is 100")
    case "banana":
        print("Price of Banana is 50")
    case "mango":
        print("Price of Mango is 150")
    case "orange":
        print("Price of Orange is 80")
    case "grapes":
        print("Price of Grapes is 70")
    case "papaya":
        print("Price of Papaya is 120")
    case "guava":
        print("Price of Guava is 90")
    case _:
        print(a.capitalize(), "is not available")
