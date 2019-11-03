#!/usr/bin/env python

from juniperSNMPv3crypt import gen_hash, crypt
# import test2

if __name__ == "__main__":
	engineid = gen_hash.gen_engineid("10.81.96.10")

	print("engineid: " + engineid + "\n")

	profile = gen_hash.hash_profile(user="TEST", auth="PASSWORD",
		engineid=engineid, alg="sha1")
	
	print(profile['auth'])
	print("c0c44a7f1151ab9f25e7c4f6b5d118530afcf287")

	print("\n")

	# print(test2.snmpv3_key_from_password("PASSWORD", engineid, "sha1"))

