with open("story.txt", 'r') as file:
    story = file.read()

start = -1 # will hold the index of starting character < . 
words = set()
for i, character in enumerate(story):
    if character == "<" and i < len(story) :
        start = i
    if i < len(story) and story[i] == '>':
        words.add(story[start : i+1])
print(words)
userResponse = {}
for word in words:
    response = input("Enter the word that goes along with this" + ' ' + word[1:-1] + ":")
    userResponse[word] = response
for word in words:
    story = story.replace(word,userResponse[word])



print(story)





# with open('projects/guesstheword/story.txt', 'r') as file:
#     story = file.read()
# print(story)

