'''Approch 1: BFS
'''
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()      
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
        '''
        Complexity Analysis

Time Complexity: O(M2×N), where MM is the length of each word and NN is the total number of words in the input word list.

For each word in the word list, we iterate over its length to find all the intermediate words corresponding to it. 
Since the length of each word is MM and we have NN words, the total number of iterations the algorithm takes to 
create all_combo_dict is M×N. Additionally, forming each of the intermediate word takes O(M) time because of the 
substring operation used to create the new string. This adds up to a complexity of O(M2×N).

Breadth first search in the worst case might go to each of the NN words. For each word, we need to examine MM possible 
intermediate words/combinations. Notice, we have used the substring operation to find each of the combination. Thus, M combinations take O({M} ^ 2). 
As a result, the time complexity of BFS traversal would also be O(M2×N).

Combining the above steps, the overall time complexity of this approach is O(M2×N).

Space Complexity: O(M2×N).

Each word in the word list would have MM intermediate combinations. To create the all_combo_dict dictionary we save an intermediate word as the key 
and its corresponding original words as the value. Note, for each of MM intermediate words we save the original word of length MM. This simply means, 
for every word we would need a space of {M}^2
  to save all the transformations corresponding to it. Thus, all_combo_dict would need a total space of O(M2×N).
Visited dictionary would need a space of O(M×N) as each word is of length MM.
Queue for BFS in worst case would need a space for all O(N) words and this would also result in a space complexity of O(M \times N)O(M×N).
Combining the above steps, the overall space complexity is O(M2×N) + O(M * N)O(M∗N) + O(M * N)O(M∗N) = O(M2×N) space.

Optimization: We can definitely reduce the space complexity of this algorithm by storing the indices corresponding to each word instead of storing the word itself.
        '''

'''Approch 2: Bidirectional Breadth First Search
'''
from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            # Next states are all the words which share the same intermediate state.
            for word in self.all_combo_dict[intermediate_word]:
                # If the intermediate state/word has already been visited from the
                # other parallel traversal this means we have found the answer.
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    # Save the level as the value of the dictionary, to save number of hops.
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queues for birdirectional BFS
        queue_begin = collections.deque([(beginWord, 1)]) # BFS starting from beginWord
        queue_end = collections.deque([(endWord, 1)]) # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # One hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0

'''
Time Complexity: O(M2×N), where MM is the length of words and NN is the total number of words 
in the input word list. 
 Similar to one directional, bidirectional also takes O(M2×N) time for finding out all the 
 transformations. But the search time reduces to half, since the two parallel searches meet 
 somewhere in the middle.

Space Complexity: O(M2×N), to store all MM transformations for each of the NN words in the 
all_combo_dict dictionary, same as one directional. But bidirectional reduces the search space. 
It narrows down because of meeting in the middle.
'''