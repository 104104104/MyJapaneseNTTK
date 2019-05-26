import MeCab, sys, pickle

fname = sys.argv[1]#ファイル名

with open(fname, "r") as f:
  text=f.read()

mecab=MeCab.Tagger("-Owakati")
wakati=mecab.parse(text)

with open(fname+"_wakati.pkl", "wb") as f:
  pickle.dump(wakati.split(), f)
