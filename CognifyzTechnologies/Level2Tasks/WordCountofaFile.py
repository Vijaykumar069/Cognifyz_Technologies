import re
import collections
def word_count(file_path):
  with open(file_path, "r") as f:
    text = f.read()
  words = re.findall(r"\w+", text)
  word_counts = collections.Counter(words)
  return word_counts
def main():
  file_path = input("Enter the path to the text file : ")
  word_counts = word_count(file_path)
  for word, count in word_counts.most_common():
    print(f"{word} : {count}")
if __name__ == "__main__":
  main()
