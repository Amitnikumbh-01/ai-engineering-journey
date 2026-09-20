# age = 5
# if age >= 18:
#     print("Adult")
#     print("Can vote")
# print("This runs always")   # not indented, so outside the block

# -------------------------------------------
# score = int(input("Enter your marks"))

# if score >=90:
#     grade='A'

# elif score >=80:
#     grade='B'

# elif score >=70:
#     grade="C"

# elif score>=60:
#     grade='D'

# else:
#     grade="F"

# print(f"Student grade is : {grade}")
# -----------------------------------------------------



# score= int(input("Enter your score : "))
# status = "pass" if score>=70 else "fail"
# print(status)



# -----------------------------------------
# age, has_id = 25, True

# if age >= 18 and has_id:
#     print("Allowed")

# if not has_id or age < 18:
#     print("Denied")

# # Membership and chained comparison
# if "a" in "data":
#     print("found")

# --------------------------------------------

# for fruit in ["apple", "banana", "cherry"]:
#     print(fruit)

# for i in range(5):           # 0,1,2,3,4
#     print(i)

# for i in range(2, 10, 3):    # start, stop, step -> 2, 5, 8
#     print(i)

# names = ["Amit", "Riya", "Sam"]
# scores = [90, 85, 70]

# # enumerate: index + value
# for i, name in enumerate(names):
#     print(i, name)

# # zip: loop over two lists together
# for name, score in zip(names, scores):
#     print(f"{name}: {score}")

# # reversed and sorted
# for n in sorted(scores, reverse=True):
#     print(n)

# -----------------------------------------
# count = 3
# while count > 0:
#     print(count)
#     count -= 1

# # Common pattern: loop until valid input
# while True:
#     answer = input("Enter a number: ")
#     if answer.isdigit():
#         break
#     print("Not a number, try again")

# -------------------------------------------
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i * j, end=" ")
#     print()

for i in range(1,5):
    for j in range (i):
        print("* ",end=" ")
    print()