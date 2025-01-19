'''
https://algo.monster/problems/alien_dictionary
'''

from typing import List

from collections import defaultdict, deque

def alienOrder(words):
    # Step 1: Initialize the graph
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}

    # Step 2: Build the graph
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        
        # Check for invalid case: word2 is a prefix of word1
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""
        
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break

    # Step 3: Perform topological sort
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)
        
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the result length doesn't match the total unique letters, there's a cycle
    if len(result) != len(in_degree):
        return ""

    return "".join(result)

if __name__ == "__main__":
    words = ["baa", "abcd", "abca", "cab", "cad"]
    res = alienOrder(words)
    print(','.join(res))
