#!/usr/bin/env python
# coding: utf-8


import requests
import datetime
import base64
import ticketpy
import pandas as pd

api_key = 'EXlelHC81kjy8tCDHXidayTuwQmukKhj'
api_key_b64 = base64.urlsafe_b64encode(api_key.encode())
tm_client = ticketpy.ApiClient(api_key)


states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

abbr_states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

genres = ['Alternative', ['Ballads', 'Romantic'], 'Blues', 'Chanson Francaise', 
          'Children’s Music', 'Classical', 'Country', ['Dance', 'Electronic'], 
          'Folk', ['Hip-Hop', 'Rap'], 'Holiday', 'Jazz', 'Latin', 
          ['Medieval', 'Rennaissance'], 'Metal', 'New Age', 'Other', 'Pop', 
          'R&B', 'Reggae', 'Religious', 'Rock', 'World']


state_event_genre_dict = {}
for state in range(len(states)):
    state_event_tally = []
    for genre in range(len(genres)):
        tally = 0
        try:
            if iter(genres[genre]):
                for sub_genre in range(len(genres[genre])):
                    pages = tm_client.events.find(
                    classification_name=str(genres[genre][sub_genre]),
                    state_code=str(states[state])).limit()
                    for event in pages:
                        tally += 1
        except:  
            pages = tm_client.events.find(
            classification_name=str(genres[genre]),
            state_code=str(states[state])).limit()

            for event in pages:
                tally += 1

        state_event_tally.append(tally)
    state_event_genre_dict[states[state]] = state_event_tally



df = pd.DataFrame(state_event_genre_dict, index=genres)
df = df.rename(columns=abbr_states)
df.to_excel("state_event_genre.xls")

