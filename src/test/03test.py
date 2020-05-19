from src.mongoDB import *
import inspect

mong = Umongo()

mong.updateMany('chatList',{"name":{"$regex":"^uk"}},{"name":"hello"})