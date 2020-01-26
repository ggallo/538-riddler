class TrieNode(object):

    def __init__(self, is_word):
        self._is_word = is_word
        self._next = {}

    @property
    def is_word(self):
        return self._is_word
    
    @is_word.setter
    def is_word(self, val):
        self._is_word = val

    def set_next(self, k, v):
        self._next[k] = v
        return self._next[k]

    def get_next(self, k):
        return self._next.get(k, None)

class Trie(object):

    def __init__(self, wordList=None):
        self._head = TrieNode(False)
        if wordList:
            for w in wordList:
                self.add_word(w)

    def add_word(self, word):
        target_word = word.lower()
        cur_node = self._head
        for l in target_word:
            cur_next = cur_node.get_next(l)
            if not cur_next:
                cur_node.set_next(l, TrieNode(False))
            cur_node = cur_node.get_next(l)
        cur_node.is_word = True

    def is_word(self, word):
        target_word = word.lower()
        cur_node = self._head
        for l in target_word:
            if not cur_node.get_next(l):
                return False
            cur_node = cur_node.get_next(l)
        return cur_node.is_word

