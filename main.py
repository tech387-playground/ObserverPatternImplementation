

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, video, subject):
        print('Hello ' + self.name + ', ' + 'new video ' + video + ' by ' + subject.name)

class Subject:

    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.videos = []

    def addVideo(self, video):
        self.videos.append(video)
        self.notifySubscribers(video)

    def getVideos(self):
        return self.videos

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        return self.subscribers.remove(subscriber)

    def getSubscribers(self):
        return self.subscribers

    def notifySubscribers(self, video):
        for sub in self.subscribers:
            sub.update(video,self)
            # self.

if __name__ == '__main__':
    pewdiepie = Subject('Pewdiepie')
    amer = Observer('Amer')
    haris = Observer('Haris')
    pewdiepie.subscribe(amer)
    pewdiepie.subscribe(haris)
    print('add video')
    pewdiepie.addVideo('Happy Wheels')
    print('add video2')
    pewdiepie.addVideo('LWAY')
    print('List videos')
    print(pewdiepie.getVideos())
    print('unsub haris and add video')
    pewdiepie.unsubscribe(haris)
    pewdiepie.addVideo('YLYL')

    