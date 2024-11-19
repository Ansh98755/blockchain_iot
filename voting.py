import streamlit as st
import hashlib
import time
class Block:
    def __init__(self, index, previous_hash, timestamp, candidate, votes):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.candidate = candidate
        self.votes = votes
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        return hashlib.sha256((str(self.index) + str(self.previous_hash) + 
                               str(self.timestamp) + self.candidate + 
                               str(self.votes)).encode()).hexdigest()
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.candidates = {}

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block", 0)
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_vote(self, candidate):
        if candidate not in self.candidates:
            self.candidates[candidate] = 0
        self.candidates[candidate] += 1
        new_block = Block(len(self.chain), self.get_latest_block().hash, 
                          time.time(), candidate, self.candidates[candidate])
        self.chain.append(new_block)
    
    def declare_results(self):
        results = sorted(self.candidates.items(), key=lambda item: item[1], reverse=True)
        return results
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = Blockchain()
st.title("Blockchain-Based Voting System")
st.write("Cast your vote for your favorite candidate!")
candidate_name = st.text_input("Enter candidate name:")
if st.button("Vote"):
    if candidate_name:
        st.session_state.blockchain.add_vote(candidate_name)
        st.success(f"Vote cast for {candidate_name}!")
    else:
        st.warning("Please enter a candidate name to vote.")
if st.button("Show Results"):
    results = st.session_state.blockchain.declare_results()
    if results:
        st.write("### Election Results:")
        for candidate, votes in results:
            st.write(f"- {candidate}: {votes} votes")
        winner = results[0]
        st.write(f"\n**Winner:** {winner[0]} with {winner[1]} votes!")
    else:
        st.write("No votes cast yet.")
