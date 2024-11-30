---
title: "Token"
layout: docs
---
# Getting Started

We are going to deploy an ERC20 token on the ethereum blockchain.

## Vyper
Why Vyper? Vyper is closer to the langauge Python, which I find to be a lot closer to my intuitive way of thinking. 

What are we going to construct.

We will make an ERC20 token, which we can call whatever we like, here we will call it `bcbooktoken` and give it the _ticker_ BCBT.


## Really simple smart contract
Before we start making tokens, we are not limited to anything. 
We are going to look at two different kinds of token. The first is a storage token, that simply stores and retrieves whatever 

1. A stroage contract. Anyone can give it a value, and anyone can red what that value is.
2. A puzzle contract, where there is an embedded puzzle that must be solved.
3. A randomness contract, that randomly retruns an integer value between, and including 1 and 5. You can input a guess, and if you get it you get a you are right button.

 
### 1) The Storage Contract
Lets load up REMIX in our browser by connecting to https://remix.ethereum.org/ (search for ethereum remix IDE)
Navigate to the file explorer, where you should see a folder called contracts. In there we will create a new file called `store.vy`. The `.vy` refers to the vyper, rather than `.sol` which stands for solidity. You may see other contracts in there with the `.sol` extension.
## code
```sh
sudo 
```