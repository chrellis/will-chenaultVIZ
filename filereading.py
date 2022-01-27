import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D
import plotly.graph_objects as go

import pandas as pd



# go to https://nsidc.org/data/G02135/versions/3 for the source data

# the ice area for each month. each element is the year '92 (0) to '21 (29). 

jan_list  = []
feb_list  = []
mar_list  = []
april_list  = []
may_list  = []
june_list  = []
july_list  = []
aug_list  = []
sep_list  = []
oct_list  = []
nov_list  = []
dec_list  = []


january = pd.read_csv("N_01_extent_v3.0.csv") 
february = pd.read_csv("N_02_extent_v3.0.csv") 
march = pd.read_csv("N_03_extent_v3.0.csv") 
april = pd.read_csv("N_04_extent_v3.0.csv") 
may = pd.read_csv("N_05_extent_v3.0.csv") 
june = pd.read_csv("N_06_extent_v3.0.csv") 
july = pd.read_csv("N_07_extent_v3.0.csv") 
august = pd.read_csv("N_08_extent_v3.0.csv") 
september = pd.read_csv("N_09_extent_v3.0.csv") 
october = pd.read_csv("N_10_extent_v3.0.csv") 
november = pd.read_csv("N_11_extent_v3.0.csv") 
december = pd.read_csv("N_12_extent_v3.0.csv") 

with open("N_01_extent_v3.0.csv") as file:
    january = file.readlines() 
for line in january[14:len(january)]: 
    x = line.split()
    jan_list.append(x[5])


with open("N_02_extent_v3.0.csv") as file:
    feb = file.readlines() 
for line in feb[14:len(feb)]: 
    x = line.split()
    feb_list.append(x[5])

with open("N_03_extent_v3.0.csv") as file:
    march = file.readlines() 
for line in march[14:len(march)]: 
    x = line.split()
    mar_list.append(x[5])

with open("N_04_extent_v3.0.csv") as file:
    apr = file.readlines() 
for line in apr[14:len(apr)]: 
    x = line.split()
    april_list.append(x[5])

with open("N_05_extent_v3.0.csv") as file:
    may = file.readlines() 
for line in may[14:len(may)]: 
    x = line.split()
    may_list.append(x[5])

with open("N_06_extent_v3.0.csv") as file:
    june = file.readlines() 
for line in june[14:len(june)]: 
    x = line.split()
    june_list.append(x[5])

with open("N_07_extent_v3.0.csv") as file:
    july = file.readlines() 
for line in july[14:len(july)]: 
    x = line.split()
    july_list.append(x[5])

with open("N_08_extent_v3.0.csv") as file:
    aug = file.readlines() 
for line in aug[14:len(aug)]: 
    x = line.split()
    aug_list.append(x[5])

with open("N_09_extent_v3.0.csv") as file:
    sep = file.readlines() 
for line in sep[14:len(sep)]: 
    x = line.split()
    sep_list.append(x[5])

with open("N_10_extent_v3.0.csv") as file:
    oct = file.readlines() 
for line in oct[14:len(oct)]: 
    x = line.split()
    oct_list.append(x[5])

with open("N_11_extent_v3.0.csv") as file:
    nov = file.readlines() 
for line in nov[15:len(nov)]: 
    x = line.split()
    nov_list.append(x[5])

with open("N_12_extent_v3.0.csv") as file:
    dec = file.readlines() 
for line in dec[15:len(dec)]: 
    x = line.split()
    dec_list.append(x[5])


year_list = jan_list+ feb_list+ mar_list + april_list +may_list +june_list +july_list +aug_list + sep_list +oct_list +nov_list +dec_list

year_lists = []
for i in range(30):
    year_lists.append(year_list[i::30])

for yl in year_lists:
    print(yl)

n92 = year_list[0::30]
n93 = year_list[1::30]
n94 = year_list[2::30]
n95 = year_list[3::30]
n96 = year_list[4::30]
n97 = year_list[5::30]
n98 = year_list[6::30]
n99 = year_list[7::30]
n00 = year_list[8::30]
n01 = year_list[9::30]
n02 = year_list[10::30]
n03 = year_list[11::30]
n04 = year_list[12::30]
n05 = year_list[13::30]
n06 = year_list[14::30]
n07 = year_list[15::30]
n08 = year_list[16::30]
n09 = year_list[17::30]
n10 = year_list[18::30]
n11 = year_list[19::30]
n12 = year_list[20::30]
n13 = year_list[21::30]
n14 = year_list[22::30]
n15 = year_list[23::30]
n16 = year_list[24::30]
n17 = year_list[25::30]
n18 = year_list[26::30]
n19 = year_list[27::30]
n20 = year_list[28::30]
n21 = year_list[29::30]


        
categories = [" January ", " February " , " March ", " April ", " May ", " June ", " July ", " August ", " September ", " October ", " November ", " Decemenber "]

fig = go.Figure()

fig.add_trace(go.Scatterpolar( 
      r= list(map(float, n92)),
      theta=categories,
      fill='toself',
      name=" 1992 "
))

fig.add_trace(go.Scatterpolar(
      r= list(map(float, n21)),
      theta=categories,
      fill='toself',
      name=" 2021 "
))



fig.update_layout(
 title = "Ice Area in the Artic Ocean in Millions of Square km, 1992 and 2021 ",
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[2, 15]
    )), 
  showlegend=True,
  legend_title = "Key"
)

fig.show()


categories = [" January ", " February " , " March ", " April ", " May ", " June ", " July ", " August ", " September ", " October ", " November ", " Decemenber "]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r= list(map(float, n09)),
      theta=categories,
      fill='toself',
      name=" After Obama's Complaining "
))

fig.add_trace(go.Scatterpolar(
      r= list(map(float, n06)),
      theta=categories,
      fill='toself',
      name=" Before Obama's Complaining"
))


fig.update_layout(
    title = "What the Liberal Media Establishment Won't Show You. Infinite Whining with Zero Problems.",
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[2, 15]
    )),
  showlegend=True, 
  legend_title = "Artic Ocean Ice Area in Millions of Square km. "
)

fig.show()




#take away- the list elements were strings!! 








