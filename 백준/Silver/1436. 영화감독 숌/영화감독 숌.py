import sys

def solve():
    n = int(sys.stdin.readline().strip())

    ans = []
    L = 3  # 최소 3자리(666)

    while True:
        cand = set()

        # "666" 시작 위치 pos: 0 .. L-3
        for pos in range(L - 2):  # range(L-2) == 0..L-3
            prefix_len = pos
            suffix_len = L - 3 - pos

            # prefix 범위(선행 0 금지)
            if prefix_len == 0:
                prefix_start, prefix_end = 0, 0  # 빈 prefix 1개 취급
            else:
                prefix_start = 10 ** (prefix_len - 1)
                prefix_end = 10 ** prefix_len - 1

            # suffix 범위(선행 0 허용: zfill로 자릿수 맞춤)
            suffix_start = 0
            suffix_end = 10 ** suffix_len - 1 if suffix_len > 0 else 0

            for p in range(prefix_start, prefix_end + 1):
                prefix_str = "" if prefix_len == 0 else str(p)

                if suffix_len == 0:
                    s = prefix_str + "666"
                    cand.add(int(s))
                else:
                    for suf in range(suffix_start, suffix_end + 1):
                        suffix_str = str(suf).zfill(suffix_len)
                        s = prefix_str + "666" + suffix_str
                        cand.add(int(s))

        # 자릿수 L에서의 오름차순 리스트
        block = sorted(cand)

        # 전체 오름차순: 자릿수 증가 순으로 누적하면 됨
        for x in block:
            ans.append(x)
            if len(ans) == n:
                print(x)
                return

        L += 1

if __name__ == "__main__":
    solve()
