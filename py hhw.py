T = ("The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog")

# A. Display ("jumps","over","the","lazy","dog")
A = T[4:9]
print("A:",A)

# B. Display ("quick","fox","over","lazy")
B = T[1:2] + T[3:4] + T[5:6] + T[7:8]
print("B:",B)

# C. Display the frequency of the word "the" in T
X=str(T).lower()
C = X.count("the")
print("C:",C)

# D. Display the number of words in the tuple T
D = len(T)
print("D:",D)
