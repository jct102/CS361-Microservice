import zmq

def sort_songs(songs):
    sorted_songs = sorted(songs, key=lambda x: x.split('. ', 1)[1])
    return sorted_songs

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv_json()
    sorted_songs = sort_songs(message)

    socket.send_json(sorted_songs)
