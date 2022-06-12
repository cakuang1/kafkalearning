#broker class. Instantiates and instance when we start up a server


from requests import delete


class broker:
    def __init__(self,id):
        self.id = id
        self.topic = {}
        self.numtopics=0


    def addtopic(self,nameoftopic):
        self.topic[nameoftopic] = []
    def deletetopic(self,nameoftopic):
        self.topic.pop(nameoftopic,None)
    def addtotopic(self,topicname,message):
        self.topic[topicname].append(message)
    def deltotopic(self,topicname,message):
        self.topic[topicname].append(message)










    
    














