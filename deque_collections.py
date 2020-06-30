from collections import deque

d = deque()
d.append(1) # adiciona ao lado direito
d.appendLeft(2) # adiciona ao lado esquerdo
d.append(3)
d.appendLeft(4)

# 4, 2, 1, 3

d.remove(2)

for i in d:
  print(i)