import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def sort_songs(songs):
    socket.send_json(songs)

    response = socket.recv_json()
    
    return response

def main():
    songs = ["1. Song1", "2. Song2", "3. Song3"]
    
    sorted_songs = sort_songs(songs)
    print(sorted_songs)
