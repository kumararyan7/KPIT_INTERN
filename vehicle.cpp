#include <iostream>
#include <thread>
#include <mutex>
#include <atomic>
#include <chrono>
#include <gtest/gtest.h>

using namespace std;

class Abs {
    float brakePressure;
    float wheelSpeed;
    mutable mutex mtx;

public:
    Abs() : brakePressure(0.0f), wheelSpeed(60.0f) {}

    void applyBrake() {
        lock_guard<mutex> lock(mtx);
        brakePressure += 1.0f;
    }

    void releaseBrake() {
        lock_guard<mutex> lock(mtx);
        brakePressure = 0.0f;
    }

    float getBrakePressure() const {
        lock_guard<mutex> lock(mtx);
        return brakePressure;
    }

    float getWheelSpeed() const {
        lock_guard<mutex> lock(mtx);
        return wheelSpeed;
    }
};

class Esc {
    float steeringAngle;
    float torque;
    mutable mutex mtx;

public:
    Esc() : steeringAngle(0.0f), torque(0.0f) {}

    void correctSteering() {
        lock_guard<mutex> lock(mtx);
        steeringAngle = 0.0f;
    }

    void applyTorque() {
        lock_guard<mutex> lock(mtx);
        torque += 10.0f;
    }

    float getSteeringAngle() const {
        lock_guard<mutex> lock(mtx);
        return steeringAngle;
    }

    float getTorque() const {
        lock_guard<mutex> lock(mtx);
        return torque;
    }
};

class Ldw {
    float laneOffset;
    float cameraOffset;
    mutable mutex mtx;

public:
    Ldw() : laneOffset(0.0f), cameraOffset(0.0f) {}

    void calculateOffset() {
        lock_guard<mutex> lock(mtx);
        laneOffset = cameraOffset * 0.01f;
    }

    void sendWarning() const {
        lock_guard<mutex> lock(mtx);
        if (laneOffset > 0.3f || laneOffset < -0.3f)
            cout << "Warning: Lane Departure Detected!\n";
    }

    float getLaneOffset() const {
        lock_guard<mutex> lock(mtx);
        return laneOffset;
    }

    float getCameraOffset() const {
        lock_guard<mutex> lock(mtx);
        return cameraOffset;
    }

    void setCameraOffset(float offset) {
        lock_guard<mutex> lock(mtx);
        cameraOffset = offset;
    }
};

class SafetySystem {
    Abs& abs;
    Esc& esc;
    Ldw& ldw;
    atomic<bool> running;

public:
    SafetySystem(Abs& a, Esc& e, Ldw& l) : abs(a), esc(e), ldw(l), running(true) {}

    void controlSafetySystem() {
        while (running) {
            abs.applyBrake();
            esc.correctSteering();
            esc.applyTorque();
            ldw.calculateOffset();
            ldw.sendWarning();
            this_thread::sleep_for(chrono::milliseconds(100));
        }
    }

    void stop() {
        running = false;
    }

    string getSafetyStatus() const {
        return "System running";
    }
};

// Google Test cases
TEST(AbsTest, ApplyBrake) {
    Abs abs;
    abs.applyBrake();
    EXPECT_GT(abs.getBrakePressure(), 0.0f);
}

TEST(AbsTest, ReleaseBrake) {
    Abs abs;
    abs.applyBrake();
    abs.releaseBrake();
    EXPECT_EQ(abs.getBrakePressure(), 0.0f);
}

TEST(AbsTest, GetBrakePressure) {
    Abs abs;
    abs.applyBrake();
    EXPECT_FLOAT_EQ(abs.getBrakePressure(), 1.0f);
}

TEST(AbsTest, GetWheelSpeed) {
    Abs abs;
    EXPECT_FLOAT_EQ(abs.getWheelSpeed(), 60.0f);
}

TEST(EscTest, CorrectSteering) {
    Esc esc;
    esc.correctSteering();
    EXPECT_FLOAT_EQ(esc.getSteeringAngle(), 0.0f);
}

TEST(EscTest, ApplyTorque) {
    Esc esc;
    esc.applyTorque();
    EXPECT_FLOAT_EQ(esc.getTorque(), 10.0f);
}

TEST(EscTest, GetSteeringAngle) {
    Esc esc;
    EXPECT_FLOAT_EQ(esc.getSteeringAngle(), 0.0f);
}

TEST(EscTest, GetTorque) {
    Esc esc;
    esc.applyTorque();
    EXPECT_FLOAT_EQ(esc.getTorque(), 10.0f);
}

TEST(LdwTest, CalculateOffset) {
    Ldw ldw;
    ldw.setCameraOffset(40.0f);
    ldw.calculateOffset();
    EXPECT_FLOAT_EQ(ldw.getLaneOffset(), 0.4f);
}

TEST(LdwTest, SendWarning) {
    Ldw ldw;
    ldw.setCameraOffset(50.0f);
    ldw.calculateOffset();
    testing::internal::CaptureStdout();
    ldw.sendWarning();
    string output = testing::internal::GetCapturedStdout();
    EXPECT_FALSE(output.empty());
}

TEST(LdwTest, GetLaneOffset) {
    Ldw ldw;
    EXPECT_FLOAT_EQ(ldw.getLaneOffset(), 0.0f);
}

TEST(LdwTest, GetCameraOffset) {
    Ldw ldw;
    EXPECT_FLOAT_EQ(ldw.getCameraOffset(), 0.0f);
}

TEST(SafetySystemTest, ControlSafetySystem) {
    Abs abs;
    Esc esc;
    Ldw ldw;
    SafetySystem system(abs, esc, ldw);
    thread safetyThread(&SafetySystem::controlSafetySystem, &system);
    this_thread::sleep_for(chrono::milliseconds(300));
    system.stop();
    safetyThread.join();
    SUCCEED();
}