#01_expando101.py
# import expando
from expando import Expando

xo = Expando()
# ( you can also use 
# from xo import * to get using xo straight away

xo.a.b.c.d.e.f.anything.youd.like.to.add = "nice"
xo.users = ["tami", "michael", "joe", "jane"]
for user in xo.users:
    xo.users[user] = 

# You can use expando like a dictionary or an object