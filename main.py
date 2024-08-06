import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def sort_songs(songs):
    socket.send_json(songs)

    response = socket.recv_json()
    
    return response

def main():
    songs = ["1. Not Like Us - Kendrick Lamar", "2. Good Luck, Babe! - Chappell Roan", "3. Who - Jimin"]
    
    sorted_songs = sort_songs(songs)
    print(sorted_songs)

main()
