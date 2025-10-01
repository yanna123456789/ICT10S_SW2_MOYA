from pyscript import display
#Restaurant Order System (Python Data Types)

#String
restaurant_name = "Duo Brew"
owner_name = "Zach Natividad"

#Integer
year_since = 2025

#Float
tax_rate = 0.08

#Boolean
has_delivery = True
is_dine_in = True
is_takeaway = False

#List
product_names = ["Carbonara", "Garlic Bread", "Ceasar Salad"]
beverages = ["Iced Tea", "Sparkling Water"]

#Tuple
business_hours = ("11:00 AM", "10:00 PM")

#Dictionarymenu =
menu = {
        "Carbonara" : 79.99,
"Garlic Bread": 50.00,
"Caesar Salad": 150.00,
"Iced Tea": 30.00,
"Sparkling Water": 20.00
}

#Set
common_allergens = {"gluten," "dairy", "nuts"}

#Display restaurant Information
display(restaurant_name, target="name1")
display(owner_name, target="owner1")
display(year_since, target="since")
display("Menu Pricelist", target="heading")

#Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Carbonara'[0]]:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Garlic Bread'[1]]:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Caesar salad'[2]]:.2f}", target="price3")

display(product_names[3], target="prod4")
display(f"₱{menu['Iced Tea'[3]]:.2f}", target="price4")
display(beverages[1], target="bev1")
display(f"₱{menu['Sparkling Water'[3]]:.2f}", target="price5")

#Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}" , target="openingHours")

#Display order type
display(f"Dine-In Available", target="orderType")
display(f"Takeaway Available: {is_takeaway}", target="takeaway")
display(f"Common Allergens: {', '.join(common_allergens)}", target="allergens")
display(f"Tax Rate: {tax_rate*100}%", target="taxrate")
display(f"Since: {year_since}", target="since")
display("Thank you for choosing Duo Brew!", target="thankyou")
