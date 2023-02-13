#python script that opens a bunch of links where you can see snow and weather conditions and forecasts

import os, sys
import webbrowser
from datetime import date
from datetime import timedelta
import requests


#get the newest date
today = date.today()
tdy = today.strftime("%Y-%m-%d")

yesterday = today - timedelta(days = 1)
yesterday = yesterday.strftime("%Y-%m-%d")


#open the following links - for the satellite imagery use yesterday as the desired observation date, however you might have to click further back in time to get an image in your AOI
#you can also adjust you AOI here with the zoom level and coordinates
    #Map geo Admin with flight status and snow depth from exosnow
link_Admin = "https://map.geo.admin.ch/?zoom=2&lang=de&topic=ech&bgLayer=ch.swisstopo.swissimage&E=2660279.65&N=1166328.70&layers=ch.bazl.luftfahrtkarten-icao,ch.vbs.swissmilpilotschart,ch.swisstopo.swissimage-product,WMTS%7C%7Csd20alps_2056%7C%7Chttps:%2F%2Fp20.cosmos-project.ch%2Fsd20alps_map%2Fwmts%3Fservice%3Dwmts%26request%3Dgetcapabilities%26SERVICE%3DWMTS%26REQUEST%3DGetCapabilities%26VERSION%3D1.0.0,ch.swisstopo.swissalti3d-reliefschattierung,KML%7C%7Chttps:%2F%2Fdata.geo.admin.ch%2Fch.swisstopo.lubis-bildstreifen%2Fflight-status%2Fkml%2Fflight_status.kml,ch.swisstopo.lubis-bildstreifen,ch.swisstopo.swissboundaries3d-kanton-flaeche.fill&layers_timestamp=,,2021,,,,2016,&layers_visibility=false,false,false,true,false,true,false,false"

    #false color image Sentinel 2 switzerland
link_S2_1 = "https://apps.sentinel-hub.com/eo-browser/?zoom=9&lat=46.72833&lng=7.71321&themeId=DEFAULT-THEME&visualizationUrl=https%3A%2F%2Fservices.sentinel-hub.com%2Fogc%2Fwms%2F42924c6c-257a-4d04-9b8e-36387513a99c&datasetId=S2L1C&fromTime="
link_S2_2 = "T00%3A00%3A00.000Z&toTime="
link_S2_3 = "T23%3A59%3A59.999Z&layerId=6-SWIR&demSource3D=%22MAPZEN%22"
link_S2 = str(link_S2_1+yesterday+link_S2_2+yesterday+link_S2_3)

    #false color image Landsat 8 switzerland
link_L8_1 = "https://apps.sentinel-hub.com/eo-browser/?zoom=9&lat=46.72833&lng=7.71321&themeId=DEFAULT-THEME&visualizationUrl=https%3A%2F%2Fservices.sentinel-hub.com%2Fogc%2Fwms%2Fe35192fe-33a1-41f3-b798-b755e771c5a5&datasetId=AWS_LOTL1&fromTime="
link_L8_2 = "T00%3A00%3A00.000Z&toTime="
link_L8_3 = "T23%3A59%3A59.999Z&layerId=3_FALSE_COLOR&demSource3D=%22MAPZEN%22"
link_L8 = str(link_L8_1+yesterday+link_L8_2+yesterday+link_L8_3)

    #false color image Sentinel 3 switzerland
link_S3_1 = "https://apps.sentinel-hub.com/eo-browser/?zoom=9&lat=46.72833&lng=7.71321&themeId=DEFAULT-THEME&visualizationUrl=https%3A%2F%2Fservices.sentinel-hub.com%2Fogc%2Fwms%2F82f84fab-9b1c-4322-beeb-207b0f05afef&datasetId=S3OLCI&fromTime="
link_S3_2 = "T00%3A00%3A00.000Z&toTime="
link_S3_3 = "T23%3A59%3A59.999Z&layerId=4_RGB__17_5_2_&demSource3D=%22MAPZEN%22"
link_S3 = str(link_S3_1+yesterday+link_S3_2+yesterday+link_S3_3)

    #Meteo Schweiz weather forecast
link_MeteoCH = "https://www.meteoschweiz.admin.ch/"

    #Meteo Blue cloud cover forecast map
link_MeteoBlue = "https://www.meteoblue.com/de/wetter/maps/thun_schweiz_2658377#coords=7.7/46.642/8.931&map=totalClouds~hourlyAll~auto~sfc~none"


#open links
webbrowser.open(link_Admin)
webbrowser.open(link_S2)
webbrowser.open(link_L8)
webbrowser.open(link_S3)
webbrowser.open(link_MeteoCH)
webbrowser.open(link_MeteoBlue)



raw_input('DONE ----- Press ENTER to exit')