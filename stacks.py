import random

class Node:
    def __init__(self, color, number, next=None):
        self.color = color
        self.number = number
        self.next = next

    def get_data(self):
        return f"{self.color} - {self.number}"

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class Stack:
    def __init__(self, limit=20):
        self.top = None
        self.limit = limit
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.limit

    def peek(self):
        return self.top.get_data()

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            removed_node = self.top
            self.top = removed_node.get_next()
            self.length -= 1
            return removed_node.get_data()

    def push(self, color, number):
        if self.is_full():
            print("I'm full, can't have more!")
        else:
            new_node = Node(color, number)
            new_node.set_next(self.top)
            self.top = new_node
            self.length += 1

    def display_data(self):
        current_node = self.top
        while current_node:
            if current_node.number != None:
                print(f"{current_node.number} - {current_node.color}")
            current_node = current_node.get_next()

colors = ["hearts", "diamonds", "clubs", "spades"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
cards_in_deck = []
deck = Stack(52)

while not deck.is_full():
    number = random.choice(cards)
    color = random.choice(colors)
    if not [number, color] in cards_in_deck:
        deck.push(color, number)
        cards_in_deck.append([number, color])

print(f"The deck of {deck.length} cards has the following:")
deck.display_data()
print("-"* 40)

player_1 = []
player_2 = []

print("Player 1 cards \t Player 2 cards")
for i in range(5):
    player_1.append(deck.pop())
    player_2.append(deck.pop())
    print(f"{player_1[i]} \t {player_2[i]}")
