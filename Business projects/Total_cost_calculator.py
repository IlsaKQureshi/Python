def calculate_itemff_price():
    
    ff_price = float(input("Enter the price of the fashionflare item: \n"))
    ff_discount = 0.1
    ff_total_cost = ff_price - (ff_price * ff_discount)

    print(f"\nThe total cost of the fashionflare item is: {ff_total_cost}\n")

    delivery_fee = 1500
    marketing = 800


    if ff_price > 0 and ff_price < 5000:
      profit = 0.45
    elif ff_price >= 5000 and ff_price < 12000:
      profit = 0.4
    elif ff_price >= 12000 and ff_price < 20000:
      profit = 0.45
    elif ff_price >= 20000:
      profit = 0.95
    else:
      print("Invalid price range.")
      return

    total_cost = ff_total_cost + delivery_fee + marketing + (ff_total_cost * profit)
    print(f"The total cost for item listing is: {total_cost}\n")
    print(f"The profit for the item is: {total_cost - ff_total_cost}\n")

while True:
  calculate_itemff_price()

  again = input("Do you want to calculate the total cost for another item? (yes/no): \n").lower()
  
  if again != "yes":
    print("Thank you for using the total cost calculator. Goodbye!")
    break