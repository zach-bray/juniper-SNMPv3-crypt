# juniper SNMPv3 crypt
This is python library to deal with hashing (md5 or sha1) and then encrypting SNMPv3 user profiles for Juniper devices. The hashing follows RFC 3414 for snmpv3 profiles.
<br/>
The $9$ encryption is a port from Perl from https://metacpan.org/pod/Crypt::Juniper
<br/>
The encrypt function supports a seed in order to have idempotent encryption.

### Install
This package works in both python 2 and 3
`pip install juniperSNMPv3crypt`
