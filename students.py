
contacts = {
    'number': 4,
    'students':
        [
            {'name':'jessica', 'email':'jessica@voorbeeld.com'},
            {'name':'danny', 'email': 'danny@voorbeeld.com'},
            {'name':'marlon', 'email': 'marlon@voorbeeld.com'},
            {'name':'quinty', 'email': 'quity@voorbeeld.com'}
            {'name':'lars', 'email': 'lars@voorbeeld.com'}
            {'name':'Fred', 'email': 'fred@voorbeeld.com'}
        ]
}

print('student emails:')

for student in contacts['students']:
    print(student['email'])
