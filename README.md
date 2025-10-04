# HPC Parallel Log Analyzer

A high-performance **Parallel Log Analyzer** built to efficiently parse, analyze, and monitor server logs in real-time. This project leverages Python's multiprocessing capabilities to handle large log files quickly and optionally provides a **Streamlit dashboard** for live visualization.

## Features

- Generates continuous fake server logs for testing.
- Parses and analyzes logs in parallel using multiprocessing for high performance.
- Provides live metrics and statistics through a Streamlit dashboard.
- Designed for high-performance computing (HPC) environments and large-scale log data.

## Project Structure

```

HPC-Log-Analyzer/
│
├── data/
│   └── sample_logs.log              # generated server logs
│
├── src/
│   ├── log_generator.py             # generates fake server logs continuously
│   ├── log_parser.py                # parses and analyzes logs in parallel
│   ├── dashboard.py                 # optional Streamlit dashboard for live stats
│
├── requirements.txt                 # project dependencies
└── README.md                         # this file

````

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/HPC-Log-Analyzer.git
cd HPC-Log-Analyzer
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Generate Logs

```bash
python src/log_generator.py
```

### 2. Parse and Analyze Logs in Parallel

```bash
python src/log_parser.py
```

### 3. Launch Streamlit Dashboard (Optional)

```bash
streamlit run src/dashboard.py
```

Open the dashboard in your browser to view real-time log analytics.

## Tools & Technologies

* Python 3.x
* Multiprocessing for parallel log analysis
* Streamlit for live dashboards
* Pandas & Matplotlib for data processing and visualization

