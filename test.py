#!/usr/bin/env python

from juniperSNMPv3crypt import gen_hash, crypt

if __name__ == "__main__":
	engineid = gen_hash.gen_engineid("10.81.96.10")

	print "engineid: " + engineid + "\n"

	profile = gen_hash.hash_profile(user="TEST", auth="PASSWORD",
		engineid=engineid, alg="sha1")
	
	print profile

