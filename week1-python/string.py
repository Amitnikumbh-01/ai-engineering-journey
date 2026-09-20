# s="artificial intelligence"
# print(len(s))
# print(s[::-1])
# print(s[0])

# # ---------------

ch="machine learning"
count=0
# ch.lower()
# for char in ch:
#     if char =='a' or char =='e' or char =='i' or char =='o' or char =='u':
#         count+=1

# print(count)

vowel='aeiouAEIOU'

for char in ch:
    if char in vowel:
        count+=1

print(f"Vowel is: {count}")


palindrome= "amit"
rvr= palindrome[::-1]
if palindrome == rvr:
    print(True)

else:
    print(False)
