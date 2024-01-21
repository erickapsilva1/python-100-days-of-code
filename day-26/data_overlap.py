with open("files/file1.txt", 'r') as f:
    file1 = f.read().splitlines()

with open("files/file2.txt", 'r') as f:
    file2 = f.read().splitlines()

results = [int(num) for num in file1 if num in file2]

print(results)