# Define the default target
.PHONY: all
all: utility trends plot kpi forecast

# Target to run utility.py
.PHONY: utility
utility:
	python utility.py

# Target to run trends.py
.PHONY: trends
trends:
	python trends.py

# Target to run plot.py
.PHONY: plot
plot:
	python plot.py

# Target to run kpi_computation.py
.PHONY: kpi
kpi:
	python kpi_computation.py

# Target to run forecast.py
.PHONY: forecast
forecast:
	python forecast.py
