#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 15:45:36 2017

@author: david
"""

import struct
import itertools

"""
You need to read complicated binary-encoded data that contains a collection
of nested and/or variable-sized records. Such data might include images,
video, shapefiles, and so on.
"""

polys = [[(1.0, 2.5), (3.5, 4.0), (2.5, 1.5)],
         [(7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0)],
         [(3.4, 6.3), (1.2, 0.5), (4.6, 9.2)]]


def write_polys(filename, polys):
    # Determine bounding box
    flattened = list(itertools.chain(*polys))
    min_x = min(x for x, y in flattened)
    max_x = max(x for x, y in flattened)
    min_y = min(y for x, y in flattened)
    max_y = max(y for x, y in flattened)

    with open(filename, 'wb') as f:
        f.write(struct.pack('<iddddi', 0x1234, min_x, min_y, max_x, max_y,
                            len(polys)))

        for poly in polys:
            size = len(poly) * struct.calcsize('<dd')
            f.write(struct.pack('<i', size+4))
            for pt in poly:
                f.write(struct.pack('<dd', *pt))


def read_polys(filename):
    with open(filename, 'rb') as f:
        # Read the header
        header = f.read(40)
        file_code, min_x, min_y, max_x, max_y, num_polys = \
            struct.unpack('<iddddi', header)

        polys = []
        for n in range(num_polys):
            pbytes, = struct.unpack('<i', f.read(4))
            poly = []
            for m in range(pbytes // 16):
                pt = struct.unpack('<dd', f.read(16))
                poly.append(pt)
            polys.append(poly)
    return polys


# Call it with our polygon data
write_polys('data/polys.bin', polys)

polys = read_polys('data/polys.bin')
print(polys)

print()


class StructField:
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format,
                                   instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r


class Structure:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)


# Example 1
class PolyHeader(Structure):
    file_code = StructField('<i', 0)
    min_x = StructField('<d', 4)
    min_y = StructField('<d', 12)
    max_x = StructField('<d', 20)
    max_y = StructField('<d', 28)
    num_polys = StructField('<i', 36)


f = open('data/polys.bin', 'rb')
data = f.read()

phead = PolyHeader(data)
print(phead.file_code == 0x1234)
print('min_x=', phead.min_x)
print('max_x=', phead.max_x)
print('min_y=', phead.min_y)
print('max_y=', phead.max_y)
print('num_polys=', phead.num_polys)

print()


# Example 2: Introduction of a metaclass
class StructureMeta(type):
    '''
    Metaclass that automatically creates StructField descriptors
    '''
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if format.startswith(('<', '>', '!', '@')):
                byte_order = format[0]
                format = format[1:]
            format = byte_order + format
            setattr(self, fieldname, StructField(format, offset))
            offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeader(Structure):
    _fields_ = [
            ('<i', 'file_code'),
            ('d', 'min_x'),
            ('d', 'min_y'),
            ('d', 'max_x'),
            ('d', 'max_y'),
            ('i', 'num_polys')
            ]


f = open('data/polys.bin', 'rb')
phead = PolyHeader.from_file(f)
print(phead.file_code == 0x1234)
print('min_x=', phead.min_x)
print('max_x=', phead.max_x)
print('min_y=', phead.min_y)
print('max_y=', phead.max_y)
print('num_polys=', phead.num_polys)

print()


# Example 3: Nested structure support
class NestedStruct:
    '''
    Descriptor representing a nested structure
    '''
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[self.offset:
                                    self.offset+self.struct_type.struct_size]
            result = self.struct_type(data)
            setattr(instance, self.name, result)
            return result


class StructureMeta(type):
    '''
    Metaclass that automatically creates StructField descriptors
    '''
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(self, fieldname, NestedStruct(fieldname, format,
                                                      offset))
                offset += format.struct_size
            else:
                if format.startswith(('<', '>', '!', '@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, StructField(format, offset))
                offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class Point(Structure):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y')
        ]


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'),    # nested struct
        (Point, 'max'),    # nested struct
        ('i', 'num_polys')
        ]


f = open('data/polys.bin', 'rb')
phead = PolyHeader.from_file(f)
print(phead.file_code == 0x1234)
print('min.x=', phead.min.x)
print('max.x=', phead.max.x)
print('min.y=', phead.min.y)
print('max.y=', phead.max.y)
print('num_polys=', phead.num_polys)

print()


# Example 4:
class SizedRecord:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

    @classmethod
    def from_file(cls, f, size_fmt, includes_size=True):
        sz_nbytes = struct.calcsize(size_fmt)
        sz_bytes = f.read(sz_nbytes)
        sz, = struct.unpack(size_fmt, sz_bytes)
        buf = f.read(sz - includes_size * sz_nbytes)
        return cls(buf)

    def iter_as(self, code):
        if isinstance(code, str):
            s = struct.Struct(code)
            for off in range(0, len(self._buffer), s.size):
                yield s.unpack_from(self._buffer, off)
        elif isinstance(code, StructureMeta):
            size = code.struct_size
            for off in range(0, len(self._buffer), size):
                data = self._buffer[off:off+size]
                yield code(data)


def read_polys(filename):
#    polys = []
    with open(filename, 'rb') as f:
        phead = PolyHeader.from_file(f)
        for n in range(phead.num_polys):
            rec = SizedRecord.from_file(f, '<i')
#            poly = [(p.x, p.y) for p in rec.iter_as(Point)]
            poly = [rec for p in range(phead.num_polys)]
        for n, pol in enumerate(poly):
            print('Polygon', n)
            for p in pol.iter_as('<dd'):
                print(p)
#            polys.append(poly)
#    return polys


polys = read_polys('data/polys.bin')
