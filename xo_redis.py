# from xo import *
import time
from unittest import skip
from xo import Expando
import redis
import dill as pk


class Redis(Expando):
	_rootName = "Redis"
	_host = "0.0.0.0"
	_port = 6379
	_db = 0
	_namespace = _rootName
	# def delete(self, id, *args,**kwargs):

	def _init_(self, *args,**kwargs):
		print(" WILL INIT REDIS ", self._id, args, kwargs, " ON REDIS")
		if self._parent is None:
			self._redis = redis.Redis(host=self._host, port=self._port, db=self._db)

		self._pubsub = self._getRoot()._redis.pubsub()
		self._binded = False
		self._live = False

		# Init key on redis
		# return self
	
	def _overloading_(self, *args,**kwargs):
		# print(" WILL CHECK IF EXISTS ",  type(self), self._id, args, kwargs, " ON REDIS")
		return True

	def _checkIfExist_(self, *args,**kwargs):
		print(" WILL CHECK IF EXISTS ", self._id, args, kwargs, " ON REDIS")
		# Check if key exits on redis
		res = self._getRoot()._redis.exists(self._id)
		print(f"{self._id} EXISTS "+ str("!" if res else "no") +f" {res}")
		print("___________________________________")
		# return True
		return res

	def _read_(self, *args,**kwargs):
		print(" WILL READ ", self._id, args, kwargs, " ON REDIS")
		# res =  str(self.value)+":FROM_REDIS"  if "value" in self else self
		r = self._getRoot()._redis
		res = r.get(self._id)
		try:
			res = pk.loads(res)
		except:
			print(" - - - COULD NOT UNPICKLE", self._id, ":::", res)
		self._setValue(res, skipUpdate = True)
		return res

		#return self to indicate that there was no change in value
		# res =  str(self.value)+":FROM_REDIS" # if "value" in self else self
		# print(res)
		return res
		# Read key on redis


	def _create_(self, value = None, *args,**kwargs):
		print(" WILL CREATE ", self._id, value, args, kwargs, " ON REDIS")
		if value is None and self._valueArg in self:
			value = self[self._valueArg]
		
		# self._update_(value, *args,**kwargs)
		# will happen automatically
			
		# Create key on redis
	
	def _update_(self, value = None, *args,**kwargs):
		if value is None and self._valueArg in self:
			value = self[self._valueArg]

		print(" WILL UPDATE ", self._id, value, args, kwargs, " ON REDIS")
		if value == self:
			value = self[self._valueArg]
		if value is not None:
			val = pk.dumps(value)
			r = self._getRoot()._redis
			res = r.set(self._id, val)
			r.publish(self._id, val)
			return True  # To continue with super() set
		return False
		# Update key on redis

	def _subscribe_to_changes_(self, *args,**kwargs):
		print(" WILL SUBSCRIBE HERE TO ", self._id, args, kwargs, " ON REDIS")

		rootSubscribe = True
		rootSubscribe = False
		# Global subscribe, only subscribe when root
		print("iiiiiiiiii", self._id)
		if rootSubscribe and self._parent is None:
			pass
			# self._redisSubscribe(key=_namespace+"*", handler=self._directBind)
		elif not rootSubscribe:
			# print("!!!!!!!!!!!!")
			# print("!!!!!!!!!!!!")
			# print("!!!!!!!!!!!!")
			# print("!!!!!!!!!!!!")
			# print(self._id)
			# print("!!!!!!!!!!!!")
			self._redisSubscribe(key=self._id, handler=self._directBind)
			# if self._getRoot()._live:
			# pass
		# also
		# TODO: consider subscribing only to specific id, to get notified for everyone
		# Subscribe to key on redis

	# def _delete_(self, *args,**kwargs):
	def _delete_(self, element=None, *args, **kwargs):
		idToDelete = self._id if element == None else element
		print(" WILL DELETE ",  idToDelete,  args, kwargs, " FROM REDIS")
		# print(" WILL DELETE ", id, args, kwargs, " FROM REDIS")
		# Delete key on redis

	# def redisSubscribe(self, key="xo/redis*", handler=lambda msg: print('XXXXXXXXXXXXHandler', msg), *args, **kwargs):

	def _redisSubscribe(self, key="Redis*", handler=lambda msg: print('XXXXXXXXXXXXHandler', msg), *args, **kwargs):
		# print("UUUUUUUUUUUUUUUUUUUUUUUU", key, handler, args, kwargs)
		# print("UUUUUUUUUUUUUUUUUUUUUUUU")
		# print("UUUUUUUUUUUUUUUUUUUUUUUU")
		# print("UUUUUUUUUUUUUUUUUUUUUUUU")
		print(" ::: SUBSCRIBING TO REDIS CHANNEL", key, ":::", )
		self._pubsub.psubscribe(**{key: handler})
		# pubsub.psubscribe(key = key, handler = handler)
		# pubsub.subscribe(subscribe_key)
		# pubsub.subscribe(key)
		# pubsub.subscribe(**{key: event_handler if handler is None else handler})
		# print("........00000")
		self._pubsub.run_in_thread(sleep_time=.00001, daemon=True)
		# for item in pubsub.listen():
		#     print(item, type(item))
		#     if item['type'] == 'message':
		#         print(item['data'])
		# print("DONE")

	# TODO: Also, implement option to lazy load, (set _needsUpdate or something like so)
	def _directBind(self, msg, *args, **kwargs):
		# print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
		# print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
		print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu", msg, args, kwargs)
		# time.sleep(1)
		if isinstance(msg, dict) and "type" in msg:
			if "message" in msg["type"]:
				# do_something with the message
				channel = msg["channel"].decode().replace(
					"/", ".")  # .strip("Redis.")  # .split(".")[-1]
				if channel.startswith(xoRedis._rootName+"."):
					channel = ".".join(channel.split(".")[1:])  # .split(".")[-1]
				# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", msg, args, kwargs)
				# return message
				# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
				# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", str(msg["channel"]).replace("/", "."))
				# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
				# msg["channel"].decode().replace("/", "."))
				# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", msg["data"])

				# EDIT 1
				# f = xo._GetXO(channel, allow_creation=True)
				if True:
					# f = self._GetXO(channel, allow_creation=False)
					f = self

					# f = xo[msg["channel"].decode().strip("xo/").replace("/", ".")]
					# f[channel] = msg["data"]
					# print("######  ", f)
					res = msg["data"]
					try:
						res = pk.loads(res)
						# print("try res:",res)
					except:
						print(" - - - COULD NOT UNPICKLE", self._id, ":::", res)

					f._setValue(res, skipUpdate=True)

				# f[self._valueArg] = res
				# f._updateSubscribers_(res)

				# print("######  ", f.value)
				# print("######  ", dict(f))
				# print(dict(f))
				# print("A@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",f)
				# print(">>>>>>>>>>>>>>>", msg["data"])
				# print(f._id, ":", dict(f))
				# print("<<<<<<<<<<<<<<<")
				# print()
			if msg["type"] == "subscribe":
				print(" ::: SUBSCRIBED TO CHANNEL", msg["pattern"])

class xoRedis(Expando):
	_rootName = "Redis"
	_host = "0.0.0.0"
	_port = 6379
	_db = 0
	_namespace = _rootName


	# def read(self, id, *args,**kwargs):
	# 	print(" WILL READ ", id, args, kwargs, " ON REDIS")

	# TODO: ADD DOC
	# TODO: check if db = "0" working instead of 0
	def __init__(self, _val=None, _id=None, _parent=None, _behaviors={},
              _host="0.0.0.0", _port=6379,
              _db=0, _namespace=_rootName,
              #  _live = False,
              *args, **kwargs):

		if _id is None:
			_id = xoRedis._rootName
		# TODO: Handle not connecting on load
		kwargs["_db"] = _db
		kwargs["_namespace"] = _namespace
		kwargs["_port"] = _port
		kwargs["_host"] = _host
		# kwargs["_live"] = _live
		# Expando.__init__(self, _val=_val, _id=_id, _parent=_parent,
		#                  _behaviors=_behaviors, _xoT_=xoRedis, *args, **kwargs)
		if _parent is None:
			self._redis = redis.Redis(host=_host, port=_port, db=_db)
		super().__init__(_val=_val, _id=_id, _parent=_parent,
                   _behaviors=_behaviors, _xoT_=xoRedis, *args, **kwargs)
		self._host = _host
		self._port = _port
		self._namespace = _namespace
		self._db = _db
		self._pubsub = self._getRoot()._redis.pubsub()
		self._binded = False
		self._live = False

		if _parent is None:
			pass  # self.disconnected @= self._tryReconnect

		# TODO: change _behaviors to simple overloads set,get,call
		# self._behaviors = {Expando.__call__: self._redisCall,
		# 			   Expando.__setattr__: self._redisSet}

		rootSubscribe = True
		rootSubscribe = False
		# Global subscribe, only subscribe when root
		print("iiiiiiiiii", self._id)
		if rootSubscribe and self._parent is None:
			self._redisSubscribe(key=_namespace+"*", handler=self._directBind)
		elif not rootSubscribe:
			# print("!!!!!!!!!!!!")
			# print("!!!!!!!!!!!!")
			# print("!!!!!!!!!!!!")
			# print("!!!!!!!!!!!!")
			# print(self._id)
			# print("!!!!!!!!!!!!")
			self._redisSubscribe(key=self._id, handler=self._directBind)
			# if self._getRoot()._live:
			# pass
		# also
		# TODO: consider subscribing only to specific id, to get notified for everyone
		# , _val = None, _id = None, _parent = None, _behaviors = {}

	# def rSub(self):
	# 	print("rrrrrrrrrr", self._id)
	# 	self._getRoot()._redisSubscribe(key=self._rootName+"*", handler=self._directBind)

	# def redisSubscribe(self, key="xo/redis*", handler=lambda msg: print('XXXXXXXXXXXXHandler', msg), *args, **kwargs):
	def _redisSubscribe(self, key="Redis*", handler=lambda msg: print('XXXXXXXXXXXXHandler', msg), *args, **kwargs):
		# print("UUUUUUUUUUUUUUUUUUUUUUUU", key, handler, args, kwargs)
		# print("UUUUUUUUUUUUUUUUUUUUUUUU")
		# print("UUUUUUUUUUUUUUUUUUUUUUUU")
		# print("UUUUUUUUUUUUUUUUUUUUUUUU")
		print(" ::: SUBSCRIBING TO REDIS CHANNEL", key, ":::", )
		self._pubsub.psubscribe(**{key: handler})
		# pubsub.psubscribe(key = key, handler = handler)
		# pubsub.subscribe(subscribe_key)
		# pubsub.subscribe(key)
		# pubsub.subscribe(**{key: event_handler if handler is None else handler})
		# print("........00000")
		self._pubsub.run_in_thread(sleep_time=.00001, daemon=True)
		# for item in pubsub.listen():
		#     print(item, type(item))
		#     if item['type'] == 'message':
		#         print(item['data'])
		# print("DONE")

	# TODO: Also, implement option to lazy load, (set _needsUpdate or something like so)
	def _directBind(self, msg, *args, **kwargs):
		if isinstance(msg, dict) and "type" in msg:
			if "message" in msg["type"]:
				# do_something with the message
				channel = msg["channel"].decode().replace(
					"/", ".")  # .strip("Redis.")  # .split(".")[-1]
				if channel.startswith(xoRedis._rootName+"."):
					channel = ".".join(channel.split(".")[1:])  # .split(".")[-1]
				# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", msg, args, kwargs)
				# return message
				# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
				# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", str(msg["channel"]).replace("/", "."))
				# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
				# msg["channel"].decode().replace("/", "."))
				# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", msg["data"])

				# EDIT 1
				# f = xo._GetXO(channel, allow_creation=True)
				f = self._GetXO(channel, allow_creation=True)

				# f = xo[msg["channel"].decode().strip("xo/").replace("/", ".")]
				# f[channel] = msg["data"]
				# print("######  ", f)
				res = msg["data"]
				try:
					res = pk.loads(res)
					# print("try res:",res)
				except:
					print(" - - - COULD NOT UNPICKLE", self._id, ":::", res)

				f._setValue(res, skipInner=True)

				# f[self._valueArg] = res
				# f._updateSubscribers_(res)

				# print("######  ", f.value)
				# print("######  ", dict(f))
				# print(dict(f))
				# print("A@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",f)
				# print(">>>>>>>>>>>>>>>", msg["data"])
				# print(f._id, ":", dict(f))
				# print("<<<<<<<<<<<<<<<")
				# print()
			if msg["type"] == "subscribe":
				print(" ::: SUBSCRIBED TO CHANNEL", msg["pattern"])

	# def _tryReconnect(self, *args, **kwargs):
	# 	self._redis = redis.Redis(host=self._host, port=self._port, db=self._db)
	# 	self._pubsub = self._redis.pubsub()
	# 	# TODO: do we need to resubscribe children ?

	def set(self, value, *args, **kwargs):
		if value is not None:
			val = pk.dumps(value)
			r = self._getRoot()._redis
			res = r.set(self._id, val)
			r.publish(self._id, val)
			return True  # To continue with super() set
		return False

	def get(self, *args, **kwargs):
		r = self._getRoot()._redis
		res = r.get(self._id)
		try:
			res = pk.loads(res)
		except:
			print(" - - - COULD NOT UNPICKLE", self._id, ":::", res)
		self._setValue(res)
		return res
		if value is not None:
			val = pk.dumps(value)
			r = self._getRoot()._redis
			res = r.set(self._id, val)
			r.publish(self._id, val)
			return True  # To continue with super() set
		return False

	# def _redisSet(self, name, value=None, *args, **kwargs):
	# 	if not self._binded:
	# 		# DONT SET VALUE BECAUSE YOU ARE SUBSCRIBED AND BINDED ANYWAY
	# 		self._binded = True
	# 		self[name]._setValue(value)
	# 	if value is None:
	# 		return self[name]._redisCall()
	# 	else:
	# 		return self[name]._redisCall(value)

	# def _redisSetX(self, name, value=None, *args, **kwargs):
	# 	# print("YYYYYYYYYYYYEEEEEEEEESSSSSSSSSSSet",self._id,name,value, args, kwargs)
	# 	self[name]  # double set to update (created, then update)
	# 	# if len (args) == 0 or value is None or name is None:
	# 	if value is None or name is None:
	# 		pass  # print("00000000000000", self._id, name, value, args, kwargs)
	# 	elif len(args) == 0:
	# 		# print("111111111111111111110", self._id, name, value, args, kwargs)
	# 		# res = self.__setattr__(*args, **kwargs)
	# 		redisID = self._id+"/"+name
	# 		kwargs["_skip_overload"] = True
	# 		# print(type(self),self)
	# 		self[name]._setValue(value)
	# 		self.__setattr__(name, value, *args, **kwargs)
	# 		res = self._redis.set(redisID, value)
	# 		# print("vvvvvvvvvvvv2",type(value),value)
	# 		# print(" ::: REDIS SET:", redisID, ":::", value)
	# 		self._redis.publish(redisID, value)
	# 		res = self._redis.get(self._id)
	# 		# print(f" ::: REDIS SET RESULTS: ({redisID})",
	# 			# ":::", res, ":::", self, ":::")
	# 		# self[args[0]]._setValue(res)
	# 		# print("RES", res)
	# 		# self.value = value
	# 		# print("ttt", name, value, self)
	# 		# self[name]._setValue(value)
	# 		# return res
	# 		# # print(" ::: REDIS GET:", self._id, args, kwargs)
	# 		# print(" ::: REDIS RESULTS:", res)
	# 		return value
	# 	else:
	# 		redisID = self._id+"/"+name
	# 		# print(" ::: REDIS SET !", redisID, args, kwargs)
	# 		res = self._redis.set(redisID, value)
	# 		self._redis.publish(redisID, value)
	# 		# self[args[0]].value = res
	# 		# print(" ::: REDIS RESULTS:", res)
	# 		self[name]._setValue(value)

	# 		# print(f" ::: REDIS SET RESULTS: ({redisID})",
	# 			# ":::", res, ":::", self, ":::")
	# 		# self.__setattr__(self,args[0], res, _skip_overload=True)# *args, **kwargs)
	# 		# *args, **kwargs)
	# 		self.__setattr__(name, value, _skip_overload=True)  # *args, **kwargs)
	# 		return value

	# def _redisCall(self, *args, **kwargs):
	# 	# print("YYYYYYYYYYYYEEEEEEEEESSSSSSSSSSSCCC",self._id, args, kwargs)
	# 	# print(" ::: REDIS SET CALL!", self._id, ":::", args, ":::", kwargs)
	# 	kwargs["_skip_overload"] = True
	# 	if len(args) == 0:
	# 		# print(" ::: REDIS GET CALL:", self._id, ":::", args, ":::", kwargs, ":::")
	# 		res = self._redis.get(self._id)
	# 		try:
	# 			res = pk.loads(res)
	# 		except:
	# 			print("COULD NOT UNPICKLE",self._id,":::",res)
	# 		# self._setValue(res)
	# 		# self.value = res
	# 		# self._updateSubscribers_(res)
	# 		# print(" ::: REDIS RESULTS:", res)
	# 		# print(f" ::: REDIS GET RESULTS: ({self._id})",":::", res, ":::")
	# 		if isinstance(res,bytes):
	# 			res = res.decode()
	# 		return res
	# 	else:
	# 		val = pk.dumps(args[0])
	# 		res = self._redis.set(self._id, val)
	# 		# res = self._redis.set(self._id, args[0])
	# 		# print("vvvvvvvvvvvv", type(value), value)
	# 		# print(args[0],type(args[0]))
	# 		self._redis.publish(self._id, val)
	# 		# print(" ::: REDIS RESULTS:", res)
	# 		if not self._binded:
	# 			self._setValue(args[0]) # DONT SET VALUE BECAUSE YOU ARE SUBSCRIBED AND BINDED ANYWAY
	# 			self._binded = True
	# 		# self._updateSubscribers_(args[0])
	# 		# print(f" ::: REDIS SET RESULTS: ({args[0]}, {self._id})",
	# 			# ":::", res,
	# 			#  ":::", self,
	# 			#   ":::")
	# 		return self


# Redis = xoRedis
# print("ooooooooooooo")
# subscribe(key='xo/redis/a/b/c', handler=lambda msg: print('Handler', msg))

# self.rsubscribe(handler=self.custom_handler)

# subscribe("xo/redis/a/b/c", handler=lambda msg: print(
#     " ::: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCCCCC CHANGED TO", msg))
# print("DONE!", str(xo.redis.a.b.c.value))
# for new_message in pubsub.listen():
#     custom_handler(new_message)
#     print("222")
# print()
# xo.redis.x.y.z("ZZZZZZZZ1")
# xo.redis.x.y.z = "ZZZZZZZZ2"
# print(xo.redis.x.y.z.value)
# print()
