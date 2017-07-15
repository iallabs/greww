import greww.data.basics as basics

ftests = ['test_basics']

DEFAULT="/home/ubuntu"

def test_basics():
    global DEFAULT
    print("directory ", basics.lsdir(DEFAULT))
    assert "greww" in basics.lsdir(DEFAULT)
