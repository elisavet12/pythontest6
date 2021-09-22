# Python sets
# 1. Write a Python program to create a non empty set and print it.

music={"rock", "ambient", "pop", "techno" "experimental"}
print(music)


# 2. Write a Python program to add member in a set.
music={"rock", "ambient", "pop", "techno", "experimental"}
music.add("classic")
print(music)

# 3. Write a Python program to remove item from set.

music={"rock", "ambient", "pop", "techno", "experimental"}
music.remove("rock")
print(music)

# Python sets
# 4. Write a Python program to find the length of a set.
music={"rock", "ambient", "pop", "techno", "experimental"}
print(len(music))

# 5. Write a Python program to find maximum and the minimum
# value in a set.
setx={ 35, 53, 98, 123, 8, 12}
print(max(setx))
print(min(setx))


# 6. Write a Python program to create an intersection of sets.
setx={ 35, 53, 98, 123, 8, 12}
sety={ 8, 15, 857, 9, 123, 89}
z=setx.intersection(sety)
print(z)
