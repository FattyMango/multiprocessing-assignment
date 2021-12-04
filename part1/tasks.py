import random
from threading import main_thread

class Tasks :
    '''
        A class contains all the tasks needed for part 1
         each 'calc' function reads from data.txt file and write
          the data in its own file which will be rad using - 
           print_all function.
        Note : 
            We need to write and read from files since 
             multiprocessing in python cant share memory.
                                                                '''
                                                                
    def __init__(self,volume) -> None:
       
        self.__max = None
        self.__min = None
        self.__avg = None
        self.__dataSet = []
        self.generate_dataSet(volume)
    def get_dataSet(self):
        return self.__dataSet

    def calc_max (self):
        print('start')
        with open('data.txt') as file_in:
            self.__dataSet = []
            for line in file_in:
                self.__dataSet.append(int(line))
        self.__max = self.__dataSet[0]
        for i in range (1,self.__dataSet.__len__()):
            if self.__dataSet[i] > self.__max:
                self.__max = self.__dataSet[i]
        f = open("max.txt",'w')
        f.write(str(self.__max))
        print("max is done")        
        return self.__max
    
    def calc_min (self):
        print('start')
        with open('data.txt') as file_in:
            self.__dataSet = []
            for line in file_in:
                self.__dataSet.append(int(line))
        self.__min = self.__dataSet[0]
        for i in range (1,self.__dataSet.__len__()):
            if self.__dataSet[i] < self.__min :
                self.__min = self.__dataSet[i]
        f = open("min.txt",'w')
        f.write(str(self.__min))
        print("min is done") 
        return self.__min    

    def calc_avg(self):
        print('start')
        with open('data.txt') as file_in:
            self.__dataSet = []
            for line in file_in:
                self.__dataSet.append(int(line))
        self.__avg = 0
        for i in range (0,self.__dataSet.__len__()):
            self.__avg += self.__dataSet[i]
            
        self.__avg = self.__avg/self.__dataSet.__len__()
        f = open("avg.txt",'w')
        f.write(str(self.__avg))
        print("avg is done") 
        return self.__avg
       
             
    
    def generate_dataSet(self,volume):
        '''
            Generate random data and write in data.txt.
                                                        '''
        print("Generating data set...")
        f = open("data.txt",'w')
        for i in range(0,volume):
            n = random.randint(1,volume)
            self.__dataSet.append(n)
            f.write(str(n)+'\n') 
        f.close()
            
        print("Data set generated successfully")


    def print_all(self):
        
        self.__max=open('max.txt','r').read()
        self.__min=open('min.txt','r').read()
        self.__avg=open('avg.txt','r').read()
        print('Max value : '+str(self.__max)+'\nMin value : '+str(self.__min)+'\nAverage value : '+str(self.__avg))
        