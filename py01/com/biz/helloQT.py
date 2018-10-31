import sys  # sys라는 패키지를 지금부터 쓰겠다.

# QApplication 패키지와 QWidget 패키지를 사용하는데
# 그 중에서 PyQT5.QtWidgets만 쓰겠다
from PyQt5.QtWidgets import QApplication, QWidget

# QApp을 지금부터 시작하겠다.
app = QApplication(sys.argv)

# 위젯(View, 도구)을 하나 생성하라
w = QWidget()
w.resize(250, 150)
w.move(300, 300)        # 위치
w.setWindowTitle("내 윈도우")
w.show()

# 현재 생성된 app을 실행상태로 유지하면서 event를 기다려라
sys.exit(app.exec_())