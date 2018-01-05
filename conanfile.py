#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class CimgConan(ConanFile):
    name = "CImg"
    version = "218"
    url = "https://github.com/bincrafters/conan-cimg"
    description = "The CImg Library is a small, open-source, and modern C++ toolkit for image processing"
    
    # Indicates License type of the packaged library
    license = "https://github.com/dtschump/CImg/blob/master/Licence_CeCILL_V2-en.txt"
    
    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]
    
    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/dtschump/CImg"
        tools.get("{0}/archive/v.{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-v." + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)


    def package(self):
        include_folder = os.path.join(self.source_subfolder)
        self.copy(pattern="LICENSE")
        self.copy(pattern="CImg.h", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
