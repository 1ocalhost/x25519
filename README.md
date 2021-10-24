# x25519 (curve25519)

A pure Python implemention of curve25519 like Go package [x/crypto/curve25519](https://pkg.go.dev/golang.org/x/crypto/curve25519):

```go
package main

import (
	"fmt"
	"bytes"
	"golang.org/x/crypto/curve25519"
)

func main() {
	var publicKey [32]byte
	privateKey := (*[32]byte)(bytes.Repeat([]byte("1"), 32))
	curve25519.ScalarBaseMult(&publicKey, privateKey)
	fmt.Printf("%x\n", publicKey)
	
	var sharedSecret [32]byte
	peerPublicKey := (*[32]byte)(bytes.Repeat([]byte("2"), 32))
	curve25519.ScalarMult(&sharedSecret, privateKey, peerPublicKey)
	fmt.Printf("%x\n", sharedSecret)
}

/* output:
04f5f29162c31a8defa18e6e742224ee806fc1718a278be859ba5620402b8f3a
a6d830c3561f210fc006c77768369af0f5b3e3e502e74bd3e80991d7cb7bfa50
*/
```

Usage of this package:

```python
# this code supports both python 2 and 3
from binascii import hexlify
import x25519

private_key = b'1' * 32
public_key = x25519.scalar_base_mult(private_key)
print(hexlify(public_key))

peer_public_key = b'2' * 32
shared_secret = x25519.scalar_mult(private_key, peer_public_key)
print(hexlify(shared_secret))

'''output:
b'04f5f29162c31a8defa18e6e742224ee806fc1718a278be859ba5620402b8f3a'
b'a6d830c3561f210fc006c77768369af0f5b3e3e502e74bd3e80991d7cb7bfa50'
'''
```

Generally, other C implementions are much faster:
```python
import pysodium

private_key = b'1' * 32
public_key = pysodium.crypto_scalarmult_curve25519_base(private_key)
print(public_key.hex())

peer_public_key = b'2' * 32
shared_secret = pysodium.crypto_scalarmult_curve25519(private_key, peer_public_key)
print(shared_secret.hex())

'''output:
04f5f29162c31a8defa18e6e742224ee806fc1718a278be859ba5620402b8f3a
a6d830c3561f210fc006c77768369af0f5b3e3e502e74bd3e80991d7cb7bfa50
'''
```
