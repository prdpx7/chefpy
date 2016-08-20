from setuptools import setup

setup(name="chefpy",
      version="0.314",
      description="Unofficial Codechef Api for user's status,rank,solutions etc.",
      url="http://github.com/zuck007/chefpy",
      author="Pradeep Khileri",
      author_email="pradeepchoudhary009@gmail.com",
      license="MIT",
      packages=["chefpy"],
      scripts=["./bin/Xchefpy"],
      classifiers=[
        'Development Status :: 0.314 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        
      ],
      keywords='api codechef automation command-line linux web-scraping',
      install_requires=[
          "bs4",
          "requests",
          "urllib2",
      ],
      zip_safe=False)

