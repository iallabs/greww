import greww.data.basics as basics

ftests = ['test_basics']

DEFAULT=basics.DEFAULT



def test_basics():
    global DEFAULT
    print("directory ", basics.lsdir(DEFAULT))
