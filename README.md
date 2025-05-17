Quantitative Portfolio Simulator & Analytics Dashboard
======================================================

Overview
--------

The Quantitative Portfolio Simulator & Analytics Dashboard is a Python-based tool that simulates and analyzes the performance of a multi-asset investment portfolio. The project integrates finance, mathematics, and programming into a platform that provides:

- Simulations of portfolio performance.
- Bond pricing and loan amortization calculations.
- Key financial metrics such as returns, volatility, and Sharpe ratio.
- Visualizations to support understanding of portfolio dynamics.
- Exportable reports summarizing performance.

The goal is to deepen understanding of quantitative finance and demonstrate strong technical and analytical skills.

Features
--------

- Portfolio simulation with customizable allocations for stocks, bonds, and cash.
- Bond pricing using present value models.
- Loan amortization schedule generator.
- Financial performance metrics:
    - Annualized return
    - Volatility (standard deviation)
    - Sharpe ratio
- Data visualization using Matplotlib and optionally Plotly:
    - Portfolio growth over time
    - Allocation breakdowns
    - Bond amortization trends
- Exportable reports in LaTeX/PDF format.

Project Structure
-----------------
quant-portfolio-sim/
├── data/ # Data files (e.g., CSVs)
├── notebooks/ # Jupyter notebooks for interactive analysis
│ └── exploration.ipynb
├── reports/ # Generated reports
├── src/ # Python source code
│ ├── init.py
│ ├── portfolio.py # Portfolio simulation code
│ └── bonds.py # Bond and amortization functions
├── README.md
├── requirements.txt
└── .gitignore


Dependencies
------------

This project uses the following key Python packages:

- pandas
- numpy
- matplotlib
- jupyter
- scipy
- plotly (optional, for interactive plots)


Usage
-----

- Run Jupyter notebooks located in the `notebooks/` folder to test and explore the portfolio simulator.
- Use the Python modules in `src/` for core functionality.
- Export reports 


Roadmap
-------

- Stage 2: Develop core portfolio simulation functions.
- Stage 3: Add bond pricing and loan amortization modules.
- Stage 4: Implement data visualization.
- Stage 5: Build report export functionality.
- Stage 6 (optional): Develop a web-based interface using Streamlit.


License
-------

This project is licensed under the MIT License.

