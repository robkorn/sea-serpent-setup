git clone https://github.com/input-output-hk/jormungandr --recursive
cd jormungandr/cardano-deps/imhamt/src/ && rm -f bitmap.rs &&
wget https://raw.githubusercontent.com/input-output-hk/rust-cardano/e1d08491988f01cda6cec1aa019226f555791f66/imhamt/src/bitmap.rs
cd ../../.. && cargo build --release &&
cd target/release/ &&
cp jormungandr ../../../node/ &&
cp jcli ../../../node/ &&
cd ../../../node/ &&
./jcli key generate --type=Ed25519Extended > private.key &&
(cat private.key | ./jcli key to-public) > public.key
cat genesis.yaml | ./jcli genesis encode --output block_0.bin
