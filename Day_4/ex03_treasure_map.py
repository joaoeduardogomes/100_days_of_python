"""
O exercÃ­cio consiste em gerar um pequeno mapa do tesouro de tamanho 3x3. O 'X', naturalmente, marcaria o local.
"""

# ð¨ Don't change the code below ð
row1 = ["â¬ï¸","ï¸â¬ï¸","ï¸â¬ï¸"]
row2 = ["â¬ï¸","â¬ï¸","ï¸â¬ï¸"]
row3 = ["â¬ï¸ï¸","â¬ï¸ï¸","â¬ï¸ï¸"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# ð¨ Don't change the code above ð

#Write your code below this row ð
col = int(position[0]) - 1
row = int(position[1]) - 1

map[row][col] = "X"


#Write your code above this row ð

# ð¨ Don't change the code below ð
print(f"{row1}\n{row2}\n{row3}")

