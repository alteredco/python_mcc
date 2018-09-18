# 1
def difference(a,b):
	return a - b

# 2
def product(a,b):
	return a*b

# 3
def print_day(num):
	wd = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
	if num >=1 and num <=7:
		num = wd[num-1]
		return num
	else:
		return None

print(print_day(4))
print(print_day(41))

#4
def last_element(l):
	if l :
		return l[-1]
	else:
		return None

print(last_element([1,2,3,4]))
print(last_element([]))

#5
def number_compare(a ,b):
	if a > b:
		return "First is greater"
	elif a < b:
		return "Second is greater"
	else:
		return "Numbers are equal"

print(number_compare(1,1))
print(number_compare(1, 2))
print(number_compare(2,1))

#6
def single_letter_count(word, l):
	cnt =0
	l = l.lower()
	word = word.lower()
	for letter in word:
		if letter == l:
			cnt += 1
	return cnt

print(single_letter_count('amazing','A'))

#7
def multiple_letter_count(msg):
	char_list = list(msg)
	nums = list(range(1, len(char_list)+1))
	return dict( zip( char_list, nums ) )
	
print(multiple_letter_count("hello"))
print(multiple_letter_count("person"))

#8
def list_manipulation(li, com, loc, val=None):
	if com == "remove" and loc == "end":
		return li.pop()
	elif com == "remove" and loc == "beginning":
		return li.pop(0)
	elif com == "add" and loc == "beginning":
		li.insert(0, val)
		return li
	else:
		li.append(val)
		return li

print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20)) 
print(list_manipulation([1,2,3], "add", "end", 30))

#9
def is_palindrome(n):
	reverse_n = []
	length_n = len(n)
	while length_n:
		length_n -= 1
		reverse_n.append(n[length_n])
	return n == ''.join(reverse_n)

print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah')) # True
print(is_palindrome('robert')) # False

#10
def frequency(li, search):
	return li.count(search)

print(frequency([1,2,3,4,4,4], 4))
print(frequency([True, False, True, True], False))

#11
def flip_case(s, l):
	return ''.join(char.swapcase() if char.lower() == l.lower() else char for char in s)

print(flip_case("Hardy har har", "h"))

#12
def multiply_even_numbers(li):
	total = 1
	for i in li:
		if i%2 == 0:
			total = total * i
	return total

print(multiply_even_numbers([2,3,4,5,6]))

#13
def mode(li):
	f = {i: li.count(i) for i in li}
	max_f = max(f.values())
	pos_max_f = list(f.values()).index(max_f)
	return list(f.keys())[pos_max_f]

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))

#14
def capitalize(s):
	return s[:1].upper() + s[1:]

print(capitalize("tim"))
print(capitalize("matt"))

#15
def compact(li):
	return [i for i in li if i]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))

#16
def partition(li, fun):
	return [[i for i in li if fun(i)],[i for i in li if not fun(i)]]

def is_even(num):
		return num % 2 == 0

print(partition([1,2,3,4], is_even))

#17
def intersection(li1, li2):
	return [i for i in li1 if i in li2]

print(intersection([1,2,3], [2,3,4]))

#18
def once(fun):
	fun.is_called = False
	def inner(*p):
		if not(fun.is_called):
			fun.is_called = True
			return fun(*p)
	return inner

def add(a,b):
	return a + b

one_addition = once(add)

print(one_addition(2,2))
print(one_addition(2,2))
print(one_addition(12,200))

def find_short(s):
	words_li = s.split(" ")
	l_word = (min(words_li, key = len))
	l = len(l_word)
	return l

print(find_short("bitcoin take over the world maybe who knows perhaps"))
