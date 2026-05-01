class Node:
    def __init__(self):
        self.child = {}
        self.EOW = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        cur.EOW = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(node, i):

            if len(word) == i:
                return node.EOW
            c = word[i]
            
            if c == ".":
                if node.child:
                    for childs in node.child.values():
                        if dfs(childs, i+1):
                            return True
                    return False
                
                if not node.child:
                    return False
            else:
                if c in node.child:
                    return dfs(node.child[c], i+1)
                else:
                    return False

        return dfs(cur, 0)
