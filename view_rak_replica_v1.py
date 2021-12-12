#!/usr/bin/python3

from rakreplica_v1 import RakreplicaV1
from argparse import ArgumentParser

def type2sql(type):
    if type == RakreplicaV1.Types.boolean:
        return 'BOOLEAN'
    elif type == RakreplicaV1.Types.integer:
        return 'INT'
    elif type == RakreplicaV1.Types.float:
        return 'FLOAT'
    elif type == RakreplicaV1.Types.date:
        return 'DATE'
    elif type == RakreplicaV1.Types.time:
        return 'TIME'
    elif type == RakreplicaV1.Types.char:
        return 'CHAR'
    elif type == RakreplicaV1.Types.bigint:
        return 'BIGINT'
    elif type == RakreplicaV1.Types.double:
        return 'DOUBLE'
    elif type == RakreplicaV1.Types.timestamp:
        return 'TIMESTAMP'
    elif type == RakreplicaV1.Types.varchar:
        return 'VARCHAR'
    elif type == RakreplicaV1.Types.blob:
        return 'BLOB'
    else:
        return type

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-l', nargs=1, metavar='rpldata.bin', type=str, help='list metadata in replication file')
    args = parser.parse_args()

    if args.l is not None:
        rak = RakreplicaV1.from_file(args.l[0])
        print('--Generation: {}-{}'.format(rak.meta.base_generation, rak.meta.current_generation))
        for table in rak.meta.tables:
            if table.length > 0:
                print('CREATE TABLE {} ('.format(table.name))
                for field in table.fields:
                    if field.length > 0:
                        # VARCHAR/CHAR
                        if field.type in (RakreplicaV1.Types.varchar, RakreplicaV1.Types.char):
                            print('\t{:31s}\t{:s}({:d}),'.format(field.name, type2sql(field.type), field.size))
                        # BLOB
                        elif field.type == RakreplicaV1.Types.blob:
                            print('\t{:31s}\t{:s}(,{:d}),'.format(field.name, type2sql(field.type), field.subtype))
                        # NUMERIC
                        elif field.type == RakreplicaV1.Types.bigint and field.scale > 0:
                            print('\t{:31s}\tNUMERIC[18,{:d}],'.format(field.name, field.scale))
                        else:
                            print('\t{:31s}\t{:s},'.format(field.name, type2sql(field.type), field.size))
                        if field.attribute_type_len > 0:
                            print('--attribute_type {:s}'.format(field.attribute_type))
                if table.key[0:11] == 'DESCENDING:':
                    print('\tPRIMARY KEY ({:s}) USING DESCENDING INDEX PK_{:s}'.format(table.key[11:], table.name[:29]))
                else:
                    print('\tPRIMARY KEY ({:s})'.format(table.key))
                print(');')
    else:
        parser.print_help()
