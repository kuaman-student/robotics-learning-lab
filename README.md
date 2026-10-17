# Robotics Learning Lab 🤖

> **Zero hardware → Simulation → ROS 2 → SLAM → Autonomous Systems**

A hands-on, software-first robotics learning journey. This repository documents my progress from programming and robotics fundamentals to simulated autonomous robots, navigation, perception, and advanced robotics concepts.

**Main goal:** Learn robotics by building small projects, testing them, documenting what I learn, and pushing progress to GitHub regularly—not just watching tutorials.

## 🎯 Why this repository?

I am learning the **software side of robotics** alongside my engineering studies. I may not always have access to a complete physical robot, so the core of this roadmap uses Python, virtual sensors, and simulation. Hardware experiments with an ESP32 and available sensors are optional extensions, not prerequisites.

This repository is intended to be a public learning log and a portfolio of reproducible projects.

## 🗺️ Roadmap

Progress is tracked phase by phase. I will check a phase off when I have completed its core concepts and built or documented a practical exercise—not simply when I have watched the related tutorials.

- [ ] **Phase 0 — Workspace & Developer Habits:** Python, VS Code, Git/GitHub, terminal basics, project structure, virtual environments.
- [ ] **Phase 1 — Programming for Robotics:** Python, NumPy, Matplotlib, CSV/JSON, input validation, unit tests, C++ basics, CMake.
- [ ] **Phase 2 — Linux, Networking & Software Engineering:** Linux/terminal, processes, TCP/UDP, logs, testing, reproducible setup.
- [ ] **Phase 3 — Robotics Mathematics:** Vectors, coordinate frames, rotations, linear algebra, calculus, probability, pose and kinematics.
- [ ] **Phase 4 — Webots Simulation:** Virtual robot, controller loop, keyboard control, virtual sensors, obstacle avoidance.
- [ ] **Phase 5 — ROS 2 Foundations:** Nodes, topics, services, actions, parameters, launch files, packages, debugging and tests.
- [ ] **Phase 6 — Robot Models & Visualization:** URDF, Xacro, TF2, robot state, RViz2 and coordinate-frame debugging.
- [ ] **Phase 7 — Gazebo Sim + ROS 2:** Physics-based simulation, virtual sensors, model spawning, ROS 2 integration and debugging.
- [ ] **Phase 8 — Control & Odometry:** Feedback, PID, differential-drive kinematics, odometry and `ros2_control`.
- [ ] **Phase 9 — Path Planning:** Grid maps, BFS, Dijkstra, A*, obstacle costs, path following and Nav2 concepts.
- [ ] **Phase 10 — Localization, Mapping & SLAM:** Occupancy grids, LiDAR concepts, odometry drift, SLAM Toolbox and localization.
- [ ] **Phase 11 — Nav2 Autonomous Navigation:** Goal navigation, planners, controllers, costmaps, waypoints and recovery behaviors.
- [ ] **Phase 12 — Computer Vision & Perception:** OpenCV, image processing, tracking, camera geometry, point clouds and a later introduction to deep learning.
- [ ] **Phase 13 — Optional ESP32 Integration:** Serial messages, sensor logging, fault handling and an optional bridge to higher-level robotics software.
- [ ] **Phase 14 — Testing & Reliability:** Unit/integration/system tests, logging, CI, repeatability and safe fallback behavior.
- [ ] **Phase 15 — Advanced Specializations:** Explore selected areas such as robotic arms/MoveIt 2, AI/ML, drones/PX4, advanced SLAM or multi-robot systems.
- [ ] **Phase 16 — Capstone: ARTZINX Virtual Autonomous Robot:** Combine simulation, control, ROS 2, robot models, SLAM, autonomous navigation, tests and documentation.

> **Learning rule:** Learn one layer, build something small, test it, explain it, then move to the next.

## 🧪 Projects & Practical Work

Projects will grow in complexity as I progress. Individual project folders will contain code, setup instructions, sample outputs, and notes where relevant.

| # | Project | Planned skills | Status |
|---|---|---|---|
| 01 | Distance Reading Analyzer | Python, validation, SAFE/WARNING/DANGER classification, min/mean, CSV | 🟡 In progress |
| 02 | Sensor Data Plotter | Matplotlib, simulated time series, noise and outlier experiments | ⬜ Planned |
| 03 | Robot Pose & Motion Commands | C++, structs/classes, vectors, basic robot state | ⬜ Planned |
| 04 | Analyzer Unit Tests | Boundary cases, invalid input, empty input, automated testing | ⬜ Planned |
| 05 | 2D Point-Robot Simulator | Pose, coordinate transforms, trajectories and plots | ⬜ Planned |
| 06 | Webots Controller | Keyboard teleoperation, virtual sensors, obstacle avoidance | ⬜ Planned |
| 07 | ROS 2 Sensor & Safety Nodes | Publisher/subscriber, sensor messages, safety states | ⬜ Planned |
| 08 | Robot Model & TF Visualization | URDF/Xacro, TF2, RViz2 | ⬜ Planned |
| 09 | Gazebo Simulation | Physics, simulated sensors, ROS 2 integration | ⬜ Planned |
| 10 | Path Planning & SLAM | A*, mapping, localization and navigation | ⬜ Planned |
| 11 | ARTZINX Virtual Autonomous Robot | Integrated simulation capstone | ⬜ Planned |

**Status legend:** 🟡 In progress · ✅ Completed · ⬜ Planned

I will update these statuses as projects actually progress. Planned does not mean completed.

## 📁 Repository Structure

The structure will evolve as the roadmap grows. A starting layout could look like this:

```text
robotics-learning-lab/
├── README.md
├── notes/
│   ├── learning-log.md
│   └── troubleshooting.md
├── python/
│   └── distance_analyzer/
│       ├── analyzer.py
│       ├── plotter.py
│       ├── test_analyzer.py
│       └── output/
├── cpp/
│   └── robot.cpp
├── math/
├── webots/
├── ros2/
├── models/
├── simulation/
├── perception/
└── capstone/
```

Only folders and files that are actually created will be committed. Generated outputs and environment files will be handled intentionally; virtual environments, caches, and machine-specific files should not be committed.

## 📆 Daily Learning & GitHub Workflow

I want to push progress regularly, ideally every day I work on robotics. A commit does **not** need to contain a huge feature: a small, meaningful improvement is enough.

For each learning session:

1. **Learn:** Pick one concept and use one main tutorial or official documentation page.
2. **Build:** Reproduce a small example without relying entirely on copy-paste.
3. **Experiment:** Change one variable and predict what will happen.
4. **Test:** Check normal, boundary, invalid, or failure cases where appropriate.
5. **Document:** Record what worked, what failed, and what I learned.
6. **Commit & push:** Save a small, meaningful change to GitHub.

### Example commit messages

```text
docs: add robotics learning roadmap
feat: add distance reading validation
feat: classify simulated sensor readings
test: cover invalid distance inputs
feat: plot noisy sensor readings
fix: handle empty sensor input
docs: record Webots obstacle avoidance experiment
```

### Daily learning log template

I can add a short entry to [`notes/learning-log.md`](notes/learning-log.md) after each session:

```markdown
## YYYY-MM-DD — Topic

- **Goal:**
- **What I learned:**
- **What I built/changed:**
- **Experiment/result:**
- **Bug or difficulty:**
- **How I fixed it / what I tried:**
- **Next step:**
```

The log should describe real work completed. If I miss a day, I will continue from where I left off rather than adding fake progress.

## 📚 Core Learning Resources

I will prioritize official documentation for installation and commands, use tutorials for intuition, and then modify examples myself.

### Programming & tools

- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [NumPy Learning](https://numpy.org/learn/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/)
- [C++ Reference](https://en.cppreference.com/)
- [CMake Tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Skills](https://skills.github.com/)

### Robotics mathematics

- [Modern Robotics — Northwestern University](https://modernrobotics.northwestern.edu/)
- [3Blue1Brown — Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)
- [Khan Academy — Calculus](https://www.khanacademy.org/math/calculus-1)

### Simulation & ROS

- [Webots Tutorials](https://cyberbotics.com/doc/guide/tutorials)
- [ROS 2 Jazzy Tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)
- [ROS 2 Concepts](https://docs.ros.org/en/jazzy/Concepts.html)
- [Gazebo Sim Documentation](https://gazebosim.org/docs/)
- [Nav2 Documentation](https://docs.nav2.org/)
- [TF2 Tutorials](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html)
- [URDF Tutorials](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html)
- [SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox)
- [ros2_control](https://control.ros.org/)

### Perception & optional specializations

- [OpenCV — Get Started](https://opencv.org/get-started/)
- [OpenCV Python Tutorials](https://docs.opencv.org/5.0/py_tutorials/py_tutorials.html)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [MoveIt 2 Documentation](https://moveit.picknik.ai/main/index.html)
- [PX4 Documentation](https://docs.px4.io/)

**Installation note:** Software versions and compatibility change. Before installing ROS 2 or Gazebo, check the official compatibility and installation instructions. The roadmap's suggested future stack is Ubuntu 24.04 + ROS 2 Jazzy with a compatible Gazebo Sim setup. I will verify the current official guidance before installing it and avoid mixing instructions from incompatible distributions.

## 🧭 Principles I Want to Follow

- Start with the tools already available; do not buy hardware just to follow a tutorial.
- Use simulated sensors until a project has a clear reason to require physical hardware.
- Learn coordinate frames, odometry and sensor topics before jumping into SLAM.
- Understand that RViz2 is for visualization, while Webots and Gazebo are simulators.
- Test invalid, noisy, delayed and missing sensor data—not only ideal cases.
- Keep projects reproducible with clear setup steps, expected output and known limitations.
- Do not treat a successful simulation as proof of real-world safety.
- Measure progress by what I can build, explain and debug—not by videos watched or tools installed.

## 🚀 Current Focus

**Current phase:** Phase 1 — Programming for Robotics

**Current project:** Distance Reading Analyzer

Immediate tasks:

- [ ] Validate simulated distance readings.
- [ ] Classify valid readings as `SAFE`, `WARNING`, or `DANGER`.
- [ ] Calculate minimum and mean distance.
- [ ] Export valid readings to CSV.
- [ ] Plot readings over time and experiment with noise/outliers.
- [ ] Write the C++ robot pose and motion-command example.
- [ ] Add unit tests for invalid values, empty input and threshold boundaries.
- [ ] Push the working code and update this README.

The thresholds used in the first exercise are learning/demo values, not certified real-robot safety limits.

## 📈 Progress Philosophy

This is a long-term learning project, not a race. The first pass through the roadmap may take 6–12 months or longer depending on college workload, available time, and laptop performance.

I will prioritize understanding and small, reproducible projects over rushing into advanced tools.

**One layer at a time. Build it. Test it. Explain it. Commit it.**
