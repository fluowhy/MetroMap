import requests
from bs4 import BeautifulSoup
import re
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import unidecode

from utils import *

page = requests.get("https://en.wikipedia.org/wiki/Santiago_Metro")
page = requests.get("https://en.wikipedia.org/wiki/Santiago_Metro_Line_1")
page = requests.get("https://en.wikipedia.org/wiki/Category:Santiago_Metro_stations")
soup = BeautifulSoup(page.content, 'html.parser')
find = soup.find_all("a", href=True, title=True, class_=False)

stations = []
names = []
P = []
for i in find[:10]:
	name = i.text
	if name.find("metro station") != - 1:
		if not name in names:
			href = i.attrs["href"]
			print(name)
			page_1 = requests.get("https://en.wikipedia.org{}".format(href))
			soup_1 = BeautifulSoup(page_1.content, 'html.parser')
			lon = soup_1.find_all(attrs = {"class": "longitude"})[0].get_text()
			lat = soup_1.find_all(attrs = {"class": "latitude"})[0].get_text()
			lon, lat = process(lon, lat)
			stations.append({"name": unidecode.unidecode(name.lower()), "lat": lat, "lon": lon})
			names.append(name)
			P.append([lon, lat])
P = np.array(P)
#save_json("stations.json", stations)
vor = Voronoi(P)
g = 0
"""
plt.scatter(P[:, 0], P[:, 1])
plt.show()
cas = [70, 33, 35.35, 33, 31 ,43]
Cas = coor2cart(cas[0:3], cas[3:])
u = [70, 39, 50, 33, 27, 28]
U = coor2cart(u[0:3], u[3:]) 
tia = [70, 31, 29, 33, 26, 12]
Tia = coor2cart(tia[0:3], tia[3:]) 
pap = [70, 39, 28, 33, 26, 14]
Pap = coor2cart(pap[0:3], pap[3:])
ben = [70, 40, 53, 33, 23, 39]
Ben = coor2cart(ben[0:3], ben[3:])
par = [70, 35, 50.47, 33, 31, 21]
Par = coor2cart(par[0:3], par[3:])

vor = Voronoi(P)
voronoi_plot_2d(vor, show_points=False, show_vertices=False)
plt.scatter(P[0:27, 0], P[0:27, 1], color='red') # L1
plt.scatter(P[27:49, 0], P[27:49, 1], color='yellow') # L2
#plt.scatter(P[49:54, 0], P[49:54, 1], color='brown') # L3
plt.scatter(P[54:78, 0], P[54:78, 1], color='blue') # L4
plt.scatter(P[78:84, 0], P[78:84, 1], color='cyan') # L4A
plt.scatter(P[84:114, 0], P[84:114, 1], color='green') # L5
plt.scatter(P[114:124, 0], P[114:124, 1], color='purple') # L6
plt.scatter([Cas[0], U[0], Tia[0], Pap[0], Ben[0], Par[0]], [Cas[1], U[1], Tia[1], Pap[1], Ben[1], Par[1]], color='black', marker='x')
plt.show()
"""



