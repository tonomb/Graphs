from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Queue, Stack
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt" #15
# map_file = "maps/test_loop.txt" # 17
# map_file = "maps/test_loop_fork.txt" # 37
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

def traverse_graph():
    traversal_path = []
    current_path=[]
    start_room = player.current_room.id
    # dft
    graph = {}

    q = Stack()
    visited = set()

    #init with starting room
    q.push(start_room)

    while q.size():
        
        room = q.pop()

        if room not in visited:

            if room not in graph:
                graph[room] = {}
            
            # gets directions in which you can move
            for direction in player.current_room.get_exits():
                # returns the room in that direction 
                if direction not in graph[room]:   
                    graph[room][direction] = '?'
                
            #choose random unexplored direction
            unexplored_directions =[]
            for k,v in graph[room].items():
                if v == '?':
                    unexplored_directions.append(k)

            # if unexplored directions exist traverse
            if len(unexplored_directions) > 0:
                r = random.choice(unexplored_directions)
                old_room = player.current_room.id
                player.travel(r)
                #log direction 
                current_path.append(r)
                traversal_path.append(r)
                graph[room][r] = player.current_room.id
                graph[player.current_room.id] = {}  
                if r == 'n':
                    graph[player.current_room.id]['s'] = old_room
                if r == 's':
                    graph[player.current_room.id]['n'] = old_room
                if r == 'e':
                    graph[player.current_room.id]['w'] = old_room
                if r == 'w':
                    graph[player.current_room.id]['e'] = old_room
        
                q.push(player.current_room.id)
                # no unexplored directions, backtrack until the node you were at
                
            else:
                visited.add(player.current_room.id)
    
                if len(visited) == 500:
                    break
                d = current_path.pop()
                if d == 'n':
                    player.travel('s')
                    traversal_path.append('s')
                if d == 's':
                    player.travel('n')
                    traversal_path.append('n')
                if d == 'e':
                    player.travel('w')
                    traversal_path.append('w')
                if d == 'w':
                    player.travel('e')
                    traversal_path.append('e')
                   
                q.push(player.current_room.id)

            
    return traversal_path 

# traversal_path = traverse_graph()  


def solve_maze():

    #dft
    lq=[]
    ls=[]
    traversal_path = []
    start_room = player.current_room
    # dft
    graph = {}

    q = Stack()
    visited = set()

    #init with starting room
    q.push(start_room)

    while q.size():
        room = q.pop()
        print('at room' , room.id)
        if room.id not in graph:
                graph[room.id] = {}
    

        if room not in visited:
            # print(room.id, 'not visited')
            visited.add(room)

            for direction in room.get_exits():
                new_room = room.get_room_in_direction(direction)
                if direction not in graph[room.id]:   
                    graph[room.id][direction] = '?'
                
                ls.append(new_room.id)
                q.push(new_room)
            # print('stack', lq)

            unexplored_paths = Queue()
            explored = set()

        
            for k,v in graph[room.id].items():
               
                if v == '?':
                    new_room = room.get_room_in_direction(k)
                  
                    graph[room.id][k] = new_room.id
                    
                    graph[new_room.id] = {} 
                   
                    if k == 'n':
                        graph[new_room.id]['s'] = room.id
                    if k == 's':
                        graph[new_room.id]['n'] = room.id
                    if k == 'e':
                        graph[new_room.id]['w'] = room.id
                    if k == 'w':
                        graph[new_room.id]['e'] = room.id

                    
                    for direction in new_room.get_exits():
                        newer_room = new_room.get_room_in_direction(direction)
                        if direction not in graph[new_room.id]:   
                            graph[new_room.id][direction] = '?'

                        print(graph)
                        q.push(new_room)

                    path = traverse_path(room, new_room.id)
                    direction = get_directions(path, graph)
                    traversal_path.append(direction)


                else:
                    pass
                

    print(traversal_path)
    return traversal_path


def traverse_path(start, end):
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()

        q.enqueue([start])
		
        visited = set()
		
        while q.size() > 0:
			
            path = q.dequeue()

            v = path[-1]
            if v not in visited:
				# CHECK IF IT'S THE TARGET
                if v.id == end:
                    real_path =[]
                    for p in path:
                        real_path.append(p.id) 
                    # print(real_path)
                    return real_path

                visited.add(v)
				
                for direction in v.get_exits():
                    new_room = v.get_room_in_direction(direction)
                    new_path = path + [new_room]
                    q.enqueue(new_path)
               
def get_directions(path, graph):
    move_from = path[0]
    move_to = path[-1]

    possibilities = graph[move_from]
    for k,v in possibilities.items():
        if v == move_to:
            return k
 
start = player.current_room
end = '?'
# traverse_path(start, 2)
traversal_path = solve_maze()    


# print(traversal_path)
# len(traversal_path)
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
