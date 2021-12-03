import multiprocessing
from multiprocessing.queues import JoinableQueue

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
        self.__children.append(ChildThread(target=target,args=args))
        

             
    def run_children(self):
        '''
            Runs all the children at once.
                                            '''
        p = []
        for child in self.__children : p.append(multiprocessing.Process(target=child.target))
        for process in p : process.start()
        for process in p : process.join()

    def run_parent(self,target=None,args=None):
        '''
            Runs parents target function.
                                            '''
        if target:
            self.__target = target
        if args:    
            self.__args = args
            m = multiprocessing.Process(target = self.__target,args=self.__args)
            
        else:
            m = multiprocessing.Process(target = self.__target)
        m.start()
        m.join()

        