def swap(a,b):
    # print("initial A", a, ", initial B", b) # debugging
    temp = a
    a, b = b, temp    
    # print("end A", a, ", end B", b) # debugging
    return a, b

def bubble_sort(a):
    input_length = len(a)
    idx = 0
    while idx < input_length:
        jdx = 0
        while jdx < input_length - idx - 1:
            # first_value = a[jdx]
            # second_value = a[jdx+1]
            # print(idx) # debugging
            # check if current index of element is greater then the element on right
            if a[jdx] > a[jdx+1]:
                # print(a[idx-1] > a[idx]) # debugging
                # swap
                swappeda, swappedb = swap(a[jdx], a[jdx+1])
                print("from a", a[jdx],"swapped to b", swappeda) # debugging
                print("from b", a[jdx+1],"swapped to a", swappedb) # debugging
                a[jdx], a[jdx+1] = swappeda, swappedb
                
            jdx += 1
        idx += 1
    return a

a = []
number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element : " %i))
    a.append(value)
print("The Sorted List in Ascending Order : ", bubble_sort(a))