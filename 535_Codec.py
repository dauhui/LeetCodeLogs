class Codec:
    def __init__(self):
        self.urls = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.urls[longUrl] = len(self.urls) + 1
        return "https://tinyurl/" + str(self.urls[longUrl])
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        self.decode_key = {v: k for k, v in self.urls.items()}
        return self.decode_key[int(shortUrl.split("/")[-1])]
        
url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
print(codec.decode(codec.encode(url)))