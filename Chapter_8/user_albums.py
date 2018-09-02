def make_album(artist, title, number_of_tracks=''):
    """Returns a dictionary of artists and their album names."""
    album = {'artist': artist, 'title': title}
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album

while True:
    print("\nPlease enter an artist and album:")
    print("(enter 'q' to quit)")

    artist = input("Enter the name of an artist: ")
    if artist == 'q':
        break

    title = input("Enter the name of an album: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)