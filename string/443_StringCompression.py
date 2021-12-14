class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        for each consecutive repeating chracters
        - change in-placed
        
        - if len == 1, append character to s
        - otherwise, append chracter followed by the len
        
        from sol: apart from creating a new array, we can directly overwrite the original array
        """
        
        def add(chars, pre, count):
            if count == 1:
                chars.append(pre)
            else:
                for c in reversed(str(count)):
                    chars.append(c)
                chars.append(pre)
            return
        
        temp = []
        pre, count = chars.pop(), 1
        
        while chars:
            char = chars.pop()
            
            if char == pre:
                count += 1
            else:
                add(temp, pre, count)
                pre = char
                count = 1
                
        add(temp, pre, count)
        
        while temp: chars.append(str(temp.pop()))
        
        return len(chars)

