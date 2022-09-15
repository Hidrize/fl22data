#include <iostream>

class Taxi {
    private:
        std::string model;
        std::string vin;
        std::string medallionNumber;
        std::string licensePlate;
        bool inspected;
     

    public:

        Taxi(std::string model = "", std::string vin = "",
             std::string medallionNumber = "", std::string licensePlate ="") {
        
            if(model == "" || vin == "" || medallionNumber == "" || licensePlate == ""){
                std::cout << "Please provide the following arguments:\n";
                std::cout << "car model, vin, medallion, license plate\n";
                exit(1); // for now we simply use exit if we find missing information
            }

            this->model = model;
            this->vin = vin;
            this->medallionNumber = medallionNumber;
            this->licensePlate = licensePlate;
            this->inspected = false;    // false by default
            std::cout << "Make sure to Inspect() before driver starts the shift";
        }

        void setVin(std::string vin){
            std::cout << "Sorry it is not possible to update the VIN\n";
        }

        void setMedallion(std::string medallion){
            this->medallionNumber = medallionNumber;
        }

        void setLicensePlate(std::string licensePlate){
            this->licensePlate = licensePlate;
        }

        std::string getModel(){
            return this->model;
        }

        std::string getVin(){
            return this->vin;
        }

        std::string getMedallion(){
            return this->medallionNumber;
        }

        std::string  getLicensePlate(){
            return this->licensePlate;
        }

        bool isTaxiReadToDrive(){
            return this->inspected;
        }

       void Inspect(){
           std::cout << "Inspecting...";
           std::cout << "Mechanic: the car was determined to be safe for driving\n";
           this->inspected = true;
        }
 
        friend std::ostream& operator<< (std::ostream &out, const Taxi &t);

}; // end of class


// not part of the class, overloaded * operator
// used to repeat a string (Note: Python already has this capability)
std::string operator * (const std::string src, unsigned int rep) {
    std::string out = "";
    while (rep--) {
        out += src;
    }
    return out;
}

// friend of class, overloaded << operator
std::ostream& operator<< (std::ostream &out, const Taxi &t) {
    std::string m1 = " Note: The taxi is ready for driver \n";
    std::string m2 ="  Note: The taxi needs to be Inspected() before driver can take it on the road\n";
    std::string pluss ="+";
    int mul = t.inspected ? m1.size() : m2.size();


    out << "\n" + pluss * mul + "\n";

    out << "\n Model: " << t.model;
    out << "\n VIN: " << t.vin;
    out << "\n Medallion: " << t.medallionNumber;
    out << "\n Plate: " << t.licensePlate;
    out << "\n\n";

     if (t.inspected){
         out << " The taxi is ready for driver \n";
     }
     else{
         out << " The taxi needs to be Inspected() before driver can take it on the road\n";
     }
    out << "\n" + pluss * mul + "\n";

  return out;
}

