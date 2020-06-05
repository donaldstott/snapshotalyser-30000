from setuptools import setup

setup(
    name='snapshotalyser-30000',
    version='0.1',
    author="Robin Norwood",
    author_email="robin@acould.guru",
    description="Snapshotalyser 30000 is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/donaldstott/snapshotalyser-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
