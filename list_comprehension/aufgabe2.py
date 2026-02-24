"""
Aufgabe: filtere aus der E-mail Liste alle Adressen, die auf den @test
Server  führen
"""

liste = ["test@gmail.com", "info@test.com", "admin@test.com",
          "test1@test.com", "info@yahoo.com", "admin@gmail.com"]

test_mails = [email for email in liste if email.endswith("@test.com")]
print(test_mails)