class J5:

    def recevingcall(self):
        print("Call received...")

    def rejectingcall(self):
        print("Call rejected...")

class J7(J5):
    def camera(self):
        print("Photo clicked...")

j7 = J7()
j7.recevingcall()
j7.rejectingcall()     
j7.camera()   