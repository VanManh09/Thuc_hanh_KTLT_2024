print("sinh viên Nguyễn Văn Mạnh")
print("MSSV 235752021610091")

def find_longest_words(text):
    words = text.split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words

with open('C:/Users/HI/Downloads/c.txt', 'r', encoding='utf-8') as file:
    text = file.read()
longest_words = find_longest_words(text)

print("Những từ dài nhất trong văn bản là:")
for word in longest_words:
    print(word)
