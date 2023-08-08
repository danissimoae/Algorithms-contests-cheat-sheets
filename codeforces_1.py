'''###Бронирование переговорки
#Задано nn интервалов. Требуется найти максимальное количество взаимно непересекающихся интервалов.
#Два интервала пересекаются, если они имеют хотя бы одну общую точку.
#В первой строке задано одно число nn (1≤n≤100)(1≤n≤100) — количество интервалов.
#В следующих nn строках заданы интервалы li,rili​,ri​ (1≤li≤ri≤50)(1≤li​≤ri​≤50).

a = int(input())
intervals = []
for i in range(a):
    intervals.append(list(map(int,input().split())))

intervals.sort()
prev = intervals[0]
count = 1

for i, current_interval in enumerate(intervals):
    for follow_interval in intervals[i + 1:]:
        if current_interval[1] <= follow_interval[0]:
            break
        count+=1
print(count)



##Сортировка выбором
##Реализуйте сортировку выбором.


n = int(input())

list = []
for i in range(n):
    list.append(input())

def findsmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1,len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selectionsort(array):
    new_arr = []
    for i in range(len(array)):
        smallest = findsmallest(array)
        new_arr.append(array.pop(smallest))
        return new_arr

print(selectionsort(list))


# Count the number of Duplicates


# Write a function that will return the count of distinct
# case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain
# only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    text = text.upper()
    d = {x: text.count(x) for x in sorted(set(text))}
    cnt = 0
    lst = list(d.values())
    for i in range(len(lst)):
        if lst[i]>1:
            cnt+=1
    return(cnt)



# Return Negative
# In this simple assignment you are given a number and have
# to make it negative. But maybe the number is already negative?

def make_negative( number ): # 1
    if number <= 0:
        return(number)
    else:
        n_number = int("-" + str(number))
        return(n_number)

def make_negative( number ): # 2
    return number if number<=0 else int("-" + str(number))



# Sum without highest and lowest number
# Sum all the numbers of a given array ( cq. list ),
# except the highest and the lowest element ( by value, not by index! ).
# If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given
# array is an empty list or a list with only 1 element, return 0.
# The highest or lowest element respectively
# is a single element at each edge, even if there
# are more than one with the same value.

def sum_array(arr):
    if arr is None:
        return 0
    if len(arr) == 1 or len(arr) == 0:
        return 0
    mx,mn = max(arr), min(arr)
    arr.remove(mx)
    arr.remove(mn)
    return(sum(arr))



def count_adjacent_pairs(st):
    slist = st.upper()
    cnt = 0
    d = {x: slist.count(x) for x in slist.split()}
    values = list(d.values())
    print(values)
    for i in range(len(values)):
        if values[i]>=2:
            cnt+=1
    return cnt


print(count_adjacent_pairs("cat cat dog dog cat cat"))

def count_adjacent_pairs(st):
    slist = st.lower().split()
    cnt = 0
    prev_word = None
    for word in slist:
        if word == prev_word:
            continue
        elif slist.count(word) > 1:
            cnt+=1
        prev_word = word
    return cnt
    



# You are given an initial 2-value array (x). You will use this to calculate a score.
# If both values in (x) are numbers, the score is the sum of the two.
# If only one is a number, the score is that number.
# If neither is a number, return 'Void!'.

# Once you have your score, you must return an array of arrays.
# Each sub array will be the same as (x) and the number of sub arrays should be equal to the score.

# if (x) == ['a', 3] you should return [['a', 3], ['a', 3], ['a', 3]].

def explode(arr):
    cnt = 0
    if all(isinstance(item,int) for item in arr):
        cnt += sum(arr)
        return cnt*[arr]
    elif any(type(item)==int for item in arr):
        cnt += sum(x for x in arr if (type(x) == int))
        return cnt*[arr]
    else:
        return("Void!")






# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith,
# but they are not capitalized in the same way he originally typed them.

def to_jaden_case(string):
    s1 = string.split()
    s2 = [item.capitalize() for item in s]
    s3 = " ".join(str(x) for x in s)
    return s3






# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application
# form that will tell prospective members which category they will be placed.

# To be a senior, a member must be at least 55 years old and have
# a handicap greater than 7. In this croquet club,
# handicaps range from -2 to +26; the better the player the lower the handicap.

def open_or_senior(data):
    ans = []
    for item in data:
        if item[0]>=55 and item[1]>7:
            ans.append(str("Senior"))
        else:
            ans.append(str("Open"))
    return ans

def nb_year(p0, percent, avg, p):
    ans = []
    percent = percent/100
    while p0<p:
        p0+=p0*percent+avg
        ans.append(p0)
    return(len(ans))





# Growth of a Population
# p0, percent, aug
# (inhabitants coming or leaving each year), p (population to equal or surpass)
# In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the
# town need to see its population greater or equal to p = 1200 inhabitants?

def nb_year(p0, percent, avg, p): # 1
    n = 0
    while p0<p:
        n+=1
        p0 = p0 + int(p0*percent/100) + avg
    if p0>=p:
        return n
    return n

def nb_year(p0, percent, avg, p): # 2
    ans = []
    percent = int(percent/100)
    while p0<p:
        p0+=p0*percent)+avg
        ans.append(p0)
    return(len(ans))





# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
# anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
    if pin.isdigit() and (len(pin)==4 or len(pin)==6):
        return True
    else:
        return False




def perfect_square(square):
    list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
    s = square.split("\n")
    r = "qwertyuiopasdfghjklzxcvbnmQW-ERTYUIOPASDFGHJ+KLZXCVBNMйцукенгшщзхъфывапр:олджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ_=+[]';/,!@#$%^&*()~`"

    if r in s or (len(s) not in list):
        return False
    cnt = len(s[0])
    for item in s:
        if len(item)!= cnt:
            return False
    return True
print(perfect_square("+"))

def perfect_square(square):
    list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
    s = square.split("\n")
    r = "qwertyuiopasdfghjklzxcvbnmQW-ERTYUIOPASDFGHJ+KLZXCVBNMйцукенгшщзхъфывапр:олджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ_=+[]';/,!@#$%^&*()~`"
    for i in range(len(s)):
        if s[i] in r:
            return False
    if len(s) in list:
        return True


# Reduce but Grow
# Given a non-empty array of integers, return the result of multiplying the values together in order.

def grow(arr):
    cnt = arr[0]
    for i in range(1,len(arr)):
        cnt = cnt * arr[i]
    return cnt




# In a factory a
# printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.
# The colors used by the printer are recorded in
# a control string. For example a "good" control string would
# be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...
# Sometimes there are problems:
# lack of colors, technical malfunction and a "bad"
# control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.
# You have to write a function printer_error
# which given a string will return the error rate
# of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.
# The string has a length greater or equal
# to one and contains only letters from ato z.

def printer_error(s):
    lst = "nopqrstuvwxyz"
    l = len(s)
    d = {x: s.count(x) for x in lst}
    m = sum(d.values())
    return f'{m}/{l}




# Given a string of digits, you should replace any digit below 5 with '0'
# and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(x):
    l = "1234"
    h = "56789"
    for char in l:
        x = x.replace(char,"0")
    for char in h:
        x = x.replace(char,"1")
    return xprint(fake_bin("21399999999124123"))



# Bit Counting
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the 
# binary representation of that number. You can guarantee that input is non-negative.

def count_bits(n):
    l = []
    bi = bin(n)[2:]
    return sum(int(digit) for digit in str(bi))
    
print(count_bits(1234))




# In this kata you will create a function that takes a list of non-negative integers
# and strings and returns a new list with the strings filtered out.

def filter_list(l):
    ans = []
    for i in l:
        if type(i) != str:
            ans.append(i)
    return ans

print(filter_list([1,2,'aasf','1','123',123]))





# Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value.
# The indices of these items should then be returned in a tuple / list
# (depending on your language) like so: (index1, index2).

def two_sum(numbers, target):
    for i, number_a in enumerate(numbers):
        for j, number_b in enumerate(numbers):
            if number_a + number_b == target and i != j:
                return (i, j)
    return False




# Given an array of integers.
# Return an array, where the first element is
# the count of positives numbers and the second element
# is sum of negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.

def count_positives_sum_negatives(arr):
    if arr==[]:
        return []
    pos = 0
    neg = 0
    for i in arr:
        if i<0:
            neg+=i
        elif i>0:
            pos+=1
    ans = []
    ans.append(pos)
    ans.append(neg)
    return ans



# List reverse

def fun(lst):
    for i in range(int(len(lst)/2)):
        item_at_i = lst[i]
        lst[i] = lst[len(lst) - i - 1]
        lst[len(lst) - i - 1] = item_at_i 
    return lst





# Check to see if a string has the same amount of 'x's
# and 'o's. The method must return a boolean and be case
# insensitive. The string can contain any char.

def xo(s):
    s = s.upper()
    print(s)
    x = 0
    o = 0
    for i in range(len(s)):
        if s[i]=="X":
            x+=1
        if s[i]=="O":
            o+=1
    print(x,o)
    if x==o:
        return True
    else:
        return False




# Ones and Zeroes
# Given an array of ones and zeroes,
# convert the equivalent binary value to an integer

def binary_array_to_number(arr):
    s = ""
    for i in arr:
        s+=str(i)
    return int(s,2)'''

