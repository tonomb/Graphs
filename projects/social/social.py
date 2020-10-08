import math
import random

from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        possible_friendships = []
        
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        random.shuffle(possible_friendships)
        
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def populate_graph_2(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        target_friendships = num_users * avg_friendships
        total_frienships = 0

        while total_frienships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship(user_id, friend_id):
                total_frienships += 2       

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        
        # start at user_id, 
        # traverse all the tree and record all values that are connected
        # run bfs passing in all the values as a second number, set value to what comes back 
        visited = self.bft(user_id)
       
        for friend in visited:
           path = self.bfs(user_id, friend)
           visited[friend] = path

        return visited

    def get_frienships(self, user_id):
        """
        Get all friendships.
        """
        if user_id in self.users:
            return self.friendships[user_id]
       

    def bft(self, user_id):
        """
        Print each vertex in breadth-first order
        beginning from user_id.
        """
        visited = {}

        q = Queue()
    
        q.enqueue(user_id)

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                visited[v] = [user_id]
                for neighbor in self.get_frienships(v):
                    q.enqueue(neighbor)

        return visited 

    def bfs(self, starting_friend, end_friend):
        """
        Return a list containing the shortest path from
        starting_friend to end_friend in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_friend])
		# Create a Set to store visited vertices
        visited = set()
		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first PATH
            path = q.dequeue()
			# Grab the last vertex from the PATH
            v = path[-1]
			# If that vertex has not been visited...
            if v not in visited:
				# CHECK IF IT'S THE TARGET
                if v == end_friend:
				  # IF SO, RETURN PATH
                    return path
				# Mark it as visited...
                visited.add(v)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_frienships(v):
				  # COPY THE PATH
                    new_path = path[:]
                    new_path.append(neighbor)
				  # APPEND THE NEIGHOR TO THE BACK
                    q.enqueue(new_path)   

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
