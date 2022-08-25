nodes, routes = map(int, input().split())
graph_list = list(map(int, input().split()))
root_node = 1

def DFS_with_adj_list(graph, start_node):
    visited_list = []
    dfs_stack = [start_node]

    while dfs_stack:
        node = dfs_stack.pop()
        if node not in visited_list:
            visited_list.append(node)
            dfs_stack.append(graph[node])
    return visited_list

print(DFS_with_adj_list(graph_list, root_node))