meta:
  id: server_blob
  title: ncore server blob format V1
  endian: be
doc: | 
  Some docs
seq:
  - id: files
    type: file
    repeat: eos
types:
  file:
    seq:
      - id: index
        type: s4
      - id: version
        type: s4
      - id: corrid_exists
        type: s1
      - id: corrid
        type: s8
        if: corrid_exists != 0
      - id: filename_length
        type: s2
      - id: filename
        type: str
        size: filename_length
        encoding: UTF-8
      - id: compressed
        type: s1
        if: version == 2
      - id: blocks
        type: block
        repeat: until
        repeat-until: _.length == 0
  block:
    seq:
      - id: length
        type: s4
      - id: data
        size: length
        if: length != 0
