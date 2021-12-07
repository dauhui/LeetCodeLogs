import random
import string

class Codec:

    def __init__(self):
        self.longToShort = {}
        self.shortToLong = {}
        self.characters = string.ascii_letters + "0123456789"
        
    def getUniqueCode(self):
        code = None
        while not code or code in self.shortToLong:
            code = "".join(random.choice(self.characters) for _ in range(6))
        return code

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.longToShort: return self.longToShort[longUrl]

        shortUrl = 'http://tinyurl.com/' + self.getUniqueCode()
        
        self.shortToLong[shortUrl] = longUrl
        self.longToShort[longUrl] = shortUrl
        
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.shortToLong[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

