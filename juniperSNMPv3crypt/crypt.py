#!/usr/bin/env python

"""
A python port of https://metacpan.org/pod/Crypt::Juniper

Original Author: Kevin Brintnall
Ported by: Zach Bray
"""

import re
import random

MAGIC = "$9$"
EXTRA = {}
ENCODING = [
    [1,  4, 32],
    [1, 16, 32],
    [1,  8, 32],
    [1, 64],
    [1, 32],
    [1,  4, 16, 128],
    [1, 32, 64]
]

# letter families to encrypt with
FAMILY = ["QzF3n6/9CAtpu0O", "B1IREhcSyrleKvMW8LXx", "7N-dVbwsY2g4oaJZGUDj", "iHkq.mPf5T"]
EXTRA = {char: 3-i for i,fam in enumerate(FAMILY) for char in fam}

# builds regex to match valid encrypted string
letters = MAGIC + "([" + ''.join(FAMILY) + "]{4,})"
letters = re.sub(r"([-|/|$])", r"\\\1", letters)
VALID = r"^" + letters + "$"

# forward and reverse dicts
NUM_ALPHA = [char for char in ''.join(FAMILY)]
ALPHA_NUM = {NUM_ALPHA[i]: i for i,c in enumerate(NUM_ALPHA)}


def decrypt(crypt):
    m = re.match(VALID, crypt)

    if not m:
        print('invalid crypt string')
        exit(1)

    chars = m.group(1)
    chars, first = _nibble(chars, 1)    
    chars,_ = _nibble(chars, EXTRA[first])
    
    prev = first
    decrypt = ""

    while(chars):
        decode = ENCODING[len(decrypt) % len(ENCODING)]
        chars, nibble = _nibble(chars, len(decode))

        gaps = []
        for nib in nibble:
            dist = (ALPHA_NUM[nib] - ALPHA_NUM[prev]) % len(NUM_ALPHA) - 1
            gaps.append(dist)
            prev = nib

        decrypt += _gap_decode(gaps, decode)
    return decrypt

def _nibble(chars, length):
    nib = chars[:length]
    chars = chars[length:]
    return chars, nib

def _gap_decode(gaps, decode):
    num = 0
    for i in range(len(gaps)):
        num += gaps[i] * decode[i]
    
    return chr(num % 256)



# encrypts <secret> for junipers $9$ format
# allows use of seed for idempotent secrets
def encrypt(secret, seed=False):
    if seed:
        random.seed(seed)

    salt = _random_salt(1)
    rand = _random_salt(EXTRA[salt])

    pos = 0
    prev = salt
    crypt = MAGIC + salt + rand

    for char in secret:
        encode = ENCODING[pos % len(ENCODING)]
        crypt += _gap_encode(char, prev, encode)
        prev = crypt[-1]
        pos += 1

    return crypt

# returns number of characters from the alphabet
def _random_salt(length):
    salt = ""
    for i in range(length):
        salt += NUM_ALPHA[random.randrange(len(NUM_ALPHA))]
    return salt

# encode plain text character with a series of gaps
def _gap_encode(char, prev, encode):
    crypt = ""
    val = ord(char)
    gaps = []

    for enc in encode[::-1]:
        gaps.insert(0, val // enc)
        val %= enc

    for gap in gaps:
        gap += ALPHA_NUM[prev] + 1
        c = prev = NUM_ALPHA[gap % len(NUM_ALPHA)]
        crypt += c

    return crypt
