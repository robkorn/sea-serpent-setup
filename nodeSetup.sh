git clone https://github.com/input-output-hk/jormungandr --recursive
cd jormungandr &&
cargo build --release &&
cd target/release/ &&
cp jormungandr ../../../jormungandr-node/ &&
cp jcli ../../../jormungandr-node/ &&
cd ../../../jormungandr-node/ &&
./jcli key generate --type=Ed25519Extended > private.key &&
(cat private.key | ./jcli key to-public) > public.key
cat genesis.yaml | ./jcli genesis encode --output block_0.bin
