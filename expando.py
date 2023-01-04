#expando.py
# from datetime import datetime
# from multiprocessing import current_process
# from nis import match
# from operator import ne
from dataclasses import dataclass, asdict
import importlib
from threading import Thread
# importlib.reload(module)
import time
import os
import re
import json
from typing import OrderedDict
# import inspect

# from dill.source import getsource
# import dill
import traceback

asDaemons = False
# from .osCommands import *
# from osCommands import *

# class Expando(object):
# 	"""docstring for SelfNamed."""
# 	__id = "xxx"
# 	_hiddenAttr = ["_id", "_name", "_parent", "_val", "_zzz"]

# 	def __init__(self, id = None, val = None):
# 		super().__init__()
# 		pass #print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
# 		self.__id = id
# 		self[Expando._valueArg] = val
# 		#### self.arg = arg

# 	def __setattr__(self, name, value):
# 		pass #printXx("EEEEEEEEEEEEEEEEEEEE---1")


# 	def __assign__(self, v):
# 		pass #print('called with %s' % v)


# # TODO: improve
# # def getWatchablesForFormulaMock(func):
# # 	return ["name.first","name.last"]
# def getWatchablesForFormula(func):
# 	try:
# 		# dill.detect.code(func)
# 		print("###################")
# 		print(getsource(dill.detect.code(func)))
# 		print("###################")
# 		return getAllObjects(getsource(dill.detect.code(func)))
# 	except:
# 		print("$$$$$$$$$$$$", getsource(func))
# 		return getAllObjects(getsource(func))
# 		print("$$$$$$$$$$$$")
# 	#TODO: fix for lambda in interpreter

# 	reg = r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
# 	return re.search(reg, getsource(func)).groups()


def getAllObjects(given):
	given = given.split('<<=')[-1]
	regex = re.compile(r'(?P<xo>xo(\.\w+)*)')
	# regex = re.compile(r'(?P<name>xo.name\.[a-zA-Z]+)')
	# regex = re.compile(r'\\w+(?:\\.\\w+)+')

	def removeHiddenAtEnd(s):
		print("st1", s)
		end = s.split('.')[-1]
		if not end.startswith('_'):
			return s
		else:
			return removeHiddenAtEnd('.'.join(s.split('.')[:-1]))

	return [removeHiddenAtEnd(x[0].lstrip("xo.")) for x in re.findall(regex, given)]


class Expando(dict):
# class Expando(dataclass(OrderedDict)):
# class Expando(OrderedDict):
	"""docstring for Expando."""
	_hiddenAttr = ["value", "_val", "getattr", "_recursiveImportDict"
				"show", "_id", "__dict__", "startswith","delete"]
	_rootName = "xo"
	_valueArg = "value"

	_id = "_xxx_"

	# def __assign__(self, v):
	# 	print('called with %s' % v)

	#### def __init__(self, val, id = None):
	#### 	super().__init__(id = id)
	#### 	self.__id = id


#### 	def __init__(self, val = "__17__", id = None, **entries):####, wrapper = False, main = True):
#### #### ####expando.py
#### #### 		#### def __init__(self):
#### #### 		#### es=traceback.extract_stack()
#### #### 		super().__init__(id = id)
#### #### 		self.name = self.GetName()
#### #### 		self.__dict__.update(entries)
#### #### 		self.__validID_ = False
#### #### 		#### global GD
#### #### 		#### self.xxx = self.get_my_name()
#### #### 		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@",mod_retrieve_name(self))
#### 		super().__init__(id = id)
####
#### 		exist = True
#### 		'''
#### 		birth = str(time.time())
#### 		if id is None:
#### 			id = birth
#### 		'''
####
#### 		#### self.__main__ = main
#### 		self.__id__ = "hidden"
#### 		self.__dict__.pop("__id__")
#### 		self[Expando._valueArg] = val
#### 		print("obj created! =",self[Expando._valueArg])
#### 		#### self._zzz = 5
####
####
####
####
#### 		#### print("******---",self.get_my_name())
#### 		#### self["_id"] = self.get_my_name()[0]
####
#### 		#### self.xxx.yyy.zzz = 13
#### 		#### updateID = Thread(target = self.makeID, args = [list,])
#### 		#### updateID.start()
####
#### 		print("AAAAAAAAAAA	AAA",entries,self.__name__)
#### 		for arg_name in entries:
#### 			print("AAAAAAAAAAAAA",arg_name)

	def tree(self):
		for a in self:
			if not a.startswith("_") and a not in Expando._hiddenAttr:
				yield self[a]
				if self[a] != None:
					for z in self[a].tree():
						yield z

	# def subscribe(self, func = None, autoPub = None, block = False, once= False, echo=True, debug = False, withID = False):
	# 	if func is None:
	# 		func = lambda a, *aa, **aaa : [a,aa,aaa]
	# 		withID = True
	# 	channel = self._id.replace(".","/")
	# 	# print("CCCCCCCCCCCCCCCCCC",channel)
	# 	return xo.subscribe(channel, func=func, autoPub = autoPub, block = block, once= once, echo=echo, debug = debug, withID = withID)
	def _recursiveImportDict(self, d):
		# print(self._id)
		[self[a]._recursiveImportDict(d[a]) if isinstance(
			d[a], dict) else self[a]._setValue(d[a]) if True else None for a in d]
			# d[a], dict) else self.__setattr__(a,d[a]) if True else None for a in d]
			# d[a], dict) else self[a](d[a]) if True else None for a in d]
		# for a in d:
		# 	if isinstance(d[a], dict):
		# 		# d[a] = Expando(d[a])
		# 		self[a].recursiveImportDict(d[a])
		# 	else:
		# 		self[a] = d[a]
		return self

	def fill(self,inputs):
		return self._recursiveImportDict(inputs)

	def _benchmarkChildren(self, level = 1, timeLimit = 10):
		print("BENCHMARKING Children Level:", level,"::: Time limit", timeLimit,"seconds","::: ID:", self._id)
		count = 1
		target = self
		for c in range(level):
			target = target["level"+str(c)]
		start = time.time()
		while time.time() - start < timeLimit:
			target["level_"+str(count)] = count
			count += 1
		end = time.time()
		print("BENCHMARK Children Level:", level, "::: Created ", count, "::: In", end - start,"seconds")
		print(self)
	def _benchmarkSet(self, level = 0, timeLimit = 10):
		print("BENCHMARKING Set:", level, timeLimit)
		count = 0
		target = self
		for c in range(level):
			target = target["level"+str(c)]
		start = time.time()
		while time.time() - start < timeLimit:
			target.value = count
			count += 1
		end = time.time()
		print("BENCHMARK Set Level:", level,"::: Count", count, "::: In", end - start,"seconds")
		print(self)

	# def xfill(self, inputs):
	# 	index = {}
	# 	for z in self.tree():
	# 		if z._name in inputs:
	# 			inputs.remove(z._name)
	# 			print("enter", z._name+": ")
	# 			if "/" in z._id:
	# 				si = len(self._id)
	# 				index[z._id[si:]] = input()
	# 	for a in index.keys():
	# 		self[a] = index[a]
	# 	print("\nDONE")

	# def kids(self):

	# 			for a in self:
	# 				if not a.startswith("_") and a not in Expando._hiddenAttr:
	# 					yield self[a]

	# def children(self):
	# 	# childs = []
	# 	childs = {}
	# 	for a in self:
	# 		if not a.startswith("_") and a not in Expando._hiddenAttr:
	# 			# childs.append(self[a])
	# 			childs[a]=self[a]
	# 	return childs

	def reloadImport(self, module):
		return importlib.reload(module)

# 	def __init__(self, val = None, id = None, main = True, parent = None, **entries):####, wrapper = False, main = True):
# 	####expando.py
# 		#### def __init__(self):
# 		#### es=traceback.extract_stack()
# 		# super().__init__(id = id, val = val)
# 		super().__init__()
# 		pass #print("PPPPPPPPPPPPPP", id)
# 		#### self.name = self.GetName()

# 		self.__dict__.update(entries)
# 		if id is None:
# 			id = Expando._rootName
# 		self._name = id.split("/")[-1]
# 		self._id = id
# 		# self._birth = datetime.now()

# 		# self.__id = id
# 		# # print("........")
# 		# super().__init__(val=val, id=id)
# 		# # print("........ddd")

# 		# self.__id = id
# 		self._isRoot = False
# 		if parent is None:
# 			self._isRoot = True
# 		self._parent = parent
# 		#### self.__validID_ = False
# 		#### global GD
# 		#### self.xxx = self.get_my_name()
# 		#### print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@",mod_retrieve_name(self))
# 		exist = True
# 		'''
# 		birth = str(time.time())
# 		if id is None:
# 			id = birth
# 		'''

# 		self._subscribers = []
# 		# self._triggers = []


# 		#### self.__main__ = main
# 		self.__id__ = "hidden"
# 		self.__dict__.pop("__id__")
# 		self[Expando._valueArg] = val
# 		# print("obj created! =",self[Expando._valueArg])
# 		self._zzz = 5
# 		#### print("******---",self.get_my_name())
# 		#### self["_id"] = self.get_my_name()[0]

# 		#### self.xxx.yyy.zzz = 13
# 		#### updateID = Thread(target = self.makeID, args = [list,])
# 		#### updateID.start()

# 		# print("AAAAAAAAAAA	AAA",entries,self.__name__)
# 		for arg_name in entries:
# 			pass #print("AAAAAAAAAAAAA",arg_name)


# # 		# Binding the object to the value
# #		# global manager
# # 		# self._manager = manager
# # 		# self[Expando._valueArg] = manager.bind(self.__id, val, ref=[self])

	def __hash__(self):
		pass  # print(hash(str(self)))
		return hash(str(self))

	def getID(self):
		return self.__id__

	def __xset__(self, key, val):
		pass
		# print("eeeeeeeeeeeeeeeeeeeee")
		self.__dict__[key] = val
		return True

	def __xget__(self, key):
		pass
		print("eeeeeeeeeeeeeeeeeeeeeaaa")
		return self.__dict__[key]

	# def __setattr__(self, name, value):
	# 	pass ## print("EEEEEEEEEEEEEEEEEEEE1")
	# 	if "str" not in str(type(name)):
	# 		name = str(name)
	# 	if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr:#### and "__skip" in self.__dict__ and name not in self.skip:
	# 		if "Expando" not in str(type(value)):
	# 			pass ## print("_____________________",str(type(value)))
	# 			if name not in self.__dict__:
	# 				pass ## print("2222222222")
	# 				# print("ppp33333",self._id)
	# 				# self[name] = obj(id = self._id+"/"+name, val= value, parent = __objManager.getXO(self._id))
	# 				self[name] = Expando(id = self._id+"/"+name, val= value, parent = self)
	# 			else:
	# 				pass ## print("33333333")
	# 				#### self.__set__(name,value)
	# 				#### self.save(id = self._id+"/"+name, val= value)
	# 				# if data binding
	# 				# manager.save(channel = self._id+"/"+name, data=value)
	# 				self[name][Expando._valueArg] = value #?????
	# 				self[name]._updateSubscribers_(value)
	# 		else:
	# 			pass ## print("44444")
	# 			self.__dict__[name] = value

	# 	else:
	# 		pass ## print("555555555")
	# 		self.__dict__[name] = value

	# def keys(self):
	# 	print("keysssss",self._id)
	# 	res = [*super().keys()]
	# 	if self[Expando._valueArg] is None:
	# 		res.remove(Expando._valueArg)
	# 	return res
	# 	return self.keys()

	def __xgetitem__(self, name):
		print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
		if "str" not in str(type(name)):
			name = str(name)
		elif name == "value":
			# name = "_val"
			atr = object.__getattribute__(self, name)
			# return atr[0]
			return atr

		if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr and name not in self.__dict__:
			# print("ppp44444")
			#EX1
			self.__dict__[name] = self._xoT_(
				_id=self._id+"/"+name, _parent=self, _behaviors=self._behaviors)

		if name in self.__dict__:
			#### print("FUUCKKKKKKKKKKKKKKKKKKKKKk")

			item = self.__dict__[name]
			return item

			atr = object.__getattribute__(self, name)
			return atr

	def __assign__(self, v):
		print('called with %s' % v)

	def __xsetitem__(self, name, value):
		pass  # print("iiiiiiiiiiiiiiiiioooooooo")
		if "str" not in str(type(name)):
			name = str(name)
		# and "__skip" in self.__dict__ and name not in self.skip:
		if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr:
			pass  # print("VVVVVVVV",str(type(value)))
			if "Expando" not in str(type(value)):
				pass  # print("_____________________",str(type(value)))
				if name not in self.__dict__:
					pass  # print("1",name)
					# print("ppp5555",self)
					#EX2
					self.__dict__[name] = self._xoT_(
						_id=self._id+"/"+name, _val=value, _parent=self, _behaviors=self._behaviors)
				else:
					pass  # print("2",name)
					self[name].set(value)
			else:
				pass  # print("22222222222222222222222",name,value)
				self.__dict__[name] = value
				pass  # print("YESSSSSSSSS",	self.__dict__[name])
		else:
			pass  # print("3",name)
			self.__dict__[name] = value

		#### print("FINISHED SETTING ITEM", self.__dict__)

	def __xgetattribute__(self, name, loop=True):
		# print("NAME:",name)
		# time.sleep(0.1)
		if "str" not in str(type(name)):
			name = str(name)
		elif name == "value":
			# print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
			# name = "_val"
			atr = object.__getattribute__(self, name)
			# return atr[0]
			return atr
		atr = object.__getattribute__(self, name)
		return atr

	# def __getattr__(self, name, loop = True):
	# 	print("getttt")
	# 	if "str" not in str(type(name)):
	# 		name = str(name)
	# 	#### return name
	# 	if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr and name not in self.__dict__:
	# 		pass #print("OOOOO_ooooooooooooooooooooo",name)####,self.__dict__)
	# 		pass #print("aaaaaaaaaaaaaa")
	# 		# print("ppp66666",self)
	# 		# self[name] = obj(id = self._id+"/"+name, parent = self)
	# 		self[name] = self._xoT(id = self._id+"/"+name, parent = self)
	# 		return self[name] #?
	# 	if name in self.__dict__:
	# 		pass #print("bbbbbbbbbbbbbbb")
	# 		atr = object.__getattribute__(self, name)

	# 		return atr
	# 	#### return 13
	# 	pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	# 	pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	# 	pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	# 	pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	# 	pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	# 	pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$xxxxxxxxxxxx")

	def _setValue(self, val, skipUpdate=False):
		# print(self._id, " SETTING VALUE TO " + str(val))
		
		if isinstance(val, dict):
			# self._recursiveImportDict(_val)
			Expando._recursiveImportDict(self, val)
			# self._recursiveImportDict(_val)
			val = None

		if True or skipUpdate or self.set(val):
			# set hook
			if skipUpdate:
				self.__setitem__(Expando._valueArg, val, skipUpdate=True)
			else:
				self[Expando._valueArg] = val

			object.__setattr__(self, "value", val)


			
			# if name == Expando._valueArg:
			# 				self[name] = value
			# 				self[name] = value
			# 			else:
			# 				print("........")
			# 				#final .x =
			# 				self[name] = self._xoT(id=self._id+"/"+name, val=value, parent=self)
			# 				object.__setattr__(self, name, self._xoT(
			# 					id=self._id+"/"+name, val=value, parent=self))
			self._updateSubscribers_(val)
		# print(self)

	def __xgetstate__(self):
		pass  # printX ("I'm being pickled")
		pass  # print(self.__dict__)
		pass  # print()
		return False

	def __xsetstate__(self, d):
		pass  # pprintX ("I'm being unpickled with these values:", d)
		self.__dict__ = d
		#### self[Expando._valueArg] *= 3

	def __xiter__(self):
		for a in self.__dict__:
			print("ITER", a)

			def x():
				print("xxxxxxxxxxxx")

			# if not a.startswith("_"):# and a not in Expando._hiddenAttr:
			# 	res = self[a]
			# 	if "Expando" in str(type(res)):
			# 		yield res.__iter__()
			# 	yield (a, res)
	# def default(self, o):
	# 	return o.__dict__  

	def keys(self = None):
		# keys = super().keys()
		if self == None:
			return []
		keys = self.__dict__.keys()
		return list(filter(lambda k: not k.startswith("_"), keys))
		# return [k for keys if not a.startswith("_"):  # and a not in Expando._hiddenAttr]

	# def __dict__(self):
	# 	return {k: v for k, v in list(filter(lambda i: not i[0].startswith("_") and i[0] not in self._hiddenAttr, dict(super()).items()))}
	# 	for k in self.keys():
	# 		if not k.startswith("_") and k not in self._hiddenAttr:
	# 			yield k

	def __iter__(self):
		for k in self.keys():
			if not k.startswith("_") and k not in self._hiddenAttr:
				yield k
				# print(f"ITER :{k}:")
		# return iter(self.__dict__)
		# print("ITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
		# return self.kids()

	def _getRoot(self):
		if self._parent is not None:
			return self._parent._getRoot()
		return self

	def _GetXO(self, get="", allow_creation=False, getValue=False, follow=None):
		# print("GGGGGGGGGGGGGGGGGetXO", self._id, get, getValue)
		# if "None" not in str(type(self._parent)):
		if not self._isRoot:
			# get = ".".join(self._id.replace("/",".").split(".")[1:] + get.split("."))
			return self._getRoot()._GetXO(get, allow_creation, getValue, follow)
		# print(";;@;;;;;",self._id, get)

		final = self
		# print("FFFFFFFFFFFFFFF")
		# print("FFFFFFFFFFFFFFF")
		# print("FFFFFFFFFFFFFFF",self._id)
		# print(final, final._id)
		for child in get.split("."):
			# print("tttccccchild, final",child, final._id)
			# if child not in final:
				# final[child]
			final[child] = self._xoT_(_id=final._id+"/"+child,
							 _parent=final, _behaviors=final._behaviors)
			# else:
			final = final[child]
		# print(final,final._id)
		# print("FFFFFFFFFFFFFFF")
		# print("FFFFFFFFFFFFFFF")
		# print("FFFFFFFFFFFFFFF")
		return final

	def _updateSubscribers_(self, *v, **kw):
		# for trigger in self._triggers:
		# 	#TODO: in new thread
		# 	trigger()
		# xo.a.<s>.a = 3
		for sub in self._subscribers:
			#TODO: in new thread
			# print(sub)
			# print("&&&",self[Expando._valueArg], sub)
			# print("***************")
			# print(sub(*v, **kw))
			kw["_xo"] = self
			kw["_id"] = self._id
			sub(*v, **kw)
			# sub(*v, **kw)
		# print("................")
		# print(self)
		# print("................")

	# def subscribe(self, func = None, autoPub = None, block = False, once= False, echo=True, debug = False, withID = False):
	# , autoPub = None, block = False, once= False, echo=True, debug = False, withID = False):
	def subscribe(self, funcOrXo=None):
		print(" ::: Subscribing to", self._name)
		# print("SSSSSSSSSSSSSSS",self, funcOrXo)
		if funcOrXo is None:
			# print("XxxxxxX")
			funcOrXo = lambda a, *aa, **aaa: [a, aa, aaa]
			# withID = True
		# else:
		# print("ffffffffff", funcOrXo)
		if funcOrXo not in self._subscribers and funcOrXo not in self._subscribers:
			self._subscribers.append(funcOrXo)
			# if "function" in str(type(funcOrXo)):
			# 	self._triggers.append(funcOrXo)
			# elif "Expando" in str(type(funcOrXo)):
			# 	self._subscribers.append(funcOrXo)
			# 	pass
		# return self


	def _delete(self, __name: None):
		if __name is None:
			# Call the overloaded delete function
			self._delete_(element=self._id)

			del (self)
		else:
			return self.__delattr__(__name)

	def __delattr__(self, __name: str) -> None:
		# Call the overloaded delete function
		if self._overloading_():
			self._delete_(element=__name)


		if __name in self:
			final = self.pop(__name)
			# self._updateSubscribers_()
			self.__dict__.pop(__name)
			# self.__delattr__(__name)
			# self.__delitem__(__name)
			# return final
		# return super().__delattr__(__name)
		# return self

	# lambda x: x@xo
	def __matmul__(self, other):
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
		print("@@@@@@@@   matmul  @@@@@@@")
		print("@@@@@@@@     x     @@@@@@@")
		print("@@@@@@@@     x     @@@@@@@")
		print("@@@@@@@@           @@@@@@@", type(other))
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@", other)
		if "value" in self:
			if "function" in str(type(self.value)) or "method" in str(type(self.value)):
				return self.value(*other)
		return self

	def __rmatmul__(self, other):
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
		print("@@@@@@@@  rmatmul  @@@@@@@")
		print("@@@@@@@@           @@@@@@@")
		print("@@@@@@@@           @@@@@@@")
		print("@@@@@@@@           @@@@@@@", type(other))
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@", other)
		self._setValue(other)
		# if "tuple" in str(type(other)):
		# 	res = None
		# 	for func in other:
		# 		res = self.subscribe(func)
		# 	return res
		# return self.subscribe(other)

	# xo.trigger @= lambda Subscribe to changes
	def __imatmul__(self, other):
		# print("@= @@@@@@@@@@@@",other)
		if "tuple" in str(type(other)):
			res = None
			for func in other:
				res = self.subscribe(func)
			# return res
		else:
			self.subscribe(other)
		# print("@= @@@@@@@@@@@@",other)
		return self.value

	# def _lastUpdatedNow(self):
	# 	self._lastUpdated = time.time()
	def _runFormula(self):
		if True or "formula" in self:
			if self._lastUpdated == self._lastLoaded:
				return self[Expando._valueArg]
				# return self.formula.currentValue
			else:
				# formula = self.formula[Expando._valueArg]
				# newValue = formula()
				newValue = self.formula()
				# self.formula.currentValue = newValue
				# self[Expando._valueArg] = newValue
				# self = newValue
				self._lastLoaded = self._lastUpdated
				# print("xxxxxxxx", self, formula, getsource(formula))
				print(" ::: RUNNING FORMULA ", self._id, ":::", newValue, ":::")
				# print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				# print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				# print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				self._setValue(newValue)
				# print("=========-",newValue)

				return newValue
		return None

	# xo.form <<= Formula
	def __ilshift__(self, formula):
		# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		# print(formula)
		self.formula = formula
		self._lastLoaded = time.time()
		# not matching same time on purpose -> will trigger fetch
		self._lastUpdated = time.time()
		# self.currentValue = formula()
		# self[Expando._valueArg] = currentValue
		# print("@@@@@@@@@ expando?",type(self))

		# self._setValue(lambda : self._runFormula())
		# self()

		# self[Expando._valueArg] = lambda : self._runFormula()
		# self.formula = lambda : self._parent()
		# self[Expando._valueArg] = lambda : self._parent() if self._lastUpdated == self._lastLoaded else runFormula(self.formula)
		# setValue(self, currentValue)
		# self = lambda : self[Expando._valueArg] if self._lastUpdated == self._lastLoaded else self._formula()

		def setLastUpdated(xobject):
			# print("!!!! UUUUUUUUUUUUUUUU", xobject)
			xobject._lastUpdated = time.time()
			if xobject._subscribers != None and len(xobject._subscribers) > 0:
				xobject()

		keys = getWatchablesForFormula(formula)
		# print("keys",keys)
		for key in keys:
			#TODO: remove after xo[longKey] is working
			# check = key
			# def getLast(xobj, path):
			# 	if "." in path:
			# 		return getLast(xobj[path.split(".")[1]], ".".join(path.split(".")[1:]))
			# 	else:
			# 		return xobj[path]
			# xobject = getLast(xo,key)
			print("LLLLLLLLLLLLLLL", key)

			xobject = self._GetXO(key)
			# print("LLLLLLLL",xobject._id,":::::",xobject)

			# self._lastUpdated = time.time()
			xobject @= lambda *args, **kw:  setLastUpdated(self)
		self._runFormula()
		return self
		# return self

	def __eq__(self, other):
		# print()
		# print("!!!!" , other)
		if Expando._valueArg in self and self[Expando._valueArg] == other:
			# print("#######")
			return True
		# print("$$$$$$$$$$")
		# return self
		return super().__eq__(other)

	# def __is__(self, other):
	# 	return self.__eq__(other)

	# def __and__(self, other):
	# 	return self & other

	# def __or__(self, other):
	# 	return self | other

	# def __contains__(self, key):
	# 	return key in self.__dict__

	def __xor__(self, other):
		return self ^ other

	def __invert__(self, other):
		return ~self[Expando._valueArg]

	def __lshift__(self, other):
		return self << other

	def __rshift__(self, other):
		return self >> other

	def __bool__(self):  # , other == None):
		# print("__bool__ ",self._id)
		return bool(self[Expando._valueArg])

	# def __abs__(self, other):
	# 	return abs(self[Expando._valueArg])

	# def __abs__(self, other):
	# 	return abs(self[Expando._valueArg])

	#### by value of main
	# def __eq__(self, other):
	# 	if type(self[Expando._valueArg]) is not list:
	# 		return None == other
	# 	if "bool" in str(type(other)) and ("bool" in str(type(self[Expando._valueArg])) or (self[Expando._valueArg] is not None and ("dict" in str(type(self[Expando._valueArg][0])) or "dict" in str(type(self[Expando._valueArg][0])) )and len(self[Expando._valueArg]) > 0 and "bool" in str(type(self[Expando._valueArg][0])))):
	# 		return self[Expando._valueArg][0] == other
	# 	if self.__isObj(other):
	# 		return self[Expando._valueArg][0] == other[Expando._valueArg][0]
	# 	elif "str" in str(type(other)):
	# 		return str(self[Expando._valueArg][0]) == other
	# 	return self[Expando._valueArg][0] == other
	# def __cmp__(self):
	# 	print("$$$$$$$$$$$$$$$$$$$$$$")
	# 	return self[Expando._valueArg]

	def __ge__(self, other):
		# TODO: Check if "value" in
		if type(other) is Expando:
			return self[Expando._valueArg] >= other[Expando._valueArg]
		return self[Expando._valueArg] >= other

	def __gt__(self, other):
		# if self.__isObj(other):
		if type(other) is Expando:
			return self[Expando._valueArg] > other[Expando._valueArg]
		return self[Expando._valueArg] > other

	def __le__(self, other):
		# if self.__isObj(other):
		if type(other) is Expando:
			return self[Expando._valueArg] <= other[Expando._valueArg]
		return self[Expando._valueArg] <= other

	def __lt__(self, other):
		# if self.__isObj(other):
		if type(other) is Expando:
			return self[Expando._valueArg] < other[Expando._valueArg]
		return self[Expando._valueArg] < other

	def __iadd__(self, other):
		res = self()+other
		# print("rrrrr",res)
		self._setValue(res)
		# self[Expando._valueArg] = self[Expando._valueArg] + other
		return res
		

	def __add__(self, other):
		if self[Expando._valueArg] is None:
			return other
		matchWith = other
		if self.__isObj(other):
			matchWith = other[Expando._valueArg]
			# print("$$$$$$$$$$$$$$$$$$$$$$1")
			# return self[Expando._valueArg] + other[Expando._valueArg]
		# if str(type(other)) != str(type(self[Expando._valueArg][0])):
		# 	if "list" not in str(type(other)):
		# 		other = [other]
		# 	if "list" not in str(type(self[Expando._valueArg][0])):
		# 		self[Expando._valueArg][0] = [self[Expando._valueArg][0]]
		# 	return self[Expando._valueArg][0] + other
		return type(matchWith)(self[Expando._valueArg]) + matchWith

	def __radd__(self, other):
		if self[Expando._valueArg] is None:
			return other
		matchWith = other
		if self.__isObj(other):
			print("$$$$$$$$$$$$$$$$$$$$$$2")
			matchWith = other[Expando._valueArg]
		# if str(type(other)) != str(type(self[Expando._valueArg][0])):
		# 	if "list" not in str(type(other)):
		# 		other = [other]
		# 	if "list" not in str(type(self[Expando._valueArg][0])):
		# 		self[Expando._valueArg][0] = [self[Expando._valueArg][0]]
		# 	return other + self[Expando._valueArg][0]
		return matchWith + type(matchWith)(self[Expando._valueArg])

	def __len__(self):
		return len(self.keys())


	def __pos__(self, other):
		#### # print("!!!!!!!!!")
		#### # print(type(other))
		#### # print()
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] + other

	def __sub__(self, other):
		#### print("!!!!!!!!!")
		pass  # print(type(other))
		pass  # print()
		if self.__isObj(other):
			return self[Expando._valueArg] - other[Expando._valueArg]
		elif "str" in str(type(other)):
			pass  # print("::::::::::::::xxxx:::::::::")
			return str(self[Expando._valueArg]) - other
		return self[Expando._valueArg] - other

	def __rsub__(self, other):
		pass  # print(type(other))
		pass  # print()
		if self.__isObj(other):
			return other[Expando._valueArg] - self[Expando._valueArg]
		elif "str" in str(type(other)):
			# print("::::::::::::::xxxx:::::::::")
			return other - str(self[Expando._valueArg])
		return other - self[Expando._valueArg]

	def __truediv__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] / other

	def __rtruediv__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return other / self[Expando._valueArg]

	def __floordiv__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] // other

	def __rfloordiv__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return other // self[Expando._valueArg]

	def __mod__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] % other

	def __rmod__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return other % self[Expando._valueArg]

	def __pow__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] ** other

	def __rpow__(self, other):
		return self.__mul__(other)
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] ** other

	def __mul__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] * other

	def __rmul__(self, other):
		return self.__mul__(other)
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] * other

	def __div__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] / other

	def __rdiv__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return other / self[Expando._valueArg]

	def __neg__(self):
		return -self[Expando._valueArg]
		#### print("!!!!!!!!!")
		#### print(type(other))
		#### print()
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return self[Expando._valueArg] + other

	def __isObj(self, o):
		#### print("################################################################################################################",str(type(o)))
		#### time.sleep(100)
		pass  # print("@@@@@@@@@@@@@@@@@@@@@@asdasdasd")
		return isinstance(o, Expando)  # "Expando" in str(type(o))
		# return "Expando" in str(type(o))

	def _inThread(self, data):
		target, vars, kwargs = data
		# print(" ::: Running Async Thread ::: ",target.__name__,"::: with params:\n :::",vars,str(kwargs).replace("'","").replace("}","").replace(":","=").replace("{",""))
		# print()
		return target(*vars, **kwargs)

	def _startThread(self, target, *vars, **kwargs, ):
		sT = Thread(target=self._inThread, args=[[target, vars, kwargs]])
		if asDaemons:
			sT.daemon = True ############### DAEMON XO 
		sT.start()

	def __call__(self, *args, **kwargs):
		# print(Expando.__call__ in self._behaviors)
		# print("CCCCCCCCCCCCC",self._id, self.value,args,kwargs)
		# behave = False
		# if behave:
		# 	if "_skip_overload" not in kwargs or kwargs["_skip_overload"] == False:
		# 		return self._behaviors[Expando.__call__](*args, **kwargs) \
		# 			if Expando.__call__ in self._behaviors \
		# 				else self.__call__(_skip_overload = True,*args, **kwargs);

		# kwargs.pop("_skip_overload") if "_skip_overload" in kwargs else 0
		# for a in vars:
		# 	print(type(a),"AAAAAAAAAAAAAAA,", a)
		# for a in kwargs:
		# 	print(type(kwargs),type(a),"KKKKKKKKK,", a,"=", kwargs[a])
		# print(type(vars),type(*vars),"xxxxxxxxAAAAAAAAAAAAAAA,", vars)

		if "fetch" in kwargs and kwargs["fetch"] == True and self._overloading_():
			print("xxxxxxx FFFFFFFFFFFFFFFFFFFFFFF fetching")
			read = self._read_()
			kwargs.pop("fetch")
			if read != self:
				value = read
				self._setValue(value)

		if self._id.endswith("learn"):
			newDict = {}
			appendToLearn = []
			for f in args:
				if f is not None and "function" in str(type(f)):
					ap = str(f).split(' ')[1]
					newDict[ap] = f
				elif "list" in str(type(f)):
					for ff in f:
						if ff is not None and "function" in str(type(ff)):
							ap = str(f).split(' ')[1]
							newDict[ap] = ff
				elif "dict" in str(type(f)):
					for fkey in f:
						if f[fkey] is not None:
							newDict[fkey] = f[fkey]
				else:
					appendToLearn.append(f)

			# selff = xo._GetXO(self._id)

			# print( f"Learning new trick {self}{str(self._id+" ").split(" ")[1] } yo")
			owner = "/".join(self._id.split("/")[:-1])+"/"

			for key in newDict:
				# print(owner,",,,",key)
				v = newDict[key]
				if "function" in str(type(v)):
					print(f" ::: Learning new trick {owner.strip('/')}.{key} :D")
				else:  # "function" in str(type(v)):
					# print( f" ::: New Element xo.{self._id.replace('/','.')}.{	key} = {v}")
					print(f" ::: New Element xo.{owner.strip('/')}.{	key} = {v}")
				self._parent[key] = v  # type:ignore
				# print("SSSSSSSSSSSS",owner+key)

				# print(xo.GetXO(owner)+key, v,retXO=True)
			for a in appendToLearn:
				if self._parent is not None:
					self._parent.learned += [a]
				else:
					print(" ::: WTF")
					# self[Expando._valueArg](ref=True).append(a)
					self[self._valueArg](ref=True).append(a)

				print(f" ::: New Element xo.{owner.strip('/')}.learned = {a}")

			return self._GetXO(owner)
			# print(vars)
			# print(".....")
			# print(kwargs)
		# print(":::::::::::::::::::::::",)
		# for v in vars:
		# 	print(v)
		retXO = False
		# if "function" in str(type(self[Expando._valueArg])) or "method" in str(type(self[Expando._valueArg])):
		# print()

		# print("---------1")

		if "value" in self and "function" in str(type(self[self._valueArg])):
			''' if function is saved in self.value'''
			# print("!!!!!!!!!!#####",str(type(self[Expando._valueArg])))
			return self[Expando._valueArg](*args, **kwargs)
		# print(self[Expando._valueArg]) if Expando._valueArg in self else print()
		if "formula" in self and True:  # TODO: check valid formula
			''' if self has formula'''
			# print("ccccccccccccccccccccccccall",self._lastLoaded, self._lastUpdated)
			if self._lastLoaded == self._lastUpdated:
				# print("@@@@@@@")
				# return self.getHook()
				return self[self._valueArg]
			# print("+++++++",self._id)
			return self._runFormula()

		# print("---------2")
		# elif self._valueArg in self and self[self._valueArg] is not None and "function" in str(type(self[Expando._valueArg])):
		# 	''' if self has formula'''
		# 	# print("!!!!!!!!!![0]")
		# 	if "asyn" in kwargs and kwargs["asyn"] == True:
		# 		xkwargs = {}
		# 		for a in kwargs:
		# 			if (a != "asyn" or "asyn" in self._id) and "retxo" not in a.lower():
		# 				xkwargs[a] = kwargs[a]
		# 			elif "retxo" in a.lower():
		# 				retXO = True
		# 		if not retXO:
		# 			return self._startThread(self[Expando._valueArg], args, xkwargs)
		# 		else:
		# 			self._startThread(self[Expando._valueArg], args, xkwargs)
		# 			return self
		# 	if not retXO:
		# 		return self[Expando._valueArg](*args, **kwargs)
		# 	else:
		# 		self[Expando._valueArg](*args, **kwargs)
		# 		return self

		# print(" XXX CCC",self._id, self[Expando._valueArg])
		# if not retXO:
		# 	if "value" in self and self[Expando._valueArg] is not None and ("ref" not in kwargs or kwargs["ref"] is not True):
		# 		if isinstance(self[Expando._valueArg],list) and len(self[Expando._valueArg]) == 1:
		# 			return self[Expando._valueArg]
		# 	# print(self._id, ":::x:::", args, ":::", kwargs)
		# 	if "value" in self:
		# 		return self[Expando._valueArg]
		# 	# return self[Expando._valueArg][0](*vars, **kwargs)
		# elif "value" in self: # this is not ever running
		# 	return self[Expando._valueArg] if "value" in self else None
		# print("---------3")
		if len(args) > 0 or len(kwargs) > 0:
			# SET CALL
			# imported = False
			if len(kwargs) > 0:
				# for key in kwargs:
				# 	self[key] = kwargs[key]
				# print("YYYYYYYYYYYY")
				Expando._recursiveImportDict(self, kwargs)
				# self._recursiveImportDict(kwargs)
				# imported = True
			if len(args) == 1:
				if isinstance(args[0], dict):
					# print("XXXXXXXXXXXXXXXXX")
					Expando._recursiveImportDict(self, args[0])
				else:

					# self[self._valueArg] = args[0]
					# print("02")
					self._setValue(args[0])
				# return self
				# return args[0]

			else:
				# self[self._valueArg] = args
				finalValues = []
				for a in args:
					if isinstance(a, dict):
						# print("zzzzzzzzzzzz")
						Expando._recursiveImportDict(self, a)
						# self._recursiveImportDict(a)
					else:
						finalValues.append(a)
				print("01")
				self._setValue(finalValues)
				# if imported:
				# 	return self
				# return args
			# print("---------4")
			return self
		else:
			if self._valueArg not in self:
				self[self._valueArg] = None

			# print("---------4.5")
			return self.getHook()
			return self[self._valueArg]
			# self[Expando._valueArg][0](*vars, **kwargs)
			# return self
		# print(":::::::::::::::::::::::", self.keys(), len(self.keys()))
		newData = {}
		# print(";;;;;;;;;;;;;:::", vars)
		for d in args:
			if "dict" in str(type(d)):
				# print(";;;;;;;;;;;;;", d)
				newData = {**d, **newData}
		# newData = {**kwargs, **newData,**self}
		newData = {**kwargs, **newData}
		if (len(self.keys()) == 0):
			ddd = None
			if Expando._valueArg in kwargs:
				ddd = self._xoT_.__init__(
					self, _id=self._id, _parent=self._parent, **newData)
			else:
				pass
				# print(kwargs,args)
				# ddd = Expando.__init__(self,val = self.value if "value" in self else None,
				#                     id=self._id, parent=self._parent, **newData)
				# print("@@@@@@")
				# print(newData)
				# print("@@@@@@@@")
				# print(".............",self._id, newData["_id"] if "_id" in newData else "")
			ddd = self._xoT_.__init__(self, _id=self._id, _val=self[self._valueArg] if "value" in self else None,
							 _parent=self._parent, **newData)
			# ddd =  dict.__init__(self, *vars,**kwargs)
			# print("tttttttx", ddd, type(ddd))
			# self._convertAll()
			print("---------4.6")
			return ddd
		# Update new entries
		# TODO: make this work, update

		# print("xxxxxx", args, kwargs)
		# for k in dict(vars[0]):
		# 	print("......",k,vars[0][k])
		# 	self[k] = vars[0][k]
		# print("-------", dict(self), args)

		self.update(newData)  # working

		#self.__init__(**{**dict(self), **kwargs})
		# for

		print("---------5")
		return self

		# Add the new attributes to the instance's dictionary.
		for k, v in kwargs:
			self[k] = v

		return self._id
		# return self.update({**dict(self), **kwargs})

	def _init_(self, *args, **kwargs):
		# print(" ::: THIS NEEDS TO BE OVERLOADED TO RETURN TRUE::: overloading ")
		pass

	def _overloading_(self, *args, **kwargs):
		# print(" ::: THIS NEEDS TO BE OVERLOADED TO RETURN TRUE::: overloading ")
		return False

	def _checkIfExist_(self, *args, **kwargs):
		# print(" ::: THIS CAN BE OVERLOADED ::: checkIfExist ",
		    #   type(self), self._id, args, kwargs)
		return False

	def _read_(self, *args, **kwargs):
		# print(" ::: THIS CAN BE OVERLOADED ::: read ",
		    #   type(self), self._id, args, kwargs)
		return self
		# read = self.read()
		# if read != self
		# 	value = read

	def _create_(self, value=None, *args, **kwargs):
		# print(" ::: THIS CAN BE OVERLOADED ::: create ",
		#       type(self), self._id, value, args, kwargs)
		# return self
		pass

	def _update_(self, value=None, *args, **kwargs):
		# print(" ::: THIS CAN BE OVERLOADED ::: update ",
		#       type(self), self._id, value, args, kwargs)
		pass

	def _subscribe_to_changes_(self, *args, **kwargs):
		# print(" ::: THIS CAN BE OVERLOADED ::: subscribe_to_changes ",
		#       type(self), self._id, args, kwargs)
		# return self
		pass

	def _delete_(self, element=None, *args, **kwargs):
		idToDelete = self._id if element == None else self._id+"/"+element
		# print(" ::: THIS CAN BE OVERLOADED ::: delete ",
		#       type(self), self._id, idToDelete, args, kwargs)
		return True
		# return if deleted succesfully








	# this was used to update the value of the expando, deprecated. use xo(dict) instead
	def x_update_entries(self, entries, *vars, **kwargs):
		newData = {}
		# print(";;;;;;;;;;;;;:::", entries, vars, kwargs)
		for d in vars:
			if "dict" in str(type(d)):
				# print(";;;;;;;;;;;;;", d)
				newData = {**d, **newData}
		newData = {**kwargs, **newData}
		newData = {**newData, **entries}
		# print("@@@@@@@@", newData)

		for key in newData:
			# if isinstance(newData[key],dict):
			# "Expando" in str(type(newData[key])):
			if "dict" in str(type(newData[key])) or isinstance(newData[key], Expando):
				# print("DDDDDDDD",key)
				val = None
				# if
				if "value" in newData[key]:
					val = newData[key].pop("value")
				#EX3
				self[key] = self._xoT_(_id=self._id+"/"+key, _val=val,
									_parent=self, _behaviors=self._behaviors, ** newData[key])
			else:
				# print("DDDDDDDD",key)
				# print("NNNNNNDDDDDDDD",key,type(self))
				val = newData[key]
				# self[key] = val
				# self[key] = self._xoT(_id=self._id+"/"+key, _val=val, _parent=self)
				if key in self:
					# print("AAAAAAAA")
					if isinstance(self[key], Expando):  # "Expando" in str(type(self[key])):
						self[key].value = val
						# self[key] = val
					else:
						# print("BBBBBBBB",self[key],val)
						#EX4
						if key not in Expando._hiddenAttr and not key.startswith("_"):
							self[key] = self._xoT_(_id=self._id+"/"+key, _val=val,
												   _parent=self, _behaviors=self._behaviors)
						else:
							self[key] = val
						# self[key] = val
					# print("fffffffffaaa")
					# @self[key].setter
					# check hooks updates
				else:
					#EX5
					if key not in Expando._hiddenAttr and not key.startswith("_"):
						self[key] = self._xoT_(_id=self._id+"/"+key, _val=val,
											   _parent=self, _behaviors=self._behaviors)
					else:
						self[key] = val
					# print("fffffffff",type(self[key]))
		########## self.update(newData)

	def show(self, t="    ", count=0, inLoop=False, ret=False):
		# print("ssssssssssssssss..............",self._id)
		s = ""
		#### print("///////////",self[Expando._valueArg],type(self[Expando._valueArg]))
		p = ""
		val = ""
		if "value" in self:
			# print("1111111")
			if "str" in str(type(self[Expando._valueArg])):
				# print("11111112")
				s = "\'"
			val = str(self[Expando._valueArg])
		# else:
			# print("00000000000000")
			# print("00000000000000",self._id)
			# print("00000000000000")
		finalval = " = " + s+str(val)+s if val is not None or True else ""
		p = self._id.split("/")[-1] + finalval
		tab = ""
		for i in range(count):
			tab += t

		retList = []
		res = []
		p = tab+p
		if ret:
			# print("22222221")
			retList.append(p)
		else:
			# print("22222222")
			print(p.replace("\t", "    "))
		for a in self:
			# print("33333", a, type(self[a]))
			# if "_" not in a:
			# print("st2", s)
			if not a.startswith("_"):
				if isinstance(self[a], Expando) or "dict" in str(type(self[a])):
					# print("33334",a)
					if ret:
						# print("33335555",a)
						res = self[a].show(count=count+1, ret=ret)
					else:
						# print("3333466666",a)
						self[a].show(count=count+1, ret=ret)
				# else:
					# print("33337",a)
		if count == 0 and inLoop:
			print("\n\nPress Ctrl+C to stop whileShow()\n")

		if ret:
			# print("444444444")
			if count == 0:
				# print("4444444445")
				return str(retList + res)
			# print("55555555",count)
			return retList + ["\n"] + res
		# print("777777",ret,count,retList,res,)
		# return dict(self)

	def showMag(self, t="    ", count=0):
		return self.show(t=t, count=count)
		## print("ssssssssssssssss..............")
		s = ""
		## print("///////////",self[Expando._valueArg],type(self[Expando._valueArg]))

		if "str" in str(type(self[Expando._valueArg])):
			s = "\'"

		if "list" in str(type(self[Expando._valueArg][0])):

			fullid = ""
			for i in self._id.split("/")[1:]:
				fullid += i + " "
			fullid = fullid[:-1]
			#p = self._id.split("/")[-1] +" = "+ s+str(len(self[Expando._valueArg][0]))+s + etab + str(self[Expando._valueArg])
			p = fullid + "  = x" + s+str(len(self[Expando._valueArg][0])) + " times"
			l = len(p) % len(t)
			etab = ""
			for i in range((60 - len(t)*count) - len(p)):
				etab += " "

			p += etab + "index: " + str(self[Expando._valueArg])+s
		else:
			p = self._id.split("/")[-1] + " = " + s+str(self[Expando._valueArg])+s

		tab = ""
		for i in range(count):
			tab += t

		p = tab+p
		print(p)
		for a in self.__dict__:
			if isinstance(self.__dict__[a], Expando):
				self.__dict__[a].showMag(count=count+1)


# class self._xoT(Expando):
# 	"""docstring for obj."""

# 	def __init__(self, val=None, id=None, parent=None):
# 		self.__id = id
# 		# print("........")
# 		super().__init__(val=val, id=id)
# 		# print("........ddd")

# 		self.__id = id
# 		self._parent = parent
# 		# print("!!!!!!!!", self.__id, "PPPPPPP",self._parent)
# 		# print("........xxxxx")

	def Del(self):
		if "_parent" in self.__dict__:
			if self._parent is not None:
				# self._parent.__dict__[self._name] = None
				self._parent.__dict__.pop(self._name)

	def Show(self, inLoop=False):
		pass  # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS..............")
		super().show(inLoop=inLoop)

	def ShowMag(self):
		pass  # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS..............")
		super().showMag()

	def whileShow(self):
		while (True):
			self.show(inLoop=True)
			time.sleep(0.2)
			os.system("clear")

	def whileShowMag(self):
		while (True):
			self.showMag(inLoop=True)
			time.sleep(0.2)
			os.system("clear")

	def turnTo5(self):
		pass  # print("5555555555555555")
		self = 5

	# def set(self, value):
	# 	#### id = self._id+"/"+name, val= value

	# 	# with data binding
	# 	# manager.save(self._id, value)
	# 	pass

	# def value(self, ref=False):
	# 	if ref:
	# 		return self[Expando._valueArg]
	# 	return self[Expando._valueArg]

	def toJson(self):
		return json.dumps(self.toDict())#, default=lambda o: dict(o.__dir__))
		return str(self)
		# return json.dumps(json.loads(str(self)), indent=4)

	#iiiiiiiiiiiiiiii
	_init_done_ = False
	def __init__(self, _val=None, _id=None, _parent=None,_rootName=None, _behaviors={}, _xoT_=None, *args, **kwargs):
		# print(":::::::::::::::IIIIIIIIIIIII::::::::::::::",type(self),_id, _xoT_)
		# dict.__init__(self,**entries)
		# dict.__init__(self, *vars, **entries) #
		# if isinstance(_val, dict):
		# 	# entries = {**_val, **entries}
		# 	# _val = None
		# 	super().__init__(self, *vars, **{**_val, **entries})
		# 	dict.__init__(self, *vars, **{**_val, **entries})
		# else:
		# 	super().__init__(self, *vars, **entries)
		# 	dict.__init__(self, *vars, **entries)
		if _parent is None and _id is None and _val is not None and isinstance(_val, str):
			_id = _val
			_rootName = _val
			self._rootName = _rootName
			_val = None

		if _parent is not None:
			self._root = _parent._root
		else:
			self._root = self
			# print("::: ROOT XO :::", _id)
		

		super().__init__(self, *args, **kwargs)
		dict.__init__(self, *args, **kwargs)
		

		if self is not None:
			_xoT_ = type(self)
		# Expando.__init__(self, _val=_val, _id=_id, _parent=_parent,
		#                  _behaviors=_behaviors, _xoT_=xoRedis, *vars, **entries)
		####expando.py
		#### def __init__(self):
		#### es=traceback.extract_stack()
		# super().__init__(id = id, val = val)

		
		if _id is None:
			# print("ddddddddddddd",_xoT_)
			_id = Expando._rootName
			if _xoT_ is not None:
				_id = _xoT_._rootName
				# print("11111111111")

			if _rootName is not None:
				# print("222222222")

				_id = _rootName
				#namespace
				self._rootName = _rootName
			else:
				pass
				# print("???????????????????????")
				# print("???????????????????????")
				# print("???????????????????????")
			# print("@",_rootName)
		# print(_id,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		# print(_id,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		# print(_id,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")



		self._id = _id if _id is not None else Expando._rootName
		# self._id = _id if _id is not None else None
		# if self._id is None:
		# 	self._id = self._rootName

		self._name = _id.split("/")[-1]
		
		self._xoT_ = type(self) if _xoT_ is None else _xoT_
		# print("self._xoT_",self._xoT_)
		self._xoT_ = Expando if self._xoT_ is None else self._xoT_

		self._parent = _parent
		self._isRoot = False
		if self._parent is None:
			self._isRoot = True
		else:
			self._parent.__dict__[self._name] = self

		# if _xoT_ is None:
		# 	self._xoT_ = Expando
		# else:
		# 	self._xoT_ = Expando
		# super().__init__(*(None, val))
		# super().__init__(val)
		# super().__init__()
		pass  # print("PPPPPPPPPPPPPP", id)
		#### self.name = self.GetName()

		# self._id = _id
		# self._birth = datetime.now()

		# self.__id = id
		# # print("........")
		# super().__init__(val=val, id=id)
		# # print("........ddd")

		# self.__id = id
		
		#### self.__validID_ = False
		#### global GD
		#### self.xxx = self.get_my_name()
		#### print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@",mod_retrieve_name(self))
		exist = True
		'''
		birth = str(time.time())
		if id is None:
			id = birth
		'''

		self._subscribers = []
		# self._triggers = []

		#### self.__main__ = main
		# self.__id__ = "hidden"
		# self.__dict__.pop("__id__")

		# self[Expando._valueArg] = _val
		# self.__dict__["val"] = 3
		# print("obj created! =",self[Expando._valueArg])
		# self._zzz = 5
		self._behaviors = _behaviors
		#### print("******---",self.get_my_name())
		#### self["_id"] = self.get_my_name()[0]

		self._async = self._startThread

		# self[Expando._valueArg] = val
		# self[Expando._valueArg] = val
		# if _val is not None:
		# 	# self[Expando._valueArg] = _val # set hook
		# 	if isinstance(_val, dict):
		# 		# self._recursiveImportDict(_val)
		# 		Expando._recursiveImportDict(self,_val)
		# 		# self._recursiveImportDict(_val)
		# 		_val = None
		# 	else:
		# 		self._setValue(_val)
		# 	# self[Expando._valueArg] = _val # set hook
		# self.update(entries)

		if self._overloading_():
			# print("overloading!!!!!!!!!!!", type(self), self._id)
		
			self._init_(*args, **kwargs)

			if not self._checkIfExist_():
				# calling create event
				self._create_(_val)
			else:
				if _val is None:
					# calling read event
					# res = self.read()
					read = self._read_()
					if read != self:
						_val = read
						# self._setValue(value)
						# __setvalue(self, value)
						
			if _val is not None:
				# print("@@@@@@@@@@@@")
				self._setValue(_val)

				
				# print("11111111111111")
				# self._update_(_val)
				# This happens when setting value

			self._subscribe_to_changes_(self)
		else:
			if _val is not None:
				self._setValue(_val)
				# this will call _update_() if it exists

		# self._update_entries({**entries, **{"value": _val}})
		# self._update_entries(entries)

		self._init_done_ = True
		# print(":::::::::::::::::::::::::::::::::::::::::", self._id, self._init_done_)
		pass
		#### self.xxx.yyy.zzz = 13
		#### updateID = Thread(target = self.makeID, args = [list,])
		#### updateID.start()

		# print("AAAAAAAAAAA	AAA",entries,self.__name__)
		# for arg_name in entries:
		# 	pass  # print("AAAAAAAAAAAAA",arg_name)


# 		# Binding the object to the value
#		# global manager
# 		# self._manager = manager
# 		# self[Expando._valueArg] = manager.bind(self.__id, val, ref=[self])

	# def __setattribute__(self, name, value, *args, **kwargs): # expect _skip_overload to be in kwargs
	# 	print("@S")
	# 	return self.__setattr__(name, value, *args, **kwargs)

	# def __getattribute__(self, name, loop=True):
	# 	print("GGGGGGET ATRI",name)
	# 	return super().__getattribute__(name)
	# def __getattribute__(self, name, loop=True, *args, **kwargs):
	# 	if not name.startswith("_"):
	# 		 # expect _skip_overload to be in kwargs
	# 		print("@G")
	# 		return self.__getattr__(name, loop=loop, *args, **kwargs)
	# 	else:
	# 		return object.__getattribute__(name,*args, **kwargs)

	# expect _skip_overload to be in kwargs


	def __setattr__(self, name, value, *args, **kwargs):
		# print("sssasasaaaaaaaasaaaaaaaas", self._id, name, value,":::", args,":::", kwargs)
		# print(str(type(name)))
		# print()
		# if "str" not in str(type(name)):
		# if "str" not in str(type(name)):
		if not isinstance(name, str):
			name = str(name)
		# 	print("XXSXSXSXSXSXSXSXSX", type(name), name._id)
		# 	print("XXSXSXSXSXSXSXSXSX")
		# 	print("XXSXSXSXSXSXSXSXSX")
		# 	print("XXSXSXSXSXSXSXSXSX")

		if isinstance(value, dict) and "Expando" not in str(type(value)) and not name.startswith("_"):
			# cast dict to Expando
			# print("CASTING TO EXPANDO, name=", name)
			# value = Expando(value)
			value = self._xoT_(value)
		# print("st3")
		# if name in self and name not in Expando._hiddenAttr and (not name.startswith("_") or name == Expando._valueArg):
		behave = False
		if behave:
			if name in self and name not in Expando._hiddenAttr and not name.startswith("_"):
				if ("_skip_overload" not in kwargs or kwargs["_skip_overload"] == False) and name != "_behaviors":
					pass
					# print("EEEEEEEEEEEEEEEEEEEE1", name, value)
				return self._behaviors[Expando.__setattr__](name, value, *args, **kwargs) \
									if Expando.__setattr__ in self._behaviors \
									else self.__setattr__(name, value, _skip_overload=True, *args, **kwargs)
		# TODO: make _skip_overload not a thing, instead the overload will return (True, value) if it wants to continue the default behavior

		# and "__skip" in self.__dict__ and name not in self.skip:
		if name == self._valueArg:
			self._setValue(value)
		elif name not in Expando._hiddenAttr and not name.startswith("_"):
			if not isinstance(value, Expando):
				# if type(value) is not Expando:
				# print(f"____________{name}_________", str(type(value)))
				if name not in self:
					# print("2222222222")
					# print("ppp33333",self._id)
					# self[name] = obj(id = self._id+"/"+name, val= value, parent = __objManager.getXO(self._id))
					if name == Expando._valueArg:
						# self[name] = value
						# set hook
						self._setValue(value)
						# object.__setattr__(self, name, value)
						# self[name] = value
					else:
						# print("........")
						#EX6
						#final .x =
						res = self._xoT_(_id=self._id+"/"+name, _val=value,
										 _parent=self, _behaviors=self._behaviors)
						# set hook
						self[name] = res
						# self[name]._setValue(res)
						object.__setattr__(self, name, res)
				else:
					# print("33333333")
					#### self.__set__(name,value)
					#### self.save(id = self._id+"/"+name, val= value)
					# if data binding
					# manager.save(channel = self._id+"/"+name, data=value)
					# self[name]._value = value  # ?????
					# set hook fuck
					self[name]._setValue(value)
					# self[name][Expando._valueArg] = value  # ?????
					# self[name+"2"]._val = value  # ?????

				# disable hook
				# self[name]._updateSubscribers_(value)
			else:
				# print("44444", name, value)
				self[name] = value
				# print("44444")
				# self[name]._updateSubscribers_(value)

		else:
			# print("555555555", name)
			# self.__dict__[name] = value
			# print("555555", name, value)
			# time.sleep(.1)
			self[name] = value  # hook fuck 2
			# self._setValue(value)
			# object.__setattr__(self, name, value)

		# time.sleep(.1)
	def __getitem__(self, name):
		# print("iiiiiiii", name)
		# if not name.startswith("_") and name not in Expando._hiddenAttr:
		# 	return self.__getattr__(name)
		# return super().__getitem__(name)
		# print("__getitem__", name)
		# if "str" not in str(type(name)):
		target = self
		if "/" in name or "." in name:
			# print("x PRE", target._id, "name:", name)
			for channel in name.replace("/",".").split(".")[:-1]:
				# if c not in f:
				# 	f[c] = xo()
				target = target.__getitem__(channel)
			# print("x POST",target._id)
			return target.__getitem__(name.replace("/",".").split(".")[-1])

		if not isinstance(name,str):
			name = str(name)
		#### return name
		if name == Expando._valueArg:  # name == "value":
			# self[name] = self._xoT(id=self._id+"/"+name, parent=self)
			# return self[name]
			if Expando._valueArg not in self:
				target[Expando._valueArg] = None

			### GET HOOK
			return target.getHook()
			return super().__getitem__(name)
			return self[name]

		# print(" ", name, name in self, ":::::::",
			#   dict(self), ":::::::", self.__dict__)

		# print(name in self.__dict__, name in self)
		# if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr and name not in self.__dict__:
		if not name.startswith("_") and name not in Expando._hiddenAttr:
			pass  # print("OOOOO_ooooooooooooooooooooo",name)####,self.__dict__)
			# print("aaaaaaaaaaaaaa", name, dict(self))
			# print("ppp66666",self)
			# self[name] = obj(id = self._id+"/"+name, parent = self)
			#EX7

			if name in self:
				# atr = object.__getattribute__(self, name)
				# atr = self[name]
				atr = super().__getitem__(name)

				# print("bbbbbbbbbbbbbbb", name, atr, type(atr))

				return atr
			# else:
			res = self._xoT_(_id=self._id+"/"+name, _parent=self,
						   _behaviors=self._behaviors)
			self[name] = res
			# object.__setattr__(res, "value", None)

			return super().__getitem__(name)
			return self[name]
		else:
			# self[name] = 
			pass

		# print("!!!!!!!!!!!!!!!", name)
		return super().__getitem__(name)
		return self[name]

	def __getattr__(self, name, loop=True, *args, **kwargs):
		# print("__getattr__", name)
		# if "str" not in str(type(name)):
		# 	name = str(name)
		if not isinstance(name,str):
			name = str(name)
		#### return name
		if name == Expando._valueArg:  # name == "value":
			if Expando._valueArg not in self:
				self[Expando._valueArg] = None
			# self[name] = self._xoT(id=self._id+"/"+name, parent=self)
			# Get Hook
			return self.getHook()
			return self[name]

		# print(" ", name, name in self, ":::::::",
			#   dict(self), ":::::::", self.__dict__)

		# print(name in self.__dict__, name in self)
		# if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr and name not in self.__dict__:
		if not name.startswith("_") and name not in self and name not in Expando._hiddenAttr:
			pass  # print("OOOOO_ooooooooooooooooooooo",name)####,self.__dict__)
			# print("aaaaaaaaaaaaaa", name, dict(self))
			# print("ppp66666",self)
			# self[name] = obj(id = self._id+"/"+name, parent = self)
			#EX7
			self[name] = self._xoT_(_id=self._id+"/"+name,
									_parent=self, _behaviors=self._behaviors)
			return self[name]
		if name in self:
			# atr = object.__getattribute__(self, name)
			atr = self[name]

			# print("bbbbbbbbbbbbbbb", name, atr, type(atr))

			return atr
		# print("!!!!!!!!!!!!!!!", name)
		return self[name]

	# def get(self):
	# 	return "_NotOverloaded_"

	def getHook(self, item=None, *args, **kwargs):
		# THIS CAN BE OVERLOADED BY SUBCLASS
		# print("RRRGGGGGGGGGGGGGGGGGG",self._id,type(self),type(super()))

		# res = self.get()

		if True: # res == "_NotOverloaded_":
			if item is not None:
				return super().get(item, *args, **kwargs)
			else:
				# return self[Expando._valueArg]
				# print(":iiiiii:", self._id, super().getHook(self._valueArg))
				return super().get(self._valueArg)
				# return super().__getitem__(self._valueArg)
				# return super().__getattribute__(self._valueArg)
		else:
			return res

	def set(self, value, *args, **kwargs):

		return True

	# def set(self, item, value, *args, **kwargs):
	# 	if value is not None:
	# 		return super().set(item,value,*args,**kwargs)
	# 	value = item
	# 	return self._setValue(value)

	# def __repr__(self) -> str:
	# 	return super().__repr__()
	def __repr__(self, *args, **kwargs):
		# if (not name.startswith("_") or name == Expando._valueArg) and name not in Expando._hiddenAttr:
		# if ("_skip_overload" not in kwargs or kwargs["_skip_overload"] == False):
		# 	# print("YYYYYYYYYYYYYYYYYYYYYYYYYESS GETTTTTTTTT repr")
		# 	return str(self._behaviors[Expando.__repr__](*args, **kwargs)) \
		# 		if Expando.__repr__ in self._behaviors \
		# 			else self.__repr__(_skip_overload=True, *args, **kwargs)
		# TODO and no other attributes
		# print("!!!!!!!!!!!!!!!", )
		if Expando._valueArg in self and len(self.keys()) == 1:
			# return self[Expando._valueArg].__repr__()
			if isinstance(self[Expando._valueArg], str):
				return repr(str(self[Expando._valueArg]))
			return str(self[Expando._valueArg])

		return str(dict(self))
		# return str(self.show())
		# return super().__repr__()

	def toDict(obj):
		if not  hasattr(obj,"__dict__"):
			return obj
		result = {}
		for key, val in obj.__dict__.items():
			if key.startswith("_"):
				continue
			element = []
			if isinstance(val, list):
				for item in val:
					element.append(Expando.toDict(item))
			else:
				element = Expando.toDict(val)
			result[key] = element
		return result
		
	def __str__(self, *args, **kwargs):
		# print("!!!!!!!!!!!!!!!2",)
		# behave = False
		# if behave:
		# 	if ("_skip_overload" not in kwargs or kwargs["_skip_overload"] == False):
		# 		# print("YYYYYYYYYYYYYYYYYYYYYYYYYESS GETTTTTTTTT str", args, kwargs)
		# 		return str(self._behaviors[Expando.__str__](*args, **kwargs)) \
		# 			if Expando.__str__ in self._behaviors \
		# 				else self.__str__(_skip_overload=True, *args, **kwargs)

		if Expando._valueArg in self and len(self.keys()) == 1:
			res =  str(self[Expando._valueArg])
			# print("__", res)
			return res
		# res = str(self.toDict())
		res =  self.__repr__()
		# print("_", res)
		return res
		# return str(dict(self))
		return super().__repr__()

	def default(self):
		return self.toDict()

	# @classmethod
	# def processCMD(*args, **kwargs):
	# 	print("ccccccc",args)
	# 	print(f" ::: Processing Data from CMD ::: data length {len(str(args))}\n\n")

	# # REPOSIZE
	# # curl https://api.github.com/repos/fire17/AlphaENG 2> /dev/null | grep size | tr -dc '[:digit:]'

	# # TODO: Fix *args **kwargs
	# # def osCommand(cmd = ['ping -c100 www.google.com',False], callback = processCMD):

	# def osCommand(self,cmd=["", 'ping -c100 www.google.com', False, processCMD, "cmd.res"]):
	# 	oneLine, location, cmd, asyn, callback, autoPub = cmd
	# 	# location = "/home/magic/xo-gd/main"
	# 	# cmd = "rm -rf fire17_AlphaENG && git clone https://github.com/fire17/AlphaENG.git /home/magic/xo-gd/main/fire17_AlphaENG "
	# 	# cmd = "git clone https://github.com/fire17/AlphaENG.git /home/magic/xo-gd/main/fire17_AlphaENG "
	# 	if location and not asyn:
	# 		currDir = os.getcwd()
	# 		os.chdir(location)
	# 		newDir = os.getcwd()
	# 		print(" ::: CD TO", location)
	# 	# print("RUNNING 1")
	# 	# res =
	# 	# print("ASYN", asyn)
	# 	if not asyn or True:
	# 		if not oneLine or True:
	# 			cmd = cmd.strip(" ").split(' ')
	# 			# print("bbbbbbbbbbbbbbbbbbb")
	# 		else:
	# 			cmd = [cmd.strip(" ")]
	# 		res = []
	# 		try:
	# 			print(
	# 				f" ::: Running Command ::: {' '.join(cmd)} \n ::: you can break (ctrl+c) and get the results :::  \n")
	# 			for line in os_command(cmd, print_output=True):
	# 				print(line)
	# 				res.append(line)
	# 		except:
	# 			print(" ::: STOPING CMD !!! :::")
	# 			traceback.print_exc()
	# 			pass  # so you can break and also get the results

	# 		if callback is not None:
	# 			print(" ::: Sending results to callback !!! :::", callback)
	# 			callback(res)
	# 		if autoPub is not None and autoPub != "":
	# 			if "list" not in str(type(autoPub)):
	# 				autoPub = [autoPub]
	# 			for a in autoPub:
	# 				x = self._GetXO(a,allow_creation=True)
	# 				if x:
	# 					x._setValue(res)
	# 		# xo.res = res
	# 		return res

	# def command(self,cmd = "ping 8.8.8.8 -i 1",location ="", oneLine=True, asyn = True):
	# 	# print("XXXXXD")
	# 	self._osCMD = self.osCommand
	# 	self._osCMD([oneLine, location, cmd, asyn, self.processCMD,"cmd.res"])

	# @property
	# def __json__(self):
	# 	return dict(self)

	# def toJSON(self): # NOT READY
	# 	print("####################")
	# 	print("####################")
	# 	print("####################")
	# 	print("####################")
	# 	print("####################", dict(self))
	# 	print("####################")
	# 	# print(dict(self))
	# 	jsonD = {k:v for (k,v) in dict(self).items() if "function" not in str(type(v)) if "method" not in str(type(v))}
	# 	print("####################", jsonD)
	# 	print("####################")
	# 	# print(jsonD)
	# 	# return json.dumps(jsonD, default=self.default, indent=4)
	# 	return json.dumps(jsonD, indent=4)
	# 	# return json.dumps(self, default=lambda *a,**kv: dict(self))
	# 	# print(json.dumps(self, indent=4, default=lambda x: x.__json__))
	# 	print(json.dumps(self.__dict__))


# xo = Expando()

# 	def __setattr__(self, name, value):
# 		pass  # print("EEEEEEEEEEEEEEEEEEEE000")
# 		return super().__setattr__(name=name, value=value)

# 	def __getitem__(self, name):
# 		return super().__getitem__(name=name)

	def __setitem__(self, name, value, skipUpdate=False):
		# return self.__setattr__(name=name, value=value)
		# super().__setattr__(name, Expando(value))
		# print("..............",name)
		if not isinstance(name,str):
			name = str(name)

		target = self
		if "/" in name or "." in name:
			# print("x PRE", target._id, "name:", name)
			for channel in name.replace("/",".").split(".")[:-1]:
				# if c not in f:
				# 	f[c] = xo()
				target = target.__getitem__(channel)
			# print("x POST",target._id)
			return target.__setitem__(name.replace("/",".").split(".")[-1], value, skipUpdate=skipUpdate)

		res = self
		updateTarget = self
		skip = False
		# if (not isinstance(name,str)) or (name not in Expando._hiddenAttr and not name.startswith("_")):
		if name not in Expando._hiddenAttr and not name.startswith("_"):
			# print("@@@@@@@@@@@",1)
			if not isinstance(value, Expando) and name not in self:
				# print("@@@@@@@@@@@",2)
				updateTarget = self._xoT_(_id=self._id+"/"+str(name), _val=value,
                  _parent=self, _behaviors=self._behaviors)
				object.__setattr__(self, name, updateTarget)
				
			elif name in self:
				# print("@@@@@@@@@@@",3)
				updateTarget = self[name]
			else:
				# print("@@@@@@@@@@@",4)
				pass
				# # object.__setattr__(self, name, value)
				# print("???????????????????????????",self._id, type(value))
				# print(self.__dict__)
				# print("???????????????????..........")


		else:
			# print("..............",name)
			if name != self._valueArg:
				# print("@@@11111")
				object.__setattr__(self, name, value)
				self.__dict__[name] = value
				# skip = True
				pass
				# skip = True
			else:
				skip = True
				# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", name, self._id,"skip:", skipUpdate,"value:", value,"init_done:", self._init_done_)
				if not skipUpdate and (value is not None or self._init_done_ == True and "_has_value" in self and self._has_value): #and False:
					# print("$$$$$$$$$")
					self._has_value = True
					updateTarget._update_(value)
					# print("$$$$$$$$$")
				# print("!!!!!!!")
				# time.sleep(1)

		
		# print("@@@22222222")
		# set hook
		# self[name] = res
		# self[name]._setValue(res)
		# object.__setattr__(self, name, res)
		# object.__setattr__(self, name, value)
		if not skip and False:
			if self._init_done_ and self._overloading_() and name not in Expando._hiddenAttr and not name.startswith("_"):
			# if self._overloading_():
				runUpdate = False if name != self._valueArg else True
				# updateTarget = self
				if (name not in self._hiddenAttr and not name.startswith("_")):
					print("222222222222222222222",self._id, name, name in self)
					# res._update_(value)
					# updateTarget = res
					runUpdate = True
				# if runUpdate and not skipUpdate:
					if runUpdate and not skipUpdate:
						print("......111111111", value)
						updateTarget._update_(value)
				# else:
					# print("fuck Yea !!!!!!!!!")
				object.__setattr__(updateTarget, name, value)
				# object.__setattr__(self, name, value)
				# object.__setattr__(updateTarget, "value", value)


				# elif name == self._valueArg:
				# 	print("5555555555555555555555")
				# 	self._setValue(value)
				# else:
				# 	pass
			# if redo:
			# 	return self.__setattr__(name=name, value=value)
		return super().__setitem__(name, value)
		# self[name] = value
		# return self[name]

	# def __getattribute__(self, name, loop=True):
	# 	print("__getattribute__", name)
	# 	return OrderedDict.__getattribute__(self, name)
	# 	name = str(name)
	# 	# return self.__getattribute__(name)
	# 	if not name.startswith("_") and name not in Expando._hiddenAttr:
	# 		return self.__getattr__(name=name, loop=loop)
	# 	# return super().__getattribute__(name)
	# 	return Expando.__getattr__(self, name, loop=loop)
	# def __setattribute__(self, name, value, loop=True):
	# 	print("__SSSetattribute__", name, value)
	# 	return OrderedDict.__setattr__(self,name, value)
	# 	# name = str(name)
	# 	# return self.__getattribute__(name)
	# 	if not name.startswith("_"):
	# 		return self.__setattr__(name=name, value=value, loop=loop)
	# 	return Expando.__setattr__(self,name, value)

# 	def __getattr__(self, name, loop=True):
# 		return super().__getattr__(name=name, loop=loop)

# input = "some sentence xo.url.address "
# regex to get url from input
if __name__ == "__xmain__":
	# 	print("ssssssssssssssss..............")
	# 	s = child(val= "ssssssssssssssss", id= "ssssssssssssssss")
	# 	s.show()
	# 	s.showMag()

	xo.foo = lambda x: print(f"!!!!!!!{x}")
	xo.foo(5)
	print(type(xo.a))

	xo.a = 3
	xo.ff = lambda x: print(x.a, f"!!!!!!!{x}")
	ff = xo.ff[Expando._valueArg]
	# inspect.getsource(ff)
	getsource(ff)
	for c in ff.__code__.__dir__():
		print(c, ":::", ff.__code__.__getattribute__(c))

	prefix = "xo"
	getsource(ff)

	for name in ff.__code__.co_names:
		print("name", name)
		if prefix+"."+name in getsource(ff):
			print("found", prefix+"."+name)
			print(prefix, "[", name, "]", "::::::", xo[name])

		# import importlib
		# importlib.reload(module)


# xo
# xo.a = Expando(val = 3)
# xo.a @= lambda x: print(x)
# xo.a = 4

# xo.a = Expando(val = 3)
# xo.a @= xo.b
# xo.a = 4

	# xo.name.first = "tami"
	# xo.name.last = "bar"
	# xo.fullname <<= lambda: xo.name.first() + ", " + xo.name.last()

	# # xo.fullname >>= lambda: xo.name.first() + ", " + xo.name.last()

	# xo.show()
	# print("__________________", xo.fullname._lastUpdated)
	# xo.name.first = "po"
	# print("__________________", xo.fullname._lastUpdated)
	# xo.fullname()
	# xo.fullname.show()
	# print("_______________")
	# xo


# (Warm) Reload a module
# import importlib
# importlib.reload(module)

# from dill.source import getsource
# inspect.getsource(function)


#xo.f = lambda : xo.self.name.first[Expando._valueArg] + "," + xo.self.name.last[Expando._valueArg]
#
