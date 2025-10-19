import os

def can_reach_all(heights, h):
    n = len(heights)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and abs(heights[j + 1] - heights[j]) <= h:
            j += 1
        if not any(heights[k] <= h for k in range(i, j + 1)):
            return False
        i = j + 1
    return True


def min_ladder_height(heights):
    low, high = 0, max(heights)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can_reach_all(heights, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "snake_scales_chapter_2_input.txt")
    output_path = os.path.join(script_dir, "validation_output.txt")

    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        t = int(infile.readline().strip())
        for case in range(1, t + 1):
            n = int(infile.readline().strip())
            heights = list(map(int, infile.readline().strip().split()))
            result = min_ladder_height(heights)
            outfile.write(f"Case #{case}: {result}\n")

    print(f" Output written to {output_path}")


if __name__ == "__main__":
    main()
