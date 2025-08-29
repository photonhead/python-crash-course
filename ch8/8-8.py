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