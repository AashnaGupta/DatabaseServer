import os

class Simpledb:
    def __init__(self, filename):
        self.filename = "data.txt"
        #f=open(filename, 'a')
        #f.close()
        
    def __repr__(self):
        return ('<'+'Simplebd'+' file=\''+ filename+'\'>')


    def add(self,key,value):
        f= open(self, 'a')
        f.write(key + '\t' + str(value) + '\n')
        print()
        print (key + "\t" + str(value) + " added succesfully.")
        f.close()
            

    def find(self, key):
        f = open(self, 'r')
        found = False
        for row in f:
                (k,v) = row.split('\t', 1)
                if k == key:
                    found = True
                    break

        if found == True:
            print()
            print (key + " found succesfully. The value is: " + v)
            return v
        else:
            print()
            print (key + " not found.")
            return None

    def delete(self, key):
        f = open(self, 'r')
        found = False
        new = open('new.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                found = True
            else:
                new.write(row)
 
        if found == True:
            print()
            print (key + " deleted succesfully.")
        else:
            print()
            print (key + " not found.")

        f.close()
        new.close()
        os.replace('new.txt', self)

    def update(self, key,value):
        f = open(self, 'r')
        found = False
        new = open('new.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                found = True
                #value = input("Enter the new phone number(only digits 0-9): ")
                #value = int(value)
                #print()
                new.write(key + '\t' + str(value) + '\n')
                print ("Old value of key " + key + " replaced succesfully with: " + str(value))
            
            else:
                new.write(row)

        if found== False:
            print()
            print ("Name not found.")
                      
        f.close()
        new.close()
        os.replace('new.txt', self)



    
