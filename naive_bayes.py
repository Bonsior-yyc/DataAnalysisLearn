
document1 = ["car", "wheel", "car"]
document2 = ["car", "car", "fuel"]
document3 = ["car", "tank"]
document4 = ["fly", "car", "flag"]

document = ["car", "car", "car", "fly", "flag"]


train_label = ["car", "car", "car", "not_car"]


from collections import Counter

class Naive_bayes():
    def __init__(self, train_label, *documents):
        self.documents = documents
        V = []
        for x in documents: 
            V = V + x 
        self.V = list(set(V))
        self.category = list(set(train_label))
        self.train_label = train_label

    def train_num_label_word(self, label, word):
        num = 0
        for index,x in enumerate(self.documents):
            if self.train_label[index] == label:
                for y in x:
                    if y == word:
                        num += 1
        # print("In train case: word ", word, " appears ", num, " times in category ", label)
        return num


    def label_freq(self, label):
        dic = dict(Counter(self.train_label))
        freq = dict()
        for x in self.category:
            freq[x] = (dic[x] + 0.0) / len(self.train_label)
        return freq[label]


    def train_num_label(self, label):
        length = 0
        for i in range(len(self.train_label)):
            if self.train_label[i] == label:
                length += len(self.documents[i])
        # print("train vocab num for label : ", label, " is ", length)
        return length

        
    def run(self, document):
        p = []
        for x in self.category:
            out = 1
            print("\nif case ", x)
            for y in document:
                print("word ", y, ":", (self.train_num_label_word(x, y) + 1)*(1.0) / (self.train_num_label(x) + len(self.V)))
                out *= (self.train_num_label_word(x, y) + 1)*(1.0) / (self.train_num_label(x) + len(self.V))
            p.append(out* self.label_freq(x))
            print("case", x, ": " ,out , "*", self.label_freq(x), "=", out* self.label_freq(x))
        for i in range(len(p)):
            if p[i] == max(*p):
                return self.category[i]
        return ''
    
    def __str__(self):
        return "documents:"+str(self.documents)+"\nV:"+str(self.V)+"\ncategory:"+str(self.category)+"\ntrain_label:"+str(self.train_label)

cal = Naive_bayes(train_label, document1,document2,document3,document4)
print("\nprediction:", cal.run(document))



