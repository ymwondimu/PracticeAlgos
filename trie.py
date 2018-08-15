from collections import defaultdict

def create_trie(word, d):
    print ("'" + word + "'")
    if word == None or word == "":
        return {}
    else:
        start = word[0]
        if start in d:
            child = d[start]
            create_trie(word[1:], child)
        else:
            child = {}
            d[start] = child
            create_trie(word[1:], child)

def create_trie_iterative(word):
    d = {}
    current_dict = d
    for char in word:
        current_dict = current_dict.setdefault(char, {})
    current_dict["end"] = "end"

    return d

class Tree:
    def __init__(self):
        self.dict = {}

    def add(self, word):
        current_dict = self.dict

        for char in word:
            current_dict = current_dict.setdefault(char, {})
        current_dict["end"] = "end"

    def search(self, word):
        current_dict = self.dict
        for char in word:
            if char in current_dict:
                current_dict = current_dict[char]
            else:
                return False

        
        if "end" in current_dict:
            return True
        else:
            return False



def main():
    t = Tree()
    t.add("hello")
    t.add("hells")
    print (t.search("hell"))

if __name__ == "__main__":
    main()