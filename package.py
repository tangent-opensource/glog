# -*- coding: utf-8 -*-

name = 'glog'

version = '0.4.0-ta.1.0.0'

authors = [
    'benjamin.skinner',
    'google',
]

requires = [
]

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-7']

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
    #['platform-linux', 'arch-x64'],
]

build_system = "cmake"

def commands():

     # Split and store version and package version
    split_versions = str(version).split('-')
    env.GLOG_VERSION.set(split_versions[0])
    env.GLOG_PACKAGE_VERSION.set(split_versions[1])

    env.GLOG_ROOT_DIR.set( "{root}" )
    env.GLOG_LIB_DIR.set( "{root}/lib" )
    env.GLOG_INCLUDE_DIR.set( "{root}/include" )

    env.PATH.append( "{root}/bin" )
