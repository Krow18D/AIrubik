from cube import *
import datetime
import sys

class Node :
    current_path = []
    amount = 0
    _max = 0
    def __init__(self, cube, level):
        self.cube = deepcopy(cube)
        if not current_path:#check if current path is empty
            self.move = ["L","L'","L2","R","R'","R2","F","F'","F2","D","D'","D2","U","U'","U2","B","B'","B2"]
        elif current_path[-1] == "L" or current_path[-1] == "L'" or current_path[-1] == "L2":
            self.move = ["R","R'","R2","F","F'","F2","D","D'","D2","U","U'","U2","B","B'","B2"]
        elif current_path[-1] == "R" or current_path[-1] == "R'" or current_path[-1] == "R2":
            self.move = ["L","L'","L2","F","F'","F2","D","D'","D2","U","U'","U2","B","B'","B2"]
        elif current_path[-1] == "F" or current_path[-1] == "F'" or current_path[-1] == "F2":
            self.move = ["L","L'","L2","R","R'","R2","D","D'","D2","U","U'","U2","B","B'","B2"]
        elif current_path[-1] == "D" or current_path[-1] == "D'" or current_path[-1] == "D2":
            self.move = ["L","L'","L2","R","R'","R2","F","F'","F2","U","U'","U2","B","B'","B2"]
        elif current_path[-1] == "U" or current_path[-1] == "U'" or current_path[-1] == "U2":
            self.move = ["L","L'","L2","R","R'","R2","F","F'","F2","D","D'","D2","B","B'","B2"]
        elif current_path[-1] == "B" or current_path[-1] == "B'" or current_path[-1] == "B2":
            self.move = ["L","L'","L2","R","R'","R2","F","F'","F2","D","D'","D2","U","U'","U2"]
        self.level = level
        Node.amount += 1
        #print(Node.amount)
        Node._max  = max(Node._max, Node.amount)
    def __del__(self):
        #print("del",Node.amount)
        Node.amount -= 1

current_path = []
success = False

# def DLSearch(node,depth_limit):
#     global success
#     #print(current_path)
#     #node.cube.print_cube()
#     if node.cube.check_is_goal(goal_cube):
#         return True
#     if node.level == depth_limit:
#         current_path.pop()
#         return False
#     while (not not node.move) and success!= True:
#         current_path.append(node.move.pop(0))
#         #create a node before delete a old one
#         new_node = Node(node.cube, node.level+1)
#         new_node.cube.scramble(current_path[-1])
#         success = DLSearch(new_node, depth_limit)
#     if success == True:
#         return True
#     if not not current_path:
#         current_path.pop()
#         return False
#     return False

# def IDSearch(node,level_limit):
#     for i in range(1,level_limit):
#         success = DLSearch(Node(node.cube, node.level),i)
#         if success:
#             return success

# Initialise pieces
corners = [Corner(0, 0, 'ryb'), Corner(1, 0, 'rgy'), Corner(2, 0, 'rwg'), Corner(3, 0, 'rbw'), Corner(4, 0, 'owb'), Corner(5, 0, 'ogw'), Corner(6, 0, 'oyg'), Corner(7, 0, 'oby')]
edges = [Edge(0, 0, 'ry'), Edge(1, 0, 'rg'), Edge(2, 0, 'rw'), Edge(3, 0, 'rb'), Edge(4, 0, 'yb'), Edge(5, 0, 'wb'), Edge(6, 0, 'wg'), Edge(7, 0, 'yg'), Edge(8, 0, 'ow'), Edge(9, 0, 'og'), Edge(10, 0, 'oy'), Edge(11, 0, 'ob')]
centers = [Center(0, 'r'), Center(1, 'b'), Center(2, 'w'), Center(3, 'g'), Center(4, 'y'), Center(5, 'o')]
current_cube = Cube()
current_cube.cos = deepcopy(corners)
current_cube.eds = deepcopy(edges)
current_cube.ces = deepcopy(centers)

goal_cube = deepcopy(current_cube)

# Program control
if len(sys.argv) == 1:
    try:
        s = open('scramble.txt', 'r').read()
    except:
        print("No scramble")
        s = ""
else:
    s = sys.argv[1]

# def check_multiDepth(cube,search_func):
#     global current_path
#     global success
#     level_limit = 5
#     #for i in range(1,9):
#     #current_cube.print_cube()
#     Node._max = 0
#     node = Node(cube,0)
#     print(type(node))
#     print("one node(state) =",sys.getsizeof(node), "bytes")
#     #level_limit = i
#     start_time = datetime.datetime.now()
#     print("Started Time: ",start_time.strftime("%H:%M:%S:%f"))
#     if search_func == 'IDS' :
#         success = IDSearch(node,level_limit+1)
#     elif search_func == 'DLS':
#         success = DLSearch(node,level_limit)
#     end_time = datetime.datetime.now()
#     print("Ended Time: ",end_time.strftime("%H:%M:%S:%f"))
#     print("depth limit :"+str(level_limit)+" Time interval:"+str(end_time - start_time))
#     print("node(state) mem=",sys.getsizeof(node)*Node._max, "bytes")
#     print(success, current_path)
#     success = False
#     current_path = []

if __name__ == '__main__':
    current_cube.scramble(s)
    current_cube.print_cube()
    # print("DLS")
    # check_multiDepth(current_cube,'DLS')
    # print("IDS")
    # check_multiDepth(current_cube,'IDS')
