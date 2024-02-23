import asyncio
from enum import Enum

import websockets
class Command(Enum):
    Play = 1
    PlayNext = 2
    PlayPrevious = 3
    GetMusicInfo = 4
    GetPlayerState = 5
    Like = 6
    VolumeUp = 7
    VolumeDown = 8
    Mute = 9
    SwitchPlayMode = 10
    SwitchShuffle = 11

def convert_to_string(index):
    commands = {
        1: "play",
        2: "play_next",
        3: "play_previous",
        4: "get_music_info",
        5: "get_play_state",
        6: "like",
        7: "volume_up",
        8: "volume_down",
        9: "mute",
        10: "switch_play_mode",
        11: "switch_shuffle"
    }
    return commands[index]

async def control_music():
    while True:
        async with websockets.connect('ws://127.0.0.1:8080/nons/api/v1') as websocket:
            user_input = int(input("Type your command: "))
            command = convert_to_string(user_input)
            await websocket.send(command)
            print(f"> Sent {command} command")

asyncio.run(control_music())
