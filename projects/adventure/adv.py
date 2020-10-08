from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Queue, Stack
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def traverse_graph(starting_room):
    # dft
    world = {}

    q = Stack()
    visited = set()

    #init with starting room
    q.push(starting_room)

    while q.size() > 0:
        
        room = q.pop()

        if room not in visited:
            world[room] = []
            visited.add(room)
            # gets directions in which you can move
            for direction in room.get_exits():
                # returns the room in that direction
                world[room].append(direction)
                new_room = room.get_room_in_direction(direction)
                q.push(new_room)

    return world 

world_map = traverse_graph(world.starting_room)  

def find_directions(world_map):
    traversal_path = []

    for room in world_map:
        print(room.name, world_map[room])
    
    return  traversal_path
    
traversal_path = find_directions(world_map)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
