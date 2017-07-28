# Don't be sad...be awesome
import sys
class Sad:
    
    def __init__(self,state=False):
        self.state = state

    def __call__(self):
        return self.state

    def stop(self):
        print ("Stop being sad...")
        self.state = False

def beAwesome():
    print ("Be awesome!")

def main():
    feeling = sys.argv[1]

    if (feeling.lower() == "true"):
        sad = Sad(True)
    elif (feeling.lower() == "false"):
        sad = Sad(False)
    else:
        print ("Either you are sad, or you are not. Don't be sad. Be Awesome")
        sys.exit()

    if (sad() == True):
        sad.stop()
        beAwesome();
    elif(sad() == False):
        print ("Keep being you!")

if __name__ == '__main__':
    main()
