"""
Given two words (begin_word and end_word), and a dictionary's word list, return
the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.

Each transformed word must exist in the word list. Note that begin_word is not
a transformed word.

Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"


"""
import string

words = set()
with open('words.txt') as f:    
    for w in f:
        w = w.strip()
        words.add(w)
    

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

    


# def get_neighbors(word):
#     neighbors = []

#     for w in words:
#         if len(w) == len(word):
#             diff_count = 0

#             for i in range(len(w)):
#                 if w[i] != word[i]:
#                     diff_count +=1

#                 if diff_count > 1:
#                     break

#             if diff_count == 1:
#                 neighbors.append(w)

#     return neighbors

def get_neighbors(word):
    neighbors = []

    letters = list(string.ascii_lowercase)

    word_letters = list(word)

    for i in range(len(word_letters)):
        for l in letters:
            word_letters_copy = list(word_letters)
            word_letters_copy[i] = l
            candidate_word = "".join(word_letters_copy)

            if candidate_word != word and candidate_word in words:
                neighbors.append(candidate_word)
                

    return neighbors


def bfs(begin_word, end_word):
       
        q = Queue()
        q.enqueue([begin_word])
		
        visited = set()
	
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
		
            if v not in visited:
                if v == end_word:
                    return path

                visited.add(v)
				
                for neighbor in get_neighbors(v):
                    new_path = path + [neighbor]
                    q.enqueue(new_path)


print(bfs('hit', 'cog'))