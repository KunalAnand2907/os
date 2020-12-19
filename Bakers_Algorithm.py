# BANKER'S ALGORITHM
""" 1.) n- no. of Processes, 2.) m-no. of resources
3.) Available-It is a 1-d array of size ‘m’ indicating the number of available resources of each type.
4.) System Max-It is a 1-d array of size ‘m’ indicating the max number of resources of each type in system.
5.) Max Need - It is a 2-d array of size ‘n*m’ that defines the maximum demand of each process in a system.
Max[ i, j ] = k means process Pi may request at most ‘k’ instances of resource type Rj.
6.) Allocation - It is a 2-d array of size ‘n*m’ that defines the number of resources of each type currently allocated to each process.
Allocation[ i, j ] = k means process Pi is currently allocated ‘k’ instances of resource type Rj
7.) Current Need - It is a 2-d array of size ‘n*m’ that indicates the remaining resource need of each process.
Need [ i, j ] = k means process Pi currently allocated ‘k’ instances of resource type Rj
Need [ i, j ] = Max [ i, j ] – Allocation [ i, j ]
""" 
P = 4
R = 3
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
# Function to find the current need of resources
def CalculateNeed(max_need,allocation,curr_need):
        for i in range(P):
            for j in range(R):
                curr_need[i][j]=max_need[i][j] - allocation[i][j]

# Function to find system is in Safe State or Not
def isSafe(max_need,allocation,available):    
        curr_need=[]
        for i in range(P): 
            l = [] 
            for j in range(R): 
                l.append(0) 
        curr_need.append(l) 
        CalculateNeed(max_need,allocation,curr_need)            
             
   # Mark all processes as infinish  
        finish = [0] * P 
      
    # To store safe sequence  
        safeSeq = [0] * P  
  
    #copy of available resources  
        work = [0] * R  
        for i in range(R): 
            work[i] = available[i]  
 
        count = 0
        while (count < P):  
            found = False
            for p in range(P):  
               if (finish[p] == 0):  
                  for j in range(R): 
                    if (curr_need[p][j] > work[j]): 
                        break
                        
                  if (j == R - 1):  
                     for k in range(R):  
                        work[k] += allocation[p][k]  
                     safeSeq[count] = p 
                     count += 1

                     finish[p] = 1
  
                     found = True
                  
        if (found == False): 
            print("System is not in safe state") 
            return False
        
        print("System is in safe state.", 
              "\nSafe sequence is: ", end = " ") 
        print(*safeSeq)  
  
        return True


# Driver code  
if __name__ =="__main__": 
    processes = [0,1,2,3]
    available = [3,3,0]
    max_need = [[4, 3, 1], [2, 1, 4],[1, 3, 3], [5, 4, 1]]
    allocation = [[1,0,1],[1,1,2],[1,0,3],[2,0,0]]
    
    isSafe(available, max_need, allocation) 