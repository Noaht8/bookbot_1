def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(st):
    words = st.split()
    count = len(words)
    return f"Found {count} total words"

def string_count(st):
    d = {}
    for s in st:
        for i in s.lower():
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    return d

def sort_on(items):
    return items["num"]

def sort_dict(d):
    filtered = {k:v for k, v in d.items() if k.isalpha()}
    sorted_dict = dict(sorted(filtered.items(), key=lambda item:item[1], reverse=True))
    return sorted_dict
