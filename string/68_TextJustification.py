class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        - add word until word length and total length of required blanks exceeds maxWidth
        - calculate required extra blanks
        """
        res, sentence, numberOfWords, length = [], [], 0, 0
        for word in words:
            if length + len(word) + numberOfWords - 1 < maxWidth:
                numberOfWords += 1
                length += len(word)
                sentence.append(word)
            else:
                if numberOfWords > 1:
                    padding = (maxWidth - length) // (numberOfWords - 1)
                    extraPadding = (maxWidth - length) % (numberOfWords - 1)
                    temp = ""
                    for i in range(len(sentence)-1):
                        temp += sentence[i] + " "*padding
                        if extraPadding:
                            temp += " "
                            extraPadding -= 1
                    temp += sentence[-1]
                    res.append(temp)
                else:
                    res.append(sentence[0] + " "*(maxWidth - length))
                
                numberOfWords = 1
                length = len(word)
                sentence = [word]
        
        if sentence:
            temp = " ".join(sentence)
            padding = maxWidth - len(temp)
            res.append(temp + " "*padding)
            
        return res

