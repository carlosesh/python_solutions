def number_length(num):
	if num == 0:
		return 1
	else:
		count = 0
		while int(num) > 0:
			count += 1
			num /= 10
		return count


print(number_length(10))
print(number_length(5000))
print(number_length(0))
print(number_length(4039182))
print(number_length(9999999999999999))
print(number_length(1))
print(number_length(777777777777777777777777777777))
