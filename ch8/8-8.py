'''
8-8. User Albums:
Start with your program from Ex 8-7.
Write a while loop that allows users to enter an album's artist and title.
Once you have that information, call make_album() with the user's input
and print the dictionary that's created.
Be sure to include a quit value in the while loop.
'''
# define a function make_album()
def make_album(artist_name, album_title, num_songs=None):
    '''Album information dictionary with optional number of songs.'''
    album_info = {
        'Artist': artist_name, 
        'Album': album_title, 
        'Number of Songs': num_songs
        }

    # --- while loop begins ----
    active = True

    while active:
        '''Get the user input for an album's artist, title, and number of songs (optional)'''
        prompt = "\nTo add your favorite album, please provide the following information "
        prompt += "(Artist name is case-sensitive. Enter 'q' at any time to quit.)"
        print(prompt)

        artist_name = input("Aritst name: ")
        if artist_name == 'q': # quit - stop while loop
            active = False
            break

        album_title = input("Album title: ")
        if album_title == 'q': # quit - stop while loop
            active = False
            break

        num_songs = input("Number of songs (optional, type 0 to skip): ")
        if num_songs == 0: # if 0, add it as None to the dictionary
            num_songs = None        
        elif num_songs == 'q': # quit - stop while loop
            active = False
            break

        '''Add user input information to the dictionary'''
        album_info['Artist'] = artist_name
        album_info['Album'] = album_title
        album_info['Number of Songs'] = num_songs
        
        '''Let user know the album is added to the dictionary'''
        confirm_msg = f"\nYour album has been added successfully."
        print(confirm_msg)
    # --- while loop finished. ----
    
    '''Get each values for artist, album title, and num_songs from dictionary.'''
    artist = album_info['Artist']
    album = album_info['Album']
    num_songs = album_info['Number of Songs']

    if num_songs != None:
        full_album_info = f"<{album.title()}> by {artist} ({num_songs} songs)"
    else:
        full_album_info = f"<{album.title()}> by {artist}"

    return(full_album_info)

make_album()