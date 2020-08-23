from collections import deque


baris = [-1, 0, 0, 1]
kolom = [0, -1, 1, 0]


def isValid(mat, visited, row, col):
	return (baris >= 0) and (baris < M) and (kolom >= 0) and (kolom < N) \
		   and mat[row][col] == 1 and not visited[row][col]


def BFS(mat, i, j, x, y):

	visited = [[False for x in range(N)] for y in range(M)]

	q = deque()

	visited[i][j] = True

	q.append((i, j, 0))

	min_dist = float('inf')

	while q:

		(i, j, dist) = q.popleft()

		if i == x and j == y:
			min_dist = dist
			break

		for k in range(4):
			if isValid(mat, visited, i + row[k], j + col[k]):

				visited[i + row[k]][j + col[k]] = True
				q.append((i + row[k], j + col[k], dist + 1))

	if min_dist != float('inf'):
		print("The shortest path from source to destination has length", min_dist)
	else:
		print("Destination can't be reached from given source")


if __name__ == '__main__':

	mat = [
		[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
		[0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
		[0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
		[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
		[1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
		[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
		[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
		[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
		[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
	]

	M = N = 10

	BFS(mat, 0, 0, 7, 5)
