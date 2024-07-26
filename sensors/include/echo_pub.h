#ifndef ECHO_PUB
#define ECHO_PUB

#include "publisher.h"
#include <frost_interfaces/msg/echo.h>
#include <ping1d.h>

class EchoPub : Publisher {

public:
  void setup(rcl_node_t node);
  void publish(float distance, float conf_level);
  using Publisher::destroy;

private:
  frost_interfaces__msg__Echo msg;
};

#endif // ECHO_PUB