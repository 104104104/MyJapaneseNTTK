import MeCab, random
import collections

class my_nltk:
    def __init__(self, text):
        #textで与えられた文章を分かち書きする
        #self.wakatiとする
        mecab=MeCab.Tagger("-Owakati")
        wakati=mecab.parse(text)
        self.wakati = wakati.split()
        #markov_dic_2gramを作る{単語:キーの次に出現したことのある単語のlist}
        #self.dic_2gramとする
        self.dic_2gram = {}
        for i in range(len(self.wakati)-1):
            try:
                self.dic_2gram[self.wakati[i]].append(self.wakati[i+1])
            except:
                self.dic_2gram[self.wakati[i]] = []
                self.dic_2gram[self.wakati[i]].append(self.wakati[i+1])
        #markov_dic_3gramを作る{単語:キーの次に出現したことのある単語のlist}
        #self.dic_3gramとする
        self.dic_3gram = {}
        for i in range(len(self.wakati)-2):
            try:
                self.dic_3gram[self.wakati[i],self.wakati[i+1]].append(self.wakati[i+2])
            except:
                self.dic_3gram[self.wakati[i],self.wakati[i+1]] = []
                self.dic_3gram[self.wakati[i],self.wakati[i+1]].append(self.wakati[i+2])
        #markov_dic_4gramを作る{単語:キーの次に出現したことのある単語のlist}
        #self.dic_4gramとする
        self.dic_4gram = {}
        for i in range(len(self.wakati)-3):
            try:
                self.dic_4gram[self.wakati[i],self.wakati[i+1],self.wakati[i+2]].append(self.wakati[i+3])
            except:
                self.dic_4gram[self.wakati[i],self.wakati[i+1],self.wakati[i+2]] = []
                self.dic_4gram[self.wakati[i],self.wakati[i+1],self.wakati[i+2]].append(self.wakati[i+3])

    def make_2gram(self, start_word, max_count=20):
        """
        2gramで適当な文字列を表示する
        """
        if start_word not in self.wakati:
            print("error: その単語は文中に出現しない!!")
            pass
        sentence = []#生成した単語からなるリスト
        sentence.append(start_word)#まずは最初の単語を追加
        now_word = start_word
        for i in range(int(max_count)-1):#最初の単語を追加した分、1減らす
            #self.dic_2gram[now_word]を用いて、次の単語をランダムに選ぶ
            word = random.choice(self.dic_2gram[now_word])
            sentence.append(word)
            now_word = word
        return "".join(sentence)

    def make_3gram(self, start_word, max_count=20):
        """
        3gramで適当な文字列を表示する
        """
        if start_word not in self.wakati:
            print("error: その単語は文中に出現しない!!")
            pass
        second_word = random.choice(self.dic_2gram[start_word])
        sentence = []#生成した単語からなるリスト
        sentence.append(start_word)#まずは最初の単語を追加
        sentence.append(second_word)#二番目の単語も追加
        now_word = start_word
        now_word_next = second_word
        for i in range(int(max_count)-2):#最初の単語を追加した分、1減らす
            #self.dic_3gram[now_word]を用いて、次の単語をランダムに選ぶ
            word = random.choice(self.dic_3gram[now_word,now_word_next])
            sentence.append(word)
            now_word = now_word_next
            now_word_next = word
        return "".join(sentence)

    def make_4gram(self, start_word, max_count=20):
        """
        4gramで適当な文字列を表示する
        """
        if start_word not in self.wakati:
            print("error: その単語は文中に出現しない!!")
            pass
        second_word = random.choice(self.dic_2gram[start_word])
        third_word = random.choice(self.dic_3gram[start_word, second_word])
        sentence = []#生成した単語からなるリスト
        sentence.append(start_word)#まずは最初の単語を追加
        sentence.append(second_word)#二番目の単語も追加
        sentence.append(third_word)
        now_word = start_word
        now_word_next = second_word
        now_word_next_next = third_word
        for i in range(int(max_count)-3):#最初の単語を追加した分、1減らす
            #self.dic_3gram[now_word]を用いて、次の単語をランダムに選ぶ
            word = random.choice(self.dic_4gram[now_word,now_word_next, now_word_next_next])
            sentence.append(word)
            now_word = now_word_next
            now_word_next = now_word_next_next
            now_word_next_next = word
        return "".join(sentence)

    def similar(self, word):
        """
        似た意味の単語を表示する
        """
        search = 2
        #エラーを弾く
        if len(self.wakati) < search*2+1:
            print("error: 文が短すぎる or 範囲が広すぎる!!")
            pass
        if word not in self.wakati:
            print("error: その単語は文中に出現しない!!")
            pass
        #検索(wordの位置のインデックスのリストを作る)
        indexes = [i for i, x in enumerate(self.wakati) if x == word]
        #前後の文字のリストを作る
        #####ここをどうにかしないとsearchが実装できない！！！#####
        before_after = [[self.wakati[i-2],self.wakati[i-1],self.wakati[i+1],self.wakati[i+2]] for i in indexes]
        #前後の文字のリストで検索
        similar = []
        for i in before_after:
            for j in range(len(self.wakati) - search*2):
                #####ここをどうにかしないとsearchが実装できない！！！#####
                if [self.wakati[j-2],self.wakati[j-1],self.wakati[j+1],self.wakati[j+2]] == i:
                    similar.append(self.wakati[j])

        search = 1
        #検索(wordの位置のインデックスのリストを作る)
        indexes = [i for i, x in enumerate(self.wakati) if x == word]
        #前後の文字のリストを作る
        before_after = [[self.wakati[i-1],self.wakati[i+1]] for i in indexes]
        #前後の文字のリストで検索
        similar = []
        for i in before_after:
            for j in range(len(self.wakati) - search*2):
                if [self.wakati[j-1],self.wakati[j+1]] == i:
                    similar.append(self.wakati[j])

        #多い順に並び替え
        similar_c = collections.Counter(similar)
        return " ".join([i[0] for j,i in enumerate(similar_c.most_common()) if j<=15])
