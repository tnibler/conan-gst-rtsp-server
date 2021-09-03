cmake_minimum_required(VERSION 3.21)
project(gst-rtsp-server)

set(CMAKE_CXX_STANDARD 17)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")

# find_package(PkgConfig REQUIRED)
# pkg_check_modules(GLIB REQUIRED glib-2.0)
# pkg_check_modules(GST REQUIRED gstreamer-1.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

include_directories("gst-rtsp-server")
include_directories("${CONAN_INCLUDE_DIRS_GLIB}")
include_directories("${CONAN_INCLUDE_DIRS_GSTREAMER}")
include_directories("${CONAN_INCLUDE_DIRS_GST_PLUGINS_BASE}")

add_library(gstrtspserver
    gst-rtsp-server/gst/rtsp-server/rtsp-address-pool.c
    gst-rtsp-server/gst/rtsp-server/rtsp-auth.c
    gst-rtsp-server/gst/rtsp-server/rtsp-client.c
    gst-rtsp-server/gst/rtsp-server/rtsp-context.c
    gst-rtsp-server/gst/rtsp-server/rtsp-latency-bin.c
    gst-rtsp-server/gst/rtsp-server/rtsp-media-factory-uri.c
    gst-rtsp-server/gst/rtsp-server/rtsp-media-factory.c
    gst-rtsp-server/gst/rtsp-server/rtsp-media.c
    gst-rtsp-server/gst/rtsp-server/rtsp-mount-points.c
    gst-rtsp-server/gst/rtsp-server/rtsp-onvif-client.c
    gst-rtsp-server/gst/rtsp-server/rtsp-onvif-media-factory.c
    gst-rtsp-server/gst/rtsp-server/rtsp-onvif-media.c
    gst-rtsp-server/gst/rtsp-server/rtsp-onvif-server.c
    gst-rtsp-server/gst/rtsp-server/rtsp-params.c
    gst-rtsp-server/gst/rtsp-server/rtsp-permissions.c
    gst-rtsp-server/gst/rtsp-server/rtsp-sdp.c
    gst-rtsp-server/gst/rtsp-server/rtsp-server.c
    gst-rtsp-server/gst/rtsp-server/rtsp-session-media.c
    gst-rtsp-server/gst/rtsp-server/rtsp-session-pool.c
    gst-rtsp-server/gst/rtsp-server/rtsp-session.c
    gst-rtsp-server/gst/rtsp-server/rtsp-stream-transport.c
    gst-rtsp-server/gst/rtsp-server/rtsp-stream.c
    gst-rtsp-server/gst/rtsp-server/rtsp-thread-pool.c
    gst-rtsp-server/gst/rtsp-server/rtsp-token.c
    )

set(GST_RTSP_SERVER_HEADERS
    gst-rtsp-server/gst/rtsp-server/rtsp-address-pool.h
    gst-rtsp-server/gst/rtsp-server/rtsp-auth.h
    gst-rtsp-server/gst/rtsp-server/rtsp-client.h
    gst-rtsp-server/gst/rtsp-server/rtsp-context.h
    gst-rtsp-server/gst/rtsp-server/rtsp-latency-bin.h
    gst-rtsp-server/gst/rtsp-server/rtsp-media-factory-uri.h
    gst-rtsp-server/gst/rtsp-server/rtsp-media-factory.h
    gst-rtsp-server/gst/rtsp-server/rtsp-media.h
    gst-rtsp-server/gst/rtsp-server/rtsp-mount-points.h
    gst-rtsp-server/gst/rtsp-server/rtsp-onvif-client.h
    gst-rtsp-server/gst/rtsp-server/rtsp-onvif-media-factory.h
    gst-rtsp-server/gst/rtsp-server/rtsp-onvif-media.h
    gst-rtsp-server/gst/rtsp-server/rtsp-onvif-server.h
    gst-rtsp-server/gst/rtsp-server/rtsp-params.h
    gst-rtsp-server/gst/rtsp-server/rtsp-permissions.h
    gst-rtsp-server/gst/rtsp-server/rtsp-sdp.h
    gst-rtsp-server/gst/rtsp-server/rtsp-server-internal.h
    gst-rtsp-server/gst/rtsp-server/rtsp-server-object.h
    gst-rtsp-server/gst/rtsp-server/rtsp-server-prelude.h
    gst-rtsp-server/gst/rtsp-server/rtsp-server.h
    gst-rtsp-server/gst/rtsp-server/rtsp-session-media.h
    gst-rtsp-server/gst/rtsp-server/rtsp-session-pool.h
    gst-rtsp-server/gst/rtsp-server/rtsp-session.h
    gst-rtsp-server/gst/rtsp-server/rtsp-stream-transport.h
    gst-rtsp-server/gst/rtsp-server/rtsp-stream.h
    gst-rtsp-server/gst/rtsp-server/rtsp-thread-pool.h
    gst-rtsp-server/gst/rtsp-server/rtsp-token.h
    )

set(GSTREAMER_LIBS
    gstreamer-1.0
    gstbase-1.0
    gstrtp-1.0
    gstsdp-1.0
    gstrtsp-1.0
    gstapp-1.0
  gstnet-1.0
  gobject-2.0
  gmodule-2.0
  xml2
  gthread-2.0
  glib-2.0
  gio-2.0
)
target_link_libraries(gstrtspserver "${GSTREAMER_LIBS}")

get_directory_property(hasParent PARENT_DIRECTORY)
if(hasParent)
  set(GST_RTSP_SERVER_INCLUDE_DIRS
    "${CMAKE_CURRENT_LIST_DIR}/gst-rtsp-server"
    "${CONAN_INCLUDE_DIRS_GLIB}"
    "${CONAN_INCLUDE_DIRS_GSTREAMER}"
    "${CONAN_INCLUDE_DIRS_GSTREAMER_BASE}"
    PARENT_SCOPE
  )
endif()

install(FILES
    ${GST_RTSP_SERVER_HEADERS}
    DESTINATION
    ${CMAKE_INSTALL_PREFIX}/include/gstreamer-1.0/gst/rtsp-server)

install(TARGETS gstrtspserver LIBRARY DESTINATION lib)
