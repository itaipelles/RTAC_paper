# RTAC Paper
This is the official repository for reproducing the data and plots shown in the paper (link TBD):

"A coefficient of correlation for continuous random variables based on area coverage"

## Install
First, since minepy only support Python up to 3.10 we recommend using Python 3.10, at least until support improves. From within a suiting Python environment, run
```bash
pip install -r requirements.txt
```

## Run
First, you may optionally run the following to regenerate all the data, although the last data is already stored here in git:
```bash
python plots_for_paper/generate_all_data.py
```
Then you may generate all the plots from the data by running:
```bash
python plots_for_paper/generate_all_plots.py
```
