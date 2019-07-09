#!/bin/bash
cd /opt/fabric-deploy
./bin/cryptogen generate --config=crypto-config.yaml --output ./certs
mkdir {orderer.example.com,orderer2.example.com,orderer3.example.com}
./bin/configtxgen -profile SampleDevModeKafka -channelID byfn-sys-channel -outputBlock ./orderer.example.com/genesisblock
cp ./orderer.example.com/genesisblock ./orderer2.example.com/
cp ./orderer.example.com/genesisblock ./orderer3.example.com/
cp ./config/orderer.yaml orderer.example.com/
sed -i "s/7050/6050/g" orderer.example.com/orderer.yaml
cp ./config/orderer.yaml orderer2.example.com/
cp ./config/orderer.yaml orderer3.example.com/
sed -i "s/7050/8050/g" orderer3.example.com/orderer.yaml
cp ./bin/orderer orderer.example.com/
cp ./bin/orderer orderer2.example.com/
cp ./bin/orderer orderer3.example.com/
cp -rf ./certs/ordererOrganizations/example.com/orderers/orderer.example.com/* orderer.example.com/
cp -rf ./certs/ordererOrganizations/example.com/orderers/orderer2.example.com/* orderer2.example.com/
cp -rf ./certs/ordererOrganizations/example.com/orderers/orderer3.example.com/* orderer3.example.com/
mkdir -p ./orderer.example.com/data
mkdir -p ./orderer2.example.com/data
mkdir -p ./orderer3.example.com/data


mkdir peer0.org1.example.com
cp ./bin/peer peer0.org1.example.com/
cp -rf ./certs/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/* peer0.org1.example.com/
cp ./config/core.yaml peer0.org1.example.com/
sed -i "s/7051/6051/g" peer0.org1.example.com/core.yaml 
sed -i "s/7052/6052/g" peer0.org1.example.com/core.yaml 
mkdir -p ./peer0.org1.example.com/data

mkdir peer1.org1.example.com/
cp ./bin/peer peer1.org1.example.com/
cp -rf ./certs/peerOrganizations/org1.example.com/peers/peer1.org1.example.com/* peer1.org1.example.com/
cp ./config/core.yaml peer1.org1.example.com/
mkdir -p ./peer1.org1.example.com/data
sed -i "s/7051/6051/g" peer1.org1.example.com/core.yaml 
sed -i "s/7052/6052/g" peer1.org1.example.com/core.yaml 
sed -i "s/peer0/peer1/g" peer1.org1.example.com/core.yaml 
sed -i "s/bootstrap: peer1.org1.example.com:6051/bootstrap: peer0.org1.example.com:6051/g" peer1.org1.example.com/core.yaml


mkdir peer0.org2.example.com/
cp -rf ./certs/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/*  peer0.org2.example.com/
cp ./config/core.yaml peer0.org2.example.com/
mkdir -p ./peer0.org2.example.com/data
cp ./bin/peer peer0.org2.example.com/
sed -i "s/peer0.org1.example.com/peer0\.org2\.example.com/g" ./peer0.org2.example.com/core.yaml
sed -i "s/bootstrap: peer1.org1.example.com:7051/bootstrap: peer1.org2.example.com:7051/g" ./peer0.org2.example.com/core.yaml
sed -i "s/Org1MSP/Org2MSP/g" ./peer0.org2.example.com/core.yaml
sed -i "s/org1/org2/g" ./peer0.org2.example.com/core.yaml

mkdir peer1.org2.example.com/
cp -rf ./certs/peerOrganizations/org2.example.com/peers/peer1.org2.example.com/*  peer1.org2.example.com/
cp ./config/core.yaml peer1.org2.example.com/
mkdir -p ./peer1.org2.example.com/data
cp ./bin/peer peer1.org2.example.com/
sed -i "s/peer0.org1.example.com/peer1\.org2\.example.com/g" ./peer1.org2.example.com/core.yaml
sed -i "s/bootstrap: peer1.org1.example.com:7051/bootstrap: peer0.org2.example.com:7051/g" ./peer1.org2.example.com/core.yaml
sed -i "s/Org1MSP/Org2MSP/g" ./peer1.org2.example.com/core.yaml
sed -i "s/org1/org2/g" ./peer1.org2.example.com/core.yaml

mkdir peer0.org3.example.com/
cp -rf ./certs/peerOrganizations/org3.example.com/peers/peer0.org3.example.com/*  peer0.org3.example.com/
cp ./config/core.yaml peer0.org3.example.com/
mkdir -p ./peer0.org3.example.com/data
cp ./bin/peer peer0.org3.example.com/
sed -i "s/7051/8051/g" ./peer0.org3.example.com/core.yaml 
sed -i "s/7052/8052/g" ./peer0.org3.example.com/core.yaml 
sed -i "s/peer0.org1.example.com/peer0\.org3\.example.com/g" ./peer0.org3.example.com/core.yaml
sed -i "s/bootstrap: peer1.org1.example.com:8051/bootstrap: peer1.org3.example.com:8051/g" ./peer0.org3.example.com/core.yaml
sed -i "s/Org1MSP/Org3MSP/g" ./peer0.org3.example.com/core.yaml
sed -i "s/org1/org3/g" ./peer0.org3.example.com/core.yaml

mkdir peer1.org3.example.com/
cp -rf ./certs/peerOrganizations/org3.example.com/peers/peer1.org3.example.com/*  peer1.org3.example.com/
cp ./config/core.yaml peer1.org3.example.com/
mkdir -p ./peer1.org3.example.com/data
cp ./bin/peer peer1.org3.example.com/
sed -i "s/7051/8051/g" peer1.org3.example.com/core.yaml 
sed -i "s/7052/8052/g" peer1.org3.example.com/core.yaml 
sed -i "s/peer0.org1.example.com/peer1\.org3\.example.com/g" ./peer1.org3.example.com/core.yaml
sed -i "s/bootstrap: peer1.org1.example.com:8051/bootstrap: peer0.org3.example.com:8051/g" ./peer1.org3.example.com/core.yaml
sed -i "s/Org1MSP/Org3MSP/g" ./peer1.org3.example.com/core.yaml
sed -i "s/org1/org3/g" ./peer1.org3.example.com/core.yaml



##整理用户证书
mkdir Admin\@org1.example.com
cp -rf ./certs/peerOrganizations/org1.example.com/users/Admin\@org1.example.com/* Admin\@org1.example.com/
cp ./peer0.org1.example.com/core.yaml  Admin\@org1.example.com/
cp ./config/peer.sh Admin@org1.example.com/
sed -i "s/peer0.org1.example.com:7051/peer0.org1.example.com:6051/g" Admin\@org1.example.com/peer.sh

mkdir User1\@org1.example.com
cp -rf  ./certs/peerOrganizations/org1.example.com/users/User1\@org1.example.com/* User1\@org1.example.com/
cp ./peer0.org1.example.com/core.yaml User1@org1.example.com/
cp ./config/peer.sh User1@org1.example.com/
sed -i "s/peer0.org1.example.com:7051/peer0.org1.example.com:6051/g" User1\@org1.example.com/peer.sh

mkdir Admin\@org2.example.com/
cp -rf ./certs/peerOrganizations/org2.example.com/users/Admin\@org2.example.com/* Admin\@org2.example.com/
cp ./peer0.org2.example.com/core.yaml Admin\@org2.example.com/
cp ./config/peer.sh Admin\@org2.example.com/
sed -i "s/peer0.org1.example.com:7051/peer0.org2.example.com:7051/g" Admin\@org2.example.com/peer.sh
sed -i "s/Org1MSP/Org2MSP/g" Admin\@org2.example.com/peer.sh

mkdir User1\@org2.example.com
cp -rf  ./certs/peerOrganizations/org2.example.com/users/User1\@org2.example.com/* User1\@org2.example.com/
cp ./peer0.org2.example.com/core.yaml User1\@org2.example.com/
cp ./config/peer.sh User1\@org2.example.com/
sed -i "s/peer0.org1.example.com:7051/peer0.org2.example.com:7051/g" User1\@org2.example.com/peer.sh
sed -i "s/Org1MSP/Org2MSP/g" User1\@org2.example.com/peer.sh

mkdir Admin\@org3.example.com/
cp -rf ./certs/peerOrganizations/org3.example.com/users/Admin\@org3.example.com/* Admin\@org3.example.com/
cp ./peer0.org3.example.com/core.yaml Admin\@org3.example.com/
cp ./config/peer.sh Admin\@org3.example.com/
sed -i "s/peer0.org1.example.com:7051/peer0.org3.example.com:8051/g" Admin\@org3.example.com/peer.sh
sed -i "s/Org1MSP/Org3MSP/g" Admin\@org3.example.com/peer.sh

mkdir User1\@org3.example.com
cp -rf  ./certs/peerOrganizations/org3.example.com/users/User1\@org3.example.com/* User1\@org3.example.com/
cp ./peer0.org3.example.com/core.yaml User1\@org3.example.com/
cp ./config/peer.sh User1\@org3.example.com/
sed -i "s/peer0.org1.example.com:7051/peer0.org3.example.com:8051/g" User1\@org3.example.com/peer.sh
sed -i "s/Org1MSP/Org3MSP/g" User1\@org3.example.com/peer.sh

##准备channel文件
./bin/configtxgen -profile TwoOrgsChannel -outputCreateChannelTx mychannel.tx -channelID mychannel
./bin/configtxgen -profile TwoOrgsChannel -outputAnchorPeersUpdate Org1MSPanchors.tx -channelID mychannel -asOrg Org1MSP
./bin/configtxgen -profile TwoOrgsChannel -outputAnchorPeersUpdate Org2MSPanchors.tx -channelID mychannel -asOrg Org2MSP
./bin/configtxgen -profile TwoOrgsChannel -outputAnchorPeersUpdate Org3MSPanchors.tx -channelID mychannel -asOrg Org3MSP
cp ./certs/ordererOrganizations/example.com/tlsca/tlsca.example.com-cert.pem  Admin\@org1.example.com/
cp ./certs/ordererOrganizations/example.com/tlsca/tlsca.example.com-cert.pem  User1\@org1.example.com/
cp ./certs/ordererOrganizations/example.com/tlsca/tlsca.example.com-cert.pem  Admin\@org2.example.com/
cp ./certs/ordererOrganizations/example.com/tlsca/tlsca.example.com-cert.pem  User1\@org2.example.com/
cp ./certs/ordererOrganizations/example.com/tlsca/tlsca.example.com-cert.pem  Admin\@org3.example.com/
cp ./certs/ordererOrganizations/example.com/tlsca/tlsca.example.com-cert.pem  User1\@org3.example.com/