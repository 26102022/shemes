import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from collections import Counter
import numpy as np
import random
import math 
import matplotlib as mpl

mpl.rcParams['axes.linewidth'] = 0.1

def main():
    qt_creator_file = "mainwindow.ui"
    Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)

    class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.setupUi(self)
            self.sc = MplCanvas(self)             
            toolbar = NavigationToolbar(self.sc, self)
            self.sc2 = MplCanvas1(self)             
            toolbar2 = NavigationToolbar(self.sc2, self)
            self.sc3 = MplCanvas1(self)             
            toolbar3 = NavigationToolbar(self.sc3, self)
             
            self.lay = QtWidgets.QVBoxLayout(self.mplWidget)
            self.lay.addWidget(toolbar)
            self.lay.addWidget(self.sc)  
            self.lay2 = QtWidgets.QVBoxLayout(self.mplWidget_2)
            self.lay2.addWidget(toolbar2)
            self.lay2.addWidget(self.sc2)  
            
            #self.lay2 = QtWidgets.QVBoxLayout(self.mplWidget_3)
            self.lay2.addWidget(toolbar3)
            self.lay2.addWidget(self.sc3)  
              
            self.addButton.clicked.connect(self.the_button_was_clicked)

        def the_button_was_clicked(self):
            self.sc.axes.cla()
            self.sc2.axes.cla()
            self.sc3.axes.cla()
            histo(self)
            #self.dumai.setChecked(False)


    class MplCanvas(FigureCanvasQTAgg):                                 # !!! +++
        def __init__(self, parent=None):
            fig = Figure()
            self.axes = fig.add_subplot(111)
            super(MplCanvas, self).__init__(fig)
    class MplCanvas1(FigureCanvasQTAgg):                                 # !!! +++
        def __init__(self, parent=None ):
            fig = Figure()
            self.axes = fig.add_subplot(111)
            
            super(MplCanvas1, self).__init__(fig)    
    class MplCanvas2(FigureCanvasQTAgg):                                 # !!! +++
        def __init__(self, parent=None ):
            fig = Figure(figsize=(10,10))
            

            self.axes = fig.add_subplot(211)
            super(MplCanvas2, self).__init__(fig)    
           

    
    def histo(self):
        #функция в функции
        self.pred = False
        vr= self.vrub.currentText()
        esh=self.esh.currentText()
        insk= self.inskv.currentText()
        rows = self.rows.value()
        wels = self.wels.value()
        
        
        if self.poty.isChecked()==True:
            devskv=['0','25',"50","75","100","125","150","175","200","225","250","300","350","400","450","500","750",'1000']
            stdevskv=[0,2,2.5,3.5,3.5,4,4.5,5.5,6,6,6.3,6.3,6.3,6.3,6.3,10.5,12.4,18.5]
            dictskv={}
            for i in range(len(devskv)):
                dictskv[devskv[i]]=stdevskv[i]
            devsp=['0','17',"25","42","67","109","176"]
            stdevsp=[0,1.9,2.3,3,3.2,3.5,5.5]
            dictsp={}
            for i in range(len(devsp)):
                dictsp[devsp[i]]=stdevsp[i]
            self.sig_vr.setText(str(dictsp[str(vr)]))
            self.mid_vr.setText(str(vr))
            self.sig_esh.setText(str(dictsp[str(esh)])) 
            self.mid_esh.setText(str(esh))
            self.sig_in.setText(str(dictskv[str(insk)]))
            self.mid_in.setText(str(insk))  
        if self.belin.isChecked()==True:
            dictsp={}
            dictskv={}
            
            devskv=['0','25',"50","75","100","125","150","175","200","225","250","300","350","400","450","500", '750','1000']
            stdevskv=[0,6.8,9.7,10.6,11.5,12.4,13.3,14.2,15.1,16.0,16.9,18.7,20.5,22.3,24.1,25.7,43.1,111.9]
            devsp=['0','17',"25","42","67","109","176"]
            stdevsp=[0,8.5,6.8,10.8,9.5,13.3,19.28]
            meanlistskv=[0,29.6,57.6854076,86.5281114,115.3708152,144.213519,173.0562228,201.8989266,230.7416304,259.5843342,288.427038,346.1124456,403.7978532,461.4832608,519.1686684,539,822.15,1105.3]
            meanlist=[0,22.6,29.6,51.4,76.1,119.7,202.4]
            if self.checkTime.isChecked() ==True:
                for i in range(len(stdevskv)):
                    stdevskv[i]=2*stdevskv[i]
                for i in range(len(stdevsp)):
                    stdevsp[i]=2*stdevsp[i]
                    
            if self.holod.isChecked() ==True:
                for i in range(len(stdevskv)):
                    stdevskv[i]=2*stdevskv[i]
                for i in range(len(stdevsp)):
                    stdevsp[i]=2*stdevsp[i]
                    
            if self.otkl_v_min.isChecked() ==True:
                for i in range(len(meanlistskv)):
                    meanlistskv[i]=float(devskv[i])-(meanlistskv[i]-float(devskv[i]))
                for i in range(len(meanlist)):
                    meanlist[i]=float(devsp[i])-(meanlist[i]-float(devsp[i]))
                    
            for i in range(len(devskv)):
                dictskv[devskv[i]]=round(stdevskv[i]/6,1)
            for i in range(len(devsp)):
                dictsp[devsp[i]]=round(stdevsp[i]/6,1)


            meand={}
            for i in range(len(devskv)):
                meand[devskv[i]]=round(meanlistskv[i],1)
            for i in range(len(devsp)):
                meand[devsp[i]]=round(meanlist[i],1)
            
                
            self.sig_vr.setText(str(dictsp[vr]))
            self.sig_esh.setText(str(dictsp[esh])) 
            self.sig_in.setText(str(dictskv[insk]))
            vr=meand[vr]
            esh=meand[esh]
            insk=meand[insk]
            self.mid_vr.setText(str(vr))
            self.mid_esh.setText(str(esh))
            self.mid_in.setText(str(insk))
        if self.kuzgtu.isChecked()==True:
            vr= float(self.vrub.currentText())
            esh= float(self.esh.currentText())
            insk= float(self.inskv.currentText())
            s_vr=0.01*vr*(3.97*math.exp(-0.008*vr)+2)
            s_esh=0.01*esh*(3.97*math.exp(-0.008*esh)+2)
            s_insk=0.01*insk*(3.97*math.exp(-0.008*insk)+2)
            self.sig_vr.setText(str(round(s_vr,2)))
            self.mid_vr.setText(str(vr))
            self.sig_esh.setText(str(round(s_esh,2))) 
            self.mid_esh.setText(str(esh))
            self.sig_in.setText(str(round(s_insk,2)))
            self.mid_in.setText(str(insk))
           
        
        
        
        if self.zheskyi.isChecked()==True:
            sg_e= float(self.sig_esh.text())
            mid_esh=float(self.mid_esh.text())
            sig_in= float(self.sig_in.text())
            mid_in= float(self.mid_in.text())
            sg_vr= float(self.sig_vr.text())
        
        
        
        
        
        mid_vr= float(self.mid_vr.text())
        sg_e= float(self.sig_esh.text())
        mid_esh=float(self.mid_esh.text())
        sig_in= float(self.sig_in.text())
        mid_in= float(self.mid_in.text())
        sg_vr= float(self.sig_vr.text())
        mid_vr= float(self.mid_vr.text())
        vrub=mid_vr
        eshelon=mid_esh
        
        list1=[]
        list2=[]
        if self.ininsk.isChecked() == True:
            for i in range(600):
                    list1.append(round(random.gauss(vrub, sg_vr)+random.gauss(mid_in, sig_in),1))
            for i in range(600):
                    list2.append(round(random.gauss(eshelon,sg_e)+random.gauss(mid_in, sig_in),1))
            vrub=mid_vr+mid_in
            eshelon=mid_esh+mid_in
        else:
            for i in range(600):
                    list1.append(round(random.gauss(vrub, sg_vr),1))
            for i in range(600):
                    list2.append(round(random.gauss(eshelon,sg_e),1))

        
            
            
                
        self.list1=list1                  
        self.list2=list2                  
        self.sc.axes.cla()
        list1=self.list1
        list2=self.list2
         
        self.sc.axes.axvline(vrub)
        self.sc.axes.axvline(eshelon)
        
        self.sc.axes.hist(
                [list1], alpha=0.5
            )
        self.sc.axes.hist(
                [list2], alpha=0.5
            )
        self.sc.draw()
        c1=[]
        a1=list1
        b1=list2                       
        for i1 in a1:
                for j1 in b1:
                    if i1 == j1:
                
                        c1.append(i1)
                        break
                        
                        
        tr2=round(100*(len(c1)/len(a1)),1)
        self.label_5.setText("Процент пересечения = "+str(tr2)+" %")
        def memblecs(self):
            wels_list=[]
            wels_l=[]
            vrub=mid_vr
            eshelon=mid_esh      
            if self.no_miss.isChecked() == True:
                for j in range(wels):
                    wels_list.append(vrub)
                wels_l.append(wels_list)
                for j in range(rows-1):
                    wels_list=[]
                    for i in range(wels):
                        wels_list.append(eshelon)
                    wels_l.append(wels_list)
            else:
                for j in range(wels):
                    wels_list.append(round(random.gauss(vrub, sg_vr),1))
                wels_l.append(wels_list)
                for j in range(rows-1):
                    wels_list=[]
                    for i in range(wels):
                        wels_list.append(round(random.gauss(eshelon,sg_e),1))
                    wels_l.append(wels_list)
            suma=[]
            sum=[wels_l[0][0]]
            sum1=[wels_l[0][0]]
            for i in range(wels-1):
                sum.append(round(sum[i]+wels_l[0][i+1],1))
                sum1.append(round(sum[i]+wels_l[0][i+1],1))
            suma.append(sum1)
            sum1=[]
            for i in range(wels):
                sum.append(round(sum[i]+wels_l[1][i],1))
                sum1.append(round(sum[i]+wels_l[1][i],1))
            suma.append(sum1) 
            for j in range(2,rows):
                sum1=[]
                for i in range(wels):
                    sum.append(round(sum[i+wels*(j-1)]+wels_l[j][i],1))
                    sum1.append(round(sum[i+wels*(j-1)]+wels_l[j][i],1))
                suma.append(sum1)
            if self.ininsk.isChecked() == True:
                if self.no_miss.isChecked() == True:
                    for i in range(rows):
                        for j in range(wels):
                            suma[i][j] = suma[i][j]+float(mid_in)  
                else:
                    for i in range(rows):
                        for j in range(wels):
                            suma[i][j] = suma[i][j]+round(float(random.gauss(mid_in, sig_in)),1)
            rowes = suma

            minus=[]
            for j in range(wels):
                mmii=[]
                for i in range(rows-1):
                    mmii.append(suma[i+1][j]-suma[i][j])
                minus.append(mmii)
            mmii=[0]
            for i in range(wels-1):
                mmii.append(suma[0][i+1]-suma[0][i])
            flip=np.transpose(minus)
            flip=np.flip(flip)      
            minus=list(flip)
            minus.append(mmii)
            minus.reverse()

            return minus,rowes
        minus,rowes = memblecs(self)  
        self.minus=minus
        self.sc2.axes.cla()
        self.sc2.axes.matshow(rowes, cmap = matplotlib.colors.ListedColormap(['g', 'b', 'y', 'r', 'maroon']))
        
        self.sc3.axes.cla()
        self.sc3.axes.matshow(minus, cmap = matplotlib.colors.ListedColormap(['g', 'b', 'y', 'r', 'maroon']))
        if (wels > 10 and rows > 10) and self.pred==False:
            self.memtext.setChecked(True)
            self.pred = not self.pred
      
        if self.memtext.isChecked()==False:
            for (i, j), z in np.ndenumerate(rowes):
                self.sc2.axes.text(j, i, '{:0.1f}'.format(z), ha='center', va='center',
                        bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.3'))
            for (i, j), z in np.ndenumerate(minus):
                self.sc3.axes.text(j, i, '{:0.1f}'.format(z), ha='center', va='center',
                        bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.3'))
                
        self.sc2.draw()

        self.sc3.draw()


        count=False
        ccc=0
        scolp=0
        if self.dumai.isChecked() == True:
            if tr2 > 0:
                for monte in range(10**3):
                    minus,rowes=memblecs(self)
                    for i in range(rows):
                        for j in range(wels):
                            scolp=scolp+1
                            if minus[i][j] <=0 and (i!=0 and j !=0):
                                count=True
                                
                            if count == True:
                                ccc=ccc+1  
                          
                print(scolp)           
                print(ccc)           
                self.montecarlo.setText("Вероятность того, что хотя бы одна скважина отработает раньше\n(на 1000 случаев) = "+str(100*round(ccc/scolp,2))+" %")
            else:
                self.sc3.axes.cla()
                self.montecarlo.setText("Вероятность того, что хотя бы одна скважина отработает раньше\n(на 1000 случаев) = 0 %")
                
                count = 0
    
 
 
 
        
        

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
main()