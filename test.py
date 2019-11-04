#!/usr/bin/env python

from juniperSNMPv3crypt import snmpv3_hash, crypt9

if __name__ == "__main__":
	engineid = snmpv3_hash.gen_engineid("10.81.96.10")

	print("engineid: " + engineid + "\n")

	profile = snmpv3_hash.hash_profile(user="TEST", auth="PASSWORD",
		priv="PASSWORD", engineid=engineid, alg="sha1")
	
	print(profile)