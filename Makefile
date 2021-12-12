all: rakreplica_v0.py rakreplica_v1.py server_blob.py

rakreplica_v0.py: kaitai/rakreplica_v0.ksy
	ksc -t python kaitai/rakreplica_v0.ksy

rakreplica_v1.py: kaitai/rakreplica_v1.ksy
	ksc -t python kaitai/rakreplica_v1.ksy

server_blob.py: kaitai/server_blob.ksy
	ksc -t python kaitai/server_blob.ksy
