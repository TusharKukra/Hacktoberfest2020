def rotate_square_matrix(sq_matrix):
	for i in range(length):
		for j in range(i):
			temp=sq_matrix[i][j]
			sq_matrix[i][j]=sq_matrix[j][i]
			sq_matrix[j][i]=temp
	for i in range(length):
		for j in range(length // 2):
			temp=sq_matrix[i][j]
			sq_matrix[i][j]=sq_matrix[i][length-j-1]
			sq_matrix[i][length-j-1]=temp



sq_matrix = [
	[11,12,13,14],
	[15,16,17,18],
	[19,20,21,22],
	[23,24,25,26]
]

length = len(sq_matrix)

rotate_square_matrix(sq_matrix)

for i in range(length):
	print(sq_matrix[i])
	
print("The above matrix is rotated by 90 degrees clockwise")