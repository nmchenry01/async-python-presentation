

filename = "insert.txt"
with open(filename, "a") as file:
    for idx in range(20000):
        content = f',("Task {idx+1}", "A description of task {idx+1}", {idx+1})\n'
        file.write(content)