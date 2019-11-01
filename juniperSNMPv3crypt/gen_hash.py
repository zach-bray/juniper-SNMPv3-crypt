#!/usr/bin/env python

"""
This file returns a hash of the snmpv3 profile


"""

import hashlib

from itertools import repeat

# uses mgmt ip addr to genereate engine id
def gen_engineid(ipaddr, prefix="80000a4c01"):
	suffix = ""

	for octet in ipaddr.split('.'):
		suffix += '{0:0{1}x}'.format(int(octet), 2)

	return prefix + suffix

# returns the hash of all values
def hash_profile(user="username", auth=None, priv=None, alg="sha1", engineid=None):
	
	auth_msg = derive_msg(auth, engineid, alg)
	priv_msg = derive_msg(priv, engineid, alg) if priv else "-"
	
	mode = "authpriv" if priv else "auth"

	return {
		"user": user,
		"auth": auth_msg,
		"priv": priv_msg,
		"mode": mode,
		"exsi_str": user + "/" + str((auth_msg)) + "/" + str((priv_msg)) + "/" + mode
	}


# first expand secret to 1MB length and then hash
def derive_msg(secret, engineid, alg):
	MB = pow(2,20)
	c = MB // len(secret)
	expanded = u''.join(list(repeat(secret, c)))[:MB].encode('utf-8')
	
	digest = bytearray(hashlib.md5(expanded).digest())
	engine = bytearray.fromhex(engineid)
	
	local_hash = hashlib.new(alg)
	local_hash.update(digest)
	local_hash.update(engine)
	local_hash.update(digest)

	return local_hash.hexdigest()
