words = ["joma", "john", "jack", "techlead"]


class Node:
    def __init__(self):
        self.count = 0
        self.children = {}


class Try:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                current_node.children[character] = Node()
            current_node = current_node.children[character]
            current_node.count += 1

    def unique_prefix(self, word):
        current_node = self.root
        prefix = ""

        for character in word:
            if current_node.count == 1:
                return prefix
            else:
                current_node = current_node.children[character]
                prefix += character
        return prefix


def shortest_unique_prefix(words):
    trie = Try()

    for word in words:
        trie.insert(word)

    unique_prefixes = []

    for word in words:
        unique_prefixes.append(trie.unique_prefix(word))
    return unique_prefixes


print(shortest_unique_prefix(words))
