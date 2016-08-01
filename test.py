#!/usr/bin/python

import puppet

p = puppet.Puppet(host='puppetmaster01.core.cmc.lan', port=8140, key_file='api-key.pem', cert_file='api-cert.pem')

print p.certificates()

p.certificate_delete()
