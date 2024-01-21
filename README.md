# Test Harmony - Python Selenium Test Automation Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/travis/yourusername/test-harmony.svg?branch=main)](https://travis-ci.org/prateeksethiDev/test-harmony)
[![Code Coverage](https://img.shields.io/codecov/c/github/yourusername/test-harmony.svg)](https://codecov.io/gh/prateeksethiDev/test-harmony)

Welcome to Test Harmony, a powerful and flexible Python-based test automation framework designed for web applications. Test Harmony seamlessly integrates Selenium, Pytest, and Pyxl to provide a comprehensive testing solution.

## Features

### 1. Page Object Model (POM)

Test Harmony embraces the Page Object Model design pattern to ensure maintainability, reusability, and organization of your test code. The framework's structure promotes clear separation of concerns between test logic and web page representation.

### 2. Logging Support

Enjoy detailed and insightful logging to track the execution flow of your test scripts. Test Harmony provides logging support that aids in identifying issues quickly and understanding the progression of your test suite.

### 3. Data Parametrization

Parameterize your test data effortlessly using Pyxl or using Pytest fixtures. Test Harmony supports dynamic data-driven testing, allowing you to run the same test scenario with different input values, enhancing test coverage.

### 4. Pytest Integration

Harness the power of Pytest for efficient test discovery, execution, and reporting. Pytest's simple and expressive syntax makes writing test cases a breeze, catering to both beginners and experienced testers alike.

### 5. Fixtures

Utilize Pytest fixtures to set up and manage test preconditions. Fixtures ensure a clean and isolated environment for each test, promoting reliable and repeatable test execution.

## Getting Started

### Prerequisites

- Python 3.x installed
- Pip (Python package installer)
- ChromeDriver or GeckoDriver (depending on your browser choice)
- pip install -U pytest
- pip install pytest-html

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/TestHarmony.git
   cd TestHarmony
   

### How to execute the automation suite

This will create html report for the automation run. 
   ```bash
    pytest -v -s --html=report.html