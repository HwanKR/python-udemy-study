# TODO-1: Ask the user for input
import art
print(art.logo)

bid_info = {}
has_other_bidders = True
while has_other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
# TODO-2: Save data into dictionary {name: price}
    bid_info[name] = bid
# TODO-3: Whether if new bids need to be added
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n" * 20)
# TODO-4: Compare bids in dictionary


    if other_bidders == 'no':
        winner = ''
        winner_price = 0
        for bidder in bid_info:
            if bid_info[bidder] > winner_price:
                winner_price = bid_info[bidder]
                winner = bidder
        print(f"The winner is {winner} with a bid of ${winner_price}")
        break

