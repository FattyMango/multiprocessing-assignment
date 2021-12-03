
from multiprocessing import Pool
import multiprocessing
class ChildThread:
    '''
        A class to serialize child data.
                                        '''
    def __init__(self,target,args=None) -> None:
        self.target = target
        self.args = args
        
    
    
          
class ParentThread:
    '''
    A class for parent thread 
        to manage and run children
        which waits the children
        to finish then start
        execution.
                                '''
    def __init__(self,target,args = None) -> None:
        self.__children = []
        self.__target = target
        self.__args = args
        
        
        
    def create_child (self,target,args=None):
        
        if args:      
            self.__children.append(ChildThread(target=target,args=args))
        else:
            self.__children.append(ChildThread(target=target))

             
    def run_children(self):
        '''
            Runs all the children at once.
                                            '''
        pool = Pool(4)  
        return pool.map(self.__children[0].target,self.__children[0].args)
        
    def run_parent(self,target=None,args=None):
        '''
            Runs parents target function.
                                            '''
        if target:
            self.__target = target
        if args:    
            self.__args = args

        m = multiprocessing.Process(target = self.__target,args=(self.__args,))
        m.start()
        m.join()