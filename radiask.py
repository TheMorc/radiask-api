#radia.sk, pythonová verzia
#Morc, výmysel vznikol 31.1.2022

import requests, os
import xml.etree.ElementTree as ET

params = (
    ('lid', 'FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF'),
)

api_response = requests.get('http://api.radia.sk/app/init/ios/3.0.0/', params=params)
root = ET.fromstring(api_response.text)

for child in root:
	print(child.find('id').text + " | " + child.find('orderString').text + " | " + child.find('name').text + " | " + child.find('logo').text)
	for song in child.findall('onairSong'):
		if song.find('artist') is not None:
			print(song.find('artist').text + " - " + song.find('title').text)
		if song.find('albumImage') is not None:
			print(song.find('albumImage').text)		
	for stream in child.find('streams').findall('stream'):
		print(stream.find('format').text + stream.find('bitrate').text + " - " + stream.find('url').text)
	print()
