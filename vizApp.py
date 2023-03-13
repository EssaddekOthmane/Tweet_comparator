import numpy as np
import pandas as pd
from datetime import datetime
import altair as alt
import streamlit as st
import re
from datetime import timedelta  
# from spellchecker import SpellChecker

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
    # p=df['daate'][0][0:10]
    j=0
    i=1
    l=[]
    t=0
    T=df['Timestamp'].to_list()
    while i < len(T)-15:
        t=0
        while t!=1:
            if(i<len(T) and T[i][0:10]==T[i-1][0:10]):
                j=j+1
                i=i+1
                t=0
                
            
            else:
                l.append(j)
                i=i+1
                j=0
                t=1
    l.append(12)
    return(l)


macron=pd.read_csv('Dt_macron.csv')
zemour=pd.read_csv('Dt_zemour.csv')
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




st.title('Comparateur des tweets de candidats à la  présidentielle 2022')
#st.subheader("Author")
#st.markdown("ESSADDEK Othmane     \n        \n")
st.markdown( "On s'est intéresé durant ce projet à certains candidats à la présidentielle 2022 **Emmanuelle Macron, Eric Zemmour** et **Jean Luc Melenchon**.")

st.subheader("Analyse des données quantitatives : Likes, re-tweets, commentaires et heures des tweets ")

st.markdown( "On a fait en premier lieu une étude quantitative sur la réactivité de la communauté Twitter pour chaque des candidat.")
st.markdown( "On vous propose alors de visualiser la moyenne mobile (*sur 15 tweets*) de la variable que vous voulez, et cela vous donnera une idée sur le moment de chaque candidat par rapport aux deux autres.   ")
st.markdown("**Remarque:** Vous pouvez aussi visualiser les résultats de l'enquête du journal Le Monde par rapport à l'utilisation de faux comptes Twitter par zemmour. En effet vous pourrez le voir en comparant visuelemt la tendance des variables avant et après le début de la campagne présidentielle  :)")
var = st.radio(
     "Quelle est la  variable que vous souhaitez visualiser ",
     ('re-tweets', 'commentaires', 'likes'))

st.write(
     "On compare en premier tous les politiciens ! Macron est en jaune, Zemour en violet et Melenchon en vert. ")

#d_cov=datetime.date("2020-01-30")

date_time_str = '2020-03-01 08:15:27.243860'
d_cov= datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')


#st.write(d_cov)
d_in=datetime.date(macron.daate[0])

#     varo = st.radio(
#      "quel est la  variable que vous souhaitez visualiser ",
#      ('re-tweets', 'commentaires', 'likes'))



d1o = st.date_input("La date du début",value=d_in,key =1)#,value= datetime.date(macron.daate[0])

dd1o=d1o.strftime('%Y-%m-%d %H:%M:%S')


d2o = st.date_input(
     "La date de fin",value=d_in+ timedelta(days=5000),key =2)#value= datetime.date(macron.daate[-1])

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
    line11o = base1o.mark_line(color='#8A2BE2').encode(
        x='daate',
        y=E[0],)
    line12o = base2o.mark_line(color='#E3CF57').encode(
        x='daate',
        y=E[0],)
    line13o = base3o.mark_line(color='#458B00').encode(
        x='daate',
        y=E[0],)

if var=='commentaires':
    line11o = base1o.mark_line(color='#8A2BE2').encode(
       x='daate',
        y=E[1],)
    line12o = base2o.mark_line(color='#E3CF57').encode(
        x='daate',
        y=E[1],)
    line13o = base3o.mark_line(color='#458B00').encode(
        x='daate',
        y=E[1],)

if var=='likes':
    line11o = base1o.mark_line(color='#8A2BE2').encode(
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
     "Quel est le premier  politicien que vous choisissez ? (bleu) ",
     ('Zemmour', 'Macron', 'Melenchon'))

pol2 = st.radio(
     "Quel est le deuxieme ? (rouge) ",
     ('Macron','Zemmour', 'Melenchon'))

# var = st.radio(
#      "Quelle est la  variable que vous souhaitez visualiser ",
#      ('re-tweets', 'commentaires', 'likes'))



d1 = st.date_input(
     "La date du début",value=d_in,key =3)


dd1=d1.strftime('%Y-%m-%d %H:%M:%S')

  
d2 = st.date_input(
     "La date de fin",value=d_in+ timedelta(days=5000),key =4)

dd2=d2.strftime('%Y-%m-%d %H:%M:%S')
  
pols= ['Zemmour', 'Macron', 'Melenchon']

class Candidat(str):

    def __init__(self,str):

        if str is 'Zemmour':
            self.data=zemour.copy()
            self.datam=pd.read_csv('Data_zemour.csv')
            self.datam['daate'] = self.datam['Timestamp'].apply( lambda x : lasq_date(x) )
            self.datatr = zemour[dd1<zemour['daate']]
            self.datatr=self.datatr[self.datatr['daate']<dd2]

        if str is 'Macron':
            self.data=macron.copy()
            self.datam=pd.read_csv('Data_macron.csv')
            self.datam['daate'] = self.datam['Timestamp'].apply( lambda x : lasq_date(x) )
            self.datatr=macron[dd1<macron['daate']]
            self.datatr=self.datatr[self.datatr['daate']<dd2]
        
        if str is 'Melenchon':
            self.data=mel.copy()
            self.datam=pd.read_csv('Data_mel.csv')
            self.datam['daate'] = self.datam['Timestamp'].apply( lambda x : lasq_date(x) )
            self.datatr=mel[dd1<mel['daate']]
            self.datatr=self.datatr[self.datatr['daate']<dd2]
    


Abstractpol1=Candidat(pol1) 
Abstractpol2=Candidat(pol2) 

base1 = alt.Chart(Abstractpol1.datatr)
base2=alt.Chart(Abstractpol2.datatr)

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
st.markdown("On peut aussi voir l'évolution du nombre de tweets par jour de chaque politiciens, et aussi la distribution sur une journée de  l'heure à laquelle chuaqun publie ses tweets.")
polh = st.radio(
     "Quel est le  politicien que vouz choisisez?",
     ('Zemmour', 'Macron', 'Melenchon'))
Abstractpolh=Candidat(polh)

Tj=tweetPJ(Abstractpolh.data)   
x=[k for k in range(len(Tj))]
dfh = pd.DataFrame(list(zip(x, Tj)),columns =['x', 'Tj'])

baseh=alt.Chart(dfh)

lineh = baseh.mark_line(color = '#8A2BE2').encode(
        x='x',
        y='Tj',)
st.altair_chart(lineh, use_container_width=True)
st.markdown("Maintenant pour la distribution moyenne (en %) des tweet sur une journée.    \n En d'autres termes: En moyenne sur tous les jours, si le candidat tweet 100 fois en 24h, alors le graphe en bas représente nombre de tweets par heure  ")

temp=Abstractpolh.data
for k in range(24):
    temp[f'{k}'] = temp['daate'].apply(lambda x : is_hour(x,k))
    
somme = [temp[f'{k}'].sum() for k in range(24)]
somme = somme/sum(somme)
somme = somme*100
heures= [k for k in range(24)]
dfj=pd.DataFrame(list(zip(somme,heures)),columns=['Tweets','Heure'])

chart=alt.Chart(dfj).mark_bar().encode(
    x='Heure',
    y='Tweets',
 
)
st.altair_chart(chart, use_container_width=False)


st.subheader("Analyse textuelle des tweets" )

st.markdown("On passe maintenant à l'analyse des tweets, on commence par regarder les tweets.")
st.markdown("**Remarque :** Les tweets bruts de Melenchon sont à venir !")
polt = st.radio(
     "Quel est le politicien que vous choisissez ?  ",
     ('Macron','Zemmour','Melenchon'))

Abstractpolt=Candidat(polt) 

d_1 = st.date_input("La date du début",value=d_cov,key =5)

dd_1=d_1.strftime('%Y-%m-%d %H:%M:%S')


d_2 = st.date_input(
     "La date de fin",value=d_cov+ timedelta(days=5),key =6)

dd_2=d_2.strftime('%Y-%m-%d %H:%M:%S')

data_t = Abstractpolt.datam[dd_1<Abstractpolt.datam['daate']]
data_t=data_t[data_t['daate']<dd_2]

st.write(data_t['Embedded_text'])

# processing = st.radio(
#                       "Voulez vous voir les tweets en détail ?",
#                       ("Non", "Oui"))

# if processing == "Oui":

#     for str in data_t['Embedded_text']:
#         st.write("***********************************************")
#         st.write(str)
# else:
#   pass

# datam_ = macron[dd_1<macron['daate']]
# datam_=datam_[datam_['daate']<dd_2]

# datamel_ = mel[dd_1<mel['daate']]
# datamel_=datamel_[datamel_['daate']<dd_2]
 
st.markdown("   \n On vous propose maintenant de pluger un mot pour voir le nombre de fois que chaque candidat l'a utilisé depuis la création de son compte twitter.")

st.markdown("**Proposition de mots :** immigration , gauche , égalité , agriculture , migrants , pauvres , capitalisme , impôt , nucléaire , écologie , arabe , jeune , solidarité , justice , europe ...")
# option = st.sidebar.checkbox('quel mot?')
st.write('Quel est le mot que vous souhaitez tester?')
mot_space=st.text_input('Quel est le mot que vous souhaitez tester?',"")
mot=re.sub(r"\s+", "", mot_space)
mot = mot.lower()
if(mot in list(Mot)):
    st.write('le mot ',mot, 'a était cité par Zemmour ',diccc[mot][0], 'fois,  par Melenchon ',diccc[mot][1],'fois et par Macron',diccc[mot][2], 'fois')
    
if(mot not in list(Mot)):
     st.write("Aucun candidat n'a utiliser le mot ",mot)
    

#st.write(mot)
# ID={pol1:{
# df
# },
# pol2:{

# }}
