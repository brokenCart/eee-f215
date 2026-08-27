def Gblk():
    for i in range(16):
        print(f"assign #(2) Gblk_{i}  = (a[{i*4 + 3}] & b[{i*4 + 3}])   | ((a[{i*4 + 3}] ^ b[{i*4 + 3}])   & ((a[{i*4 + 2}] & b[{i*4 + 2}])   | ((a[{i*4 + 2}] ^ b[{i*4 + 2}])   & ((a[{i*4 + 1}] & b[{i*4 + 1}])   | ((a[{i*4 + 1}] ^ b[{i*4 + 1}])   & (a[{i*4}] & b[{i*4}]))))));")


def Pblk():
    for i in range(16):
        print(f"assign #(2) Pblk_{i}  = (a[{i*4}]  | b[{i*4}])  & (a[{i*4 + 1}]  | b[{i*4 + 1}])  & (a[{i*4 + 2}]  | b[{i*4 + 2}])  & (a[{i*4 + 3}]  | b[{i*4 + 3}]);")


def Cblk():
    terms = ["Pblk_0 & cin", "Gblk_0"]
    for i in range(16):
        c = "cout" if i == 15 else f"Cblk_{i+1}"
        print(f"assign #(2) {c} = {' | '.join([f'({term})' for term in terms[::-1]])};")
        terms = [f"Pblk_{i+1} & {term}" for term in terms] + [f"Gblk_{i+1}"]


def cla64_blocked():
    for i in range(16):
        cin = "cin" if i == 0 else f"Cblk_{i}"
        print(f"cla4 block{i} (.a(a[{i*4 + 3}:{i*4}]), .b(b[{i*4 + 3}:{i*4}]), .cin({cin}), .sum(sum[{i*4 + 3}:{i*4}]), .cout(unused[{i}]));")
