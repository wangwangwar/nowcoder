#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
# 思路：
# dict[string][dict]
# {
#   "a": {
#       exists: bool,
#       dict: dict()
#       }
# }

# @lc code=start


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dict = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        d = self._dict
        for i in range(len(word)):
            c = word[i]
            if c in d:
                if i == len(word) - 1:
                    d[c]["exist"] = True
                d = d[c]["next"]
                continue
            next_level_dict = dict()
            if i == len(word) - 1:
                exist = True
            else:
                exist = False
            d[c] = {"exist": exist, "next": next_level_dict}
            d = next_level_dict

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        d = self._dict
        exist = False
        for c in word:
            if c in d:
                exist, d = d[c]["exist"], d[c]["next"]
                continue
            return False
        return exist

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        d = self._dict
        for c in prefix:
            if c in d:
                d = d[c]["next"]
                continue
            return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

if __name__ == '__main__':
    obj = Trie()
    obj.insert("abc")
    print(obj.search("abc"))
    print(obj.search("ab"))
    print(obj.search("abce"))
    print(obj.startsWith("ab"))
    print(obj.startsWith("abc"))
    print(obj.startsWith("abce"))
