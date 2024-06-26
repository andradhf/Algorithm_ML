class HashTable:
  def __init__(self,size):
    self.size = size
    self.table = {}
    for i in range(size):
      self.table[i] = []
  
  def hash(self,key):
    return key % self.size
  
  def get(self,key):
    return self.table[self.hash(key)]
  
  def put(self,key,value):
    bucket = self.table[self.hash(key)]
    if value not in bucket:
      bucket.append(value)
      
table = HashTable(8) 
books = [
  "The Little Prince",
  "The Old Man and the Sea",
  "The Little Mermaid",
  "Beauty and the Beast",
  "The Last Leaf",
]
for book in books: 
  key = sum(map(ord,book))
  table.put(key,book)

judul = 'The Old Man and the Sea'
key = sum(map(ord,judul))
bucket = table.get(key)
print(key,bucket)