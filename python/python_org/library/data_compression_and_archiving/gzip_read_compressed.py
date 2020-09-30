import gzip

with gzip.open('file.txt.gz', 'rb') as f:
    file_content = f.read()

print(file_content)
print(file_content.decode('utf-8'))
