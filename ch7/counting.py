'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
'''
'''
current_number = 0 # 0부터 시작
while current_number < 10: # 10 미만까지만 실행
    current_number += 1 # 1씩 증가
    if current_number % 2 == 0: # 숫자를 2로 나눠서 0이 되면 (즉, 짝수)
        continue # 계속 조건 진행 (즉, 다시 숫자 증가하러 보냄)
        
    print(current_number) # 홀수였다면 조건을 빠져나옴, if문 밖에 있으므로 진행되어 출력
'''
x = 1
while x <= 5:
    print(x)
    x += 1 