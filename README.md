# Pizza
[+]First project Blockchain


-------------------------------------------------------------------------------------------------------------------------------------------
[+] Commands

geth --datadir . --http --http.addr 0.0.0.0 --http.port 8545 --http.api web3,net,eth,personal,admin,miner --http.vhosts * --http.corsdomain * --allow-insecure-unlock --mine --miner.threads 1 --rpc.txfeecap "0"

geth attach http://127.0.0.1:8545
personal.unlockAccount("3B9e6Efe6304A4ec3aE48bA61452a555FA86b0Eb", "123", 0)

-------------------------------------------------------------------------------------------------------------------------------------------

