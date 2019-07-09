git clone https://github.com/hyperledger/fabric-ca.git
make fabric-ca-server
make fabric-ca-client

问题1: .go:26:18: fatal error: ltdl.h: No such file or directory
解决:yum install libtool-ltdl-devel