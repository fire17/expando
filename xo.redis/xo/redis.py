# from xo import *
import time
import traceback
from unittest import skip
from expando import Expando
from redis import Redis as RedisClient
# xo = Expando()



from xo.xo import xo
# from expando



# from x import *
# import x

# import xo
import dill as pk

defaultRedisConfig = {
	"host" : "0.0.0.0",
	"port" : 6379,
}

# TODO: Get host and port from config / env / args
# Get host and port from argparser
def getArgs():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("--host", help="Redis host",
						default="localhost")
	parser.add_argument("--port", help="Redis port",
						default=6379)
	args = parser.parse_args()
	return args

host = getArgs().host
port = getArgs().port
# print("Redis host:", host, "port:", port)

def getArgsFromEnv(defaultHost = "localhost", defaultPort = 6379):
	import os
	host = os.getenv("REDIS_HOST", defaultHost)
	port = os.getenv("REDIS_PORT", defaultPort)
	return host, port

host, port = getArgsFromEnv(host, port)

class xoRedis(Expando):
	_rootName = "Redis"
	_host = host
	_port = port
	_db = 0
	_namespace = _rootName
	# def delete(self, id, *args,**kwargs):

	def _init_(self, *args,**kwargs):
		# print(" WILL INIT REDIS ", self._id, args, kwargs, " ON REDIS")
		if "host" in kwargs:
			self._host = kwargs["host"]
		if "port" in kwargs:
			self._port = kwargs["port"]

		self._namespace = self._rootName
		# if self._isRoot: # should work the same
		if self._parent is None:
			self._redis = RedisClient(host=self._host, port=self._port, db=self._db)

		self._pubsub = self._getRoot()._redis.pubsub()
		self._binded = False
		self._live = False



		# Init key on redis
		# return self
	
	def _overloading_(self, *args,**kwargs):
		# print(" WILL CHECK IF EXISTS ",  type(self), self._id, args, kwargs, " ON REDIS")
		return True

	def _checkIfExist_(self, *args,**kwargs):
		# print(" WILL CHECK IF EXISTS ", self._id, args, kwargs, " ON REDIS")
		# Check if key exits on redis
		res = self._getRoot()._redis.exists(self._id)
		# print(f"{self._id} EXISTS "+ str("!" if res else "no") +f" {res}")
		# print("___________________________________")
		# return True
		return res

	def _read_(self, *args,**kwargs):
		# print(" WILL READ ", self._id, args, kwargs, " ON REDIS")
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
		# print(" WILL CREATE ", self._id, value, args, kwargs, " ON REDIS")
		if value is None and self._valueArg in self:
			value = self[self._valueArg]
		
		# self._update_(value, *args,**kwargs)
		# will happen automatically
			
		# Create key on redis
	
	def _update_(self, value = None, *args,**kwargs):
		if value is None and self._valueArg in self:
			value = self[self._valueArg]

		# print(" WILL UPDATE ", self._id, value, args, kwargs, " ON REDIS")
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
		# print(" WILL SUBSCRIBE HERE TO ", self._id, args, kwargs, " ON REDIS")

		rootSubscribe = True
		rootSubscribe = False
		rootSubscribe = True
		# Global subscribe, only subscribe when root
		# print("iiiiiiiiii", self._id)
		if rootSubscribe and self._parent is None:
			self._redisSubscribe(key=self._namespace+"*", handler=self._directBind)
			pass
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
		idToDelete = self._id if element == None else self._id+"/"+element
		print(" ::: Deleting ",  idToDelete,element,  args, kwargs, f" from redis ::: db: {self._db} namespace {self._namespace}")
		target = self
		if element is not None:
			target = self[element]
		# Send empy bytes to indecate it was deleted
		# delete entire tree ? make option available
		target._setValue(bytes(), skipUpdate = False)
		r = self._getRoot()._redis
		r.delete(idToDelete)
		# print(" WILL DELETE ", id, args, kwargs, " FROM REDIS")
		# Delete key on redis

	# def redisSubscribe(self, key="xo/redis*", handler=lambda msg: print('XXXXXXXXXXXXHandler', msg), *args, **kwargs):

	def _redisSubscribe(self, key="Redis*", handler=lambda msg: print('XXXXXXXXXXXXHandler', msg), *args, **kwargs):
		# print("UUUUUUUUUUUUUUUUUUUUUUUU", key, handler, args, kwargs)
		# print("UUUUUUUUUUUUUUUUUUUUUUUU")
		# print("UUUUUUUUUUUUUUUUUUUUUUUU")
		# print("UUUUUUUUUUUUUUUUUUUUUUUU")
		# print(" ::: SUBSCRIBING TO REDIS CHANNEL", key, ":::", )
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
		# print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu", msg, args, kwargs)
		# time.sleep(1)
		if isinstance(msg, dict) and "type" in msg:
			if "message" in msg["type"]:
				# do_something with the message
				channel = msg["channel"].decode().replace(
					"/", ".")  # .strip("Redis.")  # .split(".")[-1]
				# if channel.startswith(xoRedis._rootName+"."):
				if channel.startswith(self._rootName+"."):
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
					# print("ggggg", channel)
					# f = self._GetXO(channel, allow_creation=False)
					# time.sleep(1)

					f = self
					# print("PRE", f._id, "channel:", channel)
					f = f[channel]
					# for c in channel.replace("/",".").split("."):
					# 	# if c not in f:
					# 	# 	f[c] = xo()
					# 	f = f[c]
					# print("POST",f._id)
					
					# print("ggggg2")

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
				# print(" ::: SUBSCRIBED TO CHANNEL", msg["pattern"])
				pass

try:
	_redis = xoRedis("redis", host=host, port=port)
	print(" ::: Connected to redis server on", _redis._host, ":", _redis._port, " :::")
except:
	traceback.print_exc()
	print(f"Could not connect to redis server, make sure it is running and accessible on {host}:{port}.\n You can also use --host and --port to specify the host and port of the redis server. ")
	_redis = None

redis = _redis
# def redis():
# 	return _redis

