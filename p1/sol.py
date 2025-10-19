# Snake Scales Problem - Output to File

# Read all data from the validation input file
with open("snake_scales_chapter_1_input.txt", "r") as file:
    data = list(map(int, file.read().split()))

# Open file to write results
with open("validation_output.txt", "w") as out:
    T = data[0]
    index = 1

    for t in range(1, T + 1):
        N = data[index]
        index += 1
        A = data[index:index + N]
        index += N

        if N == 1:
            min_ladder = 0
        else:
            min_ladder = max(abs(A[i] - A[i - 1]) for i in range(1, N))

        # Write output to file instead of printing
        out.write(f"Case #{t}: {min_ladder}\n")
