'''
Created by auto_sdk on 2016.04.13
'''
from base import RestApi
class PictureUserinfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'taobao.picture.userinfo.get'
