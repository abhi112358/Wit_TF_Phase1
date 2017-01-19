queries = []

f = open('queries.txt', 'r')
for line in iter(f):
    queries.append(line)
    print line
f.close()

print queries