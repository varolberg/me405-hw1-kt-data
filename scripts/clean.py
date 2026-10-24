{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1450ef82-d742-4210-b37f-d3f509d9e76f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# load the raw file (';' separator, ',' decimal, no header)\n",
    "df = pd.read_csv(\"raw/kt_A15-1.csv\",\n",
    "                 sep=\";\", decimal=\",\", header=None,\n",
    "                 skipinitialspace=True, names=[\"d_over_w\", \"Kt\"])\n",
    "\n",
    "# sort the points by d/w (they were saved in click order)\n",
    "df = df.sort_values(\"d_over_w\").reset_index(drop=True)\n",
    "\n",
    "# save the cleaned table in standard CSV format\n",
    "df[[\"d_over_w\", \"Kt\"]].to_csv(\"processed/kt_A15-1_clean.csv\", index=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
