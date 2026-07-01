class Solution:

    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_chunks = []
        for s in strs:
            # Combine length, delimiter, and the actual string
            encoded_chunks.append(f"{len(s)}#{s}")
        return "".join(encoded_chunks)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        decoded_strs = []
        i = 0
        
        while i < len(s):
            # Find the position of the delimiter
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length of the string
            length = int(s[i:j])
            
            # Move index right past the delimiter
            start_of_str = j + 1
            end_of_str = start_of_str + length
            
            # Extract the actual string segment
            decoded_strs.append(s[start_of_str:end_of_str])
            
            # Move the pointer to the next block
            i = end_of_str
            
        return decoded_strs