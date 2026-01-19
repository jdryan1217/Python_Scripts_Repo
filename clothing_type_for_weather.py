def clothing_type(temp):
    if clothing_type > 65:
        clothing = "T-Shirt"
    elif clothing_type > 50 and clothing_type < 65:
        clothing = "Sweatshirt"
    elif clothing_type > 32 and clothing_type < 51:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72)) # Should print T-Shirt
print(clothing_type(55)) # Should print Sweatshirt
print(clothing_type(65)) # Should print Sweatshirt
print(clothing_type(50)) # Should print Jacket
print(clothing_type(45)) # Should print Jacket
print(clothing_type(32)) # Should print Heavy Coat
print(clothing_type(0)) # Should print Heavy Coat