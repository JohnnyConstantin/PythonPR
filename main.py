import sqlite3

def main():
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT ((2*MAX(two) - SUM(two)) + (2*MAX(four) - SUM(four)) + (2*MAX(three) - SUM(three))) FROM test GROUP BY five")
    one_result = cur.fetchmany(5)
    print(one_result)


if __name__ == '__main__':
    main()