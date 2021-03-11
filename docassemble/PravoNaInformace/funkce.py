import json
import yaml
import requests
from docassemble.base.util import *

def ziskejSituace():
  page = requests.get(url_of("situace.json", _external=True))
  y = json.loads(page.content)
  dict = {}

  for x in y["Situace"]:
    dict[x["ID"]] = x["title"]
  return dict

def ziskejDuvody(parent):
  page = requests.get(url_of("duvody.json", _external=True))
  y = json.loads(page.content)
  dict = {}

  for x in y["Důvody"]:
    if x["parent"] == int(parent) and x["v"] == 1:
      dict[x["ID"]] = x["title"]
  return dict

def ziskejArgumentyProti(parent):
  page = requests.get(url_of("argumenty.json", _external=True))
  y = json.loads(page.content)
  dict = {}

  for x in y["Argumenty"]:
    if x["parent"] == int(parent) and x["titleMinus"] != None:
      dict[x["ID"]] = x["titleMinus"]
  return dict

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
