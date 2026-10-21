import re
import sys

base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def char_to_binary(c):
    return format(ord(c), "08b")


def extract(text):
    return re.findall(r"[A-Za-z_]\w*(?:\([^)]*\))?", text, re.ASCII)


def parse_two_ints(operation):
    # Parse 'NAME(a,b)' into (a, b)
    open_ = operation.find("(")
    comma = operation.find(",")
    close = operation.find(")")
    a = int(operation[open_ + 1:comma])
    b = int(operation[comma + 1:close])

    if a <= 127 or a >= 1000:
        print("INVALID value of n")
        exit()
    return a, b


def main():
    line = sys.stdin.readline().split(" ")
    text = line[0]
    operations = extract(line[1].strip())
    result = []

    if len(text) >= 100 or len(text) < 1:
        print("Invalid string", end="")
        return

    for operation in operations:
        if "RSA_ENC" in operation:
            n, e = parse_two_ints(operation)

            if e < 1:
                print("INVALID value of e")
                return

            codes = [pow(ord(c), e, n) for c in text]
            result.append(codes)
            codes = [str(x) for x in codes]
            print(f"After {operation}: {"-".join(codes)}")

        if "RSA_DEC" in operation:
            n, d = parse_two_ints(operation)
            decrypted_text = ""

            if d > n:
                print("INVALID value of d")
                return

            if not result:
                pass
            else:
                latest_update = result[-1]
                for code in latest_update:
                    decrypted_text += chr(pow(code, d, n))

                result.append(decrypted_text)
                print(f"After {operation}: {decrypted_text}")

        if "B64_ENC" in operation:
            bits = "".join(char_to_binary(c) for c in text)

            rem = len(bits) % 6
            if rem:
                bits += "0" * (6 - rem)

            encoded = "".join(
                base64_alphabet[int(bits[i:i + 6], 2)]
                for i in range(0, len(bits), 6)
            )
            encoded += "=" * (-len(encoded) % 4)

            print(f"After B64_ENC: {encoded}")

        if "B64_DEC" in operation:
            stripped = text.rstrip("=")
            if any(ch not in base64_alphabet for ch in stripped):
                print("INVALID base64 string", end="")
                return

            bits = "".join(format(base64_alphabet.index(ch), "06b") for ch in stripped)
            usable = len(bits) // 8 * 8  # drop leftover padding bits
            raw = bytes(int(bits[i:i + 8], 2) for i in range(0, usable, 8))

            result.append([int(y) for y in raw.decode('utf-8', errors='replace').split('-')])
            print(f"After {operation}: {raw.decode('utf-8', errors='replace')}")

    
if __name__ == "__main__":
    main()
