# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class ServerBlob(KaitaiStruct):
    """Some docs
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.files = []
        i = 0
        while not self._io.is_eof():
            self.files.append(ServerBlob.File(self._io, self, self._root))
            i += 1


    class File(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.index = self._io.read_s4be()
            self.version = self._io.read_s4be()
            self.corrid_exists = self._io.read_s1()
            if self.corrid_exists != 0:
                self.corrid = self._io.read_s8be()

            self.filename_length = self._io.read_s2be()
            self.filename = (self._io.read_bytes(self.filename_length)).decode(u"UTF-8")
            if self.version == 2:
                self.compressed = self._io.read_s1()

            self.blocks = []
            i = 0
            while True:
                _ = ServerBlob.Block(self._io, self, self._root)
                self.blocks.append(_)
                if _.length == 0:
                    break
                i += 1


    class Block(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_s4be()
            if self.length != 0:
                self.data = self._io.read_bytes(self.length)
