def solve():
    input_path = r"C:\Users\dell\Desktop\MetaHackerCup\p5\narrowing_down_input.txt"
    output_path = r"C:\Users\dell\Desktop\MetaHackerCup\p5\output.txt"

    with open(input_path, "r") as fin, open(output_path, "w") as fout:
        T = int(fin.readline())
        for t in range(1, T + 1):
            N = int(fin.readline())
            A = list(map(int, fin.readline().split()))

            # Compute prefix XORs
            S = [0] * (N + 1)
            for i in range(1, N + 1):
                S[i] = S[i - 1] ^ A[i - 1]

            # Count frequencies of prefix XORs
            freq = {}
            for val in S:
                freq[val] = freq.get(val, 0) + 1

            # Calculate sub = sum of m*(m^2 - 1)//6
            sub = 0
            for m in freq.values():
                sub += m * (m * m - 1) // 6

            # Total number of subarrays = N*(N+1)*(N+2)//6
            total = N * (N + 1) * (N + 2) // 6
            ans = total - sub

            result = f"Case #{t}: {ans}\n"
            fout.write(result)
            print(result, end="")

    print(f"\n✅ Output saved successfully to {output_path}")


if __name__ == "__main__":
    solve()
