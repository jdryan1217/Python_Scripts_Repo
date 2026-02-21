## Project Structure

```
car-sales-report-automation/
│
├── data/
│   └── car_sales.json          # Sample dataset
│
├── utils/
│   └── cars.py                 # Data loading + analysis utilities
│
├── reports/
│   └── pdf.py                  # PDF generation module
│
├── emailer/
│   └── sender.py               # Email creation + sending
│
├── output/                     # Generated PDFs (gitignored)
│
├── generate_report.py          # Main script
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```
