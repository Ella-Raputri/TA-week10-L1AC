#user input
length_word1 = int(input("Enter length of the first word: "))
word1 = input("First word: ")

length_word2 = int(input("Enter length of the second word: "))
word2 = input("Second word: ")


#to see what is the index of character in word2 that is 
#the same with the last character in word1 (can be more than 1, so I make a list)
point_list = []
for i in range(0, min(length_word2, length_word1)):
    if word2[i] == word1[-1]:
        point_list.append(i)

#check whether the order from the character in index "point" until the first character in word2
#is the same with the order from the last character in word1 until some extent
#if there is a character that is same from word1 and word2
dict_word_same = {}
point_copy_list = []

for point in point_list:
    #point_copy_list is for the index, so that the index will not be out of range when point -= 1 every loop
    point_copy_list.append(point+2)


#since both point and point_copy are lists. then we loop for each element of them
for a in range(0, len(point_copy_list)):
    #assign every point_copy as a key of the dictionary and the value is an empty list
    dict_word_same[point_copy_list[a]] = []

    #loop from 1 to the breakpoint that is contained in the point_copy_list
    for i in range(1, point_copy_list[a]):
        if word1[-i] == word2[point_list[a]]:
            #if there's a same character, append the value to dict with the corresponding key
            dict_word_same[point_copy_list[a]].append(word1[-i])
            point_list[a] -= 1
        else:
            #if the order's not correct, remove the key-value in dict, break from the loop 
            #that was used to search if the order of the chars is the same or not and increase a
            #so we can check the next element in point_copy_list
            del dict_word_same[point_copy_list[a]]
            break


#if the order is correct, print the result of the max(key) to obtain the longest possible subword
if (len(dict_word_same) != 0):
    dict_word_same[max(dict_word_same)].reverse()
    result = "".join(dict_word_same[max(dict_word_same)])   
    print(f"Both words can be linked with the subword {result}")
else:
#if there isn't any characters that is the same from word1 and word2 or the dictionary is empty
    print("Both words cannot be linked.")

#the reason i use dict is to make sure that words like forbesese and besese, the output is subword besese