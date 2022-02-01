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
        
def is_hour(x,k):
    if k== x.hour:
        return 1
    else:
        return 0
    
def tweetPJ(df):
    p=df['Timestamp'][0][0:10]
    j=0
    i=1
    l=[]
    t=0
    T=df['Timestamp'].to_list()
    while i < len(T)-4:
        t=0
        while t!=1:
            if(T[i][0:10]==T[i-1][0:10]):
                j=j+1
                i=i+1
                t=0
                
            
            else:
                l.append(j)
                i=i+1
                j=0
                t=1
    return(l)



macron=pd.read_csv('Data_macron.csv')
zemour=pd.read_csv('Data_zemour.csv')
mel=pd.read_csv('Df_mell.csv')

macron['daate'] = macron['Timestamp'].apply( lambda x : lasq_date(x) )
macron['heuure'] = macron['Timestamp'].apply( lambda x : lasq_heure(x) )
# macron['month'] = macron['date'].apply(lambda d: d.month)

zemour['daate'] = zemour['Timestamp'].apply( lambda x : lasq_date(x) )
zemour['heuure'] = zemour['Timestamp'].apply( lambda x : lasq_heure(x) )
# zemour['month'] = zemour['date'].apply(lambda d: d.month)

mel['daate'] = mel['Timestamp'].apply( lambda x : lasq_date(x) )
mel['heuure'] = mel['Timestamp'].apply( lambda x : lasq_heure(x) )
# mel['month'] = mel['date'].apply(lambda d: d.month)

# zemour['month'] = zemour['date'].apply(lambda d: d.month)
# mel['month'] = mel['date'].apply(lambda d: d.month)

mDf=pd.read_csv('occurM.csv')
Mot=mDf['Unnamed: 0']
diccc=mDf.set_index('Unnamed: 0').T.to_dict('list')

# DataMtronc1=macron[macron['date']>'2019-11-01 21:53:43']
E=['SMA_R3','SMA_C3','SMA_L3']




st.title('Comparateur des tweets de candidats de la  présidentielle 2022')
st.markdown( "On s'est intereser durant ce projet a certains candidats de la présidentielle 2022 **Emmanuelle Macron, Eric Zemmour** et **Jean Luc Melenchon**.")
st.markdown( "On a fait en premier lieux une étude quantitative sur la réactivité de la communauté tweeter avec chacun des candidats.")
st.markdown( "On vous propose alors de visualiser la moyenne mobile (*sur un mois*) de la variable que vous voulez, et cela vous donnera une idée sur le moment de chaque candidat par rapport au deux autres.   ")

var = st.radio(
     "quel est la  variable que vous souhaitez visualiser ",
     ('re-tweets', 'commentaires', 'likes'))

st.write(
     "On compare en premier tous les politiciens ! Macron est en jaune, Zemour en violet et Melenchon en vert. ")


#     varo = st.radio(
#      "quel est la  variable que vous souhaitez visualiser ",
#      ('re-tweets', 'commentaires', 'likes'))



d1o = st.date_input("La date du début",key =1)

dd1o=d1o.strftime('%Y-%m-%d %H:%M:%S')


d2o = st.date_input(
     "La date de fin",key =2)

dd2o=d2o.strftime('%Y-%m-%d %H:%M:%S')

dataz = zemour[dd1o<zemour['daate']]
dataz=dataz[dataz['daate']<dd2o]

datam = macron[dd1o<macron['daate']]
datam=datam[datam['daate']<dd2o]

datamel = mel[dd1o<mel['daate']]
datamel=datamel[datamel['daate']<dd2o]

base1o = alt.Chart(dataz)
base2o=alt.Chart(datam)
base3o=alt.Chart(datamel)

if var=='re-tweets':
    line11o = base1o.mark_line(color='#DC143C').encode(
        x='daate',
        y=E[0],)
    line12o = base2o.mark_line(color='#E3CF57').encode(
        x='daate',
        y=E[0],)
    line13o = base3o.mark_line(color='#458B00').encode(
        x='daate',
        y=E[0],)

if var=='commentaires':
    line11o = base1o.mark_line(color='#DC143C').encode(
       x='daate',
        y=E[1],)
    line12o = base2o.mark_line(color='#E3CF57').encode(
        x='daate',
        y=E[1],)
    line13o = base3o.mark_line(color='#458B00').encode(
        x='daate',
        y=E[1],)

if var=='likes':
    line11o = base1o.mark_line(color='#DC143C').encode(
        x='daate',
        y=E[2],)
    line12o = base2o.mark_line(color='#E3CF57').encode(
        x='daate',
        y=E[2],)
    line13o = base3o.mark_line(color='#458B00').encode(
        x='daate',
        y=E[2],)



st.altair_chart(line11o+line12o+line13o, use_container_width=True)

st.markdown("Maintenant vous pouvez faire des comparaisons pour une paire de politiciens.")
pol1 = st.radio(
     "quel est le premier  politicien que vouz choisisez? (bleu) ",
     ('Zemmour', 'Macron', 'Melenchon'))

pol2 = st.radio(
     "quel est le deuxieme  politicien que vouz choisisez? (rouge) ",
     ('Zemmour', 'Macron', 'Mellonchon'))

# var = st.radio(
#      "quel est la  variable que vous souhaitez visualiser ",
#      ('re-tweets', 'commentaires', 'likes'))



d1 = st.date_input(
     "La date du début",key =3)


dd1=d1.strftime('%Y-%m-%d %H:%M:%S')

  
d2 = st.date_input(
     "La date de fin",key =4)

dd2=d2.strftime('%Y-%m-%d %H:%M:%S')
  
pols= ['Zemmour', 'Macron', 'Mellonchon']

class Candidat(str):

    def __init__(self,str):

        if str is 'Zemmour':

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

st.markdown("En passe maintenat a l'analyse des tweets, on vous propose alors de pluger un mot pour voir le nombre de fois que chaque candidat a utiliser depuis la création de son compte tweeter. ")
st.markdown("Les mots doivent etre en **minuscule!** ")
st.markdown("**Proposition de mots :** islam , immigration , gauche , égalité ...")
# option = st.sidebar.checkbox('quel mot?')
st.write('Quel est le mot que vous souhaitez tester?')
mot=st.text_input('Quel est le mot que vous souhaitez tester?',"")

if(mot in list(Mot)):
    st.write('le mot ',mot,'a etait cité ',diccc[mot][0], 'par Zemmour, ',diccc[mot][1], 'par Mellonchon et ',diccc[mot][2], 'par Macron')
    
if(mot not in list(Mot)):
     st.write("Aucun candidat n'a utiliser le mot ",mot)
    

#st.write(mot)
# ID={pol1:{
# df
# },
# pol2:{

# }}
