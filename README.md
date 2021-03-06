# will-chenaultVIZ

## Our first truthful visualization: 
<img width="973" alt="630truthful" src="https://user-images.githubusercontent.com/95489525/151275390-5088b6bf-6467-45cf-b2e0-2fe26a671353.png">

Because our data on ice is a measure of area, we thought a visualization where size was the most influential visual variable would be the most effective. Radar charts’ increments in angles lend themselves nicely to visualizing consecutive months in a calendar year. Different chart colors make it easy to distinguish between each year. Originally, we were going to visualize every year from 1992 to 2021 (a whopping 30 graphs!). Our more minimalist final graphs are a lot less cluttered while still communicating the intended message. 

## Earlier Versions of the Radar Charts. 

![66457456364__4325743B-086B-4307-AF1B-D558F972AF95](https://user-images.githubusercontent.com/95489525/151276525-d4ecf379-abf3-4693-ada2-a7dda011117f.png)

![66457422608__C227B771-7A96-484D-914A-621570D31DA3](https://user-images.githubusercontent.com/95489525/151276528-ba2c51df-8ec2-4e1a-8a24-dde6bc005cbb.png)

We originally used the matplot library to make radar charts. PLT's long, complicated functions were much more inconvenient to use than plotly's concise tools. The visualizations were also wonky because our lists of data weren't lists of floats, but rather lists of strings.

## Our first misleading visualization: 
<img width="992" alt="630misleading" src="https://user-images.githubusercontent.com/95489525/151275545-cee74662-24e0-42e1-8db2-483a4c9e5d91.png">

## Our second truthful visualization:

I decided to do a simple line chart of the data from around 800,000 BCE to 2018 CE. To emphasize how the recent CO2 concentration is significantly higher than the natural variation over the last hundreds of thousands of years, I marked a line at the greatest CO2 concentration before 1900, using `max(df['Concentration'][0:1769]`, and then compared this value to the 2018 CE value of 408.5 ppm, and writing with text that this is 36.8% higher. I played around with trying to make it interactive, but I decided that this was less effective. I also had to make sure that the bottom of the y axis is 0 so the proportions are accurate.

<img width="973" alt="630truthful" src="authentic_co2.svg">

## Our second misleading visualization:
<img width="973" alt="630misleading" src="fake_co2.svg">

Annotations:

<img width="973" alt="630misleading" src="misleading_annotations.png">


