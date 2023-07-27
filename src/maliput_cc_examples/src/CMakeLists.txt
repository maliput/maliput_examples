add_library(integration
  tools.cc
)

target_link_libraries(integration
  PUBLIC
    maliput::api
    maliput::base
    maliput::common
  PRIVATE
    maliput_dragway::maliput_dragway
    maliput_malidrive::builder
    maliput_malidrive::loader
    maliput_multilane::maliput_multilane
    maliput_osm::builder
    yaml-cpp
)

add_executable(maliput_derive_lane_s_routes
  maliput_derive_lane_s_routes.cc
)

target_link_libraries(maliput_derive_lane_s_routes
    gflags
    maliput::common
    maliput::routing
    maliput::utility
    integration
)
