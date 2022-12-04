# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:47:51 2021

@author: HEYA2
"""

import pandas as pd
import plotly.graph_objs as go
import plotly
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None 

ticketMaster = pd.read_excel('state_event_genre.xls').T.reset_index()

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

ticketMaster.columns.values[0] = 'States'
stateCodes = ["States"]
for key in list(us_state_abbrev.keys()):
            for i in range(len(ticketMaster["States"])):
                if key == ticketMaster.loc[i,"States"]:
                    ticketMaster.loc[i,"States"] = us_state_abbrev[key]
                    

genres = ['Alternative',['Ballads', 'Romantic'],'Blues''Chanson Francaise','Children’s Music','Classical',
'Country',['Dance', 'Electronic'],'Folk',['Hip-Hop', 'Rap'],'Holiday','Jazz','Latin',['Medieval', 'Rennaissance'],'Metal'
'New Age','Other','Pop','R&B','Reggae','Religious','Rock','World']

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
                 opacity=0.75)
]

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
plotly.offline.plot(fig, filename='popular_genres.html')

