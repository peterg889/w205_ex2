import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

path = "/Users/petergrabowski/berk/w205_ex2/results.txt"

f = open(path, 'r')

i = 0
words = OrderedDict()

while i < 20:
	i = i + 1
	line = f.readline()
	word, count = line.rstrip().split(",")
	words[word] = count


plt.figure(figsize=(10,5))
plt.bar(range(len(words)), words.values(), align='center')
plt.xticks(range(len(words)), words.keys())

plt.ylabel('Frequency')
plt.title('Most Commmon Words from Twitter Stream')
plt.savefig("/Users/petergrabowski/berk/w205_ex2/tweetwordcount/Plot.png")
plt.show()
