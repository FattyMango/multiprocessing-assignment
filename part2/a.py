import random
import numpy as np
import timeit

from threadsmanager import ParentThread

class List:
    '''
        A class to create and manage lists(array)
         and make all the needed process on them.

        We will use numpy since it can create and split 
         lists with a good complexitiy time.
                                                        '''
    def __init__(self,dataSet=None,volume=0) -> None:
        
        self.__dataSet = dataSet
        self.__volume = volume
        if not dataSet:
            self.generate_set()
    
    def generate_set(self):
        print("Generating data set...\n")
        self.__dataSet = np.arange(self.__volume)
        print("Data set generated successfully.\n")
        

    def shuffle_set(self):
        random.shuffle(self.__dataSet)   
        

    def split_set(self):
        split = []
        for l in np.split(self.__dataSet,4):
            split.append(list(l))
        return split
    def sort_set(self):
        self.__dataSet.sort()
        
        return self.__dataSet
    def get_dataSet(self):
        return self.__dataSet

def merge_sets(sets): 
    '''
        Takes a list of lists and merge them
         together.

        Only prints the first 10 elemnts to make 
         the output secreen clean and readable.
                                                '''
    final = []
    for set in sets:
        for i in set:
            
            final.append(i)
    final.sort()
    lnth = len(final)
    print(str(final[0:10])+'...'+str(final[lnth-10:lnth]))
def subList_process(file):
    '''
    Takes a file name that contains the list elements
        then shuffle it and sort it.
                                                    '''
    print("start")
    
    with open(file) as file_in:
        list = []
        for line in file_in:
            list.append(int(line))
    
    l = List(dataSet=list)
    l.shuffle_set()
    l.sort_set()
    print("done")
    return l.get_dataSet()
def single():
    '''
        Start the tasks sequentially
                                        '''

    print("Single computing starts...\n")
    
    x = []
    x.append(subList_process('1.txt'))
    x.append(subList_process('2.txt'))
    x.append(subList_process('3.txt'))
    x.append(subList_process('4.txt'))
    merge_sets(x)     
    print("Single computing ended...\n")

def parallel():
    '''
        Start the tasks in parallel.
                                        '''
    parent = ParentThread(None)
       
    parent.create_child(target=subList_process,args=["1.txt","2.txt","3.txt","4.txt"])
    res = parent.run_children()  
    parent.run_parent(target=merge_sets,args=res)

    
    print("Parallel computing ended.\n")

def writetxt(lists):
    '''
        Write sub lists to their .txt files
                                            '''

    f = open("1.txt",'w')
    for i in lists[0]:
      f.write(str(i)+'\n') 
    f.close()
    
    f = open("2.txt",'w')
    for i in lists[1]:
      f.write(str(i)+'\n')   
    f.close()

    f = open("3.txt",'w')
    for i in lists[2]:
      f.write(str(i)+'\n')   
    f.close()

    f = open("4.txt",'w')
    for i in lists[3]:
      f.write(str(i)+'\n')   
    f.close()
   

if __name__ == '__main__':  
    '''
        Main.
        Calling the functions and 
            measure their time.
                                    '''
    volume = int(input("please enter the data set size : \n"))
    print("-------------------------------------------------\n") 
    l = List(volume = volume)
    
    
    l.shuffle_set()
    lists = l.split_set()
    
    writetxt(lists)
    print("Parallel computing starts...\n")
    start = timeit.default_timer()
    
    
    parallel()

    end = timeit.default_timer()
    elapsed_time = end-start

    print("time with threads: ",elapsed_time)
    print("-------------------------------------------------\n")
    
    


    
    start = timeit.default_timer()

    single()

    end = timeit.default_timer()
    elapsed_time = end-start
    print("time without threads: ",elapsed_time)
    print("-------------------------------------------------")
    