def process_instructions(instructions):
    # Initialize the register with all bits as '?'
    register = ['?'] * 32
    
    for instruction in instructions:
        parts = instruction.split()
        cmd = parts[0]
        if cmd == 'CLEAR':
            pos = int(parts[1])
            register[31 - pos] = '0'
        elif cmd == 'SET':
            pos = int(parts[1])
            register[31 - pos] = '1'
        elif cmd == 'AND':
            i = int(parts[1])
            j = int(parts[2])
            if register[31 - i] == '0' or register[31 - j] == '0':
                register[31 - i] = '0'
            elif register[31 - i] == '1' and register[31 - j] == '1':
                register[31 - i] = '1'
            else:
                register[31 - i] = '?'
        elif cmd == 'OR':
            i = int(parts[1])
            j = int(parts[2])
            if register[31 - i] == '1' or register[31 - j] == '1':
                register[31 - i] = '1'
            elif register[31 - i] == '0' and register[31 - j] == '0':
                register[31 - i] = '0'
            else:
                register[31 - i] = '?'
    
    return ''.join(register)

# Reading input
import sys
input = sys.stdin.read
data = input().strip().split('\n')

instructions = []
i = 0
while i < len(data):
    n = int(data[i])
    if n == 0:
        break
    instruction_block = data[i+1:i+1+n]
    instructions.append(instruction_block)
    i += n + 1

# Process each set of instructions and output the result
for instruction_block in instructions:
    result = process_instructions(instruction_block)
    print(result)
