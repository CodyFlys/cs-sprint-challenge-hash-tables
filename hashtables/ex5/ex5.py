# Your code here



def finder(files, queries, cache={}):
    result = []

    for file in files:
        print(file)

    for query in queries:
        print(query)


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
