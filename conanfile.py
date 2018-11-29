#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class VisitStructConan(ConanFile):
    name = "visit_struct"
    version = "1.0"
    url = "https://github.com/ambroff/conan-visit_struct"
    description = "A miniature library for struct-field reflection in C++"

    exports_sources = "include/*"
    no_copy_source = True

    # Indicates License type of the packaged library
    license = "BSL-1.0"

    def source(self):
        archive_url = 'https://github.com/cbeck88/visit_struct/archive/v{}.zip'.format(
            self.version)
        checksum = '7152df2f6b0ce4c64d94a116073b196ec1e188a0a142a5138b016562f9bdc4e4'
        tools.get(archive_url, sha256=checksum)

    def package(self):
        self.copy(pattern="LICENSE", dst="license")
        self.copy(
            '*.hpp',
            src=os.path.join('{}-{}'.format(self.name, self.version), 'include'),
            dst='include')
    
    def package_id(self):
        self.info.header_only()
