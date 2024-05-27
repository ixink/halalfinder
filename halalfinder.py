#In the name of God, the Most Gracious, the Most Merciful.

#Note: Do not copy code without permission ask for permission. I will give you permission without any cost.

#Coded by: ixink( Rayhan Ahmed )
#Contact me: t.me/ImamSword
#Hire me: http://linkedin.com/in/rayhan-ahmed-uiu
#Github: http://github.com/ixink
import subprocess
print("بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ")

print(" _   _       _       _     _____ _           _    ")      
print("| | | | __ _| | __ _| |   |  ___(_)_ __   __| | ___ _ __")
print("| |_| |/ _` | |/ _` | |   | |_  | | '_ \ / _` |/ _ \ '__|")
print("|  _  | (_| | | (_| | |   |  _| | | | | | (_| |  __/ |   ")
print("|_| |_|\__,_|_|\__,_|_|___|_|   |_|_| |_|\__,_|\___|_|   ")
print("____________________________ coded by: ixink(Rayhan Ahmed)")
print("_____________ contact me: linkedin.com/in/rayah-ahmed-uiu")
print("___________________________________________________________")

# Database of halal and haram food items
halal_meat = ["chiken", "beef", "lamb", "goat", "duck", "goose", "cow", "buffalo", "camel", "sheep", "dumba", "deer", "raindeer"]
halal_grain = ["rice", "wheat", "oat", "lentil", "chikpea" "pasta", "bread", "breakfast cereal"]
halal_milk_products = ["milk", "yogourt", "cheese", "ice cream", "microbial rennet", "tofu",]
halal_nuts = ["almond", "walnut", "cashews", "sunflower seed"]
halal_beverages = ["fruit juice", "carbonated drink", "punch", "tea", "coffee"]
halal_fat = ["butter", "margarine", "mayonnaise", "vegetable oil", "sunflower oil", "soyabin oil"]
halal_miscellaneous = ["chutney", "coconut milk", "jam", "pickle", "spicies"]
halal_sweetner = ["honey", "sugar", "syrup", "chocolate liquor", "agar", "carrageenan"]
halal_fruit = ["apple", "apricot", "avocado", "banana", "blackberry", "blueberry", "cherry", "clementine", "coconut", "cranberry", "grape", "grapefruit", "guava", "honeydew melon", "kiwi", "kumquat", "lemon", "lime", "mango", "mangosteen"]
halal_vegetable = ["acorn squash", "alfalfa sprouts", "all blue potato", "amaranth", "ambercup aquash", "anise", "artichoke", "arugula", "ash Gourd", "asparagus", "avocado", "adzuki bean","ahipa", "aonori", "arame", "arikara squash", "arrowroot", "asian greens", "azuki bean","baby boo pumpkin", "bamboo shoot", "banana pepper", "banana squash", "basil","bean sprout", "beet", "belgian endive", "bell pepper", "bintje potato", "bitter melon","black bean", "black-eyed pea", "black radish", "broccoli", "brussels sprouts","butternut squash", "cabbage", "cantaloupe", "carrot", "cauliflower", "celery","chayote", "chickpea", "chicory", "chinese Cabbage", "collard Greens", "corn","cucumber", "daikon radish", "delicata squash", "dill", "eggplant", "endive","fennel", "garlic", "ginger", "green bean", "green onion", "jicama", "kale","kohlrabi", "leek", "lettuce", "lima Bean", "mung Bean", "mushroom", "mustard greens","napa cabbage", "okra", "onion", "parsnip", "pea", "pumpkin", "radish", "romaine lettuce","rutabaga", "salsify", "snow Pea", "spinach", "squash", "sweet potato", "swiss chard","taro", "tomato", "turnip", "watercress", "watermelon", "winter Squash", "zucchini"]
haram_items = ["shark", "monkey", "whale", "blue whale", "urine", "crocodile", "snake", "pig", "piggy", "dog", "cat", "poop", "chigar", "chigaratte", "tobaco", "pork", "alcohol", "wine", "beer", "spirit", "vanila extract", "animal shortening", "broth", "gelatin", "ham", "bacon", "lard", "l-cysteine", "lipase", "mono", "diglycerides", "pepsin", "rennet", "sodium stearoyl-lactylate", "whey", ]
halal_milk =["cow","goat", "sheep", "camel", "buffalo"]
# User interaction
while True:
    def main():
        
        print("Welcome to the Halal Food Finder!  [Under development]\n")
        print("Choose an option:")
        print("1. Meat")
        print("2. Grain")
        print("3. Milk Product")
        print("4. Nut")
        print("5. Beverage")
        print("6. Fat")
        print("7. Miscellaneous")
        print("8. Sweetner")
        print("9. Fruit")
        print("10. Vegetable")
        print("11. Fish")
        print("12. Other")
        print("\n")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            food_name = input("Enter the food name: ")
            print("Is slaughtered according to Islamic dietary law (Zabihah)?\n1. Yes\n2. No\n")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                if food_name.lower() in halal_meat:
                    print(f"{food_name} is halal meat. \nSay, 'Bismillsh Before Eat.'\n")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
                elif food_name.lower() in haram_items:
                    print(f"{food_name} is haram.\n")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
                else:
                    print(f"Unknown food: {food_name}\n")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
            else:
                print(f"{food_name} is not slaughtered according to Islamic dietary law (Zabihah). It's Haram")
                
        elif choice == 2:
            food_name = input("Enter the food name: ")
            if food_name.lower() in halal_grain:
                print(f"{food_name} is halal grain.\nSay, 'Bismillsh Before Eat.'")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            elif food_name.lower() in haram_items:
                print(f"{food_name} is haram.")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            else:
                print(f"Unknown food: {food_name}")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
        elif choice == 3:
            food_name = input("Enter the food name: ")
            milk_name = input("Milk product come from which animal: ")
            if milk_name.lower() in halal_milk:
                if food_name.lower() in halal_milk_products:
                    print(f"{food_name} is halal milk product. \nSay, 'Bismillsh Before Eat.\n'")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
                elif food_name.lower() in haram_items:
                    print(f"{food_name} is haram.")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
                else:
                    print(f"Unknown food: {food_name}")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(2)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
            elif milk_name.lower() in haram_items:
                    print(f"{food_name} is haram.")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
            else:
                print(f"We are researching on {milk_name} milk")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            
            
        elif choice == 4:
            food_name = input("Enter the food name: ")
            print("Is it poisonous?\n1. Yes\2. No\n")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                if food_name.lower() in halal_nuts:
                    print(f"{food_name} is halal nut. \nSay, 'Bismillsh Before Eat.'")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
                elif food_name.lower() in haram_items:
                    print(f"{food_name} is haram.")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
                else:
                    print(f"Unknown food: {food_name}")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
            elif choice == 2:
                print(f"{food_name} is haram")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            else:
                print("Invalid. Choose 1 for Yes.\nChoose 2 for No")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
        elif choice == 5:
            food_name = input("Enter the food name: ")
            if food_name.lower() in halal_beverages:
                print(f"{food_name} is halal beverage. \nSay, 'Bismillsh Before Eat.'")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            elif food_name.lower() in haram_items:
                print(f"{food_name} is haram.")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            else:
                print(f"Unknown food: {food_name}")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
        elif choice == 6:
            food_name = input("Enter the food name: ")
            if food_name.lower() in halal_fat:
                print(f"{food_name} is halal fat. \nSay, 'Bismillsh Before Eat.'")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            elif food_name.lower() in haram_items:
                print(f"{food_name} is haram.")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            else:
                print(f"Unknown food: {food_name}")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
        elif choice == 7:
            food_name = input("Enter the food name: ")
            if food_name.lower() in halal_miscellaneous:
                print(f"{food_name} is halal miscellaneous. \nSay, 'Bismillsh Before Eat.'")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            elif food_name.lower() in haram_items:
                print(f"{food_name} is haram.")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            else:
                print(f"Unknown food: {food_name}")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
        elif choice == 8:
            food_name = input("Enter the food name: ")
            if food_name.lower() in halal_sweetner:
                print(f"{food_name} is halal sweetner. \nSay, 'Bismillsh Before Eat.'")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            elif food_name.lower() in haram_items:
                print(f"{food_name} is haram.")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            else:
                print(f"Unknown food: {food_name}")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
        elif choice == 9:
            food_name = input("Enter the food name: ")
            if food_name.lower() in halal_fruit:
                if food_name.lower() in haram_items:
                    print(f"{food_name} is haram")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
                else:
                    print(f"{food_name} is halal fruit. \nSay, 'Bismillsh Before Eat.'")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
            else:
                print(f"Unknown food: {food_name}")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
        elif choice == 10:
            food_name = input("Enter the food name: ")
            if food_name.lower() in halal_vegetable:
                if food_name.lower() in haram_items:
                    print(f"{food_name} is haram")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
                else:
                    print(f"{food_name} is halal vegetable. \nSay, 'Bismillsh Before Eat.'\nRemember: If mix any haram product with halal product, it will be haram to eat.")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
            else:
                print(f"Unknown food: {food_name}")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
        elif choice == 11:
            food_name = input("Enter the food name: ")
            print("Is it poisonous or does it take humans or large animals as food?\n1. No\n2. Yes")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                if food_name.lower() in haram_items:
                    print(f"{food_name} is haram")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
                else:
                    print(f"{food_name} Halal Fish. ")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
            elif choice == 2:
                print("Haram. You can't eat it.")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            else:
                print("Invalid. Choose 1 for No.\nChoose 2 for Yes")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
        elif choice == 12:
            food_name = input("Enter the food name: ")
            if food_name.lower() in haram_items:
                    print(f"{food_name} is haram")
                    print("Do you like to ask more?\n")
                    choice = int(input("Yes(1)\nNo(2)\n"))
                    if choice == 1:
                        subprocess.run(["python3", "halalfinder.py"], check=True)
                    elif choice == 2:
                        print("Thanks for using")
                    else:
                        print("Please one of them: 1 or 2")
            else:
                print(f"We are researching on {food_name}")
                print("Do you like to ask more?\n")
                choice = int(input("Yes(1)\nNo(2)\n"))
                if choice == 1:
                    subprocess.run(["python3", "halalfinder.py"], check=True)
                elif choice == 2:
                    print("Thanks for using")
                else:
                    print("Please one of them: 1 or 2")
            
            
        else:
            print("Invalid choice. Please select 1 or 12.")
            print("Do you like to ask more?\n")
            choice = int(input("Yes(1)\nNo(2)\n"))
            if choice == 1:
                subprocess.run(["python3", "halalfinder.py"], check=True)
            elif choice == 2:
                print("Thanks for using")
            else:
                print("Please one of them: 1 or 2")
            


    if __name__ == "__main__":
        main()
    break
#halal food info collected from: https://www.halalrc.org/images/Research%20Material/Literature/Guide%20to%20Halal%20Foods.pdf
