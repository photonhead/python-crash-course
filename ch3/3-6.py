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

# print the updated guest list
print(guestList) # ['kim nam-joon', 'jeong jae-seung', 'yoo si-min', 'jeong ho-seok']

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

print(f"Dear {guestList[0].title()}, I would like to invite you to my dinner party this Friday. Please RSVP by Wednesday.")
print(f"Dear {guestList[1].title()}, I would like to invite you to my dinner party this Friday. Please RSVP by Wednesday.")
print(f"Dear {guestList[2].title()}, I would like to invite you to my dinner party this Friday. Please RSVP by Wednesday.")
print(f"Dear {guestList[3].title()}, I would like to invite you to my dinner party this Friday. Please RSVP by Wednesday.")
print(f"Dear {guestList[4].title()}, I would like to invite you to my dinner party this Friday. Please RSVP by Wednesday.")
print(f"Dear {guestList[5].title()}, I would like to invite you to my dinner party this Friday. Please RSVP by Wednesday.")
print(f"Dear {guestList[6].title()}, I would like to invite you to my dinner party this Friday. Please RSVP by Wednesday.")
print(f"Dear {guestList[7].title()}, I would like to invite you to my dinner party this Friday. Please RSVP by Wednesday.")
print(f"Dear {guestList[8].title()}, I would like to invite you to my dinner party this Friday. Please RSVP by Wednesday.")