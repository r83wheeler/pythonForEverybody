fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() #strips the whitespace from the right of the line, preventing blank lines being printed out. 
    if line.startswith('From:'):
        print(line)

for line in fhand:
    line = line.rstrip()
    # Skip lines that don't start with From
    if not line.startswith('From:'):
        continue
    # Process lines that start with From
    print(line)
