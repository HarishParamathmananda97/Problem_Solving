"""
Using the struct Module
- Write binary data from C structs
- Read binary data in Python
- Create data object classes
- Diagnose binary problems
- MemoryView

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
import code  # import this code to view the local variable values using *locals()


class Vector:
    def __init__(self, mem_float32):
        if mem_float32.format not in "fd":
            raise TypeError("Vector: memoryview values must be floating-point numbers")
        if len(mem_float32) < 3:
            raise TypeError("Vector: memoryview must contain at least 3 floats")
        self._mem = mem_float32
        
    @property
    def x(self):
        return self._mem[0]
    def y(self):
        return self._mem[1]
    def z(self):
        return self._mem[2]
    
    def __repr__(self):
        return 'Vector({}, {}, {})'.format(self.x, self.y, self.z)
class Color:
    def __init__(self, mem_uint16):
        if mem_uint16.format not in "HILQ":
            raise TypeError("Color: memoryview values must be unsigned integers")
        if len(mem_uint16)< 3:
            raise TypeError("Color: memoryview must contain at least 3 integers")
        self._mem = mem_uint16

    @property
    def red(self):
        return self._mem[0]
    @property
    def green(self):
        return self._mem[0]
    @property
    def blue(self):
        return self._mem[0]
    def __repr__(self):
        return 'Color({},{},{})'.format(self.red, self.blue, self.green)
    
class Vertex:
    def __init__(self, vector, color):
        self.vector = vector
        self.color = color 
    def  __repr__(self):
        return 'Vertex({!r}, {!r})'.format(self.vector, self.color)

def make_colored_vertex(mem_vertex):
    mem_vector = mem_vertex[0:12].cast('f')
    mem_color = mem_vertex[12:18].cast('H')
    return Vertex(Vector(mem_vector), Color(mem_color))



def main():
    with open('colors.bin', 'rb') as f:
        buffer = f.read()

    print("buffer: {} bytes".format(len(buffer)))
    
    indexes = ' '.join(str(n).zfill(2) for n in range(len(buffer)))
    print(indexes)

    hex_buffer = hexlify(buffer).decode('ascii')
    hex_pairs = ' '.join(hex_buffer[i: i+2] for i in range(0, len(hex_buffer), 2))
    print(hex_pairs)
    # print(hexlify(buffer))

    # using memory view instances with BufferProtocal CAPI
    mem = memoryview(buffer)
    # interrupt the code by using (code.interact) and lets you run in terminal
    # code.interact(local = locals())  
    """
    follows are entered in interpretter...
    >>> mem
    <memory at 0x101324d0B>
    >>> hex(mem[21])
    <memory at 0x101324dcB>
    >>> hex(mem[12:18][0])
    '0xe0'
    >>> mem[12:18].cast('H')
    <memory at 0x101324eBB)
    >>> mem[12:18].cast('H')[0]
    3040
    >>> mem[12:18].cast('H')[1]
    34423
    >>> mem[12:18].cast('H')[2]
    54321
    >>mem[12:18].cast('H').tolist()
    [3040,34423,54321]
    
    """

    VERTEX_SIZE = 18
    VERTEX_STRIDE = VERTEX_SIZE + 2

    vertex_mems = (mem[i: i+VERTEX_SIZE] for i in range(0, len(mem), VERTEX_STRIDE))
    vertices = [make_colored_vertex(vertex_mem) for vertex_mem in vertex_mems]

    pp(vertices)


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