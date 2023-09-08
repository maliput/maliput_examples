/*****************************************************************************
 * License: BSD-3
 * URL: https://github.com/stonier/maliput_examples/blob/main/LICENSE
 *****************************************************************************/

/* https : // github.com/jbeder/yaml-cpp/wiki/Tutorial */

/*****************************************************************************
** Includes
*****************************************************************************/

#include <fstream>
#include <iostream>
#include <string>

#include <yaml-cpp/yaml.h>

/*****************************************************************************
** Main
*****************************************************************************/

int main()
{
    YAML::Node config = YAML::LoadFile("tutorial.yaml");

    if (config["last_login"])
    {
        std::cout << "Last logged in: " << config["last_login"].as<std::string>() << "\n";
    }

    const std::string username = config["username"].as<std::string>();
    const std::string password = config["password"].as<std::string>();

    std::cout << "username: " << username << std::endl;
    std::cout << "password: " << password << std::endl;

    config["last_login"] = std::string("now");

    std::ofstream fout("tutorial.yaml");
    fout << config;
    return 0;
}
