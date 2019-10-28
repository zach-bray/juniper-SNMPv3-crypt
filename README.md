# juniper-crypt
Encrypts and decrypts Juniper $9$ passwords. This is a port from Perl from https://metacpan.org/pod/Crypt::Juniper
<br/>
The encrypt function supports a seed in order to have idempotent encryption.

### Install
`pip install junipercrypt`

### Usage
```
>>> from junipercrypt import junipercrypt
>>> print junipercrypt.encrypt('hey')
$9$GBUi.Qz69pB
>>> print junipercrypt.encrypt('hey')
$9$VSbYoDjqmT3
>>> print junipercrypt.encrypt('hey', seed=1)
$9$CiJ1Au1SyKMX-
>>> print junipercrypt.encrypt('hey', seed=1)
$9$CiJ1Au1SyKMX-
>>> print junipercrypt.decrypt('$9$CiJ1Au1SyKMX-')
hey
```