def cla64_blocked():
    for i in range(16):
        cin = "cin" if i == 0 else f"c[{i}]"
        cout = "cout" if i == 15 else f"c[{i + 1}]"
        print(f"cla4 block{i} (.a(a[{i*4 + 3}:{i*4}]), .b(b[{i*4 + 3}:{i*4}]), .cin({cin}), .sum(sum[{i*4 + 3}:{i*4}]), .cout({cout}));")


def cla64_flat():
    terms = ["p[0] & cin", "g[0]"]
    for i in range(64):
        print(f"assign #(2) c[{i+1}] = {' | '.join([f'({term})' for term in terms[::-1]])};")
        terms = [f"p[{i+1}] & {term}" for term in terms] + [f"g[{i+1}]"]
    print("assign #(2) cout = c[64];")
