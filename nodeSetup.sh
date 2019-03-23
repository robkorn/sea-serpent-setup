sudo apt-get install pkg-config
git clone https://github.com/input-output-hk/jormungandr --recursive
cd jormungandr/cardano-deps/imhamt/src/ && rm -f bitmap.rs &&
wget https://raw.githubusercontent.com/input-output-hk/rust-cardano/e1d08491988f01cda6cec1aa019226f555791f66/imhamt/src/bitmap.rs
cd ../../.. && cargo build &&
cd target/debug/ &&
cp jormungandr ../../../node/ &&
cp jormungandr_cli ../../../node/ &&
cd ../../../node/ &&
./jormungandr generate-priv-key --type=Ed25519Extended > private.key &&
(cat private.key | ./jormungandr generate-pub-key) > public.key

