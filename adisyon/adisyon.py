import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import *
#Author Abdurrahim bulut



class Masa():
    def __init__(self):
        super(Masa, self).__init__()
        self.i1 = 0
        self.i2=0
        self.i3=0
        self.i4=0
        self.hesap =0

    def i1a(self):
        self.i1+=1
        print(self.i1)
        self.hesapla()
        return self.i1
    def i1e(self):
        if self.i1>0:
            self.i1-=1
        print(self.i1)
        self.hesapla()
        return self.i1

    def i2a(self):
        self.i2+=1
        print(self.i2)
        self.hesapla()
        return self.i2
    def i2e(self):
        if self.i2>0:
            self.i2-=1
        self.hesapla()
        print(self.i2)

        return self.i2

    def i3a(self):
        self.i3+=1
        self.hesapla()
        print(self.i3)

        return self.i3

    def i3e(self):
        if self.i3>0:
            self.i3-=1
        self.hesapla()
        print(self.i3)
        return self.i3

    def i4a(self):
        self.i4+=1
        print(self.i4)
        self.hesapla()
        return self.i4

    def i4e(self):
        if self.i4>0:
            self.i4-=1
        self.hesapla()
        print(self.i4)
        return self.i4

    def hesapla(self):
        self.hesap=1*self.i1+3*self.i2+5*self.i3+2*self.i4
        return self.hesap





class Adisyon(QWidget):
    kasa=0
    def __init__(self):
        super(Adisyon,self).__init__()
        loadUi("adisyon.ui",self)
        self.setWindowTitle("Adisyon Programı")



        masa1=Masa()
        self.pushButton_17.clicked.connect(lambda: masa1.i1a())
        self.pushButton_17.clicked.connect(lambda: self.masaText(masa1.i1,self.label_25,masa1.hesap,self.label_29))
        self.pushButton_18.clicked.connect(lambda: masa1.i1e())
        self.pushButton_18.clicked.connect(lambda: self.masaText(masa1.i1,self.label_25,masa1.hesap,self.label_29))

        self.pushButton_11.clicked.connect(lambda: masa1.i2a())
        self.pushButton_11.clicked.connect(lambda: self.masaText(masa1.i2,self.label_26,masa1.hesap,self.label_29))
        self.pushButton_13.clicked.connect(lambda: masa1.i2e())
        self.pushButton_13.clicked.connect(lambda: self.masaText(masa1.i2,self.label_26,masa1.hesap,self.label_29))

        self.pushButton_14.clicked.connect(lambda: masa1.i3a())
        self.pushButton_14.clicked.connect(lambda: self.masaText(masa1.i3,self.label_27,masa1.hesap,self.label_29))
        self.pushButton_12.clicked.connect(lambda: masa1.i3e())
        self.pushButton_12.clicked.connect(lambda: self.masaText(masa1.i3,self.label_27,masa1.hesap,self.label_29))

        self.pushButton_15.clicked.connect(lambda: masa1.i4a())
        self.pushButton_15.clicked.connect(lambda: self.masaText(masa1.i4,self.label_28,masa1.hesap,self.label_29))
        self.pushButton_16.clicked.connect(lambda: masa1.i4e())
        self.pushButton_16.clicked.connect(lambda: self.masaText(masa1.i4,self.label_28,masa1.hesap,self.label_29))


        masa2=Masa()
        self.pushButton_2.clicked.connect(lambda: masa2.i1a())
        self.pushButton_2.clicked.connect(lambda: self.masaText(masa2.i1,self.label_7,masa2.hesap,self.label_12))
        self.pushButton.clicked.connect(lambda: masa1.i1e())
        self.pushButton.clicked.connect(lambda: self.masaText(masa2.i1,self.label_7,masa2.hesap,self.label_12))

        self.pushButton_4.clicked.connect(lambda: masa2.i2a())
        self.pushButton_4.clicked.connect(lambda: self.masaText(masa2.i2,self.label_8,masa2.hesap,self.label_12))
        self.pushButton_3.clicked.connect(lambda: masa2.i2e())
        self.pushButton_3.clicked.connect(lambda: self.masaText(masa2.i2,self.label_8,masa2.hesap,self.label_12))

        self.pushButton_6.clicked.connect(lambda: masa2.i3a())
        self.pushButton_6.clicked.connect(lambda: self.masaText(masa2.i3,self.label_9,masa2.hesap,self.label_12))
        self.pushButton_5.clicked.connect(lambda: masa2.i3e())
        self.pushButton_5.clicked.connect(lambda: self.masaText(masa2.i3,self.label_9,masa2.hesap,self.label_12))

        self.pushButton_8.clicked.connect(lambda: masa2.i4a())
        self.pushButton_8.clicked.connect(lambda: self.masaText(masa2.i4,self.label_10,masa2.hesap,self.label_12))
        self.pushButton_7.clicked.connect(lambda: masa2.i4e())
        self.pushButton_7.clicked.connect(lambda: self.masaText(masa2.i4,self.label_10,masa2.hesap,self.label_12))


        masa3=Masa()
        self.pushButton_43.clicked.connect(lambda: masa3.i1a())
        self.pushButton_43.clicked.connect(lambda: self.masaText(masa3.i1,self.label_53,masa3.hesap,self.label_57))
        self.pushButton_44.clicked.connect(lambda: masa3.i1e())
        self.pushButton_44.clicked.connect(lambda: self.masaText(masa3.i1,self.label_53,masa3.hesap,self.label_57))

        self.pushButton_37.clicked.connect(lambda: masa3.i2a())
        self.pushButton_37.clicked.connect(lambda: self.masaText(masa3.i2,self.label_54,masa3.hesap,self.label_57))
        self.pushButton_39.clicked.connect(lambda: masa3.i2e())
        self.pushButton_39.clicked.connect(lambda: self.masaText(masa3.i2,self.label_54,masa3.hesap,self.label_57))

        self.pushButton_40.clicked.connect(lambda: masa3.i3a())
        self.pushButton_40.clicked.connect(lambda: self.masaText(masa3.i3,self.label_55,masa3.hesap,self.label_57))
        self.pushButton_38.clicked.connect(lambda: masa3.i3e())
        self.pushButton_38.clicked.connect(lambda: self.masaText(masa3.i3,self.label_55,masa3.hesap,self.label_57))

        self.pushButton_41.clicked.connect(lambda: masa3.i4a())
        self.pushButton_41.clicked.connect(lambda: self.masaText(masa3.i4,self.label_56,masa3.hesap,self.label_57))
        self.pushButton_42.clicked.connect(lambda: masa3.i4e())
        self.pushButton_42.clicked.connect(lambda: self.masaText(masa3.i4,self.label_56,masa3.hesap,self.label_57))

        masa3=Masa()
        self.pushButton_43.clicked.connect(lambda: masa3.i1a())
        self.pushButton_43.clicked.connect(lambda: self.masaText(masa3.i1,self.label_53,masa3.hesap,self.label_57))
        self.pushButton_44.clicked.connect(lambda: masa3.i1e())
        self.pushButton_44.clicked.connect(lambda: self.masaText(masa3.i1,self.label_53,masa3.hesap,self.label_57))

        self.pushButton_37.clicked.connect(lambda: masa3.i2a())
        self.pushButton_37.clicked.connect(lambda: self.masaText(masa3.i2,self.label_54,masa3.hesap,self.label_57))
        self.pushButton_39.clicked.connect(lambda: masa3.i2e())
        self.pushButton_39.clicked.connect(lambda: self.masaText(masa3.i2,self.label_54,masa3.hesap,self.label_57))

        self.pushButton_40.clicked.connect(lambda: masa3.i3a())
        self.pushButton_40.clicked.connect(lambda: self.masaText(masa3.i3,self.label_55,masa3.hesap,self.label_57))
        self.pushButton_38.clicked.connect(lambda: masa3.i3e())
        self.pushButton_38.clicked.connect(lambda: self.masaText(masa3.i3,self.label_55,masa3.hesap,self.label_57))

        self.pushButton_41.clicked.connect(lambda: masa3.i4a())
        self.pushButton_41.clicked.connect(lambda: self.masaText(masa3.i4,self.label_56,masa3.hesap,self.label_57))
        self.pushButton_42.clicked.connect(lambda: masa3.i4e())
        self.pushButton_42.clicked.connect(lambda: self.masaText(masa3.i4,self.label_56,masa3.hesap,self.label_57))


        masa4=Masa()
        self.pushButton_34.clicked.connect(lambda: masa4.i1a())
        self.pushButton_34.clicked.connect(lambda: self.masaText(masa4.i1,self.label_43,masa4.hesap,self.label_47))
        self.pushButton_35.clicked.connect(lambda: masa4.i1e())
        self.pushButton_35.clicked.connect(lambda: self.masaText(masa4.i1,self.label_43,masa4.hesap,self.label_47))

        self.pushButton_28.clicked.connect(lambda: masa4.i2a())
        self.pushButton_28.clicked.connect(lambda: self.masaText(masa4.i2,self.label_44,masa4.hesap,self.label_47))
        self.pushButton_30.clicked.connect(lambda: masa4.i2e())
        self.pushButton_30.clicked.connect(lambda: self.masaText(masa4.i2,self.label_44,masa4.hesap,self.label_47))

        self.pushButton_31.clicked.connect(lambda: masa4.i3a())
        self.pushButton_31.clicked.connect(lambda: self.masaText(masa4.i3,self.label_45,masa4.hesap,self.label_47))
        self.pushButton_29.clicked.connect(lambda: masa4.i3e())
        self.pushButton_29.clicked.connect(lambda: self.masaText(masa4.i3,self.label_45,masa4.hesap,self.label_47))

        self.pushButton_32.clicked.connect(lambda: masa4.i4a())
        self.pushButton_32.clicked.connect(lambda: self.masaText(masa4.i4,self.label_46,masa4.hesap,self.label_47))
        self.pushButton_33.clicked.connect(lambda: masa4.i4e())
        self.pushButton_33.clicked.connect(lambda: self.masaText(masa4.i4,self.label_46,masa4.hesap,self.label_47))



        masa5=Masa()
        self.pushButton_52.clicked.connect(lambda: masa5.i1a())
        self.pushButton_52.clicked.connect(lambda: self.masaText(masa5.i1,self.label_63,masa5.hesap,self.label_67))
        self.pushButton_53.clicked.connect(lambda: masa5.i1e())
        self.pushButton_53.clicked.connect(lambda: self.masaText(masa5.i1,self.label_63,masa5.hesap,self.label_67))

        self.pushButton_46.clicked.connect(lambda: masa5.i2a())
        self.pushButton_46.clicked.connect(lambda: self.masaText(masa5.i2,self.label_64,masa5.hesap,self.label_67))
        self.pushButton_48.clicked.connect(lambda: masa5.i2e())
        self.pushButton_48.clicked.connect(lambda: self.masaText(masa5.i2,self.label_64,masa5.hesap,self.label_67))

        self.pushButton_49.clicked.connect(lambda: masa5.i3a())
        self.pushButton_49.clicked.connect(lambda: self.masaText(masa5.i3,self.label_65,masa5.hesap,self.label_67))
        self.pushButton_47.clicked.connect(lambda: masa5.i3e())
        self.pushButton_47.clicked.connect(lambda: self.masaText(masa5.i3,self.label_65,masa5.hesap,self.label_67))

        self.pushButton_50.clicked.connect(lambda: masa5.i4a())
        self.pushButton_50.clicked.connect(lambda: self.masaText(masa5.i4,self.label_66,masa5.hesap,self.label_67))
        self.pushButton_51.clicked.connect(lambda: masa5.i4e())
        self.pushButton_51.clicked.connect(lambda: self.masaText(masa5.i4,self.label_66,masa5.hesap,self.label_67))



        masa6=Masa()
        self.pushButton_61.clicked.connect(lambda: masa6.i1a())
        self.pushButton_61.clicked.connect(lambda: self.masaText(masa6.i1,self.label_73,masa6.hesap,self.label_77))
        self.pushButton_62.clicked.connect(lambda: masa6.i1e())
        self.pushButton_62.clicked.connect(lambda: self.masaText(masa6.i1,self.label_73,masa6.hesap,self.label_77))

        self.pushButton_55.clicked.connect(lambda: masa6.i2a())
        self.pushButton_55.clicked.connect(lambda: self.masaText(masa6.i2,self.label_74,masa6.hesap,self.label_77))
        self.pushButton_57.clicked.connect(lambda: masa6.i2e())
        self.pushButton_57.clicked.connect(lambda: self.masaText(masa6.i2,self.label_74,masa6.hesap,self.label_77))

        self.pushButton_58.clicked.connect(lambda: masa6.i3a())
        self.pushButton_58.clicked.connect(lambda: self.masaText(masa6.i3,self.label_75,masa6.hesap,self.label_77))
        self.pushButton_56.clicked.connect(lambda: masa6.i3e())
        self.pushButton_56.clicked.connect(lambda: self.masaText(masa6.i3,self.label_75,masa6.hesap,self.label_77))

        self.pushButton_59.clicked.connect(lambda: masa6.i4a())
        self.pushButton_59.clicked.connect(lambda: self.masaText(masa6.i4,self.label_76,masa6.hesap,self.label_77))
        self.pushButton_60.clicked.connect(lambda: masa6.i4e())
        self.pushButton_60.clicked.connect(lambda: self.masaText(masa6.i4,self.label_76,masa6.hesap,self.label_77))


        #ödeme ve sıfırlama
        self.pushButton_10.clicked.connect(lambda: self.masaSifirla(masa1, self.label_29,self.label_25,self.label_26,self.label_27,self.label_28, self.label))
        self.pushButton_9.clicked.connect(lambda: self.masaSifirla(masa2, self.label_12,self.label_7,self.label_8,self.label_9,self.label_10, self.label))
        self.pushButton_36.clicked.connect(lambda: self.masaSifirla(masa3, self.label_57,self.label_53,self.label_54,self.label_55,self.label_56, self.label))
        self.pushButton_19.clicked.connect(lambda: self.masaSifirla(masa4, self.label_47,self.label_43,self.label_44,self.label_45,self.label_46, self.label))
        self.pushButton_45.clicked.connect(lambda: self.masaSifirla(masa5, self.label_67,self.label_63,self.label_64,self.label_65,self.label_66, self.label))
        self.pushButton_54.clicked.connect(lambda: self.masaSifirla(masa6, self.label_73,self.label_74,self.label_75,self.label_76,self.label_77, self.label))


    def masaText(self,masa,label,hesap,hesapLabel):
        label.setText(str(masa))
        hesapLabel.setText(str(hesap))


    def masaSifirla(self,masa,hesapLabel,lab1,lab2,lab3,lab4,kasaLabel):
        masa.i1=0
        masa.i2=0
        masa.i3=0
        masa.i4=0
        self.kasa+=masa.hesap
        masa.hesap=0
        hesapLabel.setText(str(0))
        kasaLabel.setText(str(self.kasa))
        lab1.setText(str(0))
        lab2.setText(str(0))
        lab3.setText(str(0))
        lab4.setText(str(0))





if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    arayuz=Adisyon()
    arayuz.show()
    uygulama.exec_()