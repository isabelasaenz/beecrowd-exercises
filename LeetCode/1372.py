# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        # inicializa uma variável de classe que irá armazenar o comprimento máximo do caminho zigzag
        self.ans = 0
        
        # define uma função de busca em profundidade (DFS) que percorre a árvore binária
        def dfs(node):
            
            if not node:
                return -1,-1 # return -1 para todos os nós null
            
            # chama a função DFS recursivamente para os nós à esquerda e direita do nó atual e armazena os resultados em duas variáveis.
            left,right = dfs(node.left),dfs(node.right)
            
            # calcula o comprimento máximo do caminho zigzag atualizado e armazena na variável self.ans.
            self.ans = max(self.ans,left[1]+1,right[0]+1) 
            
            # retorna uma tupla contendo o comprimento do caminho mais longo indo para a esquerda e o caminho mais longo indo para a direita, respectivamente.
            return left[1]+1,right[0]+1
        
        # chama a função DFS para a raiz da árvore
        dfs(root)
        
        # retorna o comprimento máximo do caminho zigzag encontrado
        return self.ans