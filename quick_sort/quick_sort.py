def partition(a,p,r):
	x=a[r]
	i=p-1
	j=p
	while j<r:
		if(a[j]<x):
			i=i+1
			temp=a[j]
			a[j]=a[i]
			a[i]=temp
		j=j+1
	temp=x
	a[r]=a[i+1]
	a[i+1]=temp
	# print(a)
	return i+1

def quick_sort(a,p,r):
	if p<r:
		q=partition(a,p,r)
		quick_sort(a,p,q-1)
		quick_sort(a,q+1,r)
	# print(a)

a=[2,8,7,1,3,5,6,4]
quick_sort(a,0,7)
print("a is ");
print(a)


