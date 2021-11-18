from urllib import request
import json
import random
import base64
import os
from git import Repo
import git
from packaging import version
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE_DIR_ENV = os.path.join(BASE_DIR, '.env')
XENPROJECT_ROOT_ENV = os.path.join(BASE_DIR, '..', '.env')

load_dotenv(BASE_DIR_ENV)
load_dotenv(XENPROJECT_ROOT_ENV)

LOCAL_REPO = os.getenv('LOCAL_REPO', os.path.join(BASE_DIR, '..', 'repo-local'))
REMOTE_REPO = os.getenv('REMOTE_REPO', os.path.join(BASE_DIR, '..', 'repo-remote'))
API_END_POINT=os.getenv('API_URL','http://z600')+":"+os.getenv('API_PORT','8000')

def get_url(url="{}/projects".format(API_END_POINT)):
	try:
		response = request.Request(url,headers={'User-Agent' : "Magic Browser"})
		read = request.urlopen(response).read()
		data = json.loads(read)
		return data
	except Exception as e:
		raise e

def check_project_available(url="{}/projects".format(API_END_POINT)):
	data = get_url(url)
	projects = data['detail']
	return projects

def check_project_execution(url="{}/executions".format(API_END_POINT)):
	data = get_url(url)
	exeution = data['detail'][0]
	return exeution

def check_project_requirement(url=None):
	if url is None:
		return "your field is null"
	response = get_url(url)
	content = response['content']
	data = base64.b64decode(content)
	data = json.loads(data)
	return data

def find_project(project_name=None):
	if project_name is None:
		return "your field is null"
	data = check_project_available()
	number_akhir = len(data)
	number_awal = 0
	output = None

	for number_awal in range(number_awal,number_akhir):
		jumlah = (number_awal+1)-1
		if project_name == data[jumlah]['projects_name']:
			#try:
			#	get_url_requirement = check_project_requirement(data[jumlah]['url_requirement'])
			#except Exception as e:
			#	return e
			output = {'url_git':data[jumlah]['projects_git_remoteurl'],'name':data[jumlah]['projects_name']}
			return output
		else:
			pass
	return output

def install_git_(url=None):
	print("this "+url)
	os.chdir('xen-project/')
	git.Git().clone(url)
	message = {'message':'your project had installed'}
	
	if url == None:
		return "your url is None"
	try:
		git.Git().clone(url)
		message = {'message':'your project had installed'}
		os.chdir('..')
	except Exception:
		message = {"message":"install failed"}
		os.chdir('..')
	
	return message

def install_git(url=None,name=None):
	directory = 'xen-project/{}'.format(name)
	os.chdir('xen-project/')
	if url == None:
		return "your url is None"
	if name == None:
		return "please input your project"
	try:
		Repo.clone_from(url, name)
		message = {'message':'your project had installed'}
		print("berhasil")
	except Exception:
		message = {"message":"install failed"}
		print("gagal")
		print(Exception)
	return message

def add_manifest(name_projecte=None,version_project=None,url=None):
	if name_projecte == None :
		return "please insert your name_projecte"
	if version_project == None :
		version = "0.1.0"
	if url == None:
		url = ""
	try:
		filename = 'manifest.json'
		with open(filename,'r') as data_file:
			data_json = json.loads(data_file.read())
		os.remove(filename)
		new_data={'name_projecte':name_projecte,'version_projecte':version_project,'url_projecte':url}
		data_json['installed_projecte'].append(new_data)
		with open(filename,'w') as data_file:
			json.dump(data_json, data_file)
	except Exception as e:
		return e

def del_manifest(name_projecte=None):
	try:
		filename = 'manifest.json'
		if name_projecte == None:
			return "please insert your project name"
		with open(filename,'r') as data_file:
			data_json = json.loads(data_file.read())
		number_akhir = len(data_json['installed_projecte'])
		number_awal = 0
		for number_awal in range(number_awal,number_akhir):
			jumlah = (number_awal+1)-1
			if name_projecte == data_json['installed_projecte'][jumlah]['name_projecte']:
				os.remove(filename)
				del data_json['installed_projecte'][jumlah]
				with open(filename,'w') as data_file:
					json.dump(data_json, data_file)
			else:
				pass
		return "project has deleted"
	except Exception as e:
		pass

def create_requirement(name_projecte=None,version_projecte=None,url_endpoint=None,requirement=None,comment=None,url=None):
	if comment is None:
		comment = "my projecte name is {name}".format(name=name_projecte)
	if requirement is None:
		requirement = "xenlib_core"
	if name_projecte==None:
		return "please insert name projecte"
	if version_projecte is None:
		version_projecte = "0.1.0"
	if url_endpoint is None:
		url_endpoint = {'url_endpoint':''.format(url=name_projecte),'type':'function'}
	else:
		url_endpoint = {'url_endpoint':url_endpoint,'type':'end_point'}
	data_json = {"name":name_projecte,
	"version": version_projecte,
	"requirement":requirement,
	"pip_library":[],
	"comment":comment,
	"type":url_endpoint['type'],
	"url":url,
	"url_endpoint":url_endpoint['url_endpoint']}
	filename = 'requirement.json'
	with open('projectes/{folder}/{filename}'.format(folder=name_projecte,filename=filename),'w') as data_file:
		json.dump(data_json, data_file)
	return "projecte has created"

def check_update_official():
	filename = 'manifest.json'
	with open(filename,'r') as data_file:
		data_json = json.loads(data_file.read())
	#return data_json
	number_akhir = len(data_json['installed_projecte'])
	number_awal = 0
	for number_awal in range(number_awal,number_akhir):
		jumlah = (number_awal+1)-1
		name_installed = data_json['installed_projecte'][jumlah]
		data_git = find_project(name_installed['name'])
		if version.parse(name_installed['version']) < version.parse(data_git['requirement']['version']):
			print("{name} update available {version}".format(name=name_installed['name'],version=data_git['requirement']['version']))
