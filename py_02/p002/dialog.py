import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

# ui 파일을 파이선에서 사용하기위한 패키지들
from PyQt5 import QtCore
from PyQt5 import uic # dialog.ui 파일을 사용하기 위한 패키지
from PyQt5.QtCore import pyqtSlot   # event 핸들링패키지


class myForm(QtWidgets.QDialog):
    def __init__(self,parent=None):
        
        # myForm에서 QtWidgets.QDialog클래스를 상속 받겠다.
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = uic.loadUi('./dialog.ui',self) #ui파일열기
        self.ui.show()
        
    # buttonBox의 OK가 눌리면
    # accepted()의 신호가 발생을하고
    # 그 신호는 어딘가에 있는 accept()함수를 찾는다
    # 만약 함수가 없으면 그냥 창을 닫아버리고 
    # 함수가 있으면 해당되는 함수를실행한다.
    def accept(self):
        txt = self.ui.lineEdit.text()
        self.ui.label.setText(txt)
        # self.done(1)    # ok 버튼을 눌렀을때, 일을 다마치고 끝내다
        
    def reject(self):
        self.done(0)    # cancle 버튼을 눌렀을때 묻지도 따지지도 말고 끝내라
        
    
        
        

app = QtWidgets.QApplication(sys.argv)
w = myForm()
sys.exit(app.exec_())
