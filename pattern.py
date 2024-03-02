'''
# Pseudo Code.
1 - Create a variable row_count = 5
2 - Create a variable start = 1
3 - Now multiply row_count by 2 and store in end variable.
4 - Now apply for loop row_number in range(start,end)
5 - Now create star_count variable and apply check row_number if row number <= row_count else end - row_number.
6 - Apply For loop for i in range(star_count)
7 - Print("*",end="")
8 - print() for the space.
'''

row_count = 5
start = 1
end = (2 * row_count) 

for row_number in range(start, end):
    star_count = row_number if row_number <= row_count else end - row_number
    for i in range(star_count):
        print("*", end=" ")
    print()