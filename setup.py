import os
import glob
import fnmatch
from setuptools import setup


def opj(*args):
    path = os.path.join(*args)
    return os.path.normpath(path)

badnames = [".pyc", ".py", "~", "no_"]


def find_data_files(srcdir, *wildcards, **kw):
    # get a list of all files under the srcdir matching wildcards,
    # returned in a format to be used for install_data
    def walk_helper(arg, dirname, files):
        if '.svn' in dirname:
            return
        names = []
        lst, wildcards = arg
        for wc in wildcards:
            wc_name = opj(dirname, wc)
            for f in files:
                filename = opj(dirname, f)

                if not any(bad in filename for bad in badnames):
                    if fnmatch.fnmatch(filename, wc_name)\
                            and not os.path.isdir(filename):
                        names.append(filename)
        if names:
            lst.append((dirname, names))

    file_list = []
    recursive = kw.get('recursive', True)
    if recursive:
        os.path.walk(srcdir, walk_helper, (file_list, wildcards))
    else:
        walk_helper((file_list, wildcards),
                    srcdir,
                    [os.path.basename(f) for f in glob.glob(opj(srcdir, '*'))])
    return file_list
files = find_data_files('pyramid_elfinder/', '*.*')
print 'files', files

setup(
    name='pyramid_elfinder',
    version='0.0.0',
    url='http://github.com/ITCase/pyramid_elfinder/',
    author='Aleksandr Rakov',

    packages=['pyramid_elfinder'],  # 'pyramid_elfinder.tests'],
    data_files=files,
    include_package_data=True,
    zip_safe=False,
    test_suite="nose.collector",
    license="GPL",
    package_dir={'pyramid_elfinder': 'pyramid_elfinder'},
    package_data={
        'pyramid_elfinder': [
            'static/*.*',
        ],
    },
    description='Connector elfinder for pyramid.',
    long_description=open('README.md').read(),
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Natural Language :: Russian',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Framework :: Pyramid ",
        "Topic :: Internet",
        "License :: Repoze Public License",
    ],
)