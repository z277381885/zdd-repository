##hosts
192.168.10.107 orderer.example.com
192.168.10.107 peer0.org1.example.com
192.168.10.104 peer1.org1.example.com
192.168.10.110 peer0.org2.example.com

192.168.10.107 data-1
192.168.10.110 data-2
192.168.10.104 data-3


configtxgen -profile SampleDevModeKafka -channelID byfn-sys-channel -outputBlock ./genesisblock

scp genesisblock /opt/app/fabric/orderer/

chaincodeListenAddress: 0.0.0.0:7052
chaincodeAddress: peer0.org1.example.com:7052