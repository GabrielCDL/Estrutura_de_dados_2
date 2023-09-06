class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    if node is None:
        return 0
    return node.height


def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


def update_height(node):
    if node is not None:
        node.height = 1 + max(height(node.left), height(node.right))


def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)

    return x


def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    update_height(x)
    update_height(y)

    return y


def insert(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    update_height(root)

    balance = balance_factor(root)

    # Casos de rotação
    # Caso esquerda-esquerda
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Caso direita-direita
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Caso esquerda-direita
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Caso direita-esquerda
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def separar_completar_palavras(prefixo, words):
    palavras = words.split()
    palavras_completas = set()
    
    for palavra in palavras:
        if palavra.startswith(prefixo):
            palavras_completas.add(palavra)
    
    return list(palavras_completas)
    
# Exemplo de uso:

root = None
words = "O gato caça o rato, enquanto o cachorro caça o gato."
prefixo = "ca"
palavras_completas = separar_completar_palavras(prefixo, words)

for word in words:
    root = insert(root, words)

print("O prefixo é: ")
print(prefixo)

if palavras_completas:
    print("Palavras completadas:")
    for palavra in palavras_completas:
        print(palavra)
else:
    print("Nenhuma palavra encontrada com o prefixo fornecido.")
