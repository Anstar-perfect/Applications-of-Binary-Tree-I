class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def print_k_distance_node_down(root,k):
    if root is None :
        return

    if k == 0:
        print(root.data,end=' ')
        return

    print_k_distance_node_down(root.left,k-1)
    print_k_distance_node_down(root.right,k-1) 

def print_k_distance_node(root,target,k):
    if root is None:
        return -1
    if root == target:
        print(f"Nodes at distance {k} from target Node {target.data}:")
        print_k_distance_node_down(root,k)
        return 0

    dl = print_k_distance_node(root.left,target,k)
    if dl != -1:
        if dl + 1 == k:
            print(root.data,end=' ')
        else:
            print_k_distance_node_down(root.right,k-dl-2)
        return 1+dl

    dr = print_k_distance_node(root.right,target,k)
    if dr != -1:
        if dr+1 ==k:
            print(root.data,end=' ')
        else:
            print_k_distance_node_down(root.left,k-dr-2)
        return 1+dr

    return -1

def main():
    root = Node(1)
    root.left = Node(2) 
    root.right = Node(3)
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)

    target = root.left.right
    k=2
    print_k_distance_node(root,target,k)
    print()
if __name__ == "__main__":
    main()   

