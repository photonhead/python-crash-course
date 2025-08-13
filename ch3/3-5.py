'''
3-5. Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.

1) Start with your program from 3-4. Add a print() call at the end of your program, stating the name of the guest who can't make it.
2) Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
3) Print a second set of invitation messages, one for each person who is still in your list.
'''

# original guest list
guestList = ['steve jobs', 'jeong jae-seung', 'yoo si-min', 'carl sagan']

# print the guest who can't make it.
absentGuest1 = guestList[0]
absentGuest2 = guestList[-1]

print(f"Absents: {absentGuest1.title()}, {absentGuest2.title()}")

# replacing absents with new guests.
newGuest1 = 'kim nam-joon'
newGuest2 = 'jeong ho-seok'

guestList[0] = newGuest1
guestList[-1] = newGuest2

# print the new guests.
print(f"New Guests: {newGuest1.title()}, {newGuest2.title()}")

# print a second set of invitation messages with people who can attend.
print(f"\nDear All,\n\nUnfortunately {absentGuest1.title()} and {absentGuest2.title()} let me know that they can\'t attend our dinner party.\nFortunately, {newGuest1.title()} and {newGuest2.title()} expressed their interest in attending the party on Friday.\nTherefore, the final participants on Friday dinner party will be as follows:\n")

print(f"Final Guest List:\n- {guestList[0].title()}\n- {guestList[1].title()}\n- {guestList[2].title()}\n- {guestList[3].title()}\nTotal: 4 Members\n")

print(f"I look forward to meet you all on Friday! Thank you.\n\nSincerely,\nJay")