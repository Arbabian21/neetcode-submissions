class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 # where we put our reversed input

        for i in range(32):
            bit = (n >> i) & 1 # 1 bit (0 bit for 0 based indexing) is on 
                               # the far right and 32nd bit (31st for 0 based 
                               # indexing) is on the far left
            # >> moves right by i bits so starting far left 
            res = res | (bit << (31 - i)) # placing it in far right

        return res