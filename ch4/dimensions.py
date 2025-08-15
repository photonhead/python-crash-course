dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100) # tuple 안에 있는 항목을 바꾸고 싶다면 자체를 재정의해야 함
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100, 300) 
print("\nModified dimensions again:")
for dimension in dimensions:
    print(dimension)