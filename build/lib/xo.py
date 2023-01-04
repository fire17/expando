# from expando import *
# import expando 
from expando import Expando as Expando
# from xo.redis import Redis
import json
# def reload(m = expando):
# m = expando
# importlib.reload(m)
# print(" ::: Reloaded", m, "::: at ", time.time())
# reload = lambda m: reload(m)

# reload()
# xo = Expando()
# xo = expando.Expando()

# from helper import *



xo = Expando()
# redis = Redis()

def main():
    # print arguments
    import sys
    # print(xo, sys.argv, sys.__dict__)
    # parse key value in arguments

    # print(xo, sys.argv)
    print(xo)


if __name__ == "__main__":
    main()
##################################
# USEFULL FUNCTIONS

# def _safeWrap(func):
# 	def wrapped(*args, **kwargs):
# 		errors = {}
# 		try:
# 			return func(*args, **kwargs), errors
# 		except Exception as e:
# 			print(e)
# 			return None, jsonify({'error': str(e)})
# 	return wrapped


# xo.reload(Expando)

# xo = Expando(xo)


