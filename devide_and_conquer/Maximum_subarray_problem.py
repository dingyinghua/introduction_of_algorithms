def find_max_crossing_subarray(A,low,mid,high):
	left_sum=float('-inf')
	sum=0
	i=mid
	# max_left=mid
	while i>=low:
		sum+=A[i]
		if sum>left_sum:
			left_sum=sum
			max_left=i
		i-=1
	right_sum=float('-inf')
	sum=0
	i=mid+1
	while i<=high:
		sum+=A[i]
		if sum>right_sum:
			right_sum=sum
			max_right=i
		i+=1
	return (max_left,max_right,left_sum+right_sum)

def find_maximum_subarray(A,low,high):
	if high==low:
		return (low,high,A[low])
	else:
		mid=(low+high)//2
		left=find_maximum_subarray(A,low,mid)
		right=find_maximum_subarray(A,mid+1,high)
		cross=find_max_crossing_subarray(A,low,mid,high)
		if left[2]>=cross[2] and left[2]>=right[2]:
			return (left[0],left[1],left[2])
		elif right[2]>=left[2] and right[2] >=cross[2]:
			return (right[0],right[1],right[2])
		else:
			return (cross[0],cross[1],cross[2])


def find_maximum_subarray_test():
	A=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
	print(find_maximum_subarray(A,0,15))


find_maximum_subarray_test()

