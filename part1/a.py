from tasks import Tasks
from threadsmanager import ParentThread
import timeit



def parallel(instance):
    '''
        Start the tasks in parallel.
                                        '''
    print("Parallel computing starts...\n")
    parent = ParentThread(None)
    parent.create_child(target=instance.calc_max)
    parent.create_child(target=instance.calc_min)
    parent.create_child(target=instance.calc_avg)
    parent.run_children()
    parent.run_parent(target=instance.print_all)
    print("Parallel computing ended.\n")
    

def single(instance):
    '''
        Start the tasks sequentially
                                        '''
    print("Single computing starts...\n")
    instance.calc_max()
    instance.calc_min()
    instance.calc_avg()
    instance.print_all()
    print("Single computing ended...\n")


if __name__ == '__main__':  

    '''
        Main.
        Calling the functions and 
            measure their time.
                                    '''

    volume = int(input("please enter the data set size : \n"))
    print("-------------------------------------------------\n")

    task = Tasks(volume = volume)


    start = timeit.default_timer()
    
    parallel(task)
    
    end = timeit.default_timer()

    elapsed_time = end-start

    print("time with threads: ",elapsed_time)
    print("-------------------------------------------------\n")
    
    start = timeit.default_timer()

    
    single(task)

    end = timeit.default_timer()
    elapsed_time = end-start

    print("time without threads: ",elapsed_time)
    print("-------------------------------------------------")
    