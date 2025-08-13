'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
# print(motorcycles)

motorcycles.insert(0, 'ducati')
# print(motorcycles)

del motorcycles[2] # delete 'yamnaha' from the list
# print(motorcycles)

motorcycles.insert(2, 'yamaha') # insert 'yamaha' into the third position in the list
del motorcycles[0] # delete the first item 'ducati' from the list

# motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)


popped_motorcycle = motorcycles.pop() # the last item removed

print(motorcycles) # the last item was popped (removed), result = ['honda', 'yamaha']
print(popped_motorcycle) # the popped item saved as a variable 'popped_motorcycle', result = suzuki

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
'''

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # 리스트 4개 항목

too_expensive = 'ducati'
motorcycles.remove(too_expensive) # 리스트에서 'ducati'를 삭제함
print(motorcycles) # 이제 리스트는 ducati 없이 3개 항목

print(f"\nA {too_expensive.title()} is too expensive for me.")

motorcycles = []
print(motorcycles[-1])