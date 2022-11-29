#Write a function to print out the frequency of all the unique elements present in a given tuple.

Sample Input:

(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
Sample Output:

10 : 3
8 : 4
5 : 2
2 : 2
15 : 1



def unique_count(tup):
    ''' input:tup-indicates the tuple
         output:Print the unique elements and their frequency'''
    
    # YOUR CODE GOES HERE
    k = 0

    for i in tup:
        if tup.index(i)==k:
            print(i,":",tup.count(i))
        k+=1