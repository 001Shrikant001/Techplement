import time

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"      #Defining Uppercase Characters
lowercase = "abcdefghijklmnopqrstuvwxyz"      #Defining Lowercase Characters
digits = "123456789"                          #Defining Digits
character = "!#$%&()*+,-./:;<=>?@[]^_`{|}~"   #Defining Special Characters
all = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~"   #Merging all Characters


class Random:
    def __init__(self, seed=None):
        self.seed(seed)

    def seed(self, seed=None):
        if seed is None:
            seed = int(time.time() * 1000)
        self.state = seed

    def random(self):
        self.state = (self.state * 6364136223846793005 + 1) % (2**64)
        return self.state / (2**64)
    
    def choice(self, seq):
        return seq[int(self.random() * len(seq))]
        
random = Random()            #Creating Object for Class 'Random'


def passs(lenofpass,upcs,locs,dig,char):    #Creating Function
    e = True
    if (upcs+locs+dig+char)>lenofpass:      #Checking if length is not getting crossed
        print("Crossing limit of Password")
        e = False
    newpas = ''                             #Creating empty string for new password
    
    if upcs>=0 and upcs<=lenofpass:         
        for i in range(0,upcs):
            newpas += random.choice(uppercase)  #Adding Uppercase letters in password
        lenofpass -= upcs                  
        
            
    if locs>=0 and locs<=lenofpass:
        for i in range(0,locs):
            newpas += random.choice(lowercase)   #Adding Lowercase letters in Password
        lenofpass -= locs
        
            
    if char>=0 and char<=lenofpass:
        for i in range(0,char):
            newpas += random.choice(character)    #Assing Characters in password
        lenofpass -= char
        
            
    if dig>=0 and dig<=lenofpass:
        for i in range(0,dig):
            newpas += random.choice(digits)       #Adding Digits in Password
        lenofpass -= dig

    if lenofpass != 0:                       #If the length is still not zero, continue generating the password.
        for i in range(0,lenofpass):
            newpas += random.choice(all)
    
    if e == True: 
        print(newpas)                 #Printing Password if length of password is not getting crossed

lenofpass = int(input("Enter Length of password: "))          #Asking User for length of password
upcs = int(input("How many UPPERCASE letters do you want?"))  #Asking User for Numbers of Uppercase letters
locs = int(input("How many lowercase letters do you want?"))  #Asking User for Numbers of lowercase letters
dig = int(input("How many Digits do you want?"))              #Asking User for Numbers of Digits
char = int(input("How many Character do you want?"))          #Asking User for Numbers of Character

passs(lenofpass,upcs,locs,dig,char)                           #Calling Function
