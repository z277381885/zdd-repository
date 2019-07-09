#!/bin/bash
##创建channel
cd /opt/fabric-deploy
cd Admin\@org1.example.com
./peer.sh channel create -o orderer.example.com:6050 -c mychannel -f ../mychannel.tx --tls true --cafile tlsca.example.com-cert.pem
./peer.sh channel join -b mychannel.block
sed -i "s/peer0.org1.example.com/peer1.org1.example.com/g" ./peer.sh
./peer.sh channel join -b mychannel.block

cp ./mychannel.block ../Admin\@org2.example.com/
cp ./mychannel.block ../Admin\@org3.example.com/
cd ../Admin\@org2.example.com/
./peer.sh channel join -b mychannel.block
sed -i "s/peer0.org2.example.com/peer1.org2.example.com/g" ./peer.sh
./peer.sh channel join -b mychannel.block

cd ../Admin\@org3.example.com/
./peer.sh channel join -b mychannel.block
sed -i "s/peer0.org3.example.com/peer1.org3.example.com/g" ./peer.sh
./peer.sh channel join -b mychannel.block


##每个组织指定一个anchor peer
sleep 10s
cd ../Admin\@org1.example.com/
./peer.sh channel update -o orderer.example.com:6050 -c mychannel -f ../Org1MSPanchors.tx --tls true --cafile ./tlsca.example.com-cert.pem

cd ../Admin\@org2.example.com/
./peer.sh channel update -o orderer.example.com:6050 -c mychannel -f ../Org2MSPanchors.tx --tls true --cafile ./tlsca.example.com-cert.pem

cd ../Admin\@org3.example.com/
./peer.sh channel update -o orderer.example.com:6050 -c mychannel -f ../Org3MSPanchors.tx --tls true --cafile ./tlsca.example.com-cert.pem

##安装合约（chaincode）
cd ../Admin\@org1.example.com/
./peer.sh chaincode install -n demo -v 0.0.1 -l golang -p github.com/chaincode/chaincode_example02/go
sed -i "s/peer1.org1.example.com/peer0.org1.example.com/g" ./peer.sh
./peer.sh chaincode install -n demo -v 0.0.1 -l golang -p github.com/chaincode/chaincode_example02/go

cd ../Admin\@org2.example.com/
./peer.sh chaincode install -n demo -v 0.0.1 -l golang -p github.com/chaincode/chaincode_example02/go
sed -i "s/peer1.org2.example.com/peer0.org2.example.com/g" ./peer.sh
./peer.sh chaincode install -n demo -v 0.0.1 -l golang -p github.com/chaincode/chaincode_example02/go


cd ../Admin\@org3.example.com/
./peer.sh chaincode install -n demo -v 0.0.1 -l golang -p github.com/chaincode/chaincode_example02/go
sed -i "s/peer0.org3.example.com/peer1.org3.example.com/g" ./peer.sh
./peer.sh chaincode install -n demo -v 0.0.1 -l golang -p github.com/chaincode/chaincode_example02/go


cd ../Admin\@org1.example.com/
./peer.sh chaincode instantiate -o orderer.example.com:6050 --tls true --cafile ./tlsca.example.com-cert.pem -C mychannel -n demo -l golang -v 0.0.1 -c '{"Args":["init","a","100","b","200"]}' -P "AND('Org1MSP.peer','Org2MSP.peer','Org3MSP.peer')"
./peer.sh chaincode query -C mychannel -n demo -c '{"Args":["query","a"]}'