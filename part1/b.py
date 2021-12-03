
from tasks import Tasks
from threadsmanager import ParentThread
import time
import timeit

class Prime :
    '''
        A class to calculate the prime number from a random 
         data set.
        
        since the process needs only one thread there is
         no need to use files.
                                                            '''
    def __init__(self,volume) -> None:
        self.__volume = volume 
        self.__dataSet = Tasks(volume=self.__volume).get_dataSet()
    def is_prime(self,num):
        if num > 1:

            for i in range(2, int(num/2)+1):
                if (num % i) == 0:return False
                    
            else:return True

        else:return False

    def Solution(self,target_num):
        
        solSet = []
        for num in  self.__dataSet:
            if num<= target_num:
                flag = self.is_prime(num)
                if flag: solSet.append(num)
                else : pass
            else : pass
        print ('Prime numbers in the data set are : \n',set(solSet))
        print()

def parallel(instance,target_num):
    '''
        Start the tasks in parallel.
                                        '''
    parent = ParentThread(target=instance.Solution)
    print("Parallel computing starts...\n")
    parent.run_parent(args=(target_num,))
    print("Parallel computing ended.\n")
    

def single(instance,target_num):
    '''
        Start the tasks sequentially
                                        '''
    print("Single computing starts...\n")
    instance.Solution(target_num)
    print("Single computing ended...\n")

if __name__ == '__main__':   
    
    '''
        Main.
        Calling the functions and 
            measure their time.
                                    ''' 
    
    volume = int(input("Please enter the data set size : \n"))

    target_num = int(input("Please enter the target number : \n"))
    print("-------------------------------------------------\n")



    prime = Prime(volume=volume)
    t = time.process_time()
    start = timeit.default_timer()
    parallel(prime,target_num)
    end = timeit.default_timer()
    elapsed_time = end-start
    print("time with threads: ",elapsed_time)
    print("-------------------------------------------------\n")
    
   
    
    t = time.process_time()
    
    start = timeit.default_timer()
    single(prime,target_num)
    end = timeit.default_timer()
    elapsed_time = end-start
    print("time without threads: ",elapsed_time)
    print("-------------------------------------------------")