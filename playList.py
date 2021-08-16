from random import randint
from node_base_queue import Queue
from time import sleep


class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 6)


class MediaPlayerQueue(Queue):
    def __init__(self):
        super().__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        print(f'Count: {self.count}')

        while self.count > 0 and self.head is not None:
            current_track_node = self.dequeue()
            print(f'Now Playing: {current_track_node.title}')
            sleep(current_track_node.length)


''' Simular '''

tracks = []

with open('./music.txt', 'r') as f:
    tracks = f.readlines()

mediaPlayer = MediaPlayerQueue()

for track in tracks:
    mediaPlayer.add_track(Track(track))
    print(track)


mediaPlayer.play()
