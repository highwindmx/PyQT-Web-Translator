import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from guess_language import guess_language

class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1400, 800)
        self.setWindowTitle("一个属于你的简单翻译软件")
        #self.resize(800,500)

        self.tabs = QtWidgets.QTabWidget()

        self.webtab01 = QWebView()
        self.webtab01.setObjectName("dict-搜狗")
        self.webtab01.load(QtCore.QUrl("http://dict.sogou.com/"))

        self.webtab02 = QWebView()
        self.webtab02.setObjectName("dict-有道")
        self.webtab02.load(QtCore.QUrl("http://dict.youdao.com/"))

        #self.webtab03 = QWebView()
        #self.webtab03.setObjectName("dict-词霸")
        #self.webtab03.load(QtCore.QUrl("http://www.iciba.com/"))

        self.webtab04 = QWebView()
        self.webtab04.setObjectName("dict-必应")
        self.webtab04.load(QtCore.QUrl("http://www.bing.com/dict/"))

        self.webtab11 = QWebView()
        self.webtab11.setObjectName("Web-搜狗")
        self.webtab11.load(QtCore.QUrl("http://fanyi.sogou.com/"))

        self.webtab12 = QWebView()
        self.webtab12.setObjectName("Web-谷歌")
        self.webtab12.load(QtCore.QUrl("https://translate.google.cn/"))

        self.webtab13 = QWebView()
        self.webtab13.setObjectName("Web-百度")
        self.webtab13.load(QtCore.QUrl("http://fanyi.baidu.com/"))

        self.tabs.addTab(self.webtab01, "搜狗词典")
        self.tabs.addTab(self.webtab02, "有道词典")
        #self.tabs.addTab(self.webtab03, "金山词霸")
        self.tabs.addTab(self.webtab04, "必应词典")
        self.tabs.addTab(self.webtab11, "搜狗翻译")
        self.tabs.addTab(self.webtab12, "谷歌翻译")
        self.tabs.addTab(self.webtab13, "百度翻译")

        self.inputLine = QtWidgets.QLineEdit()
        self.inputLine.setObjectName("LineEditor")
        self.inputLine.setFixedHeight(30)
        self.inputLine.textChanged.connect(self.translateText)

        centralLayout = QtWidgets.QVBoxLayout()
        centralLayout.addWidget(self.inputLine, 1)
        centralLayout.addWidget(self.tabs, 2)
        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setLayout(centralLayout)
        self.setCentralWidget(self.centralWidget)

    def translateText(self):
        word = self.inputLine.text()
        #print(word)
        self.webtab01.load(QtCore.QUrl("http://dict.sogou.com/cidian?ie=utf-8&query=" + word))
        #self.webtab03.load(QtCore.QUrl("http://www.iciba.com/" + word))
        self.webtab04.load(QtCore.QUrl("https://www.bing.com/dict/search?q=" + word))
        if(guess_language(word)=="zh"):
            self.webtab11.load(QtCore.QUrl("http://fanyi.sogou.com/?fr=websearch#auto/en/" + word))
            self.webtab12.load(QtCore.QUrl("https://translate.google.cn/#zh-CN/en/" + word))
            self.webtab13.load(QtCore.QUrl("http://fanyi.baidu.com/#zh/en/" + word))
            self.webtab02.load(QtCore.QUrl("http://dict.youdao.com/w/" + word + "/#keyfrom=dict2.top"))
        else:
            self.webtab11.load(QtCore.QUrl("http://fanyi.sogou.com/?fr=websearch#auto/zh-CHS/" + word))
            self.webtab12.load(QtCore.QUrl("https://translate.google.cn/#en/zh-CN/" + word))
            self.webtab13.load(QtCore.QUrl("http://fanyi.baidu.com/#en/zh/" + word))
            self.webtab02.load(QtCore.QUrl("http://dict.youdao.com/w/eng/" + word + "/#keyfrom=dict2.index"))

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()