# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for file in files:
        f = file[1:].split('/')
        if len(f) == 2:
            cache[f[1]] = f[0]
        if len(f) > 2:
            for i in range(len(f)-1):
                cache[f[i+1]] = file[1:].split('/')[i]
    result = []
    for q in queries:
        
        if q in cache:
            answer = q
            parentfile = cache[q]
            answer = cache[q]+'/'+answer
            while parentfile in cache:
                answer = cache[parentfile]+'/'+answer
                parentfile = cache[parentfile]
            result.append("/"+answer)
    return result


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
