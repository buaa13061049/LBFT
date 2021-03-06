from mpi4py import MPI
import tx

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

group = comm.Get_group()
group1 = group.Incl([0,4,5])
group2 = group.Incl([1,4,5])
group3 = group.Incl([2,4,5])
group4 = group.Incl([3,4,5])
group5 = group.Incl([4,6])
group6 = group.Incl([5,6])
group7 = group.Incl([6,4,5])
group8 = group.Incl([4,0,1,2,3])
group9 = group.Incl([5,0,1,2,3])

comm_size = comm.Get_size()
comm1 = comm.Create(group1)
comm2 = comm.Create(group2)
comm3 = comm.Create(group3)
comm4 = comm.Create(group4)
comm5 = comm.Create(group5)
comm6 = comm.Create(group6)
comm7 = comm.Create(group7)
comm8 = comm.Create(group8)
comm9 = comm.Create(group9)

if 0<=comm_rank<=3:
    start = MPI.Wtime() 
    data = tx.create()
    comm.send(data,dest=4)
    comm.send(data,dest=5)

    data=comm.recv(source=4)
    data1=data
#    print ('rank %d :receive from rank4'%comm_rank,data)
    data=comm.recv(source=5)
#    print ('rank %d :receive from rank5'%comm_rank,data)
    if data == data1:
        print ('rank %d :Get block'%comm_rank,data)
        for ctx in data:
            if not tx.validate(ctx):
                print('rank %d :InvalidSignature'%comm_rank)
                
        comm.send([comm_rank*2],dest=4)
        comm.send([comm_rank*2],dest=5)

    data=comm.recv(source=4)
    data1=data
#    print ('rank %d :receive from rank4'%comm_rank,data)
    data=comm.recv(source=5)
#    print ('rank %d :receive from rank5'%comm_rank,data)
    if data == data1:
        print ('rank %d :Get votes'%comm_rank,data)
    stop = MPI.Wtime()
    print("rank %d time:%lfs\n"%(comm_rank,stop-start))

if 4<=comm_rank<=5:
    data=comm.recv(source=0)
#    print ('rank %d :receive'%comm_rank,data)
    comm.send(data,dest=6)
    data=comm.recv(source=1)
#    print ('rank %d :receive'%comm_rank,data)
    comm.send(data,dest=6)
    data=comm.recv(source=2)
#    print ('rank %d :receive'%comm_rank,data)
    comm.send(data,dest=6)
    data=comm.recv(source=3)
#    print ('rank %d :receive'%comm_rank,data)
    comm.send(data,dest=6)

    data=comm.recv(source=6)
#    print ('rank %d :receive'%comm_rank,data)
    comm.send(data,dest=0)
    comm.send(data,dest=1)
    comm.send(data,dest=2)
    comm.send(data,dest=3)
    for ctx in data:
        if not tx.validate(ctx):
            print('rank %d :InvalidSignature'%comm_rank)
    comm.send([comm_rank*2],dest=6)

    data=comm.recv(source=0)
#    print ('rank %d :receive'%comm_rank,data)
    comm.send(data,dest=6)
    data=comm.recv(source=1)
#    print ('rank %d :receive'%comm_rank,data)
    comm.send(data,dest=6)
    data=comm.recv(source=2)
#    print ('rank %d :receive'%comm_rank,data)
    comm.send(data,dest=6)
    data=comm.recv(source=3)
#    print ('rank %d :receive'%comm_rank,data)
    comm.send(data,dest=6)

    data=comm.recv(source=6)
#    print ('rank %d :receive'%comm_rank,data)
    comm.send(data,dest=0)
    comm.send(data,dest=1)
    comm.send(data,dest=2)
    comm.send(data,dest=3)

if comm_rank == 6:
    ids = []
    data1=comm.recv(source=4)
#    print ('rank %d :receive from rank4:'%comm_rank,data)
    data=comm.recv(source=5)
#    print ('rank %d :receive from rank5:'%comm_rank,data)
    if data == data1 :
        ids.append(data)

    data1=comm.recv(source=4)
#    print ('rank %d :receive from rank4:'%comm_rank,data)
    data=comm.recv(source=5)
#    print ('rank %d :receive from rank5:'%comm_rank,data)
    if data == data1 :
        ids.append(data)

    data1=comm.recv(source=4)
#    print ('rank %d :receive from rank4:'%comm_rank,data)
    data=comm.recv(source=5)
#    print ('rank %d :receive from rank5:'%comm_rank,data)
    if data == data1 :
        ids.append(data)

    data1=comm.recv(source=4)
#    print ('rank %d :receive from rank4:'%comm_rank,data)
    data=comm.recv(source=5)
#    print ('rank %d :receive from rank5:'%comm_rank,data)
    if data == data1 :
        ids.append(data)

    print('block:',ids)
    comm.send(ids,dest=4)
    comm.send(ids,dest=5)

    for ctx in ids:
        if not tx.validate(ctx):
            print('rank %d :InvalidSignature'%comm_rank)
    k=set([comm_rank*2])

    data=comm.recv(source=4)
    a=set(data)
#    print ('rank %d :receive from rank4:'%comm_rank,data)
    data=comm.recv(source=5)
    b=set(data)
#    print ('rank %d :receive from rank5:'%comm_rank,data)

    data=comm.recv(source=4)
    c=set(data)
#    print ('rank %d :receive from rank4:'%comm_rank,data)
    data=comm.recv(source=5)
    d=set(data)
#    print ('rank %d :receive from rank5:'%comm_rank,data)

    data=comm.recv(source=4)
    e=set(data)
#    print ('rank %d :receive from rank4:'%comm_rank,data)
    data=comm.recv(source=5)
    f=set(data)
#    print ('rank %d :receive from rank5:'%comm_rank,data)

    data=comm.recv(source=4)
    g=set(data)
#    print ('rank %d :receive from rank4:'%comm_rank,data)
    data=comm.recv(source=5)
    h=set(data)
#    print ('rank %d :receive from rank5:'%comm_rank,data)
    
    data=comm.recv(source=4)
    i=set(data)
#    print ('rank %d :receive from rank4:'%comm_rank,data)
    data=comm.recv(source=5)
    j=set(data)
#    print ('rank %d :receive from rank5:'%comm_rank,data)
    

    data=a|b|c|d|e|f|g|h|i|j|k
#    print('votes:',data)
    comm.send(data,dest=4)
    comm.send(data,dest=5)
