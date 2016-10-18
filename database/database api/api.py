import mysql.connector

inputs = [line.strip().split(':')[1] for line in open('credentials.txt').readlines()]

cnx = mysql.connector.connect(user=inputs[0], password=inputs[1], host=inputs[2], database=inputs[3])

cursor = cnx.cursor()

# open queries.txt
queries = [[line.strip().split('?')[0], int(line.strip().split('?')[1])] for line in open('queries.txt')]

# open commands.txt
commands = [line.strip() for line in open('commands.txt')]

def prompt():
    for x,command in enumerate(commands):
        print '['+str(x+1)+'] ' + command
    print('[0] Quit')

def query(pick):

    statement = str(queries[pick-1][0])
    arguments = list()

    for i in xrange(int(queries[pick-1][1])):
        arguments.append(int(input('')))

    for x, argument in enumerate(arguments):
        statement = statement.replace(' ' + str(x) + ' ', str(argument))

    cursor.execute(statement)

    for x, record in enumerate(cursor):
        print x+1,
        for attribute in record:
            print attribute,
        print('\n')

# Description of API
print 'Hospital Pharmacy API\n'

while 1:
    prompt()
    ans = input()

    if ans is 0:
        print('Goodbye! :)')
        break

    query(ans)

cnx.close()

"""
    This API can work with anyone's queries, just follow the same convention as mine.

    I used Python 2.7 for this API.

    Usage:

        credentials.txt:
            To the right of the colon symbol input the needed value for your database.
            MAKE SURE THERE IS NO WHITESPACE AROUND THE COLON OTHERWISE THE API WILL NOT PARSE YOUR CREDENTIALS PROPERLY.

        commands.txt:
            Put the description of the query per line.

        queries.txt:
            For each of the query descriptions, put your mysql query without quotes per line.

              Example:
                Description: Get all the patients first names, last names, and weight where their weight is greater than x

                Query: select fname, lname, weight from patient where weight > 0 ?1

                The example above are both on the same line in their respective files.

            For each argument in your query that the user will put in your query place 0,1,2,3,.. etc. with whitespace
            around your number. Right after your query statement place a ? followed by the number of arguments to input.

                Example:
                    select p.fname, p.lname, d.dispensed, m.description from patient p, dispenses d, medication m
                    where p.id = d.patient_id and d.prescription_id = m.id and (m.description like '% 0 %' or m.description like '% 1 %')?2


    Fall 2015
    CMPE 4333.01 Database Design and Implementation

    Dustin Ramsey Torres

"""
