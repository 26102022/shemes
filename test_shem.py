import plotly.graph_objects as go
import plotly.express as px
from dash import dash_table,Dash, dcc, html, Input, Output, callback,get_asset_url, no_update, ctx
from dash.dash_table.Format import Group
import math
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_mantine_components as dmc
import random
app = Dash(__name__)
app.layout = html.Div([
        dcc.Store(id="stored",data=[0]*55),

        html.Div([
    dmc.Grid([
        dmc.Col([
                html.P("Выберите схему бурения", style={'text-align':'center', 'font-size':'1.5rem'}),
        html.Div([dcc.RadioItems(['Шахматная', 'Прямоугольная'], 'Прямоугольная', id ='chemabur', inline=True)], style=  {"display": "flex","justify-content": "center",'font-size':'1.2rem'}),
                html.P("Для учета отклонения от номинала", style={'text-align':'center', 'font-size':'1.5rem'}),
        
        html.Div([dcc.RadioItems(['Принять отклонения по ТУ',"Принять отклонения по результатом замеров (По данным В.А. Белина)","Учет фактора отрицательных температур", "Учет фактора хранения", "Ввести своё отклонение"],'Принять отклонения по ТУ', id='oshib', style=  {'font-size':'1.2rem'})]),
        dcc.Dropdown(["12 C",'-14 C',"-22 C"],"12 C",id="temper",style={'text-align':'center', "font-size": "1.1rem"}, disabled=True),
        dcc.Dropdown(["0-0.5",'0.5-1'],"0-0.5",id="time",style={'text-align':'center', "font-size": "1.1rem"}, disabled=True),
        
        ],span=3),
        dmc.Col([
        html.Div([html.P("Выберите схему инициирования",style={"font-size": "1.5rem"}),]),
            html.Td(dcc.RadioItems(["Диагональная", "Поперечная"], "Диагональная", id = 'chemainit', style={'font-size':'1.2rem'}, inline=True)),
        html.Div([
            html.P("Внутрискважинное замедление:",style={"font-size": "1.2rem"}),
            dcc.Dropdown(['0','25',"50","75","100","125","150","175","200","225","250","300","350","400","450","500",'750','1000'],"300",id="insk",style={'text-align':'center', "font-size": "1.1rem"}),
            html.P("Стандартное (среднеквадратичное) отклонение для внутрискважинного замедления:",style={"font-size": "1.2rem"}),
            dcc.Input(id="st_insk",readOnly=True, type="number",style={'text-align':'center', "font-size": "1.1rem"}),
            
            html.P("Стандартное (среднеквадратичное) отклонение для поверхностного замедления (вруб):",style={"font-size": "1.2rem"}),
            dcc.Input(id="st_pov_vr",readOnly=True, type="number",style={'text-align':'center', "font-size": "1.1rem"}),
            
            html.P("Стандартное (среднеквадратичное) отклонение для поверхностного замедления (эшелон):",style={"font-size": "1.2rem"}),
            dcc.Input(id="st_pov_esh",readOnly=True, type="number",style={'text-align':'center', "font-size": "1.1rem"}),
            

        ])    
    ], span=3),
        dmc.Col([
            html.P("Число рядов скважин", style={'text-align':'center',"font-size": "1.2rem"}),
            dcc.Slider(1, 5,1, marks={i: f'{i}' for i in range(6)}, value=5, id='NR') ,
            html.P("Число скважин в ряду", style={'text-align':'center',"font-size": "1.2rem"}),
            dcc.Slider(1, 10,1, marks={i: f'{i}' for i in range(11)}, value=5, id='NW'),
            html.P("Расстояние между скважинами, a, м", style={'text-align':'center',"font-size": "1.2rem"}),
            dcc.Slider(0,15,0.1, marks={i: f'{i}' for i in range(16)}, value=5,id="PMC"),
            html.P("Расстояние между рядами, b, м", style={'text-align':'center',"font-size": "1.2rem"}),
            dcc.Slider(0,15,0.1, marks={i: f'{i}' for i in range(16)}, value=5, id="PMP"),
            html.Div([
    dmc.Grid([
        dmc.Col([
            html.P("a, м", style={'text-align':'center',"font-size": "1.2rem"}),
            dcc.Input(value=5,min=0,max=15,step=0.1,type="number",style={'text-align':'center', "font-size": "1.4rem"},id='PMCshow'),
        ],span=3),
        dmc.Col([],span=1), 
        dmc.Col([
            html.P("b, м", style={'text-align':'center',"font-size": "1.2rem"}),
            dcc.Input(value=5,min=0,max=15,step=0.1,type="number",style={'text-align':'center', "font-size": "1.4rem"},id='PMPshow'),  
        ],span=3)])
        ]),
    ], span=4)
    ]),
]),
    html.Div([dmc.Grid([
        dmc.Col([
            html.P("Поверхностный КД, время замедления, мс", style={'text-align':'center', "font-size": "1.2rem"}),
            html.Img(src=get_asset_url('17.png'), id='17ms'),
            html.Img(src=get_asset_url('25.png'),id='25ms'),
            html.Img(src=get_asset_url('42.png'),id='42ms'),
            html.Img(src=get_asset_url('67.png'),id='67ms'),
            html.Img(src=get_asset_url('109.png'),id='109ms'),
            html.Img(src=get_asset_url('176.png'),id='176ms'),
    ], span=5),
        dmc.Col([
            html.Div([dmc.Grid([
        dmc.Col([
            html.P("Вруб, мс",style={'text-align':'center', "font-size": "1.2rem"}),
            html.P(id="vrub",children='0',style={'text-align':'center', "font-size": 24,'background':'#D9FFAD','padding':'2px'}),
            dcc.Store(id="delayL", data=[0]*50),
            html.P("Показать подписи на графике", style={'text-align':'center',"font-size": "1.1rem"}),
            daq.BooleanSwitch(on=True,id='vakvis'),
        ],span=3),
        dmc.Col([
            html.P("Эшелон, мс",style={'text-align':'center', "font-size": "1.2rem"}),
            html.P(id="eshup",children='0',style={'text-align':'center', "font-size": '1rem'}), 
            html.P("Пользовательское замедление", style={'text-align':'center', "font-size": "1.1rem"}),
            html.Div([
            dcc.Input(id="zamedl", type="number", placeholder="Свое значение",style={'text-align':'center', "font-size": "1.1rem"}),
            html.Button(id="custom_ac", children='Принять',style ={'text-align':'center', "font-size": "1.1rem"}),
            ],style={'text-align':"center"}),    
    ],span=3),
        dmc.Col([
            html.P("Время изохрон, мс", style={'text-align':'center',"font-size": "1.2rem"}),
            dcc.Input(value=80,type='number',style={'text-align':'center', "font-size": "1.2rem"},id='izohron'),
            
            html.P("Учесть отклонения от номинала", style={'text-align':'center',"font-size": "1.1rem"}),
            daq.BooleanSwitch(on=True,id='deviation'),
    
    ],span=3),
    ])
    ]),
        html.Hr(),
        html.P(children='', id="M",style={'text-align':'center',"font-size": "1.3rem"}),
        html.P(children='', id="Mstr",style={'text-align':'center',"font-size": "1.3rem"}),
        html.P("Темп отбойки = ",id="temp", style={'text-align':'center',"font-size": "1.3rem"}),
        html.Hr(),
    ], span=6),]),
    ]),
        html.Div(children='GRAPH:', id="out"),
        html.Button(id="submit-button", children="Построить",style ={'width' : '100%', "font-size": "1.5rem",'background':'rgb(125,255,105)'}),
])


@app.callback(
    Output('17ms','n_clicks'),
    Output('25ms','n_clicks'),
    Output('42ms','n_clicks'),
    Output('67ms','n_clicks'),
    Output('109ms','n_clicks'),
    Output('176ms','n_clicks'),
    Output('custom_ac','n_clicks'),
    Output('vrub','n_clicks'),
    Output('eshup','n_clicks'),
    Output('stored','data'),
    Output('vrub','children'),
    Output('eshup','children'),
    Output('vrub','style'),
    Output('eshup','style'),
    Output("izohron", "value"),
    Output("st_insk", "value"),
    Output("st_pov_esh", "value"),
    Output("st_pov_vr", "value"),
    
    Output("st_insk", "readOnly"),
    Output("st_pov_esh", "readOnly"),
    Output("st_pov_vr", "readOnly"),
    
    Output('temper', 'disabled'),
    Output('time', 'disabled'),
    
    Input('vrub','children'),
    Input('eshup','children'),
    Input('zamedl','value'),
    Input('stored','data'),
    Input("NR", "value"),
    Input("NW", "value"),
    Input('17ms','n_clicks'),
    Input('25ms','n_clicks'),
    Input('42ms','n_clicks'),
    Input('67ms','n_clicks'),
    Input('109ms','n_clicks'),
    Input('176ms','n_clicks'),
    Input('custom_ac','n_clicks'),
    Input('vrub','n_clicks'),
    Input('eshup','n_clicks'),
    Input("deviation","on"),
    Input("oshib", 'value'),
    Input("insk", "value"),
    Input("st_insk", "value"),
    Input("st_pov_esh", "value"),
    Input("st_pov_vr", "value"),
    Input("temper", "value"),
    Input("time", "value"),
)
def wels_delay(vrub,eshup,custom,delayL,NR,NW,oran,yell,re,bly,gren,korich,user,vrubclk,eshupclk,deviation,typ,insk,st_insk,st_pov_vr,st_pov_esh,temper,time):
    try:
        delayL=[0]*50
        if vrubclk == None:
            vrubclk=0
        if eshupclk == None:
            eshupclk=0
        if oran==None:
            oran=0
        if yell==None:
            yell=0
        if re==None:
            re=0
        if bly==None:
            bly=0
        if gren==None:
            gren=0
        if korich==None:
            korich=0
        if user==None:
            user=0
        n=1
        style1={'text-align':'center', "font-size": 24,'background':'#D9FFAD','padding':'5px'}
        style2={'text-align':'center', "font-size": 24,'background':'#D9FFAD','padding':'5px'}
        if vrubclk >=n:
            style1["color"]="red"
        elif eshupclk >=n:
            style2["color"]="red"
        if oran>=n:
            delay=17
            oran=0
        elif yell>=n:
            delay=25
            yell=0
        elif re>=n:
            delay=42
            re=0
        elif bly>=n:
            delay=67
            bly=0
        elif gren>=n:
            delay=109
            gren=0
        elif korich>=n:
            delay=176
            korich=0
        elif user>=n:
            delay=custom
            user=0
        if vrubclk >=n:
            vrub=delay
            vrubclk=0
            style1["color"]="black"
        if eshupclk >=n:
            eshup=delay
            eshupclk=0
            style2["color"]="black"
        
        if deviation == False:
            st_skv = 0
            st_pv=0
            st_pe=0
            dsi=True
            hidd=True
            hidd1=True
            dsp_vr=True
            dsp_esh=True
            for i in range(NW*NR-NW):
                delayL[NW+i]=eshup   
            delayL[0]=0
            for i in range(NW-1):
                delayL[1+i]=vrub
            izohron=round(delayL[1],0)
        else:
            vr = vrub
            esh = eshup
            if typ == "Принять отклонения по ТУ":
                hidd=True
                hidd1=True
                devskv=['0','25',"50","75","100","125","150","175","200","225","250","300","350","400","450","500","750",'1000']
                stdevskv=[0,2,2.5,3.5,3.5,4,4.5,5.5,6,6,6.5,7.5,8.5,9.5,10.5,10.5,10.5,10.5]
                dictskv={}
                for i in range(len(devskv)):
                    dictskv[devskv[i]]=stdevskv[i]
                devsp=['0','17',"25","42","67","109","176"]
                stdevsp=[0,1.9,2.3,3,3.2,3.5,5.5]
                dictsp={}
                for i in range(len(devsp)):
                    dictsp[devsp[i]]=stdevsp[i]
                dsi=True
                dsp_vr=True
                dsp_esh=True
                st_insk= dictskv[str(insk)]
                st_pov_vr= dictsp[str(vr)]
                st_pov_esh= dictsp[str(esh)]

            elif typ == "Принять отклонения по результатом замеров (По данным В.А. Белина)":
                hidd=True
                hidd1=True
                dsi=True
                dsp_vr=True
                dsp_esh=True
                devskv=['0','25',"50","75","100","125","150","175","200","225","250","300","350","400","450","500", '750','1000']
                stdevskv=[0,3.4,4.8,7.2,9.6,12,14.4,16.8,19.2,21.6,24,28.8,33.6,38.5,12.9,35.6,60.9]
                dictskv={}
                for i in range(len(devskv)):
                    dictskv[devskv[i]]=stdevskv[i]/3
                devsp=['0','17',"25","42","67","109","176"]
                stdevsp=[0,math.sqrt(((22.6-26.5)**2+(22.6-18)**2)/2)/3,math.sqrt(((29.6-26)**2+(29.6-32.7)**2)/2)/3,math.sqrt(((51.4-45.6)**2+(51.4-56.3)**2)/2)/3,math.sqrt(((76.1-72.9)**2+(76.1-82.4)**2)/2)/3,math.sqrt(((119.7-113.6)**2+(119.7-126.9)**2)/2)/3,math.sqrt(((202.4-220)**2+(186.6-202.4)**2)/2)/3,]
                dictsp={}
                for i in range(len(devsp)):
                    dictsp[devsp[i]]=stdevsp[i]
                dsi=True
                dsp_vr=True
                dsp_esh=True
                st_insk= dictskv[str(insk)]
                st_pov_vr= dictsp[str(vr)]
                st_pov_esh= dictsp[str(esh)]
                meanlist=[22.6,29.6,51.4,76.1,119.7,202.4]
                meand={}
                for i in range(len(devsp)):
                    meand[devsp[i]]=meanlist
                vrub=meand[vrub]
                eshup=meand[eshup]
            elif typ == "Учет фактора отрицательных температур": 
                hidd1=True
                dsi=True
                dsp_vr=True
                dsp_esh=True
                hidd=False
                if temper == '12 C':
                    devskv=['0','25',"50","75","100","125","150","175","200","225","250","300","350","400","450","500","750","1000"]
                    stdevskv=[0,0.6,1.2,1.8,2.4,2.9,3.5,4.1,4.6,5.2,5.7,6.8,7.8,8.8,9.8,10,15.2,19]
                    dictskv={}
                    for i in range(len(devskv)):
                        dictskv[devskv[i]]=stdevskv[i]/3
                    devsp=['0','17',"25","42","67","109","176"]
                    stdevsp=[0,0.4,0.6,1,1.6,2.6,4.1]
                    dictsp={}
                    for i in range(len(devsp)):
                        dictsp[devsp[i]]=stdevsp[i]
                    st_insk= dictskv[str(insk)]
                    st_pov_vr= dictsp[str(vr)]
                    st_pov_esh= dictsp[str(esh)]
                if temper == '-14 C':
                    devskv=['0','25',"50","75","100","125","150","175","200","225","250","300","350","400","450","500","750","1000"]
                    stdevskv=[0,0.3,0.7,1.2,1.7,2.3,2.9,3.6,4.3,5.1,5.9,7.8,9.8,12.1,14.7,13,34.5,57.5]
                    dictskv={}
                    for i in range(len(devskv)):
                        dictskv[devskv[i]]=stdevskv[i]/3
                    devsp=['0','17',"25","42","67","109","176"]
                    stdevsp=[0,0.2,0.3,0.6,1,1.9,3.6]
                    dictsp={}
                    for i in range(len(devsp)):
                        dictsp[devsp[i]]=stdevsp[i]
                    st_insk= dictskv[str(insk)]
                    st_pov_vr= dictsp[str(vr)]
                    st_pov_esh= dictsp[str(esh)]
                if temper == '-22 C':
                    devskv=['0','25',"50","75","100","125","150","175","200","225","250","300","350","400","450","500","750","1000"]
                    stdevskv=[0,0.1,0.2,0.4,0.6,1,1.4,1.8,2.3,2.9,3.6,5.1,6.9,9,11.4,13,31.1,55]
                    dictskv={}
                    for i in range(len(devskv)):
                        dictskv[devskv[i]]=stdevskv[i]/3
                    devsp=['0','17',"25","42","67","109","176"]
                    stdevsp=[0,0,0.1,0.1,0.3,0.7,1.8]
                    dictsp={}
                    for i in range(len(devsp)):
                        dictsp[devsp[i]]=stdevsp[i]
                    st_insk= dictskv[str(insk)]
                    st_pov_vr= dictsp[str(vr)]
                    st_pov_esh= dictsp[str(esh)]
            elif typ == "Учет фактора хранения":
                hidd=True
                hidd1=False
                dsi=True
                dsp_vr=True
                dsp_esh=True
                if time == '0-0.5':
                    devskv=['0','25',"50","75","100","125","150","175","200","225","250","300","350","400","450","500","750","1000"]
                    stdevskv=[0,3.9,4.1,4.3,4.6,4.8,5,5.3,5.5,5.7,6,6.4,6.9,7.4,7.8,8.3,10.6,13]
                    dictskv={}
                    for i in range(len(devskv)):
                        dictskv[devskv[i]]=stdevskv[i]/3
                    devsp=['0','17',"25","42","67","109","176"]
                    stdevsp=[0,3.8,3.9,4,4.3,4.7,5.3]
                    dictsp={}
                    for i in range(len(devsp)):
                        dictsp[devsp[i]]=stdevsp[i]
                    st_insk= dictskv[str(insk)]
                    st_pov_vr= dictsp[str(vr)]
                    st_pov_esh= dictsp[str(esh)]
                elif time == '0.5-1':
                    devskv=['0','25',"50","75","100","125","150","175","200","225","250","300","350","400","450","500","750","1000"]
                    stdevskv=[10.4,10.6,10.9,11.2,11.5,11.7,12,12.3,12.6,12.8,13.4,13.9,14.5,15,15.6,18.3,21]
                    dictskv={}
                    for i in range(len(devskv)):
                        dictskv[devskv[i]]=stdevskv[i]/3
                    devsp=['0','17',"25","42","67","109","176"]
                    stdevsp=[0,10.3,10.4,10.6,10.8,11.3,12]
                    dictsp={}
                    for i in range(len(devsp)):
                        dictsp[devsp[i]]=stdevsp[i]
                    st_insk= dictskv[str(insk)]
                    st_pov_vr= dictsp[str(vr)]
                    st_pov_esh= dictsp[str(esh)]

            elif typ == "Ввести своё отклонение":
                hidd=True
                hidd1=True
                dsi=False
                dsp_vr=False
                dsp_esh=False
            st_skv=round(float(st_insk),1)
            skvaz= float(insk)
            st_pe=round(float(st_pov_esh),1)
            st_pv=round(float(st_pov_vr),1)
            for i in range(NW*NR-NW):
                delayL[NW+i]=round(round(random.gauss(eshup,st_pe),1))
            delayL[0]=0
            for i in range(NW-1):
                delayL[1+i]=round(round(random.gauss(vrub,st_pv),1))
            sumzamedl=[delayL[0]]
            zamedl=delayL
            wels=NW
            for i in range(NW-1):
                sumzamedl.append(int(sumzamedl[i])+int(zamedl[i+1]))
            for i in range(wels):
                sumzamedl.append(int(sumzamedl[i])+int(zamedl[wels+i]))
            for i in range(wels):
                sumzamedl.append(int(sumzamedl[wels+i])+int(zamedl[2*wels+i]))
            for i in range(wels):
                sumzamedl.append(int(sumzamedl[2*wels+i])+int(zamedl[3*wels+i]))
            for i in range(wels):
                sumzamedl.append(int(sumzamedl[3*wels+i])+int(zamedl[4*wels+i]))
            delayL=sumzamedl
            for i in range(NW*NR):
                delayL[i]=round(delayL[i]+round(random.gauss(skvaz,st_skv),1),0)
            #формат изохрон изменить
            izohron=round(delayL[1],0)
            #__________________________________________
    except Exception as e:
        print("Выбор замедления")
        izohron=80
        print(e)
        st_skv = 0
        st_pv=0
        st_pe=0
        dsi=True
        hidd=True
        hidd1=True
        dsp_vr=True
        dsp_esh=True
    return 0,0,0,0,0,0,0,vrubclk,eshupclk,delayL,vrub,eshup,style1,style2,izohron,st_skv,st_pv,st_pe,dsi,dsp_vr,dsp_esh,hidd,hidd1


@app.callback(
    Output('PMCshow','value'),
    Output('PMC','value'),
    Input("PMCshow", "value"),
    Input("PMC", "value"),
)
def equal(pmcs,pmc):
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = pmcs if trigger_id == "PMCshow" else pmc
    return value, value
@app.callback(
    Output('PMPshow','value'),
    Output('PMP','value'),
    Input("PMPshow", "value"),
    Input("PMP", "value"),
)
def equal1(pmps,pmp):
    trigger_id1 = ctx.triggered[0]["prop_id"].split(".")[0]
    value1 = pmps if trigger_id1 == "PMPshow" else pmp
    return value1,value1
@app.callback(
    Output('M','children'),
    Output('Mstr','children'),
    Output('out','children'),
    Output('temp','children'),

    Input('submit-button', 'n_clicks'),
    Input("chemabur", "value"),
    Input("chemainit", "value"),
    Input("NR", "value"),
    Input("NW", "value"),
    Input("PMC", "value"),
    Input("PMP", "value"),
    Input('stored','data'),
    Input("izohron", "value"),
    Input('vakvis','on'),
    Input("deviation","on"),
    Input("eshup","children"),
    Input("vrub","children"),

)
def tableANDgraph_show(n,bur,init,rows,wels,a,b,zamedl,izohron,vis,dev,esh,vr):
    try:
        if n is None:
            return no_update
        else:
# https://plotly.com/python/marker-style/     
            cpicok=[0,0]
            temp=''
            x_d=[]
            y_d=[]
            sumzamedl=[]
            fig = go.Figure()
            fig.update_layout(template="simple_white")
            x=[]
            y=[]
            if vr == 17:
                vrubcolor='orange'
            elif vr == 25:
                vrubcolor='yellow'
            elif vr == 42:
                vrubcolor='rgb(245,74,10)'
            elif vr == 67:
                vrubcolor='blue'
            elif vr == 109:
                vrubcolor='green'
            elif vr == 176:
                vrubcolor='brown'
            else:
                vrubcolor='black'
            if esh == 17:
                eshcolor='orange'
            elif esh == 25:
                eshcolor='yellow'
            elif esh == 42:
                eshcolor='rgb(245,74,10)'
            elif esh == 67:
                eshcolor='blue'
            elif esh == 109:
                eshcolor='green'
            elif esh == 176:
                eshcolor='brown'
            else:
                eshcolor='black'
            linevrubset={"color":vrubcolor,'width':5}
            lineeshset={"color":eshcolor,'width':5}
            markersett=dict(size=22,symbol="triangle-up",angleref="previous",standoff=30,)
            # fig.update_yaxes(visible=False, showticklabels=False)
            # fig.update_xaxes(visible=False, showticklabels=False)

            if bur == 'Прямоугольная':
                Y=[0]*(wels)
                X=[]
                num_del = {}
                cpicok =[]
                sumzamedl = [0]
                delayforsr1=izohron
                delayforsr2=2*delayforsr1
                for i in range(rows):
                    for k in range(wels):
                            y.append(round(b*i,1))
                    for m in range(wels):
                            step=a*m
                            x.append(round(step,1))
                for start in range(wels):
                        X.append(start*a)
                fig.add_trace(go.Scatter(x=X,y=Y,mode='lines+markers',marker=markersett,connectgaps=False,line=linevrubset,showlegend=False))
                fig.add_trace(go.Scatter(x=X,y=Y,mode='lines',connectgaps=False,line=linevrubset,name = str(vr)+' мс. <br>'+'Взрывная сеть(вруб)'))
                for i in range(wels):
                        for k in range(rows):
                            X.append(i*a)
                        X.append(None)
                for i in range(wels):
                        for i in range(rows):
                            Y.append(b*i)
                        Y.append(None)
                fig.add_trace(go.Scatter(x=X[wels:],y=Y[wels:],mode='lines+markers',marker=markersett,connectgaps=False,line=lineeshset,showlegend=False))
                fig.add_trace(go.Scatter(x=X[wels:],y=Y[wels:],mode='lines',connectgaps=False,line=lineeshset,name =str(esh)+' мс. <br>'+ 'Взрывная сеть (эшелон)'))
                if vr <= esh:
                    koef1 = 1
                else:
                    koef1=0
                try:
                        for i in range(wels-1):
                            sumzamedl.append(int(sumzamedl[i])+int(zamedl[i+1]))
                        for i in range(wels):
                            sumzamedl.append(int(sumzamedl[i])+int(zamedl[wels+i]))
                        for i in range(wels):
                            sumzamedl.append(int(sumzamedl[wels+i])+int(zamedl[2*wels+i]))
                        for i in range(wels):
                            sumzamedl.append(int(sumzamedl[2*wels+i])+int(zamedl[3*wels+i]))
                        for i in range(wels):
                            sumzamedl.append(int(sumzamedl[3*wels+i])+int(zamedl[4*wels+i]))
                        for i in range(len(x)):
                            num_del[i]=sumzamedl[i]
                        if dev == False:
                            n=len(num_del)
                            keys=list(num_del.keys())
                            for i in range(n-1):
                                for j in range(i+1,n):
                                    ki=keys[i]
                                    kj=keys[j]
                                    if num_del[ki]==num_del[kj]:
                                        y_d.append(y[ki])
                                        y_d.append(y[kj])
                                        x_d.append(x[ki])
                                        x_d.append(x[kj])
                                        x_d.append(None)
                                        y_d.append(None)
                                        cpicok.append(num_del[ki])
                        else:
                            cpicok=[]
                except Exception as e:
                        print(e)
                        print(100000)
                        temp=''
                if init == 'Диагональная' or init == 'Поперечная':
                    if dev == False:
                        try:
                                if cpicok == []:

                                    for i in range(wels):
                                        cpicok.append(delayforsr1*i)
                                    for i in range(wels):
                                        if num_del[i]<=delayforsr1:
                                            Nmax=i
                                    for k in range(rows):
                                        if num_del[k*wels]<=delayforsr1:
                                            Nmax_w=k
                                    for i in range(wels):
                                        if num_del[i]<=delayforsr2:
                                            Nmax1=i
                                    dsY=(b)/zamedl[wels]
                                    dsYX=(-a)/zamedl[wels*(Nmax_w+koef1)]
                                    deltaY= round(abs(sumzamedl[(Nmax_w)*wels]-delayforsr1)*dsY,3)
                                    deltaYX= round(abs(sumzamedl[(Nmax_w)*wels]-delayforsr1)*dsYX,3)
                                    deltaX= round(abs(sumzamedl[Nmax]-delayforsr1)*(a)/zamedl[Nmax],1)
                                    deltaX1=round(abs(sumzamedl[Nmax1]-delayforsr2)*(a)/zamedl[Nmax1],1)
                                    x_d.append(x[Nmax]+deltaX)
                                    y_d.append(y[Nmax])

                                    x_d.append(x[wels*Nmax_w])
                                    y_d.append(y[wels*Nmax_w]+deltaY)
                                    xb=x_d[-2]
                                    yb=y_d[-2]
                                    xa=x_d[-1]
                                    ya=y_d[-1]
                                    i=0
                                    yyy=0
                                    XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa
                                    while yyy <=y[wels*rows-1] and XXX >= 0:
                                        yyy=i*b/30
                                        XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa
                                        i=i+0.1
                                        if XXX < 0:
                                            break
                                    x_d.pop()
                                    y_d.pop()
                                    x_d.append(XXX)
                                    y_d.append(yyy)
                                    x_d.append(None)
                                    y_d.append(None)
                                    fig.add_annotation(x=(x_d[-3]), y=-b/5, text=str(delayforsr1)+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                                    fig.add_annotation(x=(x_d[-2]), y=yyy+b/7, text=str(delayforsr1)+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                
                                    x_d.append(x[Nmax1]+deltaX1)
                                    y_d.append(0)
                                    sted=x_d[-1]-x_d[0]
                                    x_d.append(x_d[-3]+sted)
                                    y_d.append(y_d[-3])
                                    xb=x_d[-2]
                                    yb=y_d[-2]
                                    xa=x_d[-1]
                                    ya=y_d[-1]
                                    yyy=0
                                    XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa
                                    i=0
                                    while yyy<=y[wels*rows-1] and XXX >= 0:
                                        yyy=i*b/10
                                        XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa
                                        i=i+0.1
                                    x_d.pop()
                                    y_d.pop()
                                    x_d.append(XXX)
                                    y_d.append(yyy)
                                    x_d.append(None)
                                    y_d.append(None)
                                    fig.add_annotation(x=(x_d[-3]), y=-b/5, text=str(delayforsr1*2)+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                                    fig.add_annotation(x=(x_d[-2]), y=yyy+b/5, text=str(delayforsr1*2)+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                                    k=0
                                    for i in range(wels):
                                        if delayforsr1*(i+2) < sumzamedl[wels-1]:
                                            XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa+sted*(i+1)
        
                                            while  yyy <=y[wels*rows-1] and XXX >= 0:
                                                yyy=k*b/5
                                                XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa+sted*(i+1)
                                                k=k+0.1
        
                                            x_d.append(x_d[-3]+sted)
                                            y_d.append(0)
                                            x_d.append(XXX)
                                            y_d.append(yyy)
                                            x_d.append(None)
                                            y_d.append(None)
                                            fig.add_annotation(x=(x_d[-3]), y=-b/5, text=str(delayforsr1*(i+3))+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                                            fig.add_annotation(x=(x_d[-2]), y=yyy+b/5, text=str(delayforsr1*(i+3))+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                        except Exception as e:
                            temp=''
                    #_______________________________________________________________________________________________________________________________________list index out of range???____________________________________________
                    else:
                        try:
                            temp1=[]
                            sumzamedl=zamedl
                            print(zamedl)
                            # sumzamedl[0]=zamedl[0]
                            # #сумму в функцию выбора замедления?
                            # for i in range(wels-1):
                            #     sumzamedl.append(int(sumzamedl[i])+int(zamedl[i+1]))
                            # for i in range(wels):
                            #     sumzamedl.append(int(sumzamedl[i])+int(zamedl[wels+i]))
                            # for i in range(wels):
                            #     sumzamedl.append(int(sumzamedl[wels+i])+int(zamedl[2*wels+i]))
                            # for i in range(wels):
                            #     sumzamedl.append(int(sumzamedl[2*wels+i])+int(zamedl[3*wels+i]))
                            # for i in range(wels):
                            #     sumzamedl.append(int(sumzamedl[3*wels+i])+int(zamedl[4*wels+i]))
                            for i in range(len(x)):
                                num_del[i]=sumzamedl[i]
                            for i in range(wels):
                                cpicok.append(izohron*i)
                                
                                

                            s = sumzamedl
                            
                            #для темпа 
                            qx=[]
                            qy=[]
#11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                            step=abs(zamedl[2]-zamedl[1])
                            for i in range(wels):
                                for m in range(wels):
                                    
                                    if s[m] < izohron+step*(i) and s[m+1] >= izohron+step*(i):
                                        dX=a/(sumzamedl[m+1]-sumzamedl[m])
                                        x_d.append(x[m]+dX*abs(s[m]-(izohron+step*(i))))
                                        y_d.append(0)
                                        fig.add_annotation(x=(x_d[-1]), y=-b/5, text=str(izohron+step*(i))+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                                        qx.append(x_d[0])
                                        qy.append(y_d[0])
                                        if s[wels+m] >= izohron+step*(i):
                                            dY=b/(sumzamedl[wels+m]-sumzamedl[0+m])
                                            x_d.append(x[m])
                                            y_d.append(y[wels+m]-abs(dY)*abs(s[wels+m]-(izohron+step*(i))))
                                            qx.append(x_d[1])
                                            qy.append(y_d[1])

                                            x_d.append(None)                                    
                                            y_d.append(None)                                    
                                        else:
                                            dX=a/(sumzamedl[wels+m]-sumzamedl[wels+1+m])
                                            x_d.append(x[wels+m]+abs(dX)*abs(izohron+step*(i)-s[wels+m]))
                                            y_d.append(y[wels])
                                            qx.append(x_d[1])
                                            qy.append(y_d[1])
#прописать логику вручную
                                            if s[2*wels+m] >= izohron+step*(i):
                                                dY=b/(sumzamedl[2*wels+m]-sumzamedl[wels+m])
                                                x_d.append(x[m])
                                                y_d.append(y[wels]+abs(dY)*abs(s[wels+m]-(izohron+step*(i))))
                                   
                                            else:
                                                dX=a/(sumzamedl[2*wels+m]-sumzamedl[2*wels+1+m])
                                                x_d.append(x[2*wels+m]+abs(dX)*abs(izohron+step*(i)-s[2*wels+m]))
                                                y_d.append(y[2*wels])
                                            if s[3*wels+m] >= izohron+step*(i):
                                                    dY=b/(s[3*wels+m]-s[2*wels+m])
                                                    x_d.append(x[m])
                                                    y_d.append(y[wels*2]+abs(dY)*abs(s[2*wels+m]-(izohron+step*(i))))    
                                                    x_d.append(None)      
                                                    y_d.append(None)                                    

                                            else:
                                                    dX=a/(s[3*wels+m]-s[3*wels+m+1])
                                                    x_d.append(x[m]+abs(dX)*abs(s[3*wels+m]-(izohron+step*(i))))
                                                    y_d.append(y[3*wels])
                                                    x_d.append(None)      
                                                    y_d.append(None)                                    

                                                
                                                

                            
                            
                            
                            
                            
                            
                            
                            
                            
                    
      
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
#__________________________________________перебор точек  одим временем и отметка их в списке___________________________________
#диапазон для темпа отбойки 
                        except Exception as e:
                                temp=''
                                print(e)
                                print(120000)
             
            if bur == 'Шахматная':
                if init == 'Диагональная':
                    for i in range(rows):
                            for k in range(wels):
                                y.append(round(b*i,1))
                            for m in range(wels):
                                step=a*m-a/2*i
                                x.append(round(step,1))
                    Y=[0]*(wels)
                    X=[]
                    for start in range(wels):
                            X.append(start*a)
                    fig.add_trace(go.Scatter(x=X,y=Y,mode='lines+markers',marker=markersett,showlegend=False,connectgaps=False,line=linevrubset))
                    fig.add_trace(go.Scatter(x=X,y=Y,mode='lines',connectgaps=False,line=linevrubset,name = str(zamedl[1])+' мс. <br>'+'Взрывная сеть(вруб)'))

                    for i in range(wels):
                            for k in range(rows):
                                X.append(-a/2*(k)+i*a)
                            X.append(None)
                    for i in range(wels):
                            for i in range(rows):
                                Y.append(b*i)
                            Y.append(None)
                    fig.add_trace(go.Scatter(x=X[wels:],y=Y[wels:],mode='lines+markers',marker=markersett,showlegend=False,connectgaps=False,line=lineeshset))
                    fig.add_trace(go.Scatter(x=X[wels:],y=Y[wels:],mode='lines',connectgaps=False,line=lineeshset,name = str(zamedl[wels])+' мс. <br>'+'Взрывная сеть (эшелон)'))
                    
                    delayforsr1=izohron
                    delayforsr2=2*delayforsr1
                    if zamedl[1] < zamedl[wels]:
                        koef1 = 1
                    else:
                        koef1=0
                    sumzamedl = [0]
                    cpicok =[]
                    num_del = {}

                    try:
                            for i in range(wels-1):
                                sumzamedl.append(int(sumzamedl[i])+int(zamedl[i+1]))
                            for i in range(wels):
                                sumzamedl.append(int(sumzamedl[i])+int(zamedl[wels+i]))
                            for i in range(wels):
                                sumzamedl.append(int(sumzamedl[wels+i])+int(zamedl[2*wels+i]))
                            for i in range(wels):
                                sumzamedl.append(int(sumzamedl[2*wels+i])+int(zamedl[3*wels+i]))
                            for i in range(wels):
                                sumzamedl.append(int(sumzamedl[3*wels+i])+int(zamedl[4*wels+i]))
                            for i in range(len(x)):
                                num_del[i]=sumzamedl[i]
                            n=len(num_del)
                            keys=list(num_del.keys())
                            for i in range(n-1):
                                for j in range(i+1,n):
                                    ki=keys[i]
                                    kj=keys[j]
                                    if num_del[ki]==num_del[kj]:
                                        y_d.append(y[ki])
                                        y_d.append(y[kj])

                                        x_d.append(x[ki])
                                        x_d.append(x[kj])

                                        x_d.append(None)
                                        y_d.append(None)
                                        cpicok.append(num_del[ki])

                    except Exception as e:
                            temp=''
                    try:
                        if cpicok == []:
                            for i in range(wels):
                                cpicok.append(delayforsr1*i)
                            for i in range(wels):
                                if num_del[i]<=delayforsr1:
                                    Nmax=i
                            for k in range(rows):
                                if num_del[k*wels]<=delayforsr1:
                                    Nmax_w=k
                            for i in range(wels):
                                if num_del[i]<=delayforsr2:
                                    Nmax1=i
                            dsY=(b)/zamedl[wels]
                            dsYX=(-a/2)/zamedl[wels*(Nmax_w+koef1)]
                            deltaY= round(abs(sumzamedl[(Nmax_w)*wels]-delayforsr1)*dsY,3)
                            deltaYX= round(abs(sumzamedl[(Nmax_w)*wels]-delayforsr1)*dsYX,3)
                            deltaX= round(abs(sumzamedl[Nmax]-delayforsr1)*(a)/zamedl[Nmax],1)
                            deltaX1=round(abs(sumzamedl[Nmax1]-delayforsr2)*(a)/zamedl[Nmax1],1)
                            x_d.append(x[Nmax]+deltaX)
                            y_d.append(y[Nmax])
                            x_d.append(x[wels*Nmax_w]+deltaYX)
                            y_d.append(y[wels*Nmax_w]+deltaY)
                            xb=x_d[-2]
                            yb=y_d[-2]
                            xa=x_d[-1]
                            ya=y_d[-1]
                            yyy=0 
                            i=0
                            XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa
                            while yyy <=y[wels*rows-1] and XXX >=  x[wels*(rows-1)]:
                                yyy=i*b/7
                                XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa
                                i=i+0.1
                            x_d.pop()
                            y_d.pop()
                            x_d.append(XXX)
                            y_d.append(yyy)
                            x_d.append(None)
                            y_d.append(None)
                            fig.add_annotation(x=(x_d[-3]), y=-b/5, text=str(delayforsr1)+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                            fig.add_annotation(x=(x_d[-2]), y=yyy+b/7, text=str(delayforsr1)+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                            x_d.append(x[Nmax1]+deltaX1)
                            y_d.append(0)
                            sted=x_d[-1]-x_d[0]
                            x_d.append(x_d[-3]+sted)
                            y_d.append(y_d[-3])
                            xb=x_d[-2]
                            yb=y_d[-2]
                            xa=x_d[-1]
                            ya=y_d[-1]
                            yyy=0
                            XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa
                            i=0
                            while yyy<=y[wels*rows-1] and XXX >= x[wels*(rows-1)]:
                                yyy=i*b/5
                                XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa
                                i=i+0.1
                            x_d.pop()
                            y_d.pop()
                            x_d.append(XXX)
                            y_d.append(yyy)
                            x_d.append(None)
                            y_d.append(None)
                            fig.add_annotation(x=(x_d[-3]), y=-b/5, text=str(delayforsr1*2)+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                            fig.add_annotation(x=(x_d[-2]), y=yyy+b/7, text=str(delayforsr1*2)+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                            k=0
                            for i in range(wels):
                                if delayforsr1*(i+2) < sumzamedl[wels-1]:
                                    XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa+sted*(i+1)
                                    
                                    while  yyy <=y[wels*rows-1] and XXX >= x[wels*(rows-1)]:
                                        yyy=k*b/5
                                        XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa+sted*(i+1)

                                        k=k+0.1
                                    x_d.append(x_d[-3]+sted)
                                    y_d.append(0)
                                    x_d.append(XXX)
                                    y_d.append(yyy)
                                    x_d.append(None)
                                    y_d.append(None)
                                    fig.add_annotation(x=(x_d[-3]), y=-b/5, text=str(delayforsr1*(i+3))+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                                    fig.add_annotation(x=(x_d[-2]), y=yyy+b/7, text=str(delayforsr1*(i+3))+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)

                    except Exception as e:
                        temp=''
                elif init =="Поперечная":
                    for i in range(rows):
                        for k in range(wels):
                            y.append(b*i)
                        for m in range(wels):
                            step=a*m+a/2*i
                            x.append(step)
                    Y=[0]*(wels)
                    X=[]
                    for start in range(wels):
                        X.append(start*a)
                    fig.add_trace(go.Scatter(x=X,y=Y,mode='lines+markers',marker=markersett,showlegend=False,connectgaps=False,line=linevrubset))
                    fig.add_trace(go.Scatter(x=X,y=Y,mode='lines',connectgaps=False,line=linevrubset,name =str(zamedl[1])+' мс. <br>'+ 'Взрывная сеть(вруб)'))

                    for i in range(wels):
                        for k in range(rows):
                            X.append(a/2*(k)+(i)*a)
                        X.append(None)
                    for i in range(wels):
                        for i in range(rows):
                            Y.append(b*i)
                        Y.append(None)
                    fig.add_trace(go.Scatter(x=X[wels:],y=Y[wels:],mode='lines+markers',marker=markersett,connectgaps=False,line=lineeshset,showlegend=False))
                    fig.add_trace(go.Scatter(x=X[wels:],y=Y[wels:],mode='lines',connectgaps=False,line=lineeshset,name =str(zamedl[wels])+' мс. <br>'+  'Взрывная сеть (эшелон)'))

                    delayforsr1=izohron
                    delayforsr2=2*delayforsr1
                    if zamedl[1] < zamedl[wels]:
                        koef1 = 1
                    else:
                        koef1=0
                    sumzamedl = [0]
                    cpicok =[]
                    num_del = {}
                    try:
                        y_d=[]
                        x_d=[]
                        for i in range(wels-1):
                            sumzamedl.append(int(sumzamedl[i])+int(zamedl[i+1]))
                        for i in range(wels):
                            sumzamedl.append(int(sumzamedl[i])+int(zamedl[wels+i]))
                        for i in range(wels):
                            sumzamedl.append(int(sumzamedl[wels+i])+int(zamedl[2*wels+i]))
                        for i in range(wels):
                            sumzamedl.append(int(sumzamedl[2*wels+i])+int(zamedl[3*wels+i]))
                        for i in range(wels):
                            sumzamedl.append(int(sumzamedl[3*wels+i])+int(zamedl[4*wels+i]))
                        for i in range(len(x)):
                            num_del[i]=sumzamedl[i]
                        n=len(num_del)
                        keys=list(num_del.keys())
                        for i in range(n-1):
                            for j in range(i+1,n):
                                ki=keys[i]
                                kj=keys[j]
                                if num_del[ki]==num_del[kj]:
                                    y_d.append(y[ki])
                                    y_d.append(y[kj])
                                    x_d.append(x[ki])
                                    x_d.append(x[kj])
                                    x_d.append(None)
                                    y_d.append(None)
                                    cpicok.append(num_del[ki])


                        if cpicok == []:

                            for i in range(wels):
                                cpicok.append(delayforsr1*i)
                            for i in range(wels):
                                if num_del[i]<=delayforsr1:
                                    Nmax=i
                            for k in range(rows):
                                if num_del[k*wels]<=delayforsr1:
                                    Nmax_w=k
                            for i in range(wels):
                                if num_del[i]<=delayforsr2:
                                    Nmax1=i
                            dsY=(b)/zamedl[wels]
                            dsYX=(-a/2)/zamedl[wels*(Nmax_w+koef1)]
                            deltaY= round(abs(sumzamedl[(Nmax_w)*wels]-delayforsr1)*dsY,3)
                            deltaYX= round(abs(sumzamedl[(Nmax_w)*wels]-delayforsr1)*dsYX,3)
                            deltaX= round(abs(sumzamedl[Nmax]-delayforsr1)*(a)/zamedl[Nmax],3)
                            deltaX1=round(abs(sumzamedl[Nmax1]-delayforsr2)*(a)/zamedl[Nmax1],3)
                            x_d.append(x[Nmax]+deltaX)
                            y_d.append(y[Nmax])
                            x_d.append(x[wels*Nmax_w]-deltaYX)
                            y_d.append(y[wels*Nmax_w]+deltaY)
                            xb=x_d[-2]
                            yb=y_d[-2]
                            xa=x_d[-1]
                            ya=y_d[-1]
                            yyy=0 
                            i=0
                            XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa
                            while yyy <=y[wels*rows-1] and XXX >= 0:
                                yyy=i*b/7
                                XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa
                                i=i+0.1
                            x_d.pop()
                            y_d.pop()
                            x_d.append(XXX)
                            y_d.append(yyy)

                            x_d.append(None)
                            y_d.append(None)
                            fig.add_annotation(x=(x_d[-3]), y=-b/5, text=str(delayforsr1)+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                            fig.add_annotation(x=(x_d[-2]), y=yyy+b/7, text=str(delayforsr1)+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                            x_d.append(x[Nmax1]+deltaX1)
                            y_d.append(0)
                            sted=x_d[-1]-x_d[0]
                            x_d.append(x_d[-3]+sted)
                            y_d.append(y_d[-3])
                            xb=x_d[-2]
                            yb=y_d[-2]
                            xa=x_d[-1]
                            ya=y_d[-1]
                            yyy=0 
                            XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa
                            i=0
                            while yyy<=y[wels*rows-1] and XXX >= 0:
                                yyy=i*b/5
                                XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa
                                i=i+0.1
                            x_d.pop()
                            y_d.pop()
                            x_d.append(XXX)
                            y_d.append(yyy)
                            x_d.append(None)
                            y_d.append(None)
                            fig.add_annotation(x=(x_d[-3]), y=-b/5, text=str(delayforsr1*2)+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                            fig.add_annotation(x=(x_d[-2]), y=yyy+b/7, text=str(delayforsr1*2)+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                            k=0
                            for i in range(wels):
                                if delayforsr1*(i+2) < sumzamedl[wels-1]:
                                    XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa+sted*(i+1)
                                    
                                    while  yyy <=y[wels*rows-1] and XXX >= 0:
                                        yyy=k*b/5
                                        XXX=((yyy-ya)*(xb-xa))/(yb-ya)+xa+sted*(i+1)
                                        k=k+0.1
                                    x_d.append(x_d[-3]+sted)
                                    y_d.append(0)
                                    x_d.append(XXX)
                                    y_d.append(yyy)
                                    x_d.append(None)
                                    y_d.append(None)
                                    fig.add_annotation(x=(x_d[-3]), y=-b/5, text=str(delayforsr1*(i+3))+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                                    fig.add_annotation(x=(x_d[-2]), y=yyy+b/7, text=str(delayforsr1*(i+3))+" мс",showarrow=False, font=dict(size=20,color="Red"),visible=vis)
                    except Exception as e:
                        temp=''
            try:
                    dif=cpicok[-1]-cpicok[-2]
                    temp=''
                    # a_shtrih = math.sqrt(y_d[1]*y_d[1]+(abs(x_d[1])+x_d[0])*(abs(x_d[1])+x_d[0]))
                    # treygX =math.sqrt((x_d[4]-x_d[1])*(x_d[4]-x_d[1])+ (y_d[4]-y_d[1])*(y_d[4]-y_d[1]))
                    # treygY=math.sqrt((x_d[0]-x_d[4])*(x_d[0]-x_d[4])+ (y_d[4]-y_d[0])*(y_d[4]-y_d[0]))
                    # polop=(a_shtrih+treygX+treygY)/2
                    # b_shtrih = (2*math.sqrt(polop*(polop-treygX)*(polop-treygY)*(polop-a_shtrih)))/a_shtrih

                    a_shtrih = math.sqrt((y[wels]*y[wels])+((x[1])-x[wels])*((x[1])-x[wels]))
                    treygX =math.sqrt((x[wels+1]-x[wels])*(x[wels+1]-x[wels]))
                    treygY=math.sqrt((x[wels+1]-x[1])**2+(y[wels+1]-y[1])*(y[wels+1]-y[1]))
                    polop=(a_shtrih+treygX+treygY)/2
                    b_shtrih = (2*math.sqrt(polop*(polop-treygX)*(polop-treygY)*(polop-a_shtrih)))/a_shtrih
                    
                    # fig.add_annotation(x=x_d[3], y=(y_d[1]+y_d[0])/2-b/4+b/3, text="a'(РМС') = " + str(round(a_shtrih,1)),showarrow=False, font=dict(size=20,color="Red"), bgcolor="White", borderwidth=2, borderpad=4,visible=vis)
                    # fig.add_annotation(x=x_d[3], y=(y_d[1]+y_d[0])/2+b/3, text="b'(ЛНС') = " + str(round(b_shtrih,1)),showarrow=False, font=dict(size=20,color="Red"), bgcolor="White", borderwidth=2, borderpad=4,visible=vis)
                    fig.add_annotation(
            text="b'(ЛНС') = " + str(round(b_shtrih,1))+' м'+"<br>"+"a'(РМС') = " + str(round(a_shtrih,1))+' м',
            align="left",
            showarrow=False,
            xref="paper",
            yref="paper",
            font=dict(color="black", size=18),
            bgcolor="Gold",
            y=0.4,
            x=1.03,
            xanchor="left",
                    )
                    storona1 = (x_d[1])-(x_d[0])
                    storona2 = y_d[1]
                    degree=math.atan(storona2/storona1)
                    temp=dif/b_shtrih
                    temp='Темп отбойки = ' + str(round(temp,1)) + " мс/м." +' Угол наклона изохрон = ' + str(round(abs(degree)*180/math.pi,1)) + '  градусов' 
            except Exception as e:
                    print(e)
            if vis == False:
                vis = 'legendonly'
            else:
                vis =True
                       
            #стрелка 
            # # # # sdvig=a/10+b/10
            
            # # # # arroX=[(x_d[1]-x_d[0])/4]
            # # # # arroY=[(y_d[1])/4]

            # # # # arroX.append((x_d[1]-x_d[0])/4+math.cos(degree)*(sdvig))
            # # # # arroY.append((y_d[1])/4+math.sin(degree)*(sdvig))


            # # # # arroX.append((arroX[1]-math.cos(math.pi/2+degree)*(sdvig)+arroX[0]-math.cos(math.pi/2+degree)*(sdvig))/2)
            # # # # arroY.append((arroY[1]-math.sin(math.pi/2+degree)*(sdvig)+arroY[0]-math.sin(math.pi/2+degree)*(sdvig))/2)

            # # # # arroX.append((x_d[1]-x_d[0])/4)
            # # # # arroY.append((y_d[1])/4)


            # # # # arroX.append((x_d[1]-x_d[0])/4+math.cos(degree)*(sdvig/4))
            # # # # arroY.append((y_d[1])/4+math.sin(degree)*(sdvig/4))

            # # # # arroX.append(arroX[-1]+math.cos(math.pi/2+degree)*(sdvig))
            # # # # arroY.append(arroY[-1]+math.sin(math.pi/2+degree)*(sdvig))

            # # # # arroX.append(arroX[-1]+math.cos(degree)*(sdvig/2))
            # # # # arroY.append(arroY[-1]+math.sin(degree)*(sdvig/2))

            # # # # arroX.append((x_d[1]-x_d[0])/4+math.cos(degree)*(3*sdvig/4))
            # # # # arroY.append((y_d[1])/4+math.sin(degree)*(3*sdvig/4))



            # # # # # arroX.append(None)
            # arroY.append(None)

            # arroX.append(arroX[1]-math.cos(math.pi/2+degree)*(a/10+b/10))
            # arroY.append(arroY[1]-math.sin(math.pi/2+degree)*(a/10+b/10))

            # arroX.append(arroX[0]-math.cos(math.pi/2+degree)*(a/10+b/10))
            # arroY.append(arroY[0]-math.sin(math.pi/2+degree)*(a/10+b/10))
            


#            fig.add_trace(go.Scatter(x=arroX,y=arroY, fill='toself', showlegend=False,line=dict(color="Gold",width=8),fillcolor="White"))


            fig.add_trace(go.Scatter(x=x_d,y=y_d,mode='lines',name = 'сеть изохрон',connectgaps=False,line=dict(color="red"), visible=vis))
        #     #zamedl[0]='  0<br>_____<br>  300  '
            fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode = "markers",
            marker_line_width=2,
            marker = dict(size=10,color='rgb(255,255,255)'),
            name = '<b>Скважины</b>', # Style name/legend entry with html tags
            connectgaps=True, # override default to connect the gaps
            #text=zamedl[:(len(x))],
            #textposition="top right", textfont_size=20,
            
        ))
#____________________________________________________________________________________________________________
  #учесть внутрискважинное замедление, возможно отдельными точками+текст, построить ломаные линии    
            fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode = "text+markers",
            name = '<b>Суммарное замедление</b>', # Style name/legend entry with html tags
            connectgaps=True, # override default to connect the gaps
            text=sumzamedl,
            
            textposition="top right", textfont_size=25,textfont_color="rgb(148,0,211)", visible=vis,
        ))
            
#_______________________________________________________________________________________________________________________
            fig.update_layout(height=800,
                    ),
        # fig.add_annotation(x=x[1], y=-b/4, text="a(PMC) = " + str(a),showarrow=False, font=dict(size=20,color="Black"), bgcolor="White", borderwidth=2, borderpad=4)
        # fig.add_annotation(x=x[1], y=b/3, text="b(ЛНС) = " + str(b),showarrow=False, font=dict(size=20,color="Black"), bgcolor="White", borderwidth=2, borderpad=4)

        fig.add_annotation(
            text="b(ЛНС) = " + str(b)+' м' +"<br>"+"a(PMC) = " + str(a) + ' м',
            align="left",
            showarrow=False,
            xref="paper",
            yref="paper",
            font=dict(color="black", size=18),
            bgcolor="Gold",
            y=0.5,
            x=1.03,
            xanchor="left",
        )
        fig.update_layout(legend={
            "xref": "container",
            "yref": "container",
            "y": 0.65,
            "bgcolor": "Gold",})
        fig.update_layout(font_size=18)
        
        m=a/b
        if m<1 or m>1.8:
            ahtung = ' Вне диапазона 1-1,8'
        else:
            ahtung=''
        dinM= 'Динамический коэффициент сближения m\' = ' + str(round(a_shtrih/b_shtrih,2))

    except Exception as e:
        print("wtf")
        return no_update
    return 'Коэффициент сближения сетки бурения m = '+str(round(m,2))+ahtung,dinM,dcc.Graph(figure=fig),temp
if __name__ == "__main__":
    app.run(debug=True,port=8000)