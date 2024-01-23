##
##q1= {
##"question": "Who developed Python Programming Language?",
##"options": [
##
##     "Wick van Rossum",
##     "Rasmus Lerdorf",
##     "Guido van Rossum",
##     "Niene Stom"
##
##],   
##      "answer": "Guido van Rossum"
##}
##
##
##q2 = {
##"question": "Which type of Programming does Python support?",
##"options": [
##    
##      "object-oriented programming",
##      "structured programming",
##      "functional programming",
##      "all of the mentioned",
##
##],
##      "answer":"all of the mentioned"
##}
##
##score=0
##
##q=[q1,q2]
##for i in q:
##    print(i["question"])
##    option= i["options"]
##    for j in range(len(option)):
##        print(f"    {chr(65+j)}) {option[j]}")
##
##    print()





### This function has a variable with
### name same as s.
##def f():
##	s = "Me too."
##	print(s)
##
### Global scope
##s = "I love Geeksforgeeks"
##f()
##print(s)

##nums = [1,2,3,4,5,6,7,8,9,10]
##odd_nums = [num for num in nums if num % 2 != 0]
##print(odd_nums)  # Output: [1, 3, 5, 7, 9]





##nums = [1,2,3,4,5,6,7,8,9,10]
##odd_nums = list(filter(lambda x: x % 2 != 0, nums))
##print(odd_nums)



nums = [1,2,3,4,5,6,7,8,9,10]
odd_nums = []
for num in nums:
    if num % 2 != 0:
        odd_nums.append(num)
print(odd_nums)

