big_number = input("Enter A Number >  ")
num_factors = 0
check_number = 1

while check_number < big_number / 2 :
	remainder = big_number % check_number
	print big_number, "=", check_number, "\r",
	if remainder == 0 :
		print big_number, "=", check_number, "*", big_number / check_number
		num_factors = num_factors + 1
	check_number += 1

if num_factors == 1:
	print "Prime"