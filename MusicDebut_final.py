# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:10:06 2021

@author: Yashvi
"""

import tkinter as tk
from tkinter import ttk
import pandas as pd
import plotly.graph_objs as go
import plotly
from tkinter import messagebox
import numbeoData1 #scraping numbeo website for data - please ensure steady internet connection
import numbeoData2 
#import music #- Web Scraping will take time (warning) - uncomment only if you have A LOT of time`

pd.options.mode.chained_assignment = None 
print('All modules imported and the data has been scraped')

#Reading the music data generated
musicData = pd.read_excel('MusicData.xlsx')
musicData = musicData[['listeners','name','playcount','tags']]

genres = list()

musicData['tags'] = musicData['tags'].astype('str')

#Fetching all genre tags
for tags in musicData['tags']:
    genreTags = tags.split(',')
    for i in genreTags:
        if i.strip() not in genres:
            genres.append(i.strip())
            
#Filtering data on the basis of certain genres
genreData = musicData[musicData['tags'].str.lower().str.contains("pop|rock|dubstep|hip-hop|hiphop|rap|electronic|indie|punk|jazz|country|classical")]
genreData['genre'] = ["" for i in range(len(genreData['name']))]

#Generating main genre tags
for index,rows in genreData.iterrows():
    if "pop" in genreData.loc[index,'tags'].lower():
        genreData.loc[index,'genre'] = genreData.loc[index,'genre'] + 'Pop '
    if "rock" in genreData.loc[index,'tags'].lower():
        genreData.loc[index,'genre'] = genreData.loc[index,'genre'] + 'Rock '
    if "dubstep" in genreData.loc[index,'tags'].lower():
        genreData.loc[index,'genre'] = genreData.loc[index,'genre'] + 'Dubstep '
    if "hip-hop" in genreData.loc[index,'tags'].lower() or "hiphop" in genreData.loc[index,'tags'].lower() or "rap" in genreData.loc[index,'tags'].lower():
        genreData.loc[index,'genre'] = genreData.loc[index,'genre'] + 'HipHop/Rap '
    if "electronic" in genreData.loc[index,'tags'].lower():
        genreData.loc[index,'genre'] = genreData.loc[index,'genre'] + 'Electronic '
    if "indie" in genreData.loc[index,'tags'].lower():
        genreData.loc[index,'genre'] = genreData.loc[index,'genre'] + 'Indie '
    if "punk" in genreData.loc[index,'tags'].lower():
        genreData.loc[index,'genre'] = genreData.loc[index,'genre'] + 'Punk '
    if "jazz" in genreData.loc[index,'tags'].lower():
        genreData.loc[index,'genre'] = genreData.loc[index,'genre'] + 'Jazz '
    if "country" in genreData.loc[index,'tags'].lower():
        genreData.loc[index,'genre'] = genreData.loc[index,'genre'] + 'Country '
    if "classical" in genreData.loc[index,'tags'].lower():
        genreData.loc[index,'genre'] = genreData.loc[index,'genre'] + 'Classical '

#Calculating grouped genre data by listeners and playcount
genreGroupDatabyListeners = genreData.groupby(by='genre')['listeners'].sum().reset_index()
genreGroupDatabyPlaycount = genreData.groupby(by='genre')['playcount'].sum().reset_index()
mixGenreGroupData = genreData[~genreData['genre'].isin(['Pop ','Rock ','HipHop/Rap ', 'Electronic ','Dubstep ','Indie ','Punk ','Jazz ','Country ','Classical '])].groupby(by='genre')['listeners'].sum().sort_values(ascending=False).reset_index()
mainGenreGroupData = genreData[genreData['genre'].isin(['Pop ','Rock ','HipHop/Rap ', 'Electronic ','Dubstep ','Indie ','Punk ','Jazz ','Country ','Classical '])].groupby(by='genre')['listeners'].sum().sort_values(ascending=False).reset_index()

#US Purchasing Power and Crime Index
states1 = list()
states2= list()
northEast = list()
northWest = list()
southEast = list()
southWest = list()
midWest = list()
regions = list()

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

northEast = ['CT','ME','MA','NH','NJ','NY','PA','RI','VT','DE','MD','DC']
northWest = ['CA','CO','HI','ID','MT','NV','OR','UT','WA','WY','AK']
southEast = ['AL','AR','FL','GA','KY','LA','MD','MS','NC','SC','TN','VA','WV',]
southWest = ['AZ','NM','TX','OK']
midWest = ['ND','SD','NE','KS','MO','IA','MN','WI','MI','IL','IN','OH']

#Reading Numbeo Data regarding puraching power and crime rate
costOfLivingdf = pd.read_excel('CostOfLiving.xlsx')
crimeRatingsdf = pd.read_excel('CrimeRatings.xlsx')

#Fetching important columns 
costOfLivingdf = costOfLivingdf[['City','Restaurant Price Index','Local Purchasing Power Index']]
crimeRatingsdf = crimeRatingsdf[['City','Crime Index','Safety Index']]


for cities in costOfLivingdf['City']:
    states1.append(cities.split(',')[1].strip())
    
costOfLivingdf['City'] = states1

for cities in crimeRatingsdf['City']:
    states2.append(cities.split(',')[1].strip())
    
crimeRatingsdf['City'] = states2

#Filling null values in various columns
mergedDf = pd.merge(costOfLivingdf,crimeRatingsdf,how='outer',on='City')
mergedDf.fillna(mergedDf['Restaurant Price Index'].mean(),inplace=True)
mergedDf.fillna(mergedDf['Local Purchasing Power Index'].mean(),inplace=True)
mergedDf.fillna(mergedDf['Crime Index'].mean(),inplace=True)
mergedDf.fillna(mergedDf['Safety Index'].mean(),inplace=True)
mergedDf = mergedDf.groupby('City').mean().reset_index()
mergedDf.rename(columns = {'City':'States'},inplace=True)

#Categorising States on the basis of Regions
for states in mergedDf['States']:
    if states in northEast:
        regions.append('NorthEast')
    elif states in northWest:
        regions.append('NorthWest')
    elif states in southEast:
        regions.append('SouthEast')
    elif states in southWest:
        regions.append('SouthWest')
    elif states in midWest:
        regions.append('MidWest')
    
mergedDf['Region'] = regions 

# Categorising all indexes on basis of 0.33 and 0.66 Quartile range 
#cost of living
qVal1 = (mergedDf['Restaurant Price Index'].quantile([0.33,0.66]))

cLow = [mergedDf['Restaurant Price Index'].min(),qVal1.get(0.33)]
cMod = [qVal1.get(0.33),qVal1.get(0.66)]
cHigh = [qVal1.get(0.66),mergedDf['Restaurant Price Index'].max()] #greater

#purchaing power
qVal2 = (mergedDf['Local Purchasing Power Index'].quantile([0.33,0.66]))

pLow = [mergedDf['Local Purchasing Power Index'].min(),qVal2.get(0.33)]
pMod = [qVal2.get(0.33),qVal2.get(0.66)]
pHigh = [qVal2.get(0.66),mergedDf['Local Purchasing Power Index'].max()]

#crime Index
qVal3 = (mergedDf['Crime Index'].quantile([0.33,0.66]))

crLow = [mergedDf['Crime Index'].min(),qVal3.get(0.33)]
crMod = [qVal3.get(0.33),qVal3.get(0.66)] #inclusive of lower indexes 
crHigh = [qVal3.get(0.66),mergedDf['Crime Index'].max()]

#safety Index
qVal4 = (mergedDf['Safety Index'].quantile([0.33,0.66]))

sLow=[mergedDf['Safety Index'].min(),qVal4.get(0.33)]
sMod=[qVal4.get(0.33),qVal4.get(0.66)]
sHigh=[qVal4.get(0.66),mergedDf['Safety Index'].max()]

#Data to fetch popular genre by state
ticketMaster = pd.read_excel('state_event_genre.xls').T.reset_index()
ticketMaster.columns.values[0] = "States"
stateCodes = ["States"]
for key in list(us_state_abbrev.keys()):
            for i in range(len(ticketMaster["States"])):
                if key == ticketMaster.loc[i,"States"]:
                    ticketMaster.loc[i,"States"] = us_state_abbrev[key]

genres = ['Alternative',['Ballads', 'Romantic'],'Blues''Chanson Francaise','Children’s Music','Classical',
    'Country',['Dance', 'Electronic'],'Folk',['Hip-Hop', 'Rap'],'Holiday','Jazz','Latin',['Medieval', 'Rennaissance'],'Metal'
    'New Age','Other','Pop','R&B','Reggae','Religious','Rock','World']                 

#Tkinter - GUI
root= tk.Tk()
root.title('Music Debut Helper')  
canvas1 = tk.Canvas(root, width = 800, height = 700)
canvas1.pack()

label1 = tk.Label(root, text='Welcome to Music Debut Helper!')
label1.config(font=('Arial', 20))
canvas1.create_window(400, 50, window=label1)

label2 = tk.Label(root, text='Can you please share your name? :)')
label2.config(font=('Arial', 10))
canvas1.create_window(120, 90, window=label2)
name = tk.Entry(root)
canvas1.create_window(300, 90, window=name) 

label3 = tk.Label(root, text='Let\'s get you started! Could you please fill out these preferences? :D')
label3.config(font=('Arial', 10))
canvas1.create_window(213, 120, window=label3)

label4 = tk.Label(root, text='Which genre are you into?')
label4.config(font=('Arial',10))
canvas1.create_window(93, 150, window=label4)

genrePref = tk.StringVar() 
genreList = ttk.Combobox(root, width = 27, textvariable = genrePref) 
genreList['values'] = ('Pop ','Rock ','HipHop/Rap ', 'Electronic ','Dubstep ','Indie ','Punk ','Jazz ','Country ','Classical ') 
canvas1.create_window(270, 150, window = genreList) 
genreList.current() 

label11 = tk.Label(root, text='Do you have US state region preference for music concerts/launch?')
label11.config(font=('Arial',10))
canvas1.create_window(211, 180, window=label11)

statePref = tk.StringVar() 
stateList = ttk.Combobox(root, width = 27, textvariable = statePref) 
stateList['values'] = ('NorthEast','NorthWest','SouthEast','SouthWest','MidWest') 
canvas1.create_window(510, 180, window = stateList) 
stateList.current() 

label12 = tk.Label(root, text='Please select your preferences for states recommendations:')
label12.config(font=('Arial',10))
canvas1.create_window(194, 210, window=label12)

label13 = tk.Label(root, text='Purchasing Power Index level:')
label13.config(font=('Arial',10))
canvas1.create_window(200, 240, window=label13)

purchasePref = tk.StringVar() 
purchaseList = ttk.Combobox(root, width = 27, textvariable = purchasePref) 
purchaseList['values'] = ('Low','Moderate','High') 
canvas1.create_window(510, 240, window = purchaseList) 
stateList.current() 

label14 = tk.Label(root, text='Restuarant/Entertainment Expenditure level:')
label14.config(font=('Arial',10))
canvas1.create_window(200, 270, window=label14)

enternPref = tk.StringVar() 
enternList = ttk.Combobox(root, width = 27, textvariable = enternPref) 
enternList['values'] = ('Low','Moderate','High') 
canvas1.create_window(510, 270, window = enternList) 
enternList.current() 

label15 = tk.Label(root, text='Safety Index level:')
label15.config(font=('Arial',10))
canvas1.create_window(200, 300, window=label15)

safePref = tk.StringVar() 
safeList = ttk.Combobox(root, width = 27, textvariable = safePref) 
safeList['values'] = ('Low','Moderate','High') 
canvas1.create_window(510, 300, window = safeList) 
safeList.current() 

var1 = tk.StringVar()
var1.set('NOTE: On clicking the buttons, the graphs will be plotted in your Chrome browser.Please wait to be redirected and feel free to come back and add/change more filters. Thank you!')
label16 = tk.Message( root, textvariable=var1 )
label16.config(font=('Arial',10),anchor='center')
canvas1.create_window(150, 620, window=label16)

label17 = tk.Message( root, textvariable="")
label17.config(font=('Arial',10))
canvas1.create_window(385, 520, window=label17)

label18 = tk.Message( root, textvariable="")
label18.config(font=('Arial',10))
canvas1.create_window(585, 550, window=label18)

#Function to filter and display top five artists
def top_five():
    
    genrePrefArtists = genreData[genreData['genre']==genrePref.get()].sort_values(by='listeners',ascending=False)['name'].head(5)
    
    label5 = tk.Label(root, text='Your competition will be:')
    label5.config(font=('Arial',10))
    canvas1.create_window(385, 450, window=label5)
    
    topArtist = ""
    for i in range(0,5):
        topArtist = topArtist + str(i+1) +'. '+ genrePrefArtists.iloc[i] +'\n'
    var2= tk.StringVar()
    var2.set(topArtist)
    label17.configure(text=var2.get())
    
#Functino to dilpay bar graphs of popular artists, genres and mixed genres
def create_charts():
    
    most_popular_artists_by_count = musicData.groupby(by='name')['playcount'].sum().sort_values(ascending=False)[:50]
    data = [
    
    go.Bar(
            x=most_popular_artists_by_count.index,
            y=most_popular_artists_by_count,
            text=most_popular_artists_by_count,
            textposition='auto',
            opacity=0.75
            
    )]

    layout = go.Layout(
    title='Popularity of Artists by Count',
    
    yaxis= dict(
        title='Number of Times Played',
        gridcolor='rgb(255, 255, 255)',
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
        titlefont=dict(size=15)))

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='popular_artists.html')
    
    #plot 2
    data = [
    
    go.Bar(
            x=mixGenreGroupData['genre'],
            y=mixGenreGroupData['listeners'],
            text=mixGenreGroupData,
            textposition='auto',
            opacity=0.75
            
    )]

    layout = go.Layout(
    title='Popular Mixed Genres by Listeners',
    
    yaxis= dict(
        title='Listeners Count',
        gridcolor='rgb(255, 255, 255)',
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
        titlefont=dict(size=15)))

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='popular_mixgenres.html')
    
    #graph 3
    data = [
    
    go.Bar(
            x=mainGenreGroupData['genre'],
            y=mainGenreGroupData['listeners'],
            text=mainGenreGroupData,
            textposition='auto',
            opacity=0.75
            
    )]

    layout = go.Layout(
    title='Popular Genres by Listeners',
    
    yaxis= dict(
        title='Listeners Count',
        gridcolor='rgb(255, 255, 255)',
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
        titlefont=dict(size=15)))

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='popular_genres.html')

#Function to geo map states according to different parameters/indexes  
def geomap():
    
    #Filtering the United States regions
    filterDf = mergedDf.loc[mergedDf['Region'].str.lower() == statePref.get().lower()].reset_index()
    
    #Filters for Cost of Living Index according to user selection
    if enternPref.get() == 'Low':
        filterDf = filterDf[(filterDf['Restaurant Price Index'] >= cLow[0]) & (filterDf['Restaurant Price Index'] < cLow[1])]
    elif enternPref.get() == 'Moderate':
        filterDf = filterDf[(filterDf['Restaurant Price Index'] >= cMod[0]) & (filterDf['Restaurant Price Index'] < cMod[1])]
    elif enternPref.get() == 'High':
        filterDf = filterDf[(filterDf['Restaurant Price Index'] >= cHigh[0]) & (filterDf['Restaurant Price Index'] < cHigh[1])]
    
    #Filters for Local Purchasing Power Index according to user selection
    if purchasePref.get() == 'Low':
        filterDf = filterDf[(filterDf['Local Purchasing Power Index'] >= pLow[0]) & (filterDf['Local Purchasing Power Index'] < pLow[1])]
    elif purchasePref.get() == 'Moderate':
        filterDf = filterDf[(filterDf['Local Purchasing Power Index'] >= pMod[0]) & (filterDf['Local Purchasing Power Index'] < pMod[1])]
    elif purchasePref.get() == 'High':
        filterDf = filterDf[(filterDf['Local Purchasing Power Index'] >= pHigh[0]) & (filterDf['Local Purchasing Power Index'] < pHigh[1])]
    
    #Filters for Safety Index according to user selection
    if safePref.get() == 'Low':
        filterDf = filterDf[(filterDf['Safety Index'] >= sLow[0]) & (filterDf['Safety Index'] < sLow[1])]
    elif safePref.get()  == 'Moderate':
        filterDf = filterDf[(filterDf['Safety Index'] >= sMod[0]) & (filterDf['Safety Index'] < sMod[1])]
    elif safePref.get()  == 'High':
        filterDf = filterDf[(filterDf['Safety Index'] >= sHigh[0]) & (filterDf['Safety Index'] < sHigh[1])]
    
    filterDf = filterDf.reset_index()
    label19 = tk.Label(root, text='The recommended states to debut from are:')
    label19.config(font=('Arial',10))
    canvas1.create_window(607, 450, window=label19)
    
    recommendedStates = ""
    if(statePref.get() not in ['NorthEast','NorthWest','SouthEast','SouthWest','MidWest'] ):
        recommendedStates = 'All states of United States are favourable. Goodluck!^-^' 
    elif(filterDf.empty):
        recommendedStates = 'Sorry! No states with the current selected filters were found. Please reset them.'
    else:
        for key in list(us_state_abbrev.keys()):
            for i in range(0,len(filterDf['States'])):
                if us_state_abbrev[key] == filterDf.loc[i,'States']:
                    recommendedStates = recommendedStates+key+'\n'
    var3= tk.StringVar()
    var3.set(recommendedStates)
    label18.configure(text=var3.get())
    
    if (filterDf.empty) & (statePref.get() not in {'NorthEast','NorthWest','SouthEast','SouthWest','MidWest'}) & (enternPref.get() not in {'Low','Moderate','High'}) & (purchasePref.get() not in {'Low','Moderate','High'}) & (safePref.get() not in {'Low','Moderate','High'}):
        plotDf = mergedDf.reset_index()
    elif (filterDf.empty) & ((statePref.get() in {'NorthEast','NorthWest','SouthEast','SouthWest','MidWest'})|(enternPref.get() not in {'Low','Moderate','High'})|(purchasePref.get() not in {'Low','Moderate','High'})|(safePref.get() not in {'Low','Moderate','High'})):
        return
    else:
        plotDf = filterDf
        
    data = dict(
            type = 'choropleth',
            colorscale = 'Viridis', 
            reversescale = True,
            locations = plotDf['States'],
            locationmode = "USA-states",
            z =  plotDf['Local Purchasing Power Index'].astype(float),
            text =  plotDf['States'],
            colorbar = {'title' : 'Purchasing Power'}
          )
    
       
    layout=dict(title_text = 'Purchasing Power by State')
    fig = go.Figure(data=data,layout=layout) 
    fig.update_layout(
        geo_scope='usa', # limite map scope to USA
    )
    plotly.offline.plot(fig,filename='purchaseIndex.html')
    
    data = dict(
            type = 'choropleth',
            colorscale = 'Viridis', 
            reversescale = True,
            locations = plotDf['States'],
            locationmode = "USA-states",
            z =  plotDf['Restaurant Price Index'].astype(float),
            text =  plotDf['States'],
            colorbar = {'title' : 'Restaurant/Enterntainment Index'}
          )
    
       
    layout=dict(title_text = 'Restaurant/Enterntainment Index by State')
    fig = go.Figure(data=data,layout=layout) 
    fig.update_layout(
        geo_scope='usa', # limite map scope to USA
    )
    plotly.offline.plot(fig,filename='restIndex.html')
    
    data = dict(
            type = 'choropleth',
            colorscale = 'Viridis', 
            reversescale = True,
            locations = plotDf['States'],
            locationmode = "USA-states",
            z =  plotDf['Safety Index'].astype(float),
            text =  plotDf['States'],
            colorbar = {'title' : 'Safety Index'}
          )
    
       
    layout=dict(title_text = 'Safety Index by State')
    fig = go.Figure(data=data,layout=layout) 
    fig.update_layout(
        geo_scope='usa', # limite map scope to USA
    )
    plotly.offline.plot(fig,filename='safetyIndex.html')

#Function to plot stacked bar graph for popular genres in differnet states
def pop_state():
    
    states = ticketMaster["States"]
    names = ticketMaster.columns[1:]
    data=[
                     go.Bar(name=names[0], x=states, y=ticketMaster[names[0]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[1], x=states, y=ticketMaster[names[1]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[2], x=states, y=ticketMaster[names[2]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[3], x=states, y=ticketMaster[names[3]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[4], x=states, y=ticketMaster[names[4]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[5], x=states, y=ticketMaster[names[5]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[6], x=states, y=ticketMaster[names[6]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[7], x=states, y=ticketMaster[names[7]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[8], x=states, y=ticketMaster[names[8]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[9], x=states, y=ticketMaster[names[9]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[10], x=states, y=ticketMaster[names[10]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[11], x=states, y=ticketMaster[names[11]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[12], x=states, y=ticketMaster[names[12]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[13], x=states, y=ticketMaster[names[13]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[15], x=states, y=ticketMaster[names[15]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[16], x=states, y=ticketMaster[names[16]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[17], x=states, y=ticketMaster[names[17]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[18], x=states, y=ticketMaster[names[18]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[19], x=states, y=ticketMaster[names[19]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[20], x=states, y=ticketMaster[names[20]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[21], x=states, y=ticketMaster[names[21]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75),
                     go.Bar(name=names[22], x=states, y=ticketMaster[names[22]],text=ticketMaster,
                     textposition='auto',
                     opacity=0.75)]
    layout = go.Layout(
    title='Popular Genres by US States',
        
        yaxis= dict(
            title='Genrewise Events/Concerts count',
            gridcolor='rgb(255, 255, 255)',
            zerolinewidth=1,
            ticklen=5,
            gridwidth=2,
            titlefont=dict(size=15)),
         xaxis= dict(
            title='United State Abbreviations',
            titlefont=dict(size=15)))
    
    
    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(barmode='stack')
    plotly.offline.plot(fig, filename='popular_genre.html')

#Display Goodbye dialog and destrop the window in 2000 milliseconds  
def exit_check():
     messagebox.showinfo("Goodbye!", "Goodbye, "+name.get()+" it's been fun! Goodluck :D")
     root.after(2000, root.destroy)
   
button1 = tk.Button (root, text='  Explore The Insights   ',command=create_charts, bg='lightskyblue2', font=('Arial', 11, 'bold')) 
canvas1.create_window(385, 380, window=button1)

button2 = tk.Button (root, text='Generate Popular Genre/State', command=pop_state, bg='lightskyblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(175, 420, window=button2)

button3 = tk.Button (root, text=' Check Top Five Artists ',command=top_five, bg='lightskyblue2', font=('Arial', 11, 'bold')) 
canvas1.create_window(385, 420, window=button3)

button4 = tk.Button (root, text='Generate States Suggestion  ', command=geomap, bg='lightskyblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(591, 420, window=button4)

button5 = tk.Button (root, text='Exit Application', command=exit_check, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(700, 620, window=button5)

root.mainloop()
