#membuat class
class televisi:
  def __init__(self,merk,channel,remote,volume): 
    self.merk = merk
    self.channel = channel
    self.remote = remote
    self.__volume = None

  def turontelevisi(self):
    print('televisi ON',  self.remote, ':', self.merk)
  def turnofftelevisi(self):
    print('televisi OFF',self.remote, ':', self.merk)
  def setvolume(self, num):
    #private
    self.__volume = num
    print('volume = ', self.__volume)

  def getVolume(self):
    return self.__volume

  def gantichannel(self):
    print('Televisi channel :', self.channel)


#membuat childclass
#overriding
class Television(televisi):
  def __init__(self,merk,channel,remote,volume):
    super(Television, self).__init__(merk,channel,remote,volume)
  def gantichannel(self):
    print('Televisi berganti ke channel :', self.channel)


TV1 = televisi('Polytron', 45, 'Mode', 100)
TV2 = Television('LG', 65, 'Mode', 100)


print(TV1)

#atribut ke objek
TV1.turontelevisi()
TV2.turnofftelevisi()
TV1.setvolume(100)
TV2.gantichannel()
print(TV1.getVolume())

