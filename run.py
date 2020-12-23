import gem_parser
import os
for root, dirs, files in os.walk('E:\\test'):
    for f in files:
        if f.endswith(".pdf"):
            print(gem_parser.resume_data(f))