#Exercise 1

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(200, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $200 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# Exercise 2

# Defining a function with mutiple parameters
def apply_discount(price, tier):
    if tier == 'gold':
        return price * 0.85  
    elif tier == 'silver':
        return price * 0.90  
    elif tier == 'bronze':
        return price * 0.95  
    else:
        return price  

# Calling the function with different tiers
original_price = 200

for tier in ['gold', 'silver', 'bronze', 'none']:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

    # Exercise 3

    def final_price(price, tax_rate, discount_tier):
        discounted_price = apply_discount(price, discount_tier)
        tax = calculate_tax(discounted_price, tax_rate)
        return discounted_price + tax

    # Calling the final_price function
    print(f"final_price(200, 0.07, 'gold'): ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

orders =[(200, 'gold'), (150, 'silver'), (100, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    final = final_price(price, 0.07, tier)
    print(f"Price: ${price}| Tier: {tier}| Total: ${final:.2f}")

#Exercise 6

x =100

def double_it():
    x = 999 # local x
    return x * 2

print(x)
print(double_it())
print(x)

# Self-Assesment:
# 1. The first bug I noticed was on line 6, where total = sale should have been total += sale, and I found it only after asking AI. This shows that my instinct is to reach for AI before tracing the code myself, so next time I’ll add a print(total) inside the loop and talk through each line before asking for help.
# 2. apply_discount(price, tier) takes an item’s price and a tier name and returns the price after a 15%, 10%, or 5% discount, or the original price for any other tier. A colleague could mostly use it from its name and inputs alone, but they’d have to guess that tiers must be lowercase and that an unrecognized tier silently gets no discount. A docstring listing the valid tiers and that fallback behavior would make it fully usable without reading the body.
# 3. I used AI to find bugs for excercise 5 and to help me understand the bugs and why they prodiced an error.
