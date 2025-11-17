

class PlaylistIterator:
    def __init__(self, songs):
        self.songs = songs
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.songs:
            raise StopIteration("Playlist is empty")

     
        song = self.songs[self.index]

       
        self.index = (self.index + 1) % len(self.songs)

        return song

    def prev(self):
        if not self.songs:
            raise StopIteration("Playlist is empty")

        
        self.index = (self.index - 1) % len(self.songs)

        return self.songs[self.index]




songs = ["Believer", "Faded", "Heat Waves", "On My Way", "Alone"]

player = PlaylistIterator(songs)

print(next(player))   
print(next(player))   
print(next(player))   

print(player.prev())  

print(next(player))   
print(next(player))   
print(next(player))   
print(next(player))   
