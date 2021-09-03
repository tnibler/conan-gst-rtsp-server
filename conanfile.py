from conans import ConanFile, CMake, tools
import os


class GstrtspserverConan(ConanFile):
    name = "gst_rtsp_server"
    version = "1.18.4"
    description = "RTSP server based on GStreamer"
    url = "https://github.com/conan-multimedia/gst-rtsp-server-1.0"
    homepage = "https://github.com/GStreamer/gst-rtsp-server"
    license = "GPLv2+"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {
        "shared": True
    }
    generators = "cmake"
    requires = (
        "gstreamer/1.18.4",
        "gst_plugins_base/1.18.4",
        "glib/2.69.2",
    )
    source_subfolder = "gst-rtsp-server"
    build_subfolder = "build"
    remotes = {'origin': 'https://github.com/GStreamer/gst-rtsp-server.git'}

    def source(self):
        tools.mkdir(self.source_subfolder)
        with tools.chdir(self.source_subfolder):
            self.run('git init')
            for key, val in self.remotes.items():
                self.run("git remote add %s %s" % (key, val))
            self.run('git fetch --all')
            self.run('git reset --hard %s' % (self.version))
            self.run('git submodule update --init --recursive')

    def build(self):
        cmake = CMake(self)
        if not tools.os_info.is_windows:
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = "ON"

        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ['gstrtspserver']
        self.cpp_info.includedirs = ['include/gst-rtsp-server'] + \
            self.deps_cpp_info['gst_plugins_base'].includedirs + \
            self.deps_cpp_info['gstreamer'].includedirs
