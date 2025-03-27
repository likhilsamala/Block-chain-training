import hashlib
import json
import time
from typing import List, Dict, Any


class Block:
    def __init__(self, index: int, timestamp: float, transactions: List[Dict[str, Any]], previous_hash: str, nonce: int = 0):
        """
        Initialize a new block in the blockchain
        
        Args:
            index: Block number/index
            timestamp: Time of block creation
            transactions: List of transaction data
            previous_hash: Hash of the previous block
            nonce: Number used for proof-of-work
        """
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Calculate the hash of the block based on its contents"""
        # Convert block data to a string and hash it
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty: int) -> None:
        """
        Mine a block (Proof of Work)
        
        Args:
            difficulty: Number of leading zeros required in hash
        """
        target = '0' * difficulty
        
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        
        print(f"Block #{self.index} mined: {self.hash}")


class Blockchain:
    def __init__(self, difficulty: int = 2):
        """
        Initialize a new blockchain
        
        Args:
            difficulty: Mining difficulty (number of leading zeros required)
        """
        self.chain: List[Block] = []
        self.pending_transactions: List[Dict[str, Any]] = []
        self.difficulty = difficulty
        
        # Create the genesis block
        self.create_genesis_block()
    
    def create_genesis_block(self) -> None:
        """Create the first block in the chain (genesis block)"""
        genesis_block = Block(0, time.time(), [], "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
    
    def get_latest_block(self) -> Block:
        """Get the most recent block in the chain"""
        return self.chain[-1]
    
    def add_transaction(self, sender: str, recipient: str, amount: float) -> None:
        """
        Add a new transaction to pending transactions
        
        Args:
            sender: Sender of the transaction
            recipient: Recipient of the transaction
            amount: Amount being transferred
        """
        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "timestamp": time.time()
        })
    
    def mine_pending_transactions(self, mining_reward_address: str) -> None:
        """
        Mine pending transactions and add a new block to the chain
        
        Args:
            mining_reward_address: Address to receive mining reward
        """
        # Create a reward transaction for the miner
        self.pending_transactions.append({
            "sender": "BLOCKCHAIN_REWARD",
            "recipient": mining_reward_address,
            "amount": 1.0,  # Mining reward
            "timestamp": time.time()
        })
        
        # Create a new block with pending transactions
        block = Block(
            len(self.chain),
            time.time(),
            self.pending_transactions,
            self.get_latest_block().hash
        )
        
        # Mine the block
        block.mine_block(self.difficulty)
        
        # Add the block to the chain
        self.chain.append(block)
        
        # Reset pending transactions
        self.pending_transactions = []
    
    def is_chain_valid(self) -> bool:
        """Validate the integrity of the blockchain"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Check if current block's hash is valid
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash in block #{current_block.index}")
                return False
            
            # Check if current block points to correct previous hash
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid previous hash in block #{current_block.index}")
                return False
        
        return True
    
    def print_blockchain(self) -> None:
        """Print the entire blockchain"""
        for block in self.chain:
            print("\n" + "=" * 50)
            print(f"Block #{block.index}")
            print(f"Timestamp: {time.ctime(block.timestamp)}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Nonce: {block.nonce}")
            print("Transactions:")
            for tx in block.transactions:
                print(f"  {tx['sender']} -> {tx['recipient']}: {tx['amount']}")
            print("=" * 50)
    
    def tamper_with_block(self, block_index: int, new_transactions: List[Dict[str, Any]]) -> None:
        """
        Tamper with a block's data (for demonstration purposes)
        
        Args:
            block_index: Index of the block to tamper with
            new_transactions: New transaction data to replace the original
        """
        if block_index < len(self.chain):
            self.chain[block_index].transactions = new_transactions
            print(f"Block #{block_index} has been tampered with!")