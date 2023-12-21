import csv

class EmployeeNode:
    def __init__(self, first_name, last_name, salary, gender, department, car_driven):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.gender = gender
        self.department = department
        self.car_driven = car_driven
        self.left = None
        self.right = None
        self.colleagues = []

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, employee_node):
        if not self.root:
            self.root = employee_node
        else:
            self._insert_recursive(self.root, employee_node)

    def _insert_recursive(self, current_node, employee_node):
        if employee_node.salary < current_node.salary:
            if current_node.left is None:
                current_node.left = employee_node
            else:
                self._insert_recursive(current_node.left, employee_node)
        else:
            if current_node.right is None:
                current_node.right = employee_node
            else:
                self._insert_recursive(current_node.right, employee_node)

        # Establish relationship based on shared department
        if employee_node.department == current_node.department:
            current_node.colleagues.append(employee_node)
            employee_node.colleagues.append(current_node)
            
    def inorder_traversal(self, node):
        result = []
        if node:
            # Traverse the left subtree
            result += self.inorder_traversal(node.left)
            # Visit the root
            result.append(node.first_name)
            # Traverse the right subtree
            result += self.inorder_traversal(node.right)
        return result

    def preorder_traversal(self, node):
        result = []
        if node:
            # Visit the root
            result.append(node.first_name)
            # Traverse the left subtree
            result += self.preorder_traversal(node.left)
            # Traverse the right subtree
            result += self.preorder_traversal(node.right)
        return result

    def postorder_traversal(self, node):
        result = []
        if node:
            # Traverse the left subtree
            result += self.postorder_traversal(node.left)
            # Traverse the right subtree
            result += self.postorder_traversal(node.right)
            # Visit the root
            result.append(node.first_name)
        return result
    
    def search_by_salary(self, node, max_salary, result=None):
        if result is None:
            result = []
    
        if node:
            # Check if the node's salary is less than the specified maximum salary
            if node.salary < max_salary:
                result.append(node)
    
            # Recursively search the left subtree
            self.search_by_salary(node.left, max_salary, result)
    
            # Recursively search the right subtree
            self.search_by_salary(node.right, max_salary, result)
    
        return result

# Function to read data from CSV and populate the binary tree
def populate_tree_from_csv(file_path, binary_tree):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            employee_node = EmployeeNode(
                row['first_name'],
                row['last_name'],
                int(row['salary']),
                row['gender'],
                row['department'],
                row['car']
            )
            binary_tree.insert(employee_node)

# Example usage:
csv_file_path = 'employee_data.csv'

# Create a binary tree
binary_tree = BinaryTree()

# Populate the binary tree from the CSV file
populate_tree_from_csv(csv_file_path, binary_tree)

#search employee with wages less than a certain amount
max_salary_threshold = 5000
result_salary = binary_tree.search_by_salary(binary_tree.root, max_salary_threshold)

# Display the results
for employee_node in result_salary:
    print(f"{employee_node.first_name} {employee_node.last_name} has a salary less than {max_salary_threshold}")


#different ways to traverse the tree
#result_inorder = binary_tree.inorder_traversal(binary_tree.root)
#result_preorder = binary_tree.preorder_traversal(binary_tree.root)
#result_postorder = binary_tree.postorder_traversal(binary_tree.root)

#print("Inorder Traversal:", result_inorder)
#print("Preorder Traversal:", result_preorder)
#print("Postorder Traversal:", result_postorder)
