import sys, pickle
from my_nltk import my_nltk

#fname = sys.argv[1]
fname = "kokoro_utf-8.txt"
with open(fname, "r") as f:
  text=f.read()

nltk = my_nltk(text)
try:
    inp = sys.argv[1]
except:
    inp = "先生"
print("テストです：2gram文",nltk.make_2gram(inp, 30))
print("テストです：3gram文",nltk.make_3gram(inp, 30))
print("テストです：4gram文",nltk.make_4gram(inp, 30))
print("テストです：類語は",nltk.similar(inp))


with open(fname[0:2]+".pkl", "wb") as f:
  pickle.dump(nltk, f)
