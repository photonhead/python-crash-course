# range()를 list로 numbers에 저장함
numbers = list(range(1, 6))
print(numbers) # result = [1,2,3,4,5]

# range()에서 세 번째 argument는 얼만큼씩 건너뛸지를 나타내는 숫자
even_numbers = list(range(2, 11, 2)) # 2에서 11까지 숫자를 열거할 때 2씩 건너뛰라는 뜻
print(even_numbers) # result = [2, 4, 6, 8, 10] 