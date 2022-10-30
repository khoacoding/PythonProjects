import random

MAX_VALUE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count_each_column = {
    "A": 3,
    "B": 1,
    "C": 2,
    "D": 6
}

symbol_value = {
    "A": 3,
    "B": 10,
    "C": 8,
    "D": 2
}

def check_winnings(columns, lines, bet, value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += value[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols_list = []
    for symbol, symbol_count in symbols.items(): #get both key + value associated with dict
        for _ in range(symbol_count):
            all_symbols_list.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols_list = all_symbols_list[:]
        for _ in range(rows):
            value = random.choice(current_symbols_list)
            current_symbols_list.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): #give index + items
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def get_deposit():
    while True:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a valid amount!")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines do you want to bet on (1-" + str(MAX_VALUE) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_VALUE:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Please enter a valid number!")
    return lines

def get_bet():
    while True:
        amount = input("How much do you want to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid number!")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You are betting {total_bet}. \n"
                  f"You do not have enough deposit to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} line. Your total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count_each_column)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = get_deposit()
    while True:
        print(f"Your current balance is ${balance}")
        answer = input("Press any key to spin (press q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()