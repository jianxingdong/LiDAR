import math

def getDist(time, speed=299792458):
	return speed * time/2

def getPoint(dist, azi, alt, current=[0, 0, 0]):
	x = math.cos(math.radians(alt)) * math.cos(math.radians(azi)) * dist + origin[0]
	y = math.cos(math.radians(alt)) * math.sin(math.radians(azi)) * dist + origin[1]
	z = math.sin(math.radians(alt)) * dist + origin[2]
	return [x, y, z]