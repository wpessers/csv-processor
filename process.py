import os
import csv
import pandas as pd
from pathlib import Path
import re

datadir = "data/"

html = """
<div>
      <table  style=”width:100%;”>
            <tr>
                  <th style="width: 50%;">
                        <img src="" style="width: 100%;">
                  </th>
                  <th style="width: 50%;font-weight: normal;">
                        <h1>{name}</h1>
                        <p align="left" style="margin-left:11.25pt;">
                              <b>Adres: </b> {address}<br>
                              <b>GSM: </b> {phone_number}<br>
                              <b>E-mailadres: </b> {email_address}<br>

                              <b>Functie: </b> {function}<br>
                              <b>Studies/Job: </b> {occupation}<br>
                              <b>Hobby's: </b> {hobby}<br>
                              <b>Lievelingskleur: </b> {fav_color}<br>
                              <b>Favoriete Chiro-activiteit: </b> {fav_activity}<br>
                              <b>Favoriete Chirolied: </b> {fav_song}<br>
                              <b>Leukste kamp: </b> {fav_camp}<br>
                              <b>Lievelingsmuziek: </b> {fav_music}<br>
                              <b>Lievelingsfilm of -boek: </b> {fav_lit_film}<br>

                              <b>Aantal jaren in de chiro: </b> {years}<br>
                              <b>Reeds leiding geweest van: </b> {history}<br>
                              <b>Verjaardag: </b> {date_of_birth}<br>
                        </p>
                  </th>
            </tr>
      </table>
</div>
"""

def main():
      csv_file_list = Path(datadir).glob("**/*.csv")
      if not os.path.exists("./output"):
            os.makedirs("./output")

      for csv_file_path in csv_file_list:
            naam_persoon = str(re.findall(r"[-_](.+)\.csv", str(csv_file_path)))[2:-2]
            naam_persoon = naam_persoon.strip()
            print("Reading: " + naam_persoon)
            df = pd.read_csv(csv_file_path, skipinitialspace=True, sep=":")
            colnames = df["kolom"].tolist()
            
            person_info_dict = {}
            person_info_dict["name"] = df.loc[df["kolom"] == colnames[0], "waarde"].to_string(index=False).lstrip()
            person_info_dict["address"] = df.loc[df["kolom"] == colnames[1], "waarde"].to_string(index=False).lstrip()
            person_info_dict["phone_number"] = df.loc[df["kolom"] == colnames[2], "waarde"].to_string(index=False).lstrip()
            person_info_dict["email_address"] = df.loc[df["kolom"] == colnames[3], "waarde"].to_string(index=False).lstrip()
            person_info_dict["function"] = df.loc[df["kolom"] == colnames[4], "waarde"].to_string(index=False).lstrip()
            person_info_dict["occupation"] = df.loc[df["kolom"] == colnames[5], "waarde"].to_string(index=False).lstrip()
            person_info_dict["hobby"] = df.loc[df["kolom"] == colnames[6], "waarde"].to_string(index=False).lstrip()
            person_info_dict["fav_color"] = df.loc[df["kolom"] == colnames[7], "waarde"].to_string(index=False).lstrip()
            person_info_dict["fav_activity"] = df.loc[df["kolom"] == colnames[8], "waarde"].to_string(index=False).lstrip()
            person_info_dict["fav_song"] = df.loc[df["kolom"] == colnames[9], "waarde"].to_string(index=False).lstrip()
            person_info_dict["fav_camp"] = df.loc[df["kolom"] == colnames[10], "waarde"].to_string(index=False).lstrip()
            person_info_dict["fav_music"] = df.loc[df["kolom"] == colnames[11], "waarde"].to_string(index=False).lstrip()
            person_info_dict["fav_lit_film"] = df.loc[df["kolom"] == colnames[12], "waarde"].to_string(index=False).lstrip()
            person_info_dict["years"] = df.loc[df["kolom"] == colnames[13], "waarde"].to_string(index=False).lstrip()
            person_info_dict["history"] = df.loc[df["kolom"] == colnames[14], "waarde"].to_string(index=False).lstrip()
            person_info_dict["date_of_birth"] = df.loc[df["kolom"] == colnames[15], "waarde"].to_string(index=False).lstrip()

            personalized_html = html.format(**person_info_dict)
            file_path = "output/" + naam_persoon + ".html"
            with open(file_path, "w") as fp:
                  fp.write(personalized_html)


if __name__ == "__main__":
      main()