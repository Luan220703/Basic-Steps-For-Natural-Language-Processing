import nltk
from nltk import FreqDist

list = ['table','table','table','table','table','table','table','table','table','table','chair','chair','chair','chair','chair','chair','chair','chair','chair']

freq_dist = FreqDist(list)
sorted_by_frequency = sorted(freq_dist.items(), key=lambda x: x[1], reverse=True)
result = []
for word, frequency in sorted_by_frequency:
    result.append(word)

print(result)
