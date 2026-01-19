# This function converts measurement equivalents. Output is formatted 
2	# as, "x ounces equals y pounds", with y limited to 2 decimal places. 
3	def convert_weight(ounces):
4	
5	    # Conversion formula: 1 pound = 16 ounces
6	    pounds = ounces/16 
7	    
8	    # The result is composed using the .format() method. There are two
9	    # placeholders in the string: the first is for the "ounces" 
10	    # variable and the second is for the "pounds" variable. The second
11	    # placeholder formats the float result of the conversion 
12	    # calculation to be limited to 2 decimal places.
13	    result = "{} ounces equals {:.2f} pounds".format(ounces,pounds)
14	    return result
15	
16	
17	print(convert_weight(12)) # Should be: 12 ounces equals 0.75 pounds
18	print(convert_weight(50.5)) # Should be: 50.5 ounces equals 3.16 pounds
19	print(convert_weight(16)) # Should be: 16 ounces equals 1.00 pounds
