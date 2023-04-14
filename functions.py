#importance of functions
tom_exp=[2100,6789,9000]
joe_exp=[5678,9321,5000]

def calc_total_exp(exp):
    total=0;
    for item in exp:
        total=total+item
    return total;

print("tom's total expense is: ",calc_total_exp(tom_exp))
print("joe's total expense is: ",calc_total_exp(joe_exp))

#example-sum
def sum(a,b):
    return a+b

print(sum(4,7))