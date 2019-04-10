from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from flask import request
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import urllib
import urllib.parse
import urllib.request
import requests 
import json

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):		
		loc = tracker.get_slot('location')
		response="It is currently sunny in {} at the moment".format(loc)
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]


class ActionVoter(Action):
	def name(self):
		return 'action_voter'
		
	def run(self, dispatcher, tracker, domain):
		request = json.loads(requests.get('http://localhost:5016/voterdb/voter').text)  # make an api call
		voterdetail = request['voters']# extract a voterdetail from returned json response
		dispatcher.utter_message(str(voterdetail))  # send the message back to the user
		return []

class ActionEmployee(Action):
	def name(self):
		return 'action_employee'
		
	def run(self, dispatcher, tracker, domain):
		request = json.loads(requests.get('http://localhost:5015/empdb/employee').text)  # make an api call
		empdetail = request['emps']# extract a empdetail from returned json response
		dispatcher.utter_message(str(empdetail))  # send the message back to the user
		return []
		'''emp=tracker.get_slot('empID')		
		url = 'http://localhost:5015/empdb/employee'
		response = urllib.request.urlopen(url).read()
		print(response)
		# u is a file-like object		
		data1=json.loads(response)		
		print(data1)
		print(data1[])
		#print(data1['emps']['name'])		
		#print(data1['emps']['title'])		
		#print(data1)
		#response=data1.id	
		dispatcher.utter_message(data1[emps][id])
		return [SlotSet('empID',emp)]'''
    
