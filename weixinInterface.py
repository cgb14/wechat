# -*- coding: utf-8 -*-

import hashlib
import web
import lxml
import time
import os

class WeixinInterface:
	def __init__(self):
		print 'fuck'
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root,'templates')
		self.render = web.template.render(self.templates_root)
	def GET(self):
		#获取输入参数
		data = web.input()
		signature = data.signature
		timestamp = data.timestamp
		nonce = data.nonce
		echostr = data.echostr
		#自己的token
		token = "cgb157dnfcf953"
		#字典序排序
		list = [token,timestamp,nonce]
		list.sort()
		sha1 = hashlib.sha1()
		map(sha1.update,list)
		hashcode = sha1.hexdigest()
		#sha1加密算法
		
		#如果是来自微信的请求，则回复echostr
		if hashcode == signature:
			return echostr
	
	def POST(self):
		str_xml = web.data()#获得post来的数据
		xml = etree.fromstring(str_xml)#进行xml解析
		msgType = xml.find("MsgType").text
		fromUser = xml.find("FromUserName").text
		toUser = xml.find("ToUserName".text)
		if msgType == 'text':
			content = xml.find("Content").text
			return self.render.reply_text(fromUser,toUser,int(time.time()),content)
			if(content == u"天气"):
				pass
		elif msgType == 'image':
			pass
		else:
			pass