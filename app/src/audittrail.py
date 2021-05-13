import csv

def audittrail_creation(audittrail_input, apikey_verification):
    with open('AuditTrail.csv', 'a', newline='') as audittrail:
        fieldnames = ['first name', 'last name', 'date of birth', 'test date', 'validation date', 'issuing authority',
                      'test id', 'validator', 'internal id', 'first name validator', 'last name validator', 'company']
        auditwriter = csv.DictWriter(audittrail, fieldnames=fieldnames)
        auditwriter.writerow(
            {
             'first name': audittrail_input[0], 'last name': audittrail_input[1], 'date of birth': audittrail_input[2],
             'test date': audittrail_input[3], 'validation date': audittrail_input[4],
             'issuing authority': audittrail_input[5], 'test id': audittrail_input[6],
             'validator': audittrail_input[7], 'internal id': apikey_verification[1],
             'first name validator': apikey_verification[2], 'last name validator': apikey_verification[3],
             'company': apikey_verification[4]
             }
        )