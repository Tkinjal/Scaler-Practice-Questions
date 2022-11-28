#Problem Description:

#Given the input date in DD/MM/YYYY format as a string, write a function that returns the converted date in the string formats MM/DD/YYYY #and YYYY/MM/DD and return the new date formats.

def date_format(date):
    '''Input: date takes the string as input
       Output:return resultant date formats'''


    l = date.split("/")

    return ("{}/{}/{}".format(l[1],l[0],l[2])), ("{}/{}/{}".format(l[2],l[1],l[0]))
    # YOUR CODE GOES HERE

