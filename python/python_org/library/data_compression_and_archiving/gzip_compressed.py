
import gzip
content = b'Lots of content here'
with gzip.open('file.txt.gz', 'wb') as f:
    f.write(content)
