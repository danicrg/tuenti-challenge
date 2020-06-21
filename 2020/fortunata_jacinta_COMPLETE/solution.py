import re

#################### MAKING THE RANKING #################

book = open('pg17013.txt', 'r')
words = {}
for line in book.readlines():
    # line = book.readline()
    line = line.lower()
    line = re.sub(re.compile('[^a-záéíóúüñ]'), ' ', line)
    line = line.split()
    for word in line:
        if len(word) > 2:
            try:
                words[word] += 1
            except:
                words[word] = 1

ranking = [v[0] for v in sorted(words.items(), key=lambda k: (-k[1], k[0]))]

book.close()

########################### READING CASES###############

f = open('submitInput.txt', 'r')
output = open('submitOutput.txt', 'w')

N = int(f.readline().strip())

for case in range(1, N + 1):
    word = f.readline().strip()
    if word.isdigit():
        number = int(word)
        word = ranking[number - 1]
        count = words[word]
        output.write('Case #{}: {} {}\n'.format(case, word, count))
    else:
        count = words[word]
        output.write('Case #{}: {} #{}\n'.format(case, count, ranking.index(word) + 1))

f.close()
output.close()

print('Done!')
