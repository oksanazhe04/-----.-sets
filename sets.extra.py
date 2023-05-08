#A
numbers = "1 2 3 2 1" 
numbers = numbers.split()
unique_numbers = set(numbers)
print(len(unique_numbers))

#B
list1 = [1, 2, 3]
list2 = [4, 3, 2]
count = len(set(list1) & set(list2))

print(count)

#C
list1 = [1, 2, 3]
list2 = [4, 3, 2]
growth = sorted(set(list1) & set(list2))

print(growth)

#D
numbers_list = "1 2 3 2 3 4" 
numbers_list = numbers_list.split()
used = set()
for num in numbers_list:
    if num in used:
        print("YES")
    else:
        print("NO")
        used.add(num)     

#F1
text = "She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."
words = text.split() 
newwords = set(words) 
length = len(newwords)  
print(length) 

#F2
n = int(input())
possible_numbers = set(range(1, n+1)) 

while True:
    phrase = input().strip()
    if phrase == "HELP":
        break

    numbers = set(map(int, phrase.split()))
    phrase2 = input().strip()
    if phrase2 == "NO":
        possible_numbers -= numbers

    else:
        possible_numbers &= numbers

print(sorted(possible_numbers))


