import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton,QMessageBox
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from collections import Counter
import matplotlib.backend_bases
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib as mpl
# import seaborn as sns
from openpyxl import Workbook
import time

cm=['RdBu','magma', 'inferno', 'plasma', 'viridis', 'cividis', 'twilight', 'twilight_shifted', 'turbo', 'Blues', 'BrBG', 'BuGn', 'BuPu', 'CMRmap', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', 'PRGn', 'PiYG', 'PuBu', 'PuBuGn', 'PuOr', 'PuRd', 'Purples', 'RdGy', 'RdPu', 'RdYlBu', 'RdYlGn', 'Reds', 'Spectral', 'Wistia', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'binary', 'bone', 'brg', 'bwr', 'cool', 'coolwarm', 'copper', 'cubehelix', 'flag', 'gist_earth', 'gist_gray', 'gist_heat', 'gist_ncar', 'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', 'gnuplot2', 'gray', 'hot', 'hsv', 'jet', 'nipy_spectral', 'ocean', 'pink', 'prism', 'rainbow', 'seismic', 'spring', 'summer', 'terrain', 'winter', 'Accent', 'Dark2', 'Paired', 'Pastel1', 'Pastel2', 'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c', 'grey', 'gist_grey', 'gist_yerg', 'Grays', 'magma_r', 'inferno_r', 'plasma_r', 'viridis_r', 'cividis_r', 'twilight_r', 'twilight_shifted_r', 'turbo_r', 'Blues_r', 'BrBG_r', 'BuGn_r', 'BuPu_r', 'CMRmap_r', 'GnBu_r', 'Greens_r', 'Greys_r', 'OrRd_r', 'Oranges_r', 'PRGn_r', 'PiYG_r', 'PuBu_r', 'PuBuGn_r', 'PuOr_r', 'PuRd_r', 'Purples_r', 'RdBu_r', 'RdGy_r', 'RdPu_r', 'RdYlBu_r', 'RdYlGn_r', 'Reds_r', 'Spectral_r', 'Wistia_r', 'YlGn_r', 'YlGnBu_r', 'YlOrBr_r', 'YlOrRd_r', 'afmhot_r', 'autumn_r', 'binary_r', 'bone_r', 'brg_r', 'bwr_r', 'cool_r', 'coolwarm_r', 'copper_r', 'cubehelix_r', 'flag_r', 'gist_earth_r', 'gist_gray_r', 'gist_heat_r', 'gist_ncar_r', 'gist_rainbow_r', 'gist_stern_r', 'gist_yarg_r', 'gnuplot_r', 'gnuplot2_r', 'gray_r', 'hot_r', 'hsv_r', 'jet_r', 'nipy_spectral_r', 'ocean_r', 'pink_r', 'prism_r', 'rainbow_r', 'seismic_r', 'spring_r', 'summer_r', 'terrain_r', 'winter_r', 'Accent_r', 'Dark2_r', 'Paired_r', 'Pastel1_r', 'Pastel2_r', 'Set1_r', 'Set2_r', 'Set3_r', 'tab10_r', 'tab20_r', 'tab20b_r', 'tab20c_r']
mpl.rcParams['axes.linewidth'] = 0.1
global point
point=1
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
            
            self.lay3 = QtWidgets.QVBoxLayout(self.mplWidget_3)
            self.lay3.addWidget(toolbar3)
            self.lay3.addWidget(self.sc3)  
            
            self.cmap.addItems(cm)
            self.addButton.clicked.connect(self.the_button_was_clicked)
            self.disctB.clicked.connect(self.distribution_slowdowns)
            self.savee.triggered.connect(self.save)
        def save(self):
                wb = Workbook()

                # grab the active worksheet
                ws = wb.active

                array = rowe

                for subarray in array:
                    ws.append(subarray)


                # array =rowe

                # col = 8
                # row = 5
                # for subarray in array:
                #     for index, value in enumerate(subarray):
                #         ws.cell(column=col+index, row=row).value = value
                #     col += 1
                #     row += 1
 
                # Save the file
                wb.save("delays.xlsx")
        def distribution_slowdowns(self):
            self.sc.axes.cla()    
            self.sc.draw()
            mathematical_distribution_slowdowns(self)
        def the_button_was_clicked(self):
            self.sc.axes.cla()    
            self.sc2.axes.cla()    
            self.sc3.axes.cla()    
            self.sc.draw()

            mathematical_distribution_slowdowns(self)
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
            button_press_event_id = fig.canvas.mpl_connect('button_press_event',
                                                   onMouseEvent)
            
            #fig.canvas.mpl_disconnect(button_press_event_id)
            super(MplCanvas1, self).__init__(fig)    
    class MplCanvas2(FigureCanvasQTAgg):                                 # !!! +++
        def __init__(self, parent=None ):
            fig = Figure(figsize=(10,10))
            

            self.axes = fig.add_subplot(211)
            super(MplCanvas2, self).__init__(fig)    
           
    def read_data(self):
            global mid_vr, sg_e, mid_esh, sig_in, mid_in, sg_vr
            
            mid_vr= float(self.mid_vr.text())
            sg_e= float(self.sig_esh.text())
            mid_esh=float(self.mid_esh.text())
            sig_in= float(self.sig_in.text())
            mid_in= float(self.mid_in.text())
            sg_vr= float(self.sig_vr.text())
            
            return mid_vr,sg_e,mid_esh,sig_in,mid_in,sg_vr

        
    def mathematical_distribution_slowdowns(self):
        dolgo=int(self.dolg_2.text())
        
        self.pred = False
        vr= self.vrub.currentText()
        esh=self.esh.currentText()
        insk= self.inskv.currentText()
        global rows,wels
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
        # if self.belin.isChecked()==True:
        #     dictsp={}
        #     dictskv={}
        #     devskv=['0','25',"50","75","100","125","150","175","200","225","250","300","350","400","450","500", '750','1000']
        #     stdevskv=[0,6.8,9.7,10.6,11.5,12.4,13.3,14.2,15.1,16.0,16.9,18.7,20.5,22.3,24.1,25.7,43.1,111.9]
        #     devsp=['0','17',"25","42","67","109","176"]
        #     stdevsp=[0,8.5,6.8,10.8,9.5,13.3,19.28]
        #     meanlistskv=[0,29.6,57.6854076,86.5281114,115.3708152,144.213519,173.0562228,201.8989266,230.7416304,259.5843342,288.427038,346.1124456,403.7978532,461.4832608,519.1686684,539,822.15,1105.3]
        #     meanlist=[0,22.6,29.6,51.4,76.1,119.7,202.4]
        #     if self.checkTime.isChecked() ==True:
        #         for i in range(len(stdevskv)):
        #             stdevskv[i]=2*stdevskv[i]
        #         for i in range(len(stdevsp)):
        #             stdevsp[i]=2*stdevsp[i]
                    
        #     if self.holod.isChecked() ==True:
        #         for i in range(len(stdevskv)):
        #             stdevskv[i]=2*stdevskv[i]
        #         for i in range(len(stdevsp)):
        #             stdevsp[i]=2*stdevsp[i]
                    
        #     if self.otkl_v_min.isChecked() ==True:
        #         for i in range(len(meanlistskv)):
        #             meanlistskv[i]=float(devskv[i])-(meanlistskv[i]-float(devskv[i]))
        #         for i in range(len(meanlist)):
        #             meanlist[i]=float(devsp[i])-(meanlist[i]-float(devsp[i]))
                    
        #     for i in range(len(devskv)):
        #         dictskv[devskv[i]]=round(stdevskv[i]/6,1)
        #     for i in range(len(devsp)):
        #         dictsp[devsp[i]]=round(stdevsp[i]/6,1)


        #     meand={}
        #     for i in range(len(devskv)):
        #         meand[devskv[i]]=round(meanlistskv[i],1)
        #     for i in range(len(devsp)):
        #         meand[devsp[i]]=round(meanlist[i],1)
            
                
        #     self.sig_vr.setText(str(dictsp[vr]))
        #     self.sig_esh.setText(str(dictsp[esh])) 
        #     self.sig_in.setText(str(dictskv[insk]))
        #     vr=meand[vr]
        #     esh=meand[esh]
        #     insk=meand[insk]
        #     self.mid_vr.setText(str(vr))
        #     self.mid_esh.setText(str(esh))
        #     self.mid_in.setText(str(insk))
        # if self.kuzgtu.isChecked()==True:
        #     vr= float(self.vrub.currentText())
        #     esh= float(self.esh.currentText())
        #     insk= float(self.inskv.currentText())
        #     s_vr=0.01*vr*(3.97*math.exp(-0.008*vr)+2)
        #     s_esh=0.01*esh*(3.97*math.exp(-0.008*esh)+2)
        #     s_insk=0.01*insk*(3.97*math.exp(-0.008*insk)+2)
        #     self.sig_vr.setText(str(round(s_vr,2)))
        #     self.mid_vr.setText(str(vr))
        #     self.sig_esh.setText(str(round(s_esh,2))) 
        #     self.mid_esh.setText(str(esh))
        #     self.sig_in.setText(str(round(s_insk,2)))
        #     self.mid_in.setText(str(insk))
        if self.zheskyi.isChecked()==True:
            sg_e= float(self.sig_esh.text())
            mid_esh=float(self.mid_esh.text())
            sig_in= float(self.sig_in.text())
            mid_in= float(self.mid_in.text())
            sg_vr= float(self.sig_vr.text())      
        mid_vr,sg_e,mid_esh,sig_in,mid_in,sg_vr= read_data(self)
        if self.holod.isChecked() ==True:
            sg_e=2*sg_e
            sig_in=2*sig_in
            sg_vr=2*sg_vr
        if self.checkTime.isChecked() ==True:
            sg_e=2*sg_e
            sig_in=2*sig_in
            sg_vr=2*sg_vr
        vrub=mid_vr
        eshelon=mid_esh 
        list1=[]
        list2=[]
        global instk_check
        instk_check = self.ininsk.isChecked()
        if self.ininsk.isChecked() == True:
            for i in range(dolgo):

                                    list1.append(round(random.gauss(vrub, sg_vr)+random.gauss(mid_in, sig_in),point))
            for i in range(dolgo):

                                    list2.append(round(random.gauss(eshelon,sg_e)+random.gauss(mid_in, sig_in),point))
            vrub=mid_vr+mid_in
            eshelon=mid_esh+mid_in
        else:
            for i in range(dolgo):

                                    list1.append(round(random.gauss(vrub, sg_vr),point))
            for i in range(dolgo):

                                    list2.append(round(random.gauss(eshelon,sg_e),point)) 
        self.list1=list1                  
        self.list2=list2   
        self.sc.axes.cla()
        self.sc.draw()
        self.sc.axes.axvline(vrub)
        self.sc.axes.axvline(eshelon)
        self.sc.axes.hist(
                [list1],alpha=0.5, 
            )
        self.sc.axes.hist(
                [list2],alpha=0.5
            )

        self.sc.axes.set_ylim(0,dolgo)
        self.sc.axes.set_title("Гистограммы отклонения от номинала")
        self.sc.axes.set_xlabel("Время срабатывания")
        self.sc.axes.set_ylabel(f"Количество срабатываний на {dolgo} повт.")
        self.sc.draw()             
        # def jaccard(list1, list2):
        #     intersection = len(list(set(list1).intersection(list2)))
        #     union = (len(list1)+ len(list2)) - intersection 
        #     return float(intersection) / union
        start_time=time.time()


        a = list1
        b = list2

        c = []

        for item in a:
            if item not in c:
                a_item = a.count(item)
                b_item = b.count(item)
                min_count = min(a_item, b_item)
                # c += [item] * min_count
                for i in range(min_count):
                    c.append(item)
                                        
        end_time = time.time()
        print("Время расчета вариации гистограмм: ",end_time-start_time)    
        
        self.tr2=len(c)/dolgo
        self.label_5.setText("Процент пересечения = "+str(round(100*self.tr2,1))+" %")  


    def histo(self):
 
        def memblecs(self,wels,rows):
            wels_list=[]
            wels_l=[]
            vrub=mid_vr
            eshelon=mid_esh  
            global rowe    
            if (self.action_5.isChecked())==False:
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
                sum[0]=0
                sum1[0]=0
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
                rowe=suma
                suma[0][0]=0
                if self.ininsk.isChecked() == True:
                    suma[0][0]=0
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
            else:
                rrr=rows
                www=wels
                wels=rrr
                rows=www
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
                sum[0]=0
                sum1[0]=0
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
                rowe=suma
                suma[0][0]=0
                if self.ininsk.isChecked() == True:
                    suma[0][0]=0
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
                rows=rrr
                wels=www
                minus=np.transpose(minus)
                rowes=np.transpose(rowes)
            return minus,rowes
        global rowes
        minus,rowes = memblecs(self,wels,rows)  
        self.minus=minus
        
        # #группировка по диапазону в 20 мс
        # print(minus)
        # g=[]
        # for i in range(rows):
        #     for j in range(wels-1):
        #         if minus[i][j+1]>20:
        #             break
        #         else:
        #             g.append("g"+str(i)+" "+str(j+1))
                
        # print(g)
        
        if (self.action_5.isChecked())==False:  
            for i in range(wels):        
                gx=[i,i]
                gy=[0,rows-1]
                self.sc2.axes.plot(gx,gy,linewidth=2, color='black',)
            gx=[0,wels-1]
            gy=[0,0]
            self.sc2.axes.plot(gx,gy,linewidth=2, color='black',)
        else:
            gx=[0,0]
            gy=[0,rows-1]
            self.sc2.axes.plot(gx,gy,linewidth=2, color='black',)
            for i in range(rows):        
                gx=[0,wels-1]
                gy=[i,i]
                self.sc2.axes.plot(gx,gy,linewidth=2, color='black',)      
        self.sc2.axes.matshow(rowes,interpolation = self.interpol.currentText(),origin='lower',aspect='auto', cmap =self.cmap.currentText()) 
        
        self.sc2.axes.set_xticks((np.arange(0, wels, 1)),(np.arange(1, wels+1, 1)))
        self.sc2.axes.set_yticks((np.arange(0, rows, 1)),(np.arange(1, rows+1, 1)))
        self.sc2.axes.xaxis.set_ticks_position('bottom')
        self.sc2.axes.yaxis.set_ticks_position('left')
        self.sc2.axes.set_title("Матрица времени срабатывания скважин")
        self.sc2.axes.set_xlabel("Порядковый номер скважины в ряду")
        self.sc2.axes.set_ylabel("Порядковый номер ряда")
        
        if (wels > 10 and rows > 10):
            self.memtext.setChecked(True)
        if (wels > 10 and rows > 10) and self.pred==False:
            self.pred = not self.pred
        if self.memtext.isChecked()==False:
            for (i, j), z in np.ndenumerate(rowes):
                self.sc2.axes.text(j, i, '{:0.1f}'.format(z), ha='center', va='center',
                        bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.3'))
        self.sc2.draw()
        count=False
         
         
        montecarlo=self.montenumber.value() 
        if self.sc3type.currentText() == 'Разница между временем срабатывания соседних скважин':
            x1x=[]
            y1y=[]
            holes=[]
            y=[]
            for i in range(montecarlo):
                minus1,rowes1 = memblecs(self,wels,rows)  
                
                for k in range(len(minus1)):
                    for j in range(1,len(minus1[k])):
                        holes.append(minus1[k][j])
                
            holes =dict(Counter(holes))
            holes= dict(sorted(holes.items()))
            y=list(holes.values())
            # y1y.append(y)
            # x1x.append(holes.keys())
            # x11=[]
            # for i in x1x:
            #     for j in i:
            #         x11.append(j)
            # y11=[]
            # for i in y1y:
            #     for j in i:
            #         y11.append(j)
            # print(x11,y11)        
            # self.sc3.axes.bar(x11,y11, color='blue')
            self.sc3.axes.bar(holes.keys(),y, color='blue')
            self.sc3.axes.set_title("Разница между временем срабатывания соседних скважин")
            self.sc3.axes.set_xlabel("Разница во времени")
            self.sc3.axes.set_ylabel("Количество скважин")
            self.sc3.draw()                                          
        elif self.sc3type.currentText() == 'Количество скважин отработавших раньше времени':
             
                self.sc3.axes.cla()    
                self.sc3.draw()
                if self.tr2 > 0: 
                    lul=[]
                    try:
                        start_time=time.time()
                        for monte in range(montecarlo):
 
                                        ccc=0
                                        minus,rowes=memblecs(self,wels,rows)
                                        for i in range(rows):
                                            for j in range(wels-1):
                                                if minus[i][j+1] <=0:
                                                    ccc=ccc+1
                                        lul.append(ccc)  
                        end_time = time.time()
                        print(end_time-start_time)    
                        lul =dict(Counter(lul))
                        lul=dict(sorted(lul.items()))
                        #self.montecarlo.setText(str(lul))
                        print(str(lul))
                        msg = QMessageBox()
                        msg.setWindowTitle("Значения")
                        msg.setText(f"{lul}")
                        msg.setIcon(QMessageBox.Icon.Information)
                        msg.exec()
                        showme={}
                        if len(list(lul.keys()))==1:
                            self.sc3.axes.cla()    
                            self.montecarlo.setText("0 %")
                            msg = QMessageBox()
                            msg.setWindowTitle("Информация")
                            msg.setText(f"На {montecarlo} случаев нет значений.")
                            msg.setIcon(QMessageBox.Icon.Information)

                            msg.exec()
                        else: 
                            y=list(lul.values())
                            if self.pcent.isChecked() ==True:
                                self.sc3.axes.set_yscale('linear') 
                                self.dol.setChecked(False)
                                self.logs.setChecked(False)
                                for i in range(len(y)):
                                    y[i]=100*int(y[i])/int(montecarlo)
                                    showme[list(lul.keys())[i]]=y[i]  
                                #self.montecarlo.setText(str(showme))
                                self.sc3.axes.set_ylabel("Процент случаев")    
                            elif self.dol.isChecked() == True:
                                self.pcent.setChecked(False)
                                self.logs.setChecked(False)
                                for i in range(len(y)):
                                    y[i]=int(y[i])/int(montecarlo)      
                                    showme[list(lul.keys())[i]]=y[i]        
                                #self.montecarlo.setText(str(showme))
                                self.sc3.axes.set_ylabel("Доля случаев")                                   
                            else:
                                self.logs.setChecked(True) 
                                self.dol.setChecked(False)
                                self.pcent.setChecked(False)
                                y=list(lul.values())
                                self.sc3.axes.set_yscale('log') 
                                self.sc3.axes.set_ylabel("Количество случаев")   
                            width=0.1   
                            self.sc3.axes.bar(lul.keys(),y,width,edgecolor='black', color='blue')
                            self.sc3.axes.set_title("Количество скважин отработавших раньше времени")
                            self.sc3.axes.set_xlabel("Число скважин")
                            self.sc3.draw()                                          
                    except Exception as e:
                        print(e)
                else:  
                            self.sc3.draw()
                            self.sc3.axes.cla()
                            self.montecarlo.setText("0 %")
                            msg = QMessageBox()
                            msg.setWindowTitle("Информация")
                            msg.setText(f"На {montecarlo} случаев нет значений.")
                            msg.setIcon(QMessageBox.Icon.Information)

                            msg.exec()

        elif self.sc3type.currentText() == 'Окно времени':   
               #объединение по 20 мс
                self.sc3.axes.cla()    
                if self.tr2 > 0: 
                    lul=[]
                    
                    # try:
                    #     start_time=time.time()
                    #     # for monte in range(montecarlo):
 
                    #     #                     ccc=0
                    #     #                     minus,rowes=memblecs(self,wels,rows)
                    #     #                     for i in range(rows):
                    #     #                         for j in range(wels):
                    #     #                             if minus[i][j] <=0 and (i!=0 and j !=0):

                    #     #                                     ccc=ccc+1
                    #     #                     lul.append(ccc)  
                    #     end_time = time.time()
                    #     print(end_time-start_time)    
                    # except Exception as e:
                    #     print(e)
                    # minus,rowes=memblecs(self,wels,rows)    
                    step=int(self.time_step.text())
                    start_time=time.time()
                    
            
                        
                    for i in range(rows):
                            for j in range(wels):
                                for s in range(1,1000,1):
                                    if rowes[i][j]<=s*step and rowes[i][j]>step*(s-1):
                                        lul.append((s)*step)
                                        break
                    end_time = time.time()
                    print("Время расчета вариации: ",end_time-start_time)    

                                    

                    lul =dict(Counter(lul))
                    lul=dict(sorted(lul.items()))
                    #self.montecarlo.setText(str(lul))
                    print(str(lul))
                    y=list(lul.values())
                    self.sc3.axes.set_ylabel("Количество скважин")   
                    width=step
                    self.sc3.axes.bar(lul.keys(),y,width, color='blue')
                    self.sc3.axes.set_title("Окно времени")
                    self.sc3.axes.set_xlabel("Время")
                    # self.sc3.axes.set_xticks(np.arange(min(lul.keys()),max(lul.keys())+1,20.0))
                    self.sc3.axes.set_yticks(np.arange(0,max(y)+1,1.0))
                    
                    self.sc3.draw()                                          
                else:  
                    self.sc3.draw()
                    self.sc3.axes.cla()
                    self.montecarlo.setText("0 %")
                
    def _print_event(event: matplotlib.backend_bases.Event, attr_list: list[str]):
        x=int(round(getattr(event,'xdata'),0))
        y=int(round(getattr(event,'ydata'),0))
        #print(x,y)
        def list_change(rowe,y):
            list1=[]
            mid=rowe
            if instk_check == True:
                if y >0.5:
                    sqrdev=sg_e+sig_in
                else:
                    sqrdev=sg_vr+sig_in
            else:
                if y >0.5:
                    sqrdev=sg_e
                else:
                    sqrdev=sg_vr
            try:
                
                for i in range(10**6):
                        list1.append(round(random.gauss(mid,sqrdev),1))
                lis=list1  
            except Exception as e:
                print(e)
                lis=[]
            return lis       
        data=list_change(rowe[y][x],y)
        plt.hist(data,width=1,edgecolor='black', color='blue')
        plt.show()
    def onMouseEvent(event: matplotlib.backend_bases.MouseEvent) -> None:
        '''
        Обработчик событий, связанных с мышью
        '''
        attr_list = ['name',
                    'dblclick', 'button', 'key',
                    'xdata', 'ydata',
                    'x', 'y',
                    'inaxes',
                    'step',
                    'guiEvent']
        _print_event(event, attr_list)
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.showNormal()
        window.show()
        sys.exit(app.exec())

main()