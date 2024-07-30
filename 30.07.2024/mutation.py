import functools
def mutate_string(string, position, character):
    a=list(string)
    a[position]=character
    j=functools.reduce(lambda x,y:x+y,a)
    return j