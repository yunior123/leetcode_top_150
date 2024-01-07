from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = word
        
        def dfs(i, j, node):
            c = board[i][j]
            if c not in node:
                return
            node = node[c]
            if '$' in node:
                res.append(node['$'])
                del node['$']
            board[i][j] = '#'
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, node)
            board[i][j] = c
        
        res = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)
        return res
        

# test
s = Solution()
board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(s.findWords(board, words)) # ["eat","oath"]
board = [["a","b"],["c","d"]]
words = ["abcb"]
print(s.findWords(board, words)) # []