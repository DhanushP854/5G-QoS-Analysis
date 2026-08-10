------------------------------------------------
5G QoS Analysis and Performance Monitoring
-------------------------------------------------

**Overview:** This project analyzes the performance of cellular network cells using key 5G Quality of Service (QoS) parameters. The project combines Oracle SQL, Python, Pandas, Matplotlib, and rule-based QoS analysis to identify cells with good performance and cells requiring network optimization. 
The system processes cellular performance data and generates QoS scores, performance visualizations, and recommendations for network improvement.

**Project Objectives:**
- Analyze cellular network performance.
- Evaluate important QoS parameters.
- Identify cells experiencing high load.
- Compare throughput and latency between cells.
- Calculate a normalized QoS score.
- Identify cells requiring attention.
- Generate recommendations for network optimization.
- Visualize network performance using graphs.
- Technologies Used
- Python
- Pandas
- Matplotlib
- Oracle SQL / SQL*Plus
- CSV
- GitHub
- QoS Parameters

**The analysis uses the following network parameters:**

- Parameter	Description
- Average Load	Average utilization/load of the cellular network
- Average Throughput	Data transmission performance
- Average Latency	Network response delay
- Average Packet Loss	Percentage of packets lost during transmission
- Network Status	Current status of the cell

**Project Architecture:**
(Oracle Database)
      |
      v
(SQL Query / View)
      |
      v
(CSV Dataset)
      |
      v
(Python + Pandas)
      |
      +------------------+
      |                  |
      v                  v
(Data Analysis)       (QoS Scoring)
      |                  |
      v                  v
(Performance)         (Attention)
(Graphs)              (Detection)
      |                  |
      +--------+---------+
               |
               v
       (Recommendations)
               |
               v
        (Final Results)


**Dataset:** The project analyzes 9 cellular network cells distributed across three regions:

+ North
+ Central
+ South

**The dataset contains:**

- Cell ID
- Cell Name
- Region
- Average Load
- Average Throughput
- Average Latency
- Average Packet Loss
- Network Status
- QoS Analysis

**A rule-based QoS scoring mechanism is used to compare the cells.**

**The scoring considers:**

- Network load
- Throughput
- Latency
- Packet loss

- The score is normalized to a 0–100 scale, where a higher score represents better overall QoS performance.

- Cells exceeding defined performance limits are marked as requiring attention.

**QoS Thresholds:**

-> The current analysis uses the following thresholds:
Load limit       : 60
Latency limit    : 65
Packet loss limit: 4

-> These thresholds are used to identify cells that may require optimization.

**Results:** Best Performing Cell
- CELL_N_02
- Region: North
- QoS Score: 100.0
- Throughput: 104.51
- Latency: 48.83
- Packet Loss: 2.94

**This cell achieved the highest overall QoS score in the analyzed dataset.**

-> Cell Requiring the Most Attention
- CELL_S_03
- Region: South
- QoS Score: 14.41
- Throughput: 89.90
- Latency: 62.70
- Packet Loss: 4.17
- Network Status: HIGH LOAD

**This cell has high network load and packet loss and therefore requires optimization.**
- Performance Analysis
- The project generates two major visualizations:
- QoS Score Comparison
- The graph compares the calculated QoS score of all analyzed cellular cells.

**Throughput Comparison:** 
- The graph compares the throughput performance of the cellular cells.

**Recommendations:**
- The system generates recommendations based on the detected performance problems.

**Examples include:**

- Reduce cell load / perform load balancing.
- Investigate packet loss and improve link quality.
- Optimize latency and radio resources.
- Improve throughput by allocating additional resources.
- No immediate action required for cells operating within acceptable limits.
- Project Structure
- 5G_QoS_Project/
│
├──> data/
│   └── final_qos_results.csv
│
├──> results/
│   ├── qos_score_comparison.png
│   └── throughput_comparison.png
│
├──> src/
│   └── final_dashboard.py
│
└──> README.md

-- Workflow --
1. Data Extraction: Cellular performance information is obtained from an Oracle database using SQL.

2. Data Preparation: The extracted data is converted into CSV format for Python-based analysis.

3. Data Analysis:
**Pandas is used to:**
- Load the dataset
- Clean the data
- Calculate statistics
- Analyze regional performance
- Identify high-load cells
- Compare throughput and latency

4. QoS Scoring: A rule-based scoring mechanism evaluates the overall performance of each cell.

5. Decision Analysis
**The system identifies:**
- Best QoS cell
- Worst QoS cell
- Cells requiring attention

6. Recommendations
- Performance problems are converted into practical network optimization recommendations.

7. Visualization
- Matplotlib generates performance graphs for easier interpretation.

**Future Enhancements:**
The project can be extended with:
- Machine learning-based QoS prediction.
- Real-time 5G network monitoring.
- Automatic anomaly detection.
- Time-series performance analysis.
- More cellular KPIs.
- Interactive dashboards using Power BI or Streamlit.
- Network traffic forecasting.
-  Automated database-to-dashboard pipelines.
- 5G handover performance analysis.
- Intelligent resource allocation.

**Conclusion:** *This project demonstrates how communication engineering concepts and data analysis can be combined to monitor and evaluate cellular network performance.*

**🏁 Project Status:** *Project Successfully Completed and Tested ✅. Looking forward to upgrade the project.*

-- THANKYOU --
The system provides a complete workflow from database extraction to QoS analysis, scoring, visualization, and network recommendations.

It can serve as a foundation for developing more advanced intelligent 5G network optimization systems.
