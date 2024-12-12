"""
Using the struct Module
- Write binary data from C structs
- Read binary data in Python
- Create data object classes
- Diagnose binary problems

"""

""" C99 varient.
# include <stdio.h>
struct Vector {
    float x;
    float y;
    float z;
};

struct Color{
    unsigned short int red;
    unsigned short int green;
    unsigned short int blue;
};

struct Vertex{
    struct Vector position;
    struct Color color;
};

int main(int argc, char** argv) {
    struct Vertex vertices[] = {
        {.position = { 3323.176, 6562.23, 9351.231},
        .color = {3040, 34423, 54321}
        },
        {.position = { 7623.982, 2532.231, 9823.121},
        .color = {32736, 5342, 2321}
        },
        {.position = { 6729.862, 2347.212, 3421.322},
        .color = {45263, 36291, 36701}
        },
        {.position = { 6352.121, 3432.131, 9763.232},
        .color = {56222, 36612, 11214}
        },
    }
};

File* file = fopen("colors.bin", "wb");

if (file == NULL){
    return -1;
}

fwrite(vertices, sizeof(struct Vertex), 4, file);
fclose(file);

return ;
}
"""


import struct
import pprint as pp
from binascii import hexlify

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)
class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.blue = blue
        self.green = green
    def __repr__(self):
        return 'Color({},{},{})'.format(self.red, self.blue, self.green)
    
class Vertex:
    def __init__(self, vector, color):
        self.vector = vector
        self.color = color 
    def  __repr__(self):
        return 'Vertex({!r}, {!r})'.format(self.vector, self.color)

def make_colored_vertex(x, y, z, red, green, blue):
    return Vertex(Vector(x, y, z), Color(red, blue, green))

def main():
    with open('colors.bin', 'rb') as f:
        buffer = f.read()

    print("buffer: {} bytes".format(len(buffer)))
    
    indexes = ' '.join(str(n).zfill(2) for n in range(len(buffer)))
    print(indexes)

    hex_buffer = hexlify(buffer).decode('ascii')
    hex_pairs = ' '.join(hex_buffer[i: i+2] for i in range(0, len(hex_buffer), 2))
    print(hex_pairs)
    print(hexlify(buffer))

    vertices = []
    # for x, y, z, red, green, blue in struct.iter_unpack('@3f3H', buffer):
    #     vertex = make_colored_vertex(x, y, z, red, green, blue)
    #     vertices.append(vertex)
    #to read '@3f3Hxx' use this 'xx'
    for fields in struct.iter_unpack('@3f3Hxx', buffer):
        vertex = make_colored_vertex(*fields)
        vertices.append(vertex)
    pp(vertices)
    # items = struct.unpack_from('@fffHHH', buffer) # returns tuple
    x, y, z, red, green, blue = struct.unpack_from('@3f3H', buffer)

    print(repr(x, y, z, red, green, blue))

if __name__ == '__main__':
    main()

"""
Format CType PythonType StandardSize Notes
x;pad_byte;novalue;;
c;char;bytesoflength1;1;
b;signedchar;integer;1;(1),(3)
a;unsignedchar;integer;1;(3)
.
.
.
https://docs.python.org/3/library/struct.html
"""