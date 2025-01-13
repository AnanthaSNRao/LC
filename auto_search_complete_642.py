
'''
https://algo.monster/liteproblems/642
'''
class TrieNode:
    def __init__(self):
        # Initialize 27 children for each letter in the alphabet plus the space character
        self.children = [None] * 27
        self.value = 0  # Frequency of word ending at this node
        self.word = ''  # The word ending at this node, if any

    def insert(self, word, frequency):
        # Inserts a word into the trie along with its frequency
        node = self
        for char in word:
            index = 26 if char == ' ' else ord(char) - ord('a')  # Mapping 'a'-'z' to 0-25, ' ' to 26
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.value += frequency
        node.word = word

    def search(self, prefix):
        # Searches for a node in the trie that corresponds to the given prefix
        node = self
        for char in prefix:
            index = 26 if char == ' ' else ord(char) - ord('a')
            if node.children[index] is None:
                return None
            node = node.children[index]
        return node

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.trie = TrieNode()
        for sentence, frequency in zip(sentences, times):
            self.trie.insert(sentence, frequency)
        self.typed_characters = []  # Keeps track of characters typed by the user

    def input(self, character):
        # Returns autocomplete suggestions based on the characters inputted so far

        def dfs(node):
            # Perform a depth-first search to find all words with their frequencies
            if node is None:
                return
            if node.value:
                results.append((node.value, node.word))
            for next_node in node.children:
                dfs(next_node)

        if character == '#':
            # The user finished typing a word; update the trie and reset the input
            current_sentence = ''.join(self.typed_characters)
            self.trie.insert(current_sentence, 1)  # Increment the frequency of the word
            self.typed_characters = []
            return []

        results = []
        self.typed_characters.append(character)
        current_prefix = ''.join(self.typed_characters)
        node = self.trie.search(current_prefix)
        # If the prefix doesn't exist in the trie, return an empty list
        if node is None:
            return []
        # Otherwise, find and return autocomplete suggestions
        dfs(node)
        # Sort the results in descending order of frequency, and alphabetically for ties
        results.sort(key=lambda x: (-x[0], x[1]))
        # Return the top 3 suggestions, or fewer if there aren't enough
        return [entry[1] for entry in results[:3]]