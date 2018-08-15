from collections import deque

def bfs(root):
    q = deque()
    q.append(root)
    visited = []
    visited.append(root)

    while len(q) > 0:
        node = q.popleft()
        print(node.val)
        if node.left:
            if node.left not in visited:
                q.append(node.left)
                visited.append(node.left)
        if node.right:
            if node.right not in visited:
                q.append(node.right)
                visited.append(node.right)