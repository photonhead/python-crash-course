# original guest list
guestList = ['steve jobs', 'jeong jae-seung', 'yoo si-min', 'carl sagan']

# print the guest who can't make it.
absentGuest1 = guestList[0]
absentGuest2 = guestList[-1]

# replacing absents with new guests.
newGuest1 = 'kim nam-joon'
newGuest2 = 'jeong ho-seok'

guestList[0] = newGuest1
guestList[-1] = newGuest2

# the updated guest list
# ['kim nam-joon', 'jeong jae-seung', 'yoo si-min', 'jeong ho-seok']

# add more guests
guestList.insert(1, 'kim seok-jin') 
# ['kim nam-joon', 'kim seok-jin', 'jeong jae-seung', 'yoo si-min', 'jeong ho-seok']

guestList.insert(2, 'min yoon-ki')
# ['kim nam-joon', 'kim seok-jin', 'min yoon-ki', 'jeong jae-seung', 'yoo si-min', 'jeong ho-seok']

guestList[3] = 'jeong ho-seok'
guestList[-1] = 'jeong jae-seung'
# ['kim nam-joon', 'kim seok-jin', 'min yoon-ki', 'jeong ho-seok', 'yoo si-min', 'jeong jae-seung']

guestList.insert(4, 'kim tae-hyung')
guestList.insert(5, 'park ji-min')
guestList.insert(6, 'jeon jung-kook')
# ['kim nam-joon', 'kim seok-jin', 'min yoon-ki', 'jeong ho-seok', 'kim tae-hyung', 'park ji-min', 'jeon jung-kook','yoo si-min', 'jeong jae-seung']

# add a new line that prints a message saying that you can invite only two people for dinner.
print(f"Dear All, Unfortunately, due to a table issue, we can only invite two people to our Friday night party this week.")

# use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
remove1 = guestList.pop(1)
remove2 = guestList.pop(1) 
remove3 = guestList.pop(1)
remove4 = guestList.pop(1)
remove5 = guestList.pop(1)
remove6 = guestList.pop(1)
remove7 = guestList.pop(1)
# index 1 항목이 사라져서 항목이 다 한칸씩 앞당겨지기 때문에 맨 앞이랑 맨 뒤만 남기고 하나씩 pop() 해내려면 인덱스는 계속 1이어야 함

print(f"Dear {remove1.title()}, We would appreciate your participation next time. We sincerely apologize for any inconvenience.")
print(f"Dear {remove2.title()}, We would appreciate your participation next time. We sincerely apologize for any inconvenience.")
print(f"Dear {remove3.title()}, We would appreciate your participation next time. We sincerely apologize for any inconvenience.")
print(f"Dear {remove4.title()}, We would appreciate your participation next time. We sincerely apologize for any inconvenience.")
print(f"Dear {remove5.title()}, We would appreciate your participation next time. We sincerely apologize for any inconvenience.")
print(f"Dear {remove6.title()}, We would appreciate your participation next time. We sincerely apologize for any inconvenience.")
print(f"Dear {remove7.title()}, We would appreciate your participation next time. We sincerely apologize for any inconvenience.")

# print a message to each of the two people still on your list, letting them know they're still invited.
attendee1 = guestList[0]
attendee2 = guestList[1]

print(f"\nDear {attendee1.title()}, You've been invited to our party this Friday night. Congratulations!")
print(f"Dear {attendee2.title()}, You've been invited to our party this Friday night. Congratulations!")

# use del to remove the last two names from your list, so you have an empty list.
del guestList[0]
del guestList[-1]

# print your list to make sure you actually have an empty list at the end of your program.
print(guestList) # empty list