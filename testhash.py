#!/usr/bin/python3


from FileUtils.hashob import hashob


def main():
    hashobject = hashob.hasher_if('testdoc.txt','md5')
    hashobject.fileaccess()
    hashobject.hashtype()
    hashobject.hashfile()
    print(hashobject.returnhexhash())

if __name__=="__main__":
    main()
