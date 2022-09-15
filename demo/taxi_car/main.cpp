#include "Taxi.h"

int main() {
        Taxi t1 = Taxi("2019 Nissan Rogue SV", "JN8AT2MV3KW377312", "5Y19", "XYZ-1234");
        std::cout << "\n Model: " << t1.getModel();
        std::cout << "\n VIN: " << t1.getVin();
        std::cout << "\n Medallion: " << t1.getMedallion();
        std::cout << "\n Plate: " << t1.getLicensePlate();
        std::cout << t1;
        t1.isTaxiReadToDrive();
        t1.Inspect();
        t1.isTaxiReadToDrive();
        std::cout << t1;

        Taxi t2 = Taxi();
      
    return 0;
}
