#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mplsoccer


# In[52]:


import math
from urllib.request import urlopen

import matplotlib as mpl
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image


# In[53]:


totw_player_data = pd.DataFrame(
    {
        'position': ['ST', 'ST', 'RM', 'CM', 'LM', 'LB', 'LCB', 'CB', 'RCB', 'RB', 'GK'],
        'position_id': [9, 10, 7, 11, 8, 3, 6, 5, 4, 2, 1],
        'player': ['Haaland', 'Duran', 'Bernado', 'Palmer', 'Amad', 'Van De Ven', 'Walker',
                   'Gusto', 'Ruben', 'Gvardiol', 'Ederson'],
        'score': [15, 12, 13, 14, 14, 12, 13, 13, 14, 27, 13],
        'team': ['Man City', 'Aston Villa', 'Man City', 'Chelsea', 'Man Utd', 'Spurs',
                 'Man City', 'Chelsea', 'Man City', 'Man City',
                 'Man City']
    }
)
totw_player_data


# In[23]:


pip install cairosvg


# In[59]:


badge_urls = {
    'Man Utd': 'https://www.thesportsdb.com/images/media/team/badge/xzqdr11517660252.png',
    'Chelsea': 'https://www.thesportsdb.com/images/media/team/badge/yvwvtu1448813215.png',
    'Man City': 'https://www.thesportsdb.com/images/media/team/badge/vwpvry1467462651.png',
    'Aston Villa': 'https://www.thesportsdb.com/images/media/team/badge/gev5lp1679951447.png',
    'Arsenal': "https://www.thesportsdb.com/images/media/team/badge/uyhbfe1612467038.png",
    'Spurs':"https://www.thesportsdb.com/images/media/team/badge/dfyfhl1604094109.png"
}
image_dict = {team: Image.open(urlopen(url)) for team, url in badge_urls.items()}
images = [image_dict[team] for team in totw_player_data.team]


# In[60]:


# setup figure
pitch = VerticalPitch(pitch_type='opta', pitch_color='#333333', line_color='white', line_alpha=0.2,
                      line_zorder=3)
fig, axes = pitch.grid(endnote_height=0, figheight=13, title_height=0.1, title_space=0, space=0)
fig.set_facecolor('#333333')

# title
axes['title'].axis('off')
axes['title'].text(0.5, 0.6, ' FPL Team of the Week', ha='center', va='center', color='white',
                   fontsize=20)
axes['title'].text(0.5, 0.3, 'Round 37', ha='center', va='center', color='white', fontsize=14)

# plot the league logo using the inset_image method for utils
LEAGUE_URL = 'https://www.thesportsdb.com/images/media/league/badge/dsnjpz1679951317.png'
image = Image.open(urlopen(LEAGUE_URL))
title_image = inset_image(0.9, 0.5, image, height=1, ax=axes['title'])

text_names = pitch.formation('532', kind='text', positions=totw_player_data.position_id,
                             text=totw_player_data.player, ax=axes['pitch'],
                             xoffset=-2,  # offset the player names from the centers
                             ha='center', va='center', color='white', fontsize=11)
text_scores = pitch.formation('532', kind='text', positions=totw_player_data.position_id,
                              text=totw_player_data.score, ax=axes['pitch'],
                              xoffset=-5,  # offset the scores from the centers
                              ha='center', va='center', color='white', fontsize=11,
                              bbox=dict(facecolor='green', boxstyle='round,pad=0.2', linewidth=0))
badge_axes = pitch.formation('532', kind='image', positions=totw_player_data.position_id,
                             image=images, height=10, ax=axes['pitch'],
                             xoffset=5,  # offset the images from the centers
                             )


# In[ ]:




