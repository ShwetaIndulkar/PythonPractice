
# Write all content of a file into a new file  by skipping line number 5

with open("source.txt", "r") as src , open("destination.txt", "w") as dest:
    for lineno, line in enumerate(src, start=1):
        if lineno == 5:
            continue
        dest.write(line)
