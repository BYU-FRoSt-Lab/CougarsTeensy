#ifndef DVL_DRIVER
#define DVL_DRIVER

#include <Arduino.h>

#define dvlSerial Serial7

class DVL {

public:
    DVL();
    setup();
    update();
    float roll;
    float pitch;
    float yaw;
    String wrz;
    String wrp;
    String wru;
};


#endif // DVL_DRIVER