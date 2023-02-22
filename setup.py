import setuptools
from ims_envista.version import Version

setuptools.setup(name='ims_envista',
                 version='{{VERSION_PLACEHOLDER}}',
                 long_description_content_type="text/markdown",
                 description='Israel Meteorological Service Envista API wrapper package',
                 long_description=open('README.md').read().strip(),
                 author='Guy Khmelnitsky',
                 author_email='guykhmel@gmail.com',
                 url='https://github.com/GuyKh/py-ims-envista',
                 packages=setuptools.find_packages(),
                 python_requires=">=3.6",
                 install_requires=["requests","urllib3","loguru"],
                 license='MIT License',
                 zip_safe=False,
                 keywords=['ims','weatheril','Israel Meteorological Service','Meteorological Service','weather'],
                 classifiers=[    "Intended Audience :: Developers",
                            "Topic :: Software Development :: Build Tools",
                            "License :: OSI Approved :: MIT License",
                            "Programming Language :: Python :: 3.6",
                            "Programming Language :: Python :: 3.7",
                            "Programming Language :: Python :: 3.8",
                            "Programming Language :: Python :: 3.9",
                            "Programming Language :: Python :: 3.10",
                            "Natural Language :: English",
                            "Operating System :: OS Independent",])
