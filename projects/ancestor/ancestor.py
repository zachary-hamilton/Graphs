from collections import deque

def earliest_ancestor(ancestors, starting_node):
    vertices = {}    
    # looping through to create the vertices
    for each in ancestors:
        if each[0] not in vertices:
            vertices[each[0]] = set()
        if each[1] not in vertices:
            vertices[each[1]] = set()
    # looping through to add the edges
    for each in ancestors:
        # (parent, child) is order given and we want direction to go from child to parent
        vertices[each[1]].add(each[0])

    # creating a list of all possible paths
    final_paths = []
    queue = deque()
    queue.append([starting_node])
    while len(queue) > 0:
        curr_path = queue.pop()
        curr_node = curr_path[-1]
        if vertices[curr_node] == set():
            new_path = list(curr_path)
            final_paths.append(new_path)
        for each in vertices[curr_node]:
            new_path = list(curr_path)
            new_path.append(each)
            queue.append(new_path)

    # finding which path is the longest 
    path_dict = {}
    for each in final_paths:
        if len(each) not in path_dict:
            path_dict[len(each)] = [each]
        else:
            path_dict[len(each)].append(each)
    longest_path = [0, []]
    for key, value in path_dict.items():
        if key == longest_path[0]:
            longest_path[1].append(value)
        if key > longest_path[0]:
            longest_path[0] = key
            longest_path[1] = value

    # scenario where there are no ancestors
    if starting_node == longest_path[1][0][-1]:
        return -1 
    # scenario when there is only a single longest path
    if len(longest_path[1]) == 1:
        return longest_path[1][0][-1]
    # scenario where there are multiple equal longest paths
    lowest_id = longest_path[1][0][-1]
    for each in longest_path[1]:
        if each[-1] < lowest_id:
            lowest_id = each[-1]
    return lowest_id