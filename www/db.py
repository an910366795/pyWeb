#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-11 22:52:24
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

#数据库引擎对象
class _Engine(object):
	def __init__(self, connect):
		self.connect = connect
	def connect(self):
		return self.connect()
engine = None

#持有数据库的上下文对象
class _DbCtx(threading.local):
	def __init__(self):
		self.connect = None
		self.transactions = 0

	def is_init(self):
		return not self.connection is None

	def init(self):
		self.connection = _LasyConnection()
		self.transactions = 0

	def cleanup(self):
		self.connection.cleanup()
		self.connection = None

	def cursor(self):
		retrun self.connection.cursor()
_db_ctx = _DbCtx()		

