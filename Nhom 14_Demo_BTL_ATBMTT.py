#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import những thư viện cần dùng
import base64
from PyQt5 import QtCore, QtGui, QtWidgets
import io
import random
import regex
import hashlib
import sys
from PyQt5.QtWidgets import QMessageBox
#xây dựng giao diện
class Ui_MainWindow(object):
    def ShowMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 703)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1061, 691))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(110, 50, 831, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(120, 40, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtP = QtWidgets.QLineEdit(self.groupBox)
        self.txtP.setGeometry(QtCore.QRect(190, 30, 541, 51))
        self.txtP.setObjectName("txtP")
        self.txtQ = QtWidgets.QLineEdit(self.groupBox)
        self.txtQ.setGeometry(QtCore.QRect(190, 90, 541, 51))
        self.txtQ.setObjectName("txtQ")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(110, 250, 831, 351))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 80, 381, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(80, 40, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(280, 40, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtE = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtE.setGeometry(QtCore.QRect(10, 100, 161, 51))
        self.txtE.setObjectName("txtE")
        self.txtN = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtN.setGeometry(QtCore.QRect(210, 100, 161, 51))
        self.txtN.setObjectName("txtN")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(440, 80, 381, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(270, 40, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(70, 40, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtD = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtD.setGeometry(QtCore.QRect(10, 100, 161, 51))
        self.txtD.setObjectName("txtD")
        self.txtN1 = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtN1.setGeometry(QtCore.QRect(210, 100, 161, 51))
        self.txtN1.setObjectName("txtN1")
        self.btnTaoKhoa = QtWidgets.QPushButton(self.groupBox_2)
        self.btnTaoKhoa.setGeometry(QtCore.QRect(120, 260, 151, 71))
        self.btnTaoKhoa.setMouseTracking(False)
        self.btnTaoKhoa.setObjectName("btnTaoKhoa")
        self.btnthoat = QtWidgets.QPushButton(self.groupBox_2)
        self.btnthoat.setGeometry(QtCore.QRect(560, 260, 151, 71))
        self.btnthoat.setObjectName("btnthoat")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 10, 1011, 541))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(50, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(50, 330, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(60, 460, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.txtVNCK = QtWidgets.QLineEdit(self.groupBox_5)
        self.txtVNCK.setGeometry(QtCore.QRect(310, 21, 691, 291))
        self.txtVNCK.setObjectName("txtVNCK")
        self.txtHamBam = QtWidgets.QLineEdit(self.groupBox_5)
        self.txtHamBam.setGeometry(QtCore.QRect(310, 320, 691, 111))
        self.txtHamBam.setObjectName("txtHamBam")
        self.txtChuKy = QtWidgets.QLineEdit(self.groupBox_5)
        self.txtChuKy.setGeometry(QtCore.QRect(310, 440, 691, 91))
        self.txtChuKy.setObjectName("txtChuKy")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(70, 570, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.btnKy = QtWidgets.QPushButton(self.tab_3)
        self.btnKy.setGeometry(QtCore.QRect(300, 570, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnKy.setFont(font)
        self.btnKy.setObjectName("btnKy")
        self.btnLuuChuKy = QtWidgets.QPushButton(self.tab_3)
        self.btnLuuChuKy.setGeometry(QtCore.QRect(530, 570, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnLuuChuKy.setFont(font)
        self.btnLuuChuKy.setObjectName("btnLuuChuKy")
        self.btnThoat = QtWidgets.QPushButton(self.tab_3)
        self.btnThoat.setGeometry(QtCore.QRect(830, 570, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnThoat.setFont(font)
        self.btnThoat.setObjectName("btnThoat")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 10, 1011, 541))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setGeometry(QtCore.QRect(50, 120, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        self.label_11.setGeometry(QtCore.QRect(50, 330, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setGeometry(QtCore.QRect(50, 470, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setGeometry(QtCore.QRect(310, 470, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setGeometry(QtCore.QRect(670, 470, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.txtVBCXN = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtVBCXN.setGeometry(QtCore.QRect(330, 20, 671, 281))
        self.txtVBCXN.setObjectName("txtVBCXN")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit.setGeometry(QtCore.QRect(330, 310, 671, 121))
        self.lineEdit.setObjectName("lineEdit")
        self.txtE1 = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtE1.setGeometry(QtCore.QRect(370, 461, 161, 51))
        self.txtE1.setObjectName("txtE1")
        self.txtN1_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtN1_2.setGeometry(QtCore.QRect(720, 460, 161, 51))
        self.txtN1_2.setObjectName("txtN1_2")
        self.btnTaiChuKy = QtWidgets.QPushButton(self.tab_4)
        self.btnTaiChuKy.setGeometry(QtCore.QRect(300, 570, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnTaiChuKy.setFont(font)
        self.btnTaiChuKy.setObjectName("btnTaiChuKy")
        self.btnXacNhan = QtWidgets.QPushButton(self.tab_4)
        self.btnXacNhan.setGeometry(QtCore.QRect(530, 570, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnXacNhan.setFont(font)
        self.btnXacNhan.setObjectName("btnXacNhan")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 570, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.btnThoat_2 = QtWidgets.QPushButton(self.tab_4)
        self.btnThoat_2.setGeometry(QtCore.QRect(830, 570, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnThoat_2.setFont(font)
        self.btnThoat_2.setObjectName("btnThoat_2")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnTaoKhoa.clicked.connect(self.TaoKhoa)
        self.btnKy.clicked.connect(self.HashFile)
        self.btnthoat.clicked.connect(self.exit)
        self.btnThoat.clicked.connect(self.exit)
        self.btnThoat_2.clicked.connect(self.exit)
        self.btnXacNhan.clicked.connect(self.Decrypt)
        self.pushButton_2.clicked.connect(self.TaiVanBan)
        self.pushButton.clicked.connect(self.TaiVanBan1)
        self.btnLuuChuKy.clicked.connect(self.LuuChuKy)
        self.btnTaiChuKy.clicked.connect(self.TaiChuKy)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phần mềm chữ ký điện tử RSA")) #Đặt tiêu đề của cửa sổ chính
        self.groupBox.setTitle(_translate("MainWindow", "Chọn số nguyên tố")) # Đặt tiêu đề hoặc văn bản cho các thành phần giao diện người dụng
        self.label.setText(_translate("MainWindow", "P"))
        self.label_2.setText(_translate("MainWindow", "Q"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Tìm các giá trị"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Khóa công khai"))
        self.label_3.setText(_translate("MainWindow", "E"))
        self.label_4.setText(_translate("MainWindow", "N"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Khóa bí mật"))
        self.label_6.setText(_translate("MainWindow", "N"))
        self.label_5.setText(_translate("MainWindow", "D"))
        self.btnTaoKhoa.setText(_translate("MainWindow", "Tạo khóa")) #Đặt văn bản cho các nút
        self.btnthoat.setText(_translate("MainWindow", "Thoát"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tạo khóa"))  #Đặt văn bản cho các tab trong một widget tab.
        self.groupBox_5.setTitle(_translate("MainWindow", "Ký"))
        self.label_7.setText(_translate("MainWindow", "Văn bản cần ký"))
        self.label_8.setText(_translate("MainWindow", "Hàm băm"))
        self.label_9.setText(_translate("MainWindow", "Chữ ký"))
        self.pushButton.setText(_translate("MainWindow", "Tải văn bản"))
        self.btnKy.setText(_translate("MainWindow", "Ký"))
        self.btnLuuChuKy.setText(_translate("MainWindow", "Lưu chữ ký"))
        self.btnThoat.setText(_translate("MainWindow", "Thoát"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Ký văn bản"))
        self.groupBox_6.setTitle(_translate("MainWindow", "xác nhận"))
        self.label_10.setText(_translate("MainWindow", "Văn bản cần xác nhận"))
        self.label_11.setText(_translate("MainWindow", "Xác nhận chữ ký"))
        self.label_12.setText(_translate("MainWindow", "Nhập xác nhận"))
        self.label_13.setText(_translate("MainWindow", "E"))
        self.label_14.setText(_translate("MainWindow", "N"))
        self.btnTaiChuKy.setText(_translate("MainWindow", "Tải chữ ký"))
        self.btnXacNhan.setText(_translate("MainWindow", "Xác nhận"))
        self.pushButton_2.setText(_translate("MainWindow", "Tải văn bản"))
        self.btnThoat_2.setText(_translate("MainWindow", "Thoát"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Xác nhận chữ ký"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Hướng dẫn"))

    def exit(self): #  thoát khỏi ứng dụng. Nó sẽ kết thúc quá trình ứng dụng.
        exit(self)
    def TaoKhoa(self): #tạo một cặp khóa RSA. Nó có thể tạo ra một khóa công khai và một khóa bí mật.
        TaoKhoa(self)
    def HashFile(self): #tạo một giá trị hash cho một tệp. Nó có thể sử dụng một thuật toán băm như SHA-256.
        HashFile(self)
    def Decrypt(self): #giải mã một chữ ký điện tử.
        Decrypt(self)
    def TaiVanBan(self): #tải một tệp văn bản vào ứng dụng. Chúng có thể mở một hộp thoại mở tệp để người dùng chọn tệp.
        TaiVanBan(self)
    def TaiVanBan1(self): 
        TaiVanBan1(self)
    def LuuChuKy(self): #lưu một chữ ký điện tử vào một tệp
        LuuChuKy(self)
    def TaiChuKy(self): #tải một chữ ký điện tử từ một tệp vào ứng dụng.
        TaiChuKy(self)
def checkSNT(n): #kiểm tra 1 số nguyên có phải là số nguyên tố không
    if n < 2: return False #nhỏ hơn 2 trả về giá trị false
    for i in range(2, n): #kiểm tra n có chia hết khoảng từ 2 đến n-1
        if n % i == 0:      #chia hết trả về false
            return False
    return True 
def check2SNT(a, b): #kiểm tra 2 số nguyên có phải số nguyên tố không
    if a < 2 or b < 2: return False 
    while a!=b: #thuật toán Euclib để tìm ước chung lớn nhất
        if a > b:
            a = a -b
        else: b = b- a
    if(a == 1): #là 1 thì trả về False ngược lại True
        return False

    return True


def TaoKhoa(self): #Kiểm tra xem người dùng đã nhập giá trị cho P và Q chưa. Chưa thì báo lỗi
    if(self.txtP.text()==""):
        check = "Bạn chưa nhập P"
        self.ShowMessageBox("Lỗi", check)
    if (self.txtQ.text() == ""):
        check = "Bạn chưa nhập Q"
        self.ShowMessageBox("Lỗi", check)

    else:
        p = int(self.txtP.text()) #ép kiểu
        q = int(self.txtQ.text())
        if checkSNT(p) == False: #kiểm tra số nt
            check = "P không phải là số nguyên tố"
            self.ShowMessageBox("Lỗi", check)
        else:
            if checkSNT(q) == False:
                check = "Q không phải là số nguyên tố"
                self.ShowMessageBox("Lỗi", check)
            else: #th cả 2 là số nguyên tố
                n = p * q
                phin = (p - 1) * (q - 1)
                test = int(phin)
                e = random.randint(2, test) #tạo một số e ngẫu nhiên nằm trong khoảng từ 2 đến phin
                while check2SNT(e, phin) == True: #ktra e va phin có phải là 2 số nguyên tố cùng nhau không
                    e = random.randint(2, test) #Không cùng tạo e mới
                d = 0 #sử dụng thuật toán Euclib mở rộng
                i = 2
                while ((1 + i * phin) % e) != 0 or d <= 2:
                    i += 1
                    d = int((1 + (i * test)) / e)
#Cập nhận giao diện giá trị mới
                self.txtN.setText(str(n))
                self.txtN1.setText(str(n))
                self.txtD.setText(str(d))
                self.txtE.setText(str(e))

def SoMuTheoMod1(x, n, m): #tính giá tị của x^n mod m
    b = int(x) #ép kiểu
    c = 0  
    if (n == 0): return 1;
    p = int(SoMuTheoMod1(x, n/2, m)) #nếu n khác 0
    if (n % 2 == 0): #nếu n là số chẵn
        c = (p * p) % m #p^2 mod m
    else: #nếu n là số lẻ
        c = (p * p * b) % m #b là giá trị ban đầu của x
    text = str(c) #chuyển từ số nguyên sang chuỗi
    return text

def MaHoa(s,e,n): #s: chuỗi cần mã hóa, e và n: thành phần khóa công khai
#chuyển đổi chuỗi s sang dạng mã ASCII lưu và ds số nguyên
    nguyen = len(s)
    nguyen = []
    s = s.encode('ASCII')
    for i in range(0, len(s)):
        nguyen.append(s[i])
#tạo danh sách mới
    a = len(nguyen)
    a = []
    str = ""
    for i in range(0, len(nguyen), 1):
        a.append(SoMuTheoMod1(nguyen[i], e, n)) #tính giá trị mã hóa cho từng ký tự trong S
    for i in range(0, len(nguyen)): #nối giá trị trong ds a thành một chuỗi
        str = str + a[i] + "-"
    return str
def GiaiMa(s,d2, n2): #s: chuỗi cần giải mã, d2 và n2 là hai thành phần của khóa bí mật
    #giaima = []
    #giaima = s.split("-")
    b = len(s) 
    b = []
    s = s.split("-")
    for i in range(0, len(s)):
        b.append(s[i])
    a = len(b)
    a = [] #tạo một danh sách mới a
    str = ""
    for i in range(0, len(b), 1):
        a.append(SoMuTheoMod1(b[i], d2, n2)) #tính giá trị giải mã cho từng ký tự đã được mã hóa
    c =[]
    for i in range(0, len(b), 1):
        c.append(a[i])

        str = str + chr(int(c[i]))


    return str
#GIAI MA
def Decrypt(self):
    vanban = self.txtVBCXN.text()
# tạo một giá trị hash cho văn bản đó sử dụng thuật toán MD5.
    hash_object = hashlib.md5(vanban.encode())   
    hash_object = hash_object.hexdigest()
#huyển đổi giá trị d2 và n2 từ chuỗi sang số nguyên.
    d2 = int(self.txtE1.text())
    n2 = int(self.txtN1_2.text())
#so sánh 
    if(vanban == data1):
        self.ShowMessageBox("Thông báo", "Chũ ký hợp lệ!")

    else:
        self.ShowMessageBox("Thông báo", "Không hợp lệ!")


#MA HOA
def HashFile(self):
    g = int(self.txtE.text()) # Đọc giá trị từ trường txtE và chuyển đổi thành số nguyên
    h = int(self.txtN.text())
    vbck = self.txtVNCK.text() # Đọc giá trị từ trường txtVNCK
    if vbck == "": # Kiểm tra xem vbck có rỗng không
        check = "Bạn chưa tải chữ ký"
        self.ShowMessageBox("lỗi", check)
# Hiển thị thông báo lỗi nếu vbck rỗng
    else:
        f.write(self.txtVNCK.text())  # Ghi giá trị từ trường txtVNCK vào tệp
        hash_object = hashlib.md5(vbck.encode()) # Tạo một đối tượng băm MD5 từ vbck
        self.txtHamBam.setText(hash_object.hexdigest()) # Đặt giá trị của trường txtHamBam thành giá trị băm hex của vbck
        hambam = str(self.txtHamBam.text()) # Lấy giá trị từ trường txtHamBam và chuyển đổi thành chuỗi
        sinal = MaHoa(hambam, g, h) # Gọi hàm MaHoa với các đối số hambam, g, và h
        sinal = sinal.rstrip("-") # Loại bỏ dấu "-" ở cuối chuỗi sinal nếu có
        self.txtChuKy.setText(sinal)  # Đặt giá trị của trường txtChuKy thành sinal
        f.close()

def TaiVanBan1(self):
    s = io.open("HAHA.txt", 'r', encoding = "utf-8")
    data = s.read()
    self.txtVNCK.setText(data)

def TaiVanBan(self):
    s = io.open("HAHA.txt", 'r', encoding = "utf-8")
    data = s.read()
    self.txtVBCXN.setText(data)

def LuuChuKy(self):
    sinal = self.txtChuKy.text()
    f = io.open("New Text Document.txt", 'w', encoding = "utf-8")
    f.write(sinal)
    self.ShowMessageBox("Thông báo", "Thêm chữ ký thành công")

def TaiChuKy(self):
    s = io.open("New Text Document.txt", 'r',encoding = "utf-8")
    data = s.read()
    self.lineEdit.setText(data)

def exit(self):
    raise SystemExit()
if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10000)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

