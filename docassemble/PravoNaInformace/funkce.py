import json
import yaml
import re
import requests
from docassemble.base.util import *
from collections import OrderedDict

def ziskejSituace():
  page = requests.get(url_of("situace.json", _external=True))
  y = json.loads(page.content)
  dict = {}

  for x in y["Situace"]:
    dict[x["ID"]] = x["title"]
  return OrderedDict(sorted(dict.items()))

def ziskejDuvody(parent):
  page = requests.get(url_of("duvody.json", _external=True))
  y = json.loads(page.content)
  dict = {}

  for x in y["Důvody"]:
    if x["parent"] == int(parent) and x["v"] == 1:
      if x["ust"]:
        dict[x["ID"]] = x["title"]+"<small class='ust'>"+x["ust"]+"</small>"
      else:
        dict[x["ID"]] = x["title"]
  return OrderedDict(sorted(dict.items()))

def ziskejArgumentyProti(parent):
  page = requests.get(url_of("argumenty.json", _external=True))
  y = json.loads(page.content)
  dict = {}

  for x in y["Argumenty"]:
    if x["parent"] == int(parent) and x["titleMinus"] != None:
      dict[x["ID"]] = x["titleMinus"]
  return OrderedDict(sorted(dict.items()))

def obsahArgumentu(id):
  page = requests.get(url_of("argumenty.json", _external=True))
  y = json.loads(page.content)
  dict = {}

  for x in y["Argumenty"]:
    if x["ID"] == int(id):
      dict = x.copy()
  return dict

def obsahDuvodu(id):
  page = requests.get(url_of("duvody.json", _external=True))
  y = yaml.safe_load(page.content)
  dict = {}

  for x in y["Důvody"]:
    if x["ID"] == int(id):
      dict = x.copy()
  return dict

def obsahSituace(id):
  page = requests.get(url_of("situace.json", _external=True))
  y = json.loads(page.content)
  dict = {}

  for x in y["Situace"]:
    if x["ID"] == int(id):
      dict = x.copy()
  return dict

def castClanku(nid, kapitola):
  page = requests.get(url_of(str(nid)+".md", _external=True))
  text = re.search(r'(#{1,3}) ('+kapitola+r')\?(.*?)\n\1 ', page.text, re.DOTALL)
  return text.group(3)

def poznamkaWebhook(data, poznamka):
  webhook_data_poznamka = requests.post('https://hook.integromat.com/d5jg95ywvujoqohj7mu5j6xfym6lc57p', data=json.dumps({'data': data, 'poznamka': poznamka}), headers={'Content-Type': 'application/json'})
  return