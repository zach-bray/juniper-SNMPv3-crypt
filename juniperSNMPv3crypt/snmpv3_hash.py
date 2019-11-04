#!/usr/bin/env python

"""
Author: Zach Bray

This file returns a hash of the snmpv3 profile according to RFC 3414
https://tools.ietf.org/html/rfc3414#appendix-A.2.1
"""

import hashlib

# uses mgmt ip addr to genereate engine id
# the default prefix is for Juniper
def gen_engineid(ipaddr, prefix="80000a4c01"):
	suffix = ""

	for octet in ipaddr.split('.'):
		suffix += '{0:0{1}x}'.format(int(octet), 2)

	return prefix + suffix

# returns the hash of all values
def hash_profile(user="username", auth=None, priv=None, alg="sha1", engineid=None):
	
	auth_msg = derive_msg(auth, engineid, alg)
	priv_msg = derive_msg(priv, engineid, alg) if priv else "-"
	
	mode = "authPriv" if priv else "authNoPriv"

	return {
		"user": user,
		"auth": auth_msg,
		"priv": priv_msg,
		"mode": mode,
		"exsi_str": user + "/" + str(auth_msg) + "/" + str(priv_msg) + "/" + mode
	}


# use the passhprase and engineid to build the digest
def derive_msg(passphrase, engineid, alg):
	digest = get_passphrase_digest(passphrase, alg)

	local_hash = hashlib.new(alg)
	local_hash.update(digest)
	local_hash.update(bytearray.fromhex(engineid))
	local_hash.update(digest)

	return local_hash.hexdigest()

# expand the passphrase to 1MB and hash it
def get_passphrase_digest(passphrase, alg):
	MB = pow(2,20)
	c = MB // len(passphrase)
	o = MB % len(passphrase)
	expanded = (passphrase * c + passphrase[:o]).encode('utf-8')
	
	local_hash = hashlib.new(alg)
	local_hash.update(expanded)

	return local_hash.digest()