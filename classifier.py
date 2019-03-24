from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer

import time
import _pickle as cPickle
import os.path


def init():


    file_path = os.getcwd()+"\\my_dumped_classifier.pkl"

    if os.path.exists(file_path):
        # load it again
        with open('my_dumped_classifier.pkl', 'rb') as fid:
            classifier = cPickle.load(fid)
    else:
        # save the classifier
        with open('my_dumped_classifier.pkl', 'wb') as fid:
            X_train = normalize_rus([line for line in open("C:\\Users\\alexg\\Desktop\\v2\\train_text.txt", encoding='utf-8')])

            ans = open("C:\\Users\\alexg\\Desktop\\v2\\ans.txt", 'r',  encoding='utf-8')
            xz = [int (i) for i in ans.read().split()]
            y_train = []
            for i in range(len(xz)):
                y_train += [i] * xz[i]
            ans.close()
            

            classifier = Pipeline([
                ('vectorizer', CountVectorizer(ngram_range=(1,3))),
                ('tfidf', TfidfTransformer()),
                ('clf', OneVsRestClassifier(LinearSVC()))])
            classifier.fit(X_train, y_train)
            cPickle.dump(classifier, fid)   
            print("Сеть сгенерирована за %s секунд" % time.perf_counter())
     
    return classifier