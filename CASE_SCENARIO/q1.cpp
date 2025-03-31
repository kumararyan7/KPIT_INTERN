// 2.1 Create a C++ program that simulates the
// functionality of a connected vehicle's Advanced Driver
// Assistance System. This program should feature a
// class that encapsulates key attributes of the vehicle,
// including its unique identifier (id), current speed,
// direction of travel, and safety mode status, as well as
// any other relevant characteristics. The class should
// provide an assortment of methods that enable access
// to, modification of, and utilization of these attributes.
// For instance, methods could be implemented to
// update the vehicle's state, check for potential safety
// alerts, and display the vehicle's information in a user-
// friendly format. These methods would serve to
// demonstrate the program's capabilities in simulating
// the ADAS system.

#include <iostream>
#include <string>

class Vehicle {
private:
    std::string id;
    double speed;
    std::string direction;
    bool safetyMode;
    double distanceToObstacle;

public:
    // Constructor
    Vehicle(std::string id, double speed, std::string direction, bool safetyMode, double distanceToObstacle) {
        this->id = id;
        this->speed = speed;
        this->direction = direction;
        this->safetyMode = safetyMode;
        this->distanceToObstacle = distanceToObstacle;
    }

    // Getter methods
    std::string getId() { return id; }
    double getSpeed() { return speed; }
    std::string getDirection() { return direction; }
    bool getSafetyMode() { return safetyMode; }
    double getDistanceToObstacle() { return distanceToObstacle; }

    // Setter methods
    void setSpeed(double speed) { this->speed = speed; }
    void setDirection(std::string direction) { this->direction = direction; }
    void setSafetyMode(bool safetyMode) { this->safetyMode = safetyMode; }
    void setDistanceToObstacle(double distanceToObstacle) { this->distanceToObstacle = distanceToObstacle; }

    // Method to update vehicle state
    void updateState(double speed, std::string direction, double distanceToObstacle) {
        setSpeed(speed);
        setDirection(direction);
        setDistanceToObstacle(distanceToObstacle);
    }

    // Method to check for potential safety alerts
    void checkSafetyAlerts() {
        if (getSpeed() > 60 && getDistanceToObstacle() < 10) {
            std::cout << "Safety alert: vehicle is traveling too fast and is too close to an obstacle." << std::endl;
        }
        if (getSafetyMode() == false) {
            std::cout << "Safety alert: safety mode is not enabled." << std::endl;
        }
    }

    // Method to display vehicle information
    void displayInfo() {
        std::cout << "Vehicle ID: " << getId() << std::endl;
        std::cout << "Speed: " << getSpeed() << " mph" << std::endl;
        std::cout << "Direction: " << getDirection() << std::endl;
        std::cout << "Safety Mode: " << (getSafetyMode() ? "Enabled" : "Disabled") << std::endl;
        std::cout << "Distance to Obstacle: " << getDistanceToObstacle() << " meters" << std::endl;
    }
};

int main() {
    Vehicle vehicle("VEH-001", 50, "North", true, 20);
    vehicle.displayInfo();
    vehicle.updateState(70, "South", 5);
    vehicle.checkSafetyAlerts();
    vehicle.displayInfo();
    return 0;
}

