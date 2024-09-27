# Workers Production App

## Overview

The Workers Production App is designed to streamline and optimize the management of production workflows. It provides features such as task tracking, resource allocation, and performance analytics, enabling teams to work more efficiently and effectively. 

Key features include:

- **Task Management**: Create, assign, and monitor tasks in real time.
- **Resource Allocation**: Easily allocate resources to tasks based on availability.
- **Analytics Dashboard**: Visualize performance metrics and identify bottlenecks.
- **User Management**: Manage team roles and permissions.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.12 or higher
- `pip`

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**

   ```bash
   git clone git@github.com:kevinronquillo/ProductionTracker.git
   # Or use the http repo
   cd ProductionTracker
   ```

2. **Create a Virtual Environment**

   ```bash
   python3.12 -m venv myenv
   ```

3. **Activate the Virtual Environment**

   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

To start the application, run the following command:

```bash
uvicorn app:app --reload
```

- The `--reload` flag enables automatic code reloading, making development easier.

## Contributing

If you’d like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.