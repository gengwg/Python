# find all email addresses between <>
st = "Anurag Gupa <AGupta10@example.com>; Fezal Miza <FMirza@example.com>; Donld Slvia Jr. <Donad.Sivia@xyz.com>; Lar Gln <lary.glnn@jht.com>"

import re
emails = re.findall("\<(.*?)\>", st)
for email in emails:
    print email
