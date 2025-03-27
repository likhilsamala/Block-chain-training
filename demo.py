from blockchain import Blockchain

def main():
    # Create a new blockchain
    print("Creating a new blockchain...")
    my_blockchain = Blockchain(difficulty=2)
    
    # Add some transactions
    print("\nAdding transactions...")
    my_blockchain.add_transaction("Alice", "Bob", 50)
    my_blockchain.add_transaction("Bob", "Charlie", 25)
    
    # Mine the pending transactions
    print("\nMining block...")
    my_blockchain.mine_pending_transactions("Miner1")
    
    # Add more transactions
    print("\nAdding more transactions...")
    my_blockchain.add_transaction("Charlie", "Dave", 10)
    my_blockchain.add_transaction("Alice", "Eve", 30)
    
    # Mine the pending transactions
    print("\nMining block...")
    my_blockchain.mine_pending_transactions("Miner1")
    
    # Print the blockchain
    print("\nBlockchain:")
    my_blockchain.print_blockchain()
    
    # Validate the blockchain
    print("\nValidating blockchain...")
    print(f"Is blockchain valid? {my_blockchain.is_chain_valid()}")
    
    # Tamper with the blockchain
    print("\nTampering with the blockchain...")
    tampered_transactions = [
        {"sender": "Alice", "recipient": "Hacker", "amount": 1000, "timestamp": 1234567890}
    ]
    my_blockchain.tamper_with_block(1, tampered_transactions)
    
    # Validate the blockchain again
    print("\nValidating blockchain after tampering...")
    print(f"Is blockchain valid? {my_blockchain.is_chain_valid()}")
    
    # Print the blockchain after tampering
    print("\nBlockchain after tampering:")
    my_blockchain.print_blockchain()

if __name__ == "__main__":
    main()