def binary_search(sequence,number):
    begin=0
    end=len(sequence)

    while begin<=end:
        midpoint=begin+(end-begin)//2
        midpoint_value=sequence[midpoint]
        if midpoint_value==number:
           return midpoint

        elif number < midpoint_value:
            end=midpoint
        else:
            begin=midpoint

    return None


array=[1,3,4,5,6,7,8,9,11,23,45,67]
item=3
print("number found at",binary_search(array,item)+1,"th position")

