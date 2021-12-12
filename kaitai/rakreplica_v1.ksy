meta:
  id: rakreplica_v1
  title: ncore binary replication file version 1
  endian: le
  bit-endian: le
doc: | 
  Some docs
seq:
  - id: header
    size: 13
    type: header
  - id: meta
    type: meta
types:
  header:
    seq: 
      - id: magic
        contents: "RAKReplica-v1"
        size: 13
  meta:
    seq:
      - id: base_generation
        type: s4
      - id: current_generation
        type: s4
      - id: tables
        type: table
        repeat: until
        repeat-until: _.length == 0
  table:
    seq:
      - id: length
        type: s4
      - id: name
        type: str
        encoding: UTF-8
        size: length
        if: length != 0
      - id: key_len
        type: s4
        if: length != 0
      - id: key
        type: str
        encoding: UTF-8
        size: key_len
        if: length != 0
      - id: fields
        type: field
        if: length != 0
        repeat: until
        repeat-until: _.length == 0
  field:
    seq:
      - id: length
        type: s4
      - id: name
        type: str
        encoding: UTF-8
        size: length
      - id: type
        type: s4
        enum: types
        if: length != 0
      - id: size
        type: s4
        if: length != 0
      - id: scale
        type: s1
        if: length != 0
      - id: subtype
        type: s1
        if: length != 0
      - id: attribute_type_len
        type: s4
        if: length != 0
      - id: attribute_type
        type: str
        encoding: cp1251
        size: attribute_type_len
        if: length != 0
enums:
  types:
    7: boolean    #integer
    8: integer    #scale=0 else double
    16: bigint    #LONG scale=0 else double
    10: float
    27: double
    12: date      #INTEGER
    13: time      #INTEGER
    35: timestamp #LONG
    14: char      #STRING
    37: varchar   #STRING
    261: blob
