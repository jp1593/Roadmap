# camelCase
# PascalCase
# snake_case

class StarCookie: 
    milk = 0.1
    def __init__(self, color, weight):
        self.color = color 
        self.weight = weight
        
print(StarCookie.__dict__)

star_cookie1 = StarCookie("Red", 16)
print(star_cookie1.__dict__)

star_cookie2 = StarCookie("Blue", 20) 
print(star_cookie2.milk, star_cookie2.color, star_cookie2.weight)

