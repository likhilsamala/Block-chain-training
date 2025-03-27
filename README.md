# Block-chain-training
Save the two Python files (`blockchain.py` and `demo.py`) in the same directory.

## Description 
**Block Structure**: Each block contains an index, timestamp, transactions, previous hash, current hash, and a nonce for proof-of-work.
**Hashing**: We use SHA-256 to generate a hash based on the block's contents.
**Blockchain Class**: Manages the chain of blocks with methods to:

- Add new blocks
- Add transactions
- Mine pending transactions
- Validate the chain's integrity

**Proof-of-Work**: Implemented as a mining mechanism that requires finding a hash with a specific number of leading zeros.
**Tampering Detection**: The `is_chain_valid()` method checks if any block has been tampered with by:
- Recalculating each block's hash and comparing it with the stored hash
- Verifying that each block points to the correct previous block
