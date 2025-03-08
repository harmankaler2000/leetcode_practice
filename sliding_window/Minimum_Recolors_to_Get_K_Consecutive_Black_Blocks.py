class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if 'B' not in blocks:
            return k
        min_recolour = float('inf')
        for i in range(len(blocks)):
            m = i
            n = i + k
            if n > len(blocks):
                break
            recolour = blocks[m:n].count('W')
            if recolour < min_recolour:
                min_recolour = recolour
        return min_recolour
        
