class Area:
    def __init__(self,l,w):
      self.__l = l
      self.__w = w

    def getarea(self):
        return self.__l * self.__w
    
class Volume(Area):
    def __init__(self,l,w,h):
        super().__init__(l,w)
        self.__h = h

    def getvolume(self):
        return self.getarea() * self.__h    

class Density(Volume):
    def __init__(self,l,w,h,m):
        super().__init__(l,w,h)
        self.__m = m

    def getdensity(self):
        return self.__m/self.getvolume()    

d = Density(2,3,4,100)

print(f"Area : {d.getarea()}")
print(f"Volume : {d.getvolume()}")
print(f"Density : {d.getdensity():.2f}")