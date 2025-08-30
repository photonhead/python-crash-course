'''
8-8. User Albums: Start with your program from Ex 8-7.
Write a while loop that allows users to enter an album's artist and title.
Once you have that information, call make_album() with the user's input and print the dictionary that's created.
Be sure to include a quit value in the while loop.
'''
def make_album():
    active = True # to break in while loop

    # --- while loop begins --- 
    while active:
        prompt = "\nPlease add album details to the database. "
        prompt += "Artist name is case-sensitive, and type in order first name and last name (if needed)."
        prompt += "\n(Press 'q' when you want to stop.)\n"
        print(prompt)

        artist = input("- Artist name?: ")
        if artist == 'q': # when user input is 'q', 
            active = False # end the while loop
            break

        album = input("- Album title?: ").title() # album title format
        if album == 'q':
            active = False
            break

        num_songs = input("- Number of songs?: ") # String type
        if num_songs == '0': # when user input is '0', change it to None
            num_songs = None
        elif num_songs == 'q':
            active = False
            break
        else:
            num_songs == int(num_songs) # change type from String to integer
        
        database = {
            'Artist': artist, 
            'Album': album, 
            'Number of Songs': num_songs}
        
        # print(database) # dictionary input test

        for album_info in database.items():
            ## album_info formats 
            if num_songs == None:
                album_info = f"\'{album}\' by {artist}"
            else:
                album_info = f"\'{album}\' by {artist} ({num_songs} songs)"
                
        print(album_info)
    # --- while loop finished! --- 

    print("Done. Thank you!") # when user input is 'q', show this message

# call the function
make_album()

''' Postmortem: 드디어 풀었다! ＼\ ٩( ᐛ )و /／
◦ num_of_songs -> user input 값은 숫자라도 String! (분하다.. 알고 있었는데...)
    • 유저가 0을 입력해도 타입이 스트링이기 때문에 num_of_songs == '0' (그냥 0으로 쓰면 안 됨!)
◦ 제멋대로 오해하고 있었던 부분: 
    • 함수 마지막에 return 써야 한다고 생각
    • user input album info가 dictionary에 누적되어 담겨야 한다고 생각
        • 실제로는 그냥 3가지 정보를 받은 후 정의한 포맷에 맞게 출력해 주면 됨
        • 한 번에 하나의 앨범 정보(3가지 정보)를 포맷대로 보여주기만 하면 됨
◦ 불필요했던 부분:
    • dictionary에 value를 변수로 추가한다고 정의한 후 다시 dictionary에 key에 맞춰 value를 추가하라고 할 필요 없음
'''