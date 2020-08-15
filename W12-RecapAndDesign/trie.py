"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
# Notes: looks like diff b/w search and starts with is that search requires null ending

# Define Node class
class Node:
    def __init__(self, letter, child_dict):
            self.char = letter
            self.children = child_dict
    
    def get_char(self):
        return self.char
    
    def get_children(self):
        return self.children
    
    def set_char(self, new_char):
        self.char = newChar
        
    def add_child(self, new_child):
        self.children[new_child] = Node(new_child, {})

# Define Trie Class
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('', {})
        

    def print_trie(self):
        """
        Print the trie in a semi-structured format
        """
        queue = [self.root, None]
        while queue:
            
            curr_val = queue.pop(0)
            if curr_val == None:
                print(' | ')
            else:
                print(curr_val.get_char() + ' ', end='')
                # Add all of the children (nodes) of the current char to the queue
                chrn = curr_val.get_children()
                for child in chrn:
                    queue.append(chrn[child])
                queue.append(None)
        print('--------------------------------')


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # Find the prefix that aligns with the string being inserted
        curr_node = self.root
        for i in range(len(word)):
            char = word[i]
            curr_set = curr_node.get_children()
            if char in curr_set:
                curr_node = curr_set[char]
            # Then add a chain of nodes for the rest of the values
            else:    
                for j in range(i, len(word)):
                    char = word[j]
                    curr_node.add_child(char)
                    curr_node = curr_node.get_children()[char]
                break
        # Be sure to add the nil child at the end that represents that the string is ended
        curr_node.add_child('nil')
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
    trie = Trie()
    trie.insert('hi')
    trie.print_trie()
    trie.insert('hello')
    trie.print_trie()
    trie.insert('hey')
    trie.print_trie()