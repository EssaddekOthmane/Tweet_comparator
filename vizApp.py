import numpy as np
import pandas as pd
from datetime import datetime
import altair as alt
import streamlit as st

def lasq_date(x):
    
    y=x[:10]
    d=x[11:len(x)-5]
    dd=y+' '+d
    return(datetime.strptime(dd, '%Y-%m-%d %H:%M:%S'))
        

def lasq_heure(x):
    
    
    d=x[11:len(x)-5]

    return(datetime.strptime(d, '%H:%M:%S'))
        


macron=pd.read_csv('DF_mac.csv')
zemour=pd.read_csv('DF_zem.csv')
mel=pd.read_csv('Df_mell.csv')

macron['daate'] = macron['Timestamp'].apply( lambda x : lasq_date(x) )
macron['heuure'] = macron['Timestamp'].apply( lambda x : lasq_heure(x) )
macron['month'] = macron['date'].apply(lambda d: d.month)

zemour['daate'] = zemour['Timestamp'].apply( lambda x : lasq_date(x) )
zemour['heuure'] = zemour['Timestamp'].apply( lambda x : lasq_heure(x) )
zemour['month'] = zemour['date'].apply(lambda d: d.month)

mel['daate'] = mel['Timestamp'].apply( lambda x : lasq_date(x) )
mel['heuure'] = mel['Timestamp'].apply( lambda x : lasq_heure(x) )
mel['month'] = mel['date'].apply(lambda d: d.month)

# zemour['month'] = zemour['date'].apply(lambda d: d.month)
# mel['month'] = mel['date'].apply(lambda d: d.month)

mDf=pd.read_csv('occurM.csv')
diccc=mDf.set_index('Unnamed: 0').T.to_dict('list')

DataMtronc1=macron[macron['date']>'2019-11-01 21:53:43']
E=['SMA_R3','SMA_C3','SMA_L3']




st.title('Comparateur de tweets de politiciens')



pol1 = st.radio(
     "quel est le premier  politicien que vouz choisisez? (bleu) ",
     ('Zmmour', 'Macron', 'Mellonchon'))

pol2 = st.radio(
     "quel est le deuxieme  politicien que vouz choisisez? (rouge) ",
     ('Zmmour', 'Macron', 'Mellonchon'))

var = st.radio(
     "quel est la  variable que vous souhaitez visualiser ",
     ('re-tweets', 'commentaires', 'likes'))



d1 = st.date_input(
     "La date du début")
format= '%Y-%m-%d %H:%M:%S'

dd1=d1.strftime('%Y-%m-%d %H:%M:%S')

  
d2 = st.date_input(
     "La date de fin")

dd2=d2.strftime('%Y-%m-%d %H:%M:%S')
  
pols= ['Zmmour', 'Macron', 'Mellonchon']

class Candidat(str):

    def __init__(self,str):

        if str is 'Zmmour':

            self.data = zemour[dd1<zemour['daate']]
            self.data=self.data[self.data['daate']<dd2]

        if str is 'Macron':
            self.data=macron[dd1<macron['daate']]
            self.data=self.data[self.data['daate']<dd2]
        
        if str is 'Mellonchon':
            self.data=mel[dd1<mel['daate']]
            self.data=self.data[self.data['daate']<dd2]
    


Abstractpol1=Candidat(pol1) 
Abstractpol2=Candidat(pol2) 

base1 = alt.Chart(Abstractpol1.data)
base2=alt.Chart(Abstractpol2.data)

if var=='re-tweets':
    line11 = base1.mark_line().encode(
        x='daate',
        y=E[0],)
    line12 = base2.mark_line(color='red').encode(
        x='daate',
        y=E[0],)

if var=='commentaires':
    line11 = base1.mark_line().encode(
       x='daate',
        y=E[1],)
    line12 = base2.mark_line(color='red').encode(
        x='daate',
        y=E[1],)

if var=='likes':
    line11 = base1.mark_line().encode(
        x='daate',
        y=E[2],)
    line12 = base2.mark_line(color='red').encode(
        x='daate',
        y=E[2],)
    


st.altair_chart(line11+line12, use_container_width=True)


#option = st.sidebar.checkbox('quel mot?')

st.write('Your birthday is:')

# ID={pol1:{
# df
# },
# pol2:{

# }}
