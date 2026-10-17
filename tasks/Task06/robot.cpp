
#include <iomanip>
#include <iostream>
#include <vector>

struct Pose2D {
    double x_m;
    double y_m;
    double theta_rad;
};

class MotionCommand {
public:
    double linear_mps;
    double angular_rps;

    MotionCommand(double linear, double angular)
        : linear_mps(linear), angular_rps(angular) {}
};

int main() {
    Pose2D pose{1.2, 2.5, 0.78};

    std::vector<MotionCommand> commands = {
        {0.3, 0.0},
        {0.2, 0.1},
        {0.0, 0.0}
    };

    std::cout << std::fixed << std::setprecision(2);

    std::cout << "Robot pose\n";
    std::cout << "x: " << pose.x_m << " m\n";
    std::cout << "y: " << pose.y_m << " m\n";
    std::cout << "theta: " << pose.theta_rad << " rad\n";

    std::cout << "\nMotion commands\n";

    for (const MotionCommand& command : commands) {
        std::cout
            << "linear = " << command.linear_mps
            << " m/s, angular = " << command.angular_rps
            << " rad/s\n";
    }

    return 0;
}
