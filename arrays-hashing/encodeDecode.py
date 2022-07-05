class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res, i = [], 0
        
        while i < len(s):
            j = i  # first numeric char will be at i, set j to that as well 
            while s[j] != "#": # wait till you find a "#"
                j+=1
            length = int(s[i:j])  # use i:j to get the number and convert to length
            res.append(s[j+1:j+1+length])  # then j+1 to j+1+length is where our word ends, add it to res
            i = j+1+length  # set i to beginning of the next number character
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))