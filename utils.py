import json
import re

def save_json(name, list_of_dict):
    with open(name, "w") as fout:
        json.dump(list_of_dict, fout)
    return


def read_json(filename):
    with open(filename) as json_data:
        d = json.load(json_data)
        json_data.close()
    return d


def process(longi, latit):
	"""Split and returns x, y positions.
	x1: str, longitude.
	x2: str, latitude.
	"""
	lo = re.split('°|′|″W', longi)[:-1]
	la = re.split('°|′|″S', latit)[:-1]
	X, Y = coor2cart(lo, la)
	return X, Y


def coor2cart(Lo, La):
	"""Transforms deg to cartesian coordinates.
	Lo: list of str, longitude in deg.
	La: list of str, latitude in deg.
	"""
	y = float(La[0]) + float(La[1]) / 60 + float(La[2]) / 3600
	x = float(Lo[0]) + float(Lo[1]) / 60 + float(Lo[2]) / 3600
	return - x, - y