ct = """Fsqp: rhurk415
Ie: ljjkhwaoj
Vygplkc: dr: rrudok ld tig hwuw

---

ne,

ajp rge hlpjy nayx gvt dakljn zdfpth nz enxe qoga. rip tcqe tlkmz ikyff hwu exnvzxrz-jv'w gst ceuyz yeltwo.

zltq, kubvm dazsixzfz rafpc jp xmk vxdpe.hmj. fcbdq ae c oje wa amfgexisly?

"mou dpq npxcee vpkel nca nzsu - xutm vpmis jisbfn fl hfz: ikhloknq{uw0jll_i3s3q_e1h}"

vxd ehft zx co'p hmqquxfta, lff mdk cgir emv ujhc rvdn etrwg ujtgvpfa cscs.

wqwq yr xv qho bflc nqui."""
# Convert to non-ascii first
ct = ct.encode('utf-8', 'ignore').decode('utf-8')

# Function to Encrypt using the Vigenère cipher.
def vigenere_decrypt(cipher_text, key):
    key_offset = [ord(k.upper()) - ord('A') for k in key if k.isalpha()]
    print(key_offset)
    decrypted_text = ''

    for i in range(len(cipher_text)):
        if not cipher_text[i].isalpha():
            decrypted_text += cipher_text[i]
            continue

        if cipher_text[i].isupper():
            base = ord('A')
        else:
            base = ord('a')

        new_char = (ord(cipher_text[i]) - base - key_offset[i % len(key_offset)]) % 26 + base

        decrypted_text += chr(new_char)
    # Return the final decrypted text
    return decrypted_text
print(vigenere_decrypt(ct, 'coqyxxghijkxxxxgcxxaaaaaaaaaxz'))

# coqyghijkglmcxxxxxxxxxdefghijk

# coqyghijkglmcxxxxxxxxxdefghijkxxx resembles deadface - 33
# also from the distance between the hij's - 22
# therefore must repeat every 11 characters

# fghijklm
# f to m must be in it somewhere for the deadface
# deadface{gh0sts_n3v3r_d1e}