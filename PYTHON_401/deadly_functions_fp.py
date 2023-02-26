# fonksiyonel programlama fp

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines = read('deneme.txt')
lines_count = count(example_lines)
print(example_lines)
print(lines_count)