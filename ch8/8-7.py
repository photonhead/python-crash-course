'''
8-7. Album:
Write a function called make_album() that builds a dictionary describing a music album.
The function should take in an artist name and an album title, 
and it should return a dictionary containing these two pieces of information.
Use the function to make three dictionaries representing different albums.
Print each return value to show that the dictionaries are storing the ablum information correctly.

Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
If the calling line includes a value for the number of songs,
add that value to the album's dictionary.
Make at least one new function call that includes the number of songs on an album.
'''
# define a function make_album()
def make_album(artist_name, album_title, num_songs=None):
    '''Album information dictionary with optional number of songs.'''
    album_info = {'Artist': artist_name, 'Album': album_title, 'Number of Songs': num_songs}

    '''Get each values for artist, album title, and num_songs from dictionary.'''
    artist = album_info['Artist']
    album = album_info['Album']
    num_songs = album_info['Number of Songs']

    '''Set a condition for optional parameter: number of songs'''
    if num_songs:
        full_album_info = f"<{album.title()}> by {artist} ({num_songs} songs)"
    else:
        full_album_info = f"<{album.title()}> by {artist}"
    
    return print(full_album_info)

# call the function three times with/without the number of songs on an album
make_album('RM', 'right place, wrong person', 11)
make_album('j-hope', 'killin\' it girl')
make_album('BTS', 'Proof', 35)