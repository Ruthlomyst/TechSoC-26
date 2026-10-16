# CyberSecurity : Scramble and Pack: RSA + Base64

A beginner cybersecurity problem statement in C++. You will build a small pipeline that can **encrypt**, **decrypt**, **encode** and **decode** text.

**Prerequisites:** C++ basics (variables, loops, strings, functions) and OOP basics.

**Contents**

1. [Background](#background)
2. [Encryption vs Encoding](#encryption-vs-encoding)
3. [Introduction to RSA](#introduction-to-rsa-encryption)
4. [Introduction to Base64](#introduction-to-base64-encoding)
5. [Your Task](#your-task)
6. [Specification](#specification)
7. [Operation Conventions](#operation-conventions)
8. [Rules](#rules)
9. [Input Format](#input-format)
10. [Output Format](#output-format)
11. [More Examples](#more-examples)
12. [Hints](#hints)
13. [Bonus](#bonus-not-for-marks)
14. [Resources and Official Docs](#resources-and-official-docs)
15. [Closing Remarks](#closing-remarks)

---

## Background

Cybersecurity is the field of keeping information safe from people who are not supposed to see it. Every time you log in to a website, pay with UPI, or open a "secure" page, some cryptography is working quietly in the background. While it might look like pure magic at first, do not worry. Once you build it yourself, you will realise it is just loops, strings and arithmetic. (It does get much harder later, but also much more fun :D)

In this PS, you will build a small pipeline using two algorithms: **RSA** and **Base64**.

## Encryption vs Encoding

Beginners often mix these up, so read this carefully.

| | Encryption | Encoding |
|---|---|---|
| Purpose | Hide the data from others | Change the format so data can travel or be stored |
| Needs a key? | Yes | No |
| Can anyone reverse it? | Only the person with the right key | Yes, anyone |
| In this PS | RSA | Base64 |

## Introduction to RSA (encryption)

RSA was published in 1977 by three researchers at MIT: Rivest, Shamir and Adleman (the R, S and A). Its big idea was new at the time: **you do not need to share a secret key in advance**.

RSA uses a pair of keys:

- A **public key** `(n, e)`. Anyone can have it. It is used to **lock** (encrypt) a message.
- A **private key** `(n, d)`. Only the owner keeps it. It is used to **unlock** (decrypt) the message.

Think of it like a padlock that anyone can click shut, but only you have the key to open.

### How the keys are made

1. Pick two prime numbers `p` and `q`.
2. Compute `n = p * q`.
3. Compute `phi = (p - 1) * (q - 1)`.
4. Pick a number `e` such that `gcd(e, phi) = 1`. Here `gcd` is the greatest common divisor, so this just means `e` and `phi` have no common factor other than 1.
5. Find a number `d` such that `(e * d) % phi == 1`.

### How it works

For a number `m` (smaller than `n`):

- Encrypt: `c = (m ^ e) mod n`
- Decrypt: `m = (c ^ d) mod n`

### Example

Take `p = 13` and `q = 17`.

- `n = 13 * 17 = 221`
- `phi = 12 * 16 = 192`
- Pick `e = 5` (5 and 192 share no factors)
- `d = 77`, because `5 * 77 = 385 = 2 * 192 + 1`

Public key is `(221, 5)`, private key is `(221, 77)`.

Encrypt the letter `H` (ASCII 72): `72^5 mod 221 = 89`

Decrypt 89: `89^77 mod 221 = 72`, which is `H` again.

The numbers here are tiny so that you can follow them by hand. Real RSA uses primes that are hundreds of digits long, which is why nobody can work out `d` from `n`. With `n = 221`, anyone can factor it in one second, so **this version is only for learning and is not secure**.

### Choosing your own keys

You can make your own key pair for any test case. Follow the same five steps as above, with a few limits for this PS:

1. Pick two **different** small primes `p` and `q` so that `n = p * q` is between 127 and 1000. Below 127 will not work, because ASCII values go up to 126 and every `m` must be smaller than `n`. Above 1000 breaks the input limits.
2. Compute `n = p * q` and `phi = (p - 1) * (q - 1)`.
3. Choose `e` (the **public** exponent): try `e = 3, 5, 7, 11, ...` and take the first one where `gcd(e, phi) = 1`.
4. Choose `d` (the **private** exponent): try `d = 2, 3, 4, ...` until `(e * d) % phi == 1`. The first one you find is your `d`.
5. Your public key is `(n, e)` and your private key is `(n, d)`. Keep `p`, `q`, `phi` and `d` secret. Only `n` and `e` are shared.

To check `gcd`, use the Euclidean algorithm:

```cpp
int gcd(int a, int b) {
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}
```

Always test your pair: encrypt a character with `(n, e)`, decrypt it with `(n, d)`, and make sure you get the same character back.

Here are some ready-made pairs you can use for testing:

| p | q | n | phi | e | d |
|---|---|---|---|---|---|
| 11 | 13 | 143 | 120 | 7 | 103 |
| 13 | 17 | 221 | 192 | 5 | 77 |
| 17 | 19 | 323 | 288 | 5 | 173 |
| 23 | 29 | 667 | 616 | 5 | 493 |

### Where is RSA used?

- **HTTPS (the lock icon in your browser):** websites use public-key cryptography like RSA to prove their identity and to agree on secrets with your browser.
- **SSH and digital signatures:** developers log in to servers and sign software with RSA keys.
- Messaging apps like WhatsApp use strong modern encryption in the same family of ideas, so only you and the receiver can read your chats.

## Introduction to Base64 (encoding)

Old email and messaging systems were built only for plain text. If you sent them images, files or odd symbols, the data got corrupted on the way. Base64 solves this by turning any data into just 64 safe characters:

`A-Z` (index 0 to 25), `a-z` (26 to 51), `0-9` (52 to 61), `+` (62), `/` (63).

### How to encode

1. Take 3 characters (24 bits) and join their binary.
2. Split the 24 bits into four groups of 6 bits.
3. Each group is a number from 0 to 63. Replace it with the matching character from the table.

Example with `Man`:

| Character | ASCII | Binary |
|---|---|---|
| M | 77 | 01001101 |
| a | 97 | 01100001 |
| n | 110 | 01101110 |

Joined: `010011010110000101101110`
Split: `010011 010110 000101 101110`, which is 19, 22, 5, 46, which gives `TWFu`.

### Padding

If the last group has fewer than 3 characters, fill the end with `=`:

- 1 character left gives 2 Base64 characters followed by `==`
- 2 characters left gives 3 Base64 characters followed by `=`

### Where is Base64 used?

Attaching files in emails, putting small images directly inside web pages, and inside the login tokens that apps use to remember you.

Real systems usually **encrypt first, then encode**, so the secret data can travel through plain-text channels. That is the pipeline you will build.

## Your Task

Create a program that takes in a message along with a list of operations, applies them in the given order, and prints the result after every step.

Presume that there are no input errors. Only valid operations with valid parameters are given, and decoding and decryption are only called on valid data.

## Specification

Your program must be capable of:

- Taking in a string `S` (the message).
- Taking in an array `[Arr]` of any length, populated with operations.
- Applying the operations in the exact order in which they appear in the array. The output of one operation is the input of the next.
- Printing the string after every operation.

You are required to implement these four operations:

| Operation | Meaning |
|---|---|
| `RSA_ENC(n,e)` | RSA encrypt every character using public key `(n, e)` |
| `RSA_DEC(n,d)` | RSA decrypt using private key `(n, d)` |
| `B64_ENC` | Base64 encode |
| `B64_DEC` | Base64 decode |

You may implement more operations (for example a Caesar cipher or a Hex encoder), but document them and their calling format clearly.

## Operation Conventions

- `RSA_ENC(n,e)` treats every character of the string as its ASCII value `m`, and computes `c = (m ^ e) mod n` for each one.
- The resulting numbers are written in order, separated by a `-` (dash), with no spaces. For example, `89-99`.
- `RSA_DEC(n,d)` takes such a dash-separated string, computes `m = (c ^ d) mod n` for each number, and turns each result back into a character.
- Do not compute `m ^ e` directly, because it becomes too large for any integer type. Multiply step by step and take `mod n` after every multiplication (see "Computing m ^ e mod n" below).
- Base64 uses the standard table given above, with `=` padding.
- Base64 works on the ASCII value of each character of the input string, whatever that string is (it can contain digits and dashes).
- `RSA_DEC` must perfectly undo `RSA_ENC` when given the matching keys, and `B64_DEC` must perfectly undo `B64_ENC`. Test this yourself.

### Computing m ^ e mod n

`72^5` is still small, but something like `126^77` is far too big for any integer type. The trick is this rule:

```
(a * b) mod n  =  ((a mod n) * (b mod n)) mod n
```

So you do not need the full power at all. Start with `result = 1`, then repeat `e` times: multiply `result` by `m`, and immediately take `mod n`. The number never grows beyond `n * n`, which fits easily in a `long long`.

Worked example, `72^5 mod 221`:

| Step | Calculation | After `mod 221` |
|---|---|---|
| 1 | 1 * 72 = 72 | 72 |
| 2 | 72 * 72 = 5184 | 101 |
| 3 | 101 * 72 = 7272 | 200 |
| 4 | 200 * 72 = 14400 | 35 |
| 5 | 35 * 72 = 2520 | 89 |

The answer is 89, the same value as in the RSA example above.

As code:

```cpp
long long modPow(long long m, long long e, long long n) {
    long long result = 1;
    for (long long i = 0; i < e; i++) {
        result = (result * m) % n;
    }
    return result;
}
```

Use this one function for both encryption (`modPow(m, e, n)`) and decryption (`modPow(c, d, n)`).

## Rules

- Any programming language may be used.
- Single file containing the code.
- Must run in the terminal.
- Create a separate function for each operation (for example `rsaEncrypt`, `rsaDecrypt`, `base64Encode`, `base64Decode`) and a helper for modular power.
- Do not use any library that already does Base64 or RSA for you. Writing them yourself is the whole point.

## Input Format

The input consists of two elements separated by a single space.

1. A string `S` (the message). It contains no spaces, and it does not contain the characters `[`, `]`, `(`, `)` or `,`.
2. An array of operations (non-spaced).
   - In the exact same format.
   - Square brackets and all.
   - Operations are separated by commas, with no spaces.

Constraints:

- `1 <= |S| <= 100`
- `127 <= n <= 1000`, so every ASCII character fits below `n`
- `e` and `d` are valid keys for the given `n`, and `1 < e, d < n`
- `1 <= number of operations <= 10`

### Example Input

```
HI [RSA_ENC(221,5),B64_ENC]
```

This means: take `HI`, encrypt every character with RSA using `n = 221` and `e = 5`, then Base64 encode the result.

### Input Syntax

```
RSA_ENC(221,5)
RSA_DEC(221,77)
B64_ENC
B64_DEC
```

The operation names are case-sensitive. `RSA_ENC` and `RSA_DEC` always have exactly two numbers inside the brackets. `B64_ENC` and `B64_DEC` have no brackets.

## Output Format

Print one line for every operation, in the same order as the array. Each line has the form:

```
After <operation>: <resulting string>
```

### Example Output

For the input:

```
HI [RSA_ENC(221,5),B64_ENC]
```

the output should be:

```
After RSA_ENC(221,5): 89-99
After B64_ENC: ODktOTk=
```

## More Examples

**Receiver's side (decode first, then decrypt):**

Input:

```
ODktOTk= [B64_DEC,RSA_DEC(221,77)]
```

Output:

```
After B64_DEC: 89-99
After RSA_DEC(221,77): HI
```

**Single character:**

Input:

```
A [RSA_ENC(221,5),B64_ENC]
```

Output:

```
After RSA_ENC(221,5): 182
After B64_ENC: MTgy
```

**Base64 padding:**

Input:

```
Hi [B64_ENC]
```

Output:

```
After B64_ENC: SGk=
```

The `=` is there because the last group has only 2 characters.

## Hints

- For modular power, start with `result = 1` and multiply it by the base `e` times, taking `% n` after every multiplication. Use `long long` to be safe.
- To read the array, read the message with `cin >> s`, then read the array as one more string. Cut it at the commas, and read the numbers inside the brackets (they can be more than one digit).
- For `RSA_DEC`, split the input string at every `-` to get the numbers, and use `stoi` to convert each piece.
- For Base64, keep the table in one string: `"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"` and use the 0 to 63 number as an index. You will need `<<`, `>>` and `&`, so go through bit operations.

## Bonus🦕✨

1. Write a function that takes `p`, `q` and `e`, and finds `d` on its own. (Hint: try every `d` from 1 to `phi` until `(e * d) % phi == 1`.)
2. Break the toy RSA: given only `n = 221` and `e = 5`, write a program that finds `p` and `q` by trial division, and then computes `d`. Then think about why this would not work if `n` had 600 digits.
3. Answer in 2 to 3 lines: *If someone knows a message was Base64 encoded, can they read it? Why?*

## Resources and Official Docs

### Standards and specifications

| Topic | Link |
|---|---|
| Base64 (official standard, RFC 4648) | https://www.rfc-editor.org/rfc/rfc4648 |
| RSA (official standard, PKCS #1 v2.2, RFC 8017) | https://www.rfc-editor.org/rfc/rfc8017 |
| RSA original paper (Rivest, Shamir, Adleman, 1978) | https://people.csail.mit.edu/rivest/Rsapaper.pdf |

RFC 4648 is the real specification of the Base64 table and padding rules used in this PS. RFC 8017 is the industry standard for RSA. It is written for professionals, so treat it as a "look at it, don't read it all" reference. The original paper is much easier to read.

### Learn the concepts

| Topic | Link |
|---|---|
| Base64 (MDN glossary) | https://developer.mozilla.org/en-US/docs/Glossary/Base64 |
| RSA cryptosystem (Wikipedia, read the "Example" section) | https://en.wikipedia.org/wiki/RSA_(cryptosystem) |
| Modular exponentiation (the step-by-step `% n` trick) | https://en.wikipedia.org/wiki/Modular_exponentiation |

### C++ documentation

| Topic | Link |
|---|---|
| `std::string` | https://en.cppreference.com/w/cpp/string/basic_string |
| `stoi` | https://en.cppreference.com/w/cpp/string/basic_string/stol |
| Bitwise operators (`<<`, `>>`, `&`) | https://en.cppreference.com/w/cpp/language/operator_arithmetic |

## Closing Remarks

Cryptography starts with ideas like these: hide the message, change its shape, and think about how someone else would break it. We hope this PS gives you a small taste of that and makes you curious to go further.