# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alexg\Desktop\v2\interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from classifier import init

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer

from tst import normalize_rus
names = ['SupportMKDO', 'SupportNPO', 'SupportOIR', 'SupportOPR', 'SupportORPB', 'SupportReception', 'SupportSPD', 'SupportSynerdocs']

classific = Pipeline([
                ('vectorizer', CountVectorizer(ngram_range=(1,3))),
                ('tfidf', TfidfTransformer()),
                ('clf', OneVsRestClassifier(LinearSVC()))])

class Ui_Form(object):
    def setupUi(self, Form):

        #net connect
        self.classific = init()
        
        Form.setObjectName("Form")
        Form.resize(370, 584)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(324, 530, 41, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_push_button_click)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 530, 311, 41))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 351, 471))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText("Доброе время суток))"+'\n')
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", ">"))
        
    def sendMessage(self):
        query = self.textEdit.toPlainText()
        self.textBrowser.setText(self.textBrowser.toPlainText() + query+'\n')
        self.getNetAns(query)
        self.textEdit.setText("")



    def getNetAns(self, query):
        if (query != "пока"):
            
            X_test = normalize_rus([query])
            predicted = self.classific.decision_function(X_test)
            # weight print
            #print(predicted)
            if(list(filter(lambda x: x > 0, predicted[0])) == []):
                self.textBrowser.setText(self.textBrowser.toPlainText() + "Уточните свой вопрос!" +'\n')
                return
            var = self.classific.predict(X_test)

            self.textBrowser.setText(self.textBrowser.toPlainText() + names[var[0]] +'\n')
       
        else:
            self.textBrowser.setText(self.textBrowser.toPlainText() + "_ДО СВИДАНИЯ_"+'\n')


    def on_push_button_click(self):
        self.sendMessage()
       
        print("clicked on button")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

