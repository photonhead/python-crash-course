'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}
'''
'''
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

language_type = favorite_languages.get('jason', 'No language assigned to Jason.')
print(language_type)
'''
'''
# call keys as name and each values as language from favorite_languages dictionary using items() method
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# call keys as name from favorite_languages dictionary and print them in title() form
for name in favorite_languages.keys(): 
    print(name.title())
'''
'''
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}.") # dictionary의 key에 있는 이름 전부에게 인사

    if name in friends: # 그 중에서 특히 이름이 friends 리스트에 있다면
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!") # 이 메시지를 추가
'''
'''
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
'''
'''
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
'''
'''
# set() -> remove repetition
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(f"\t- {language.title()}")
'''
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

# dictionary item을 가져와서
for name, languages in favorite_languages.items():
    if len(languages) > 1:  # 값이 둘 이상인 경우
        print(f"\n{name.title()}'s favorite languages are:") # 복수형 텍스트
        for language in languages:
            print(f"\t{language.title()}") # 언어 나열
    else: # 값이 하나인 경우
        print(f"\n{name.title()}'s favorite language is {language.title()}.") # 단수형 텍스트