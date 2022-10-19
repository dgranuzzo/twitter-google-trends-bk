
# https://pypi.org/project/google-search/

from googlesearch import search

class Google_Pysearch:
   def __init__(self,name_search):
      self.name = name_search

   def Gsearch(self):
      count = 0
      for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=1,pause=2):
         count += 1
         print (count)
         print(i + '\n')


if __name__=='__main__':
   gs = Google_Pysearch("Tutorialspoint Python")
   gs.Gsearch()
