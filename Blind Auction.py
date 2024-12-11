#from art import logo

continue_bid = "yes"
bids = {}
max_value = 0
max_bidder = None
#print(logo)
print("Welcome to the secret auction program.")

while continue_bid.lower() == "yes":
    name = input("What is you name?: ")
    bid = int(input("What is your bid?: $"))
    # print("\n" * 20)
    bids[name] = bid
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'")

for bidder in bids:
    if bids[bidder] > max_value:
        max_value = bids[bidder]
        max_bidder = bidder

print(f'The winner is {max_bidder} with a bid of ${max_value}')

#find the same result using max()
a = max(bids, key=bids.get) #max bidder
b = bids[a] #max bid
print(b)
