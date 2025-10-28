with open(r'C:\Users\mingh\Documents\Github\CTF-writeups\NexusCTF\Miscellaneous\Annoying Yes\encoded.txt', 'r') as f:
    input_data = f.read().strip()
    lines = input_data.split('/')
    print(lines)

    output = ''
    for line in lines:
        chars = line.split(' ')
        for char in chars:
            if char == '-----':
                output += '0'
            elif char == '.----':
                output += '1'
        output += ' '
    print(output)