# CSV Docker - Data Analysis Tool

A containerized Python application for analyzing CSV and Excel data files with comprehensive statistics and insights.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Commands](#docker-commands)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Output](#output)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## 🔍 Overview

This project provides a Docker-containerized Python application that analyzes CSV and Excel files, providing detailed insights including:

- Dataset information (shape, columns, data types)
- Statistical summaries
- Missing value analysis
- Data quality assessment

The application is designed to be portable, reproducible, and easy to deploy across different environments using Docker.

## ✨ Features

- **Multi-format Support**: Processes both CSV (`.csv`) and Excel (`.xlsx`, `.xls`) files
- **Comprehensive Analysis**: 
  - Dataset shape and structure
  - Column information and data types
  - Statistical summaries (mean, median, std, etc.)
  - Missing value detection and reporting
- **Containerized**: Fully dockerized for consistent execution across environments
- **Error Handling**: Robust error handling for file operations and data processing
- **Clean Output**: Well-formatted, readable analysis results

## 🛠 Prerequisites

- **Docker**: Ensure Docker is installed and running on your system
  - [Install Docker Desktop](https://www.docker.com/products/docker-desktop/)
- **Git** (optional): For cloning the repository

## 📦 Installation

### Option 1: Clone the Repository
```bash
git clone <repository-url>
cd csv-docker
```

### Option 2: Download the Project
Download and extract the project files to your local machine.

## 🚀 Usage

### Building the Docker Image

Build the Docker container with the following command:

```bash
docker build -t csv-docker .
```

### Running the Application

#### Basic Usage (Default Data File)
```bash
docker run csv-docker
```

#### With Custom Data Directory
If you want to analyze your own CSV/Excel files, mount your data directory:

```bash
docker run -v "/path/to/your/data:/app/Data" csv-docker
```

**Windows Example:**
```cmd
docker run -v "C:\your\data\folder:/app/Data" csv-docker
```

**Linux/macOS Example:**
```bash
docker run -v "/home/user/data:/app/Data" csv-docker
```

#### Interactive Mode
To run the container in interactive mode for debugging:

```bash
docker run -it csv-docker /bin/bash
```

## 🐳 Docker Commands

| Command | Description |
|---------|-------------|
| `docker build -t csv-docker .` | Build the Docker image |
| `docker run csv-docker` | Run the container with default settings |
| `docker run -v "local/path:/app/Data" csv-docker` | Run with custom data directory |
| `docker images` | List all Docker images |
| `docker ps -a` | List all containers (running and stopped) |
| `docker rmi csv-docker` | Remove the Docker image |

## 📁 Project Structure

```
csv-docker/
├── Data/
│   └── measurements.csv      # Sample data file
├── Dockerfile               # Docker configuration
├── requirements.txt         # Python dependencies
├── script.py               # Main application script
└── README.md               # Project documentation
```

### File Descriptions

- **`Dockerfile`**: Defines the container environment and build process
- **`script.py`**: Main Python script that performs data analysis
- **`requirements.txt`**: Python package dependencies (pandas, openpyxl)
- **`Data/`**: Directory containing data files to be analyzed
- **`measurements.csv`**: Sample dataset for demonstration

## ⚙️ Configuration

### Modifying the Data Source

To analyze a different file, you have several options:

1. **Replace the existing file**: Place your CSV/Excel file in the `Data/` directory and name it `measurements.csv`

2. **Mount a different directory**: Use Docker volume mounting to point to your data directory

3. **Modify the script**: Edit `script.py` line 57 to change the default file path:
   ```python
   process_data("Data/your-file-name.csv")
   ```

### Adding Dependencies

To add new Python packages:

1. Update `requirements.txt` with the new package name
2. Rebuild the Docker image

## 📊 Output

The application provides the following analysis output:

### Dataset Information
- Number of rows and columns
- Column names
- Data types for each column

### Data Preview
- First 5 rows of the dataset

### Summary Statistics
- Count, mean, standard deviation
- Min/max values
- Quartiles (25%, 50%, 75%)

### Missing Value Analysis
- Count of missing values per column
- Total missing values in the dataset

### Example Output
```
Loading data from: Data/measurements.csv
Successfully loaded 1000 rows and 5 columns

=== DATASET INFORMATION ===
Shape: (1000, 5)
Columns: ['id', 'temperature', 'humidity', 'pressure', 'timestamp']

=== FIRST 5 ROWS ===
   id  temperature  humidity  pressure            timestamp
0   1         23.5      45.2    1013.2  2023-01-01 10:00:00
1   2         24.1      47.8    1012.8  2023-01-01 10:15:00
...

=== DATA TYPES ===
id             int64
temperature  float64
humidity     float64
pressure     float64
timestamp     object

=== SUMMARY STATISTICS ===
              id  temperature     humidity     pressure
count  1000.000     1000.000     1000.000     1000.000
mean    500.500       23.456       46.789     1013.456
...

=== MISSING VALUES ===
id             0
temperature    0
humidity       2
pressure       1
timestamp      0
✅ No missing values found!
```

## 🔧 Troubleshooting

### Common Issues

#### 1. File Not Found Error
```
Error: File 'Data/measurements.csv' not found!
```
**Solution**: Ensure your data file exists in the correct location or mount the correct directory.

#### 2. Docker Build Fails
**Solution**: 
- Check Docker is running
- Ensure you're in the project directory
- Verify internet connection for downloading dependencies

#### 3. Permission Issues (Linux/macOS)
**Solution**: 
```bash
sudo docker run -v "/path/to/data:/app/Data" csv-docker
```

#### 4. Windows Path Issues
**Solution**: Use forward slashes or properly escape backslashes:
```cmd
docker run -v "C:/your/data/folder:/app/Data" csv-docker
```

### Getting Help

If you encounter issues:

1. Check Docker logs: `docker logs <container-id>`
2. Run in interactive mode: `docker run -it csv-docker /bin/bash`
3. Verify file permissions and paths

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -am 'Add new feature'`)
6. Push to the branch (`git push origin feature/new-feature`)
7. Create a Pull Request

### Development Setup

For local development without Docker:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the script directly
python script.py
```

## 📝 License

This project is open source. Please refer to the LICENSE file for details.

## 🔄 Version History

- **v1.0.0**: Initial release with basic CSV/Excel analysis capabilities
- **v1.0.1**: Added Docker containerization
- **v1.0.2**: Enhanced error handling and documentation

---

## 📞 Support

For questions, issues, or contributions, please:
- Open an issue in the repository
- Contact the development team
- Check the troubleshooting section above

---

**Built with ❤️ using Python, Pandas, and Docker**
