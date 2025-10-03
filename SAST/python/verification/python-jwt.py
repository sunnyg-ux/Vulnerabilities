# If a JSON Web Token (JWT) is not signed with a strong cipher algorithm 
# (or not signed at all) an attacker can forge it and impersonate user identities.

#     Don’t use none algorithm to sign or verify the validity of a token.
#     Don’t use a token without verifying its signature before.

import python_jwt

jwt.process_jwt(token)  # Noncompliant