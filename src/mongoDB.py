import pymongo

class Umongo():
    def __init__(self):
        self.myclient = pymongo.MongoClient('121.151.120.199',27017)
        self.mydb = self.myclient['db']
        self.mydb.authenticate('ukhyun','dnr68425')

    def insert(self,*args):
        self.col = self.mydb[args[0]]
        self.x = self.col.insert_one(args[1])
        return self.x

    def select(self,*args):
        #args[0] := Name of Collection
        #args[1] := Where Statement
        #args[2] := Select Statement
        if len(args) == 2:
            self.col = self.mydb[args[0]]
            self.x = self.col.find({},args[1])
            return self.x
        else:
            self.col = self.mydb[args[0]]
            self.x = self.col.find(args[1],args[2])
            return self.x
    
    def update(self,*args):
        #args[0] := Collection Name
        #args[1] := Where Statement
        #args[2] := New Value
        self.col = self.mydb[args[0]]
        self.x = self.col.update(args[1],{"$set": args[2]})
        return self.x

    def updateMany(self,*args):
        #args[0] := Collection Name
        #args[1] := Where Statement
        #args[2] := New Value
        self.col = self.mydb[args[0]]
        self.x = self.col.update_many(args[1],{"$set": args[2]})
        for x in self.select('chatList',{"_id":0}):
            print(x)
        return self.x

    