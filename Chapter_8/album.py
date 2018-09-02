def make_album(artist, title, number_of_tracks=''):
    """Returns a dictionary of artists and their album names."""
    album = {'artist': artist, 'title': title}
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album

album = make_album('jimi hendrix', 'all along the watchtower')
print(album)

album = make_album('electric light orchestra', 'mr blue sky')
print(album)

album = make_album('blue swede', 'album name', '8')
print(album)