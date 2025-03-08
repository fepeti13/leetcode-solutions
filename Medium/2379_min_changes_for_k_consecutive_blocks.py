class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        min_white = k
        for i in range(0, k):
            if blocks[i] == "W":
                white += 1

        if(white < min_white):
            min_white = white

        for i in range(k, len(blocks)):
            if blocks[i-k] == "W":
                white -= 1
            if blocks[i] == "W":
                white += 1

            if white < min_white:
                min_white = white
            
        return min_white