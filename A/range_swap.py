n,p,q,r,s = map(int, input().split())
a_list = list(map(int, input().split()))

a_list[r-1:s], a_list[p-1:q] = a_list[p-1:q], a_list[r-1:s]
print(*a_list)