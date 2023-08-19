n,k=map(int,input().split())
b=0
num_alphabet=0
while k > num_alphabet:
	b=b+1
	pre_num_alpha=num_alphabet
	num_alphabet=(n**b)*b+num_alphabet
num_alphabet =  (k - pre_num_alpha) %  b
num_word = (k - pre_num_alpha)/b
int_num_word = int(num_word)
if  int_num_word != num_word:
	num_word=int_num_word+1
if num_alphabet == 0:
	num_alphabet = b
num_word=int(num_word)
if num_word == n ** b :
	print(chr(97+n-1))
else:
	num_word=num_word-1
	if num_word == 0:
		nums= [0]
	else:
		nums = []
		while num_word:
			num_word, r = divmod(num_word, n)
			nums.append((r))
	nums=nums[::-1]
	pos=num_alphabet - ((b-len(nums))+1)
	if pos >= 0 :
		print(chr(nums[pos]+97))
	else:
		print(chr(97+0))

#extra solution with recursive function----------------------->>>>>



# def CA1_DS(x,base_mat,finall_mat,n):
# 	size=len(''.join(finall_mat))
# 	if size < n:
# 		mat=[]
# 		for i in range(0,len(x)):
# 			for j in range(0,len(base_mat)):
# 				val=x[i]+base_mat[j]
# 				mat.append(val)
# 		finall_mat.extend(mat)
# 		return CA1_DS(mat,base_mat,finall_mat,n)
# 	else:
# 		return(finall_mat) #please explain this part for me?i don't know why this part work correctly
# val=input().split()
# k=int(val[0])
# n=int(val[1])
# alphabet=[];
# for i in range(97,97+k):
# 	alphabet.append(chr(i))
# new_alphabet=alphabet[:]	# we use it copy in another place :)
# ans_mat=''.join(CA1_DS(alphabet,alphabet,new_alphabet,n))
# print(ans_mat[n-1])		