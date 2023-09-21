/*****************************************************************************
 * License: BSD-3
 * URL: https://github.com/stonier/maliput_examples/blob/main/LICENSE
*****************************************************************************/

/*****************************************************************************
** Includes
*****************************************************************************/

#include <iostream>

#include <maliput/api/lane.h>

/*****************************************************************************
** Main
*****************************************************************************/

int main()
{
    maliput::api::LaneId lane_id("Ramen Street");
    std::cout << lane_id.string() << std::endl;

    std::cout << "May you be blessed with a tickle from his noodly appendages" << std::endl;

    return 0;
}
