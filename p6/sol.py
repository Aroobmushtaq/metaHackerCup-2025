def solve_game(N, S):
    alice_turns = 0
    bob_turns = 0
    left = 0
    right = N - 1

    while left <= right:
        # Alice's turn: find first 'A' from the left
        found_A = False
        for i in range(left, right + 1):
            if S[i] == 'A':
                alice_turns += 1
                left = i + 1
                found_A = True
                break
        if not found_A:
            break

        # Bob's turn: find first 'B' from the right
        found_B = False
        for i in range(right, left - 1, -1):
            if S[i] == 'B':
                bob_turns += 1
                right = i - 1
                found_B = True
                break
        if not found_B:
            break

    return "Alice" if alice_turns > bob_turns else "Bob"


def solve_file():
    input_path = r"C:\Users\dell\Desktop\MetaHackerCup\p6\crash_course_input.txt"
    output_path = r"C:\Users\dell\Desktop\MetaHackerCup\p6\output.txt"

    with open(input_path, "r") as fin, open(output_path, "w") as fout:
        T = int(fin.readline())
        for cas in range(1, T + 1):
            N = int(fin.readline())
            S = fin.readline().strip()
            result = solve_game(N, S)
            fout.write(f"Case #{cas}: {result}\n")
            print(f"Case #{cas}: {result}")  # optional: show on console


if __name__ == "__main__":
    solve_file()
