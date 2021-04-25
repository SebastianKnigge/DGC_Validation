import csv

def audittrail_creation(audittrail_input):
    with open('AuditTrail.csv', 'a', newline='') as audittrail:
        fieldnames = ['first name', 'last name', 'date of birth', 'test date', 'validation date', 'issuing authority',
                      'test id', 'validator']
        auditwriter = csv.DictWriter(audittrail, fieldnames=fieldnames)
        auditwriter.writerow(
            {'first name': audittrail_input[0], 'last name': audittrail_input[1], 'date of birth': audittrail_input[2],
             'test date': audittrail_input[3], 'validation date': audittrail_input[4],
             'issuing authority': audittrail_input[5], 'test id': audittrail_input[6],
             'validator': audittrail_input[7]})
